#!/usr/bin/env python3
"""
Starter template for prompt-based Codex skill testing.

This file is a scaffold to copy and adapt for a specific skill or skill set.
It is not meant to be executed unchanged as a canonical script for every skill.

What this template does:
- reads numbered prompts from a markdown file
- runs each prompt in a fresh `codex exec --ephemeral` session
- captures raw transcript, final response, and exact command per prompt
- writes a simple markdown summary report

What this template intentionally does NOT do:
- detect which skills triggered
- auto-grade the results
- infer whether a run passed or failed
- assume any specific skill domain such as Playwright

Review should still be done manually from the saved artifacts.

Suggested prompt file shape:

## Category Name
1. `Prompt text here`
2. `Another prompt here`

## Another Category
3. `A harder boundary prompt`

You can adapt the parser if your prompt file uses a different format.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


DEFAULT_WORKSPACE = Path(__file__).resolve().parent
DEFAULT_PROMPTS = DEFAULT_WORKSPACE / "skill_testing_prompts.md"
DEFAULT_RESULTS = DEFAULT_WORKSPACE / "skill_testing_prompt_results.md"
DEFAULT_RUNS_DIR = DEFAULT_WORKSPACE / "skill_test_runs"
DEFAULT_CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
DEFAULT_MODEL = "gpt-5.4"
DEFAULT_REASONING_EFFORT = "low"
DEFAULT_SANDBOX = "workspace-write"
DEFAULT_APPROVAL = "never"
DEFAULT_RESULTS_TITLE = "Skill Prompt Test Results"


@dataclass
class PromptCase:
    number: int
    category: str
    prompt: str


@dataclass
class RunResult:
    case: PromptCase
    exit_code: int
    session_id: str | None
    final_message: str
    transcript_path: Path
    final_message_path: Path
    command_path: Path


def parse_prompts(markdown_text: str) -> list[PromptCase]:
    """
    Parse prompts from a simple markdown file.

    Supported patterns:
    - markdown headings like `## Category`
    - legacy category lines like `For `skill-name`:`
    - numbered prompt lines like `1. `Prompt text``
    """
    cases: list[PromptCase] = []
    category = "Uncategorized"
    prompt_re = re.compile(r"^\s*(\d+)\.\s*`(.+?)`\s*$")
    heading_re = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")

    for raw_line in markdown_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        heading_match = heading_re.match(raw_line)
        if heading_match:
            category = heading_match.group(1).strip()
            continue

        if line.startswith("For `") and line.endswith("`:"):
            category = line[5:-2]
            continue

        prompt_match = prompt_re.match(raw_line)
        if prompt_match:
            cases.append(
                PromptCase(
                    number=int(prompt_match.group(1)),
                    category=category,
                    prompt=prompt_match.group(2),
                )
            )

    return cases


def choose_cases(cases: list[PromptCase], numbers: set[int] | None) -> list[PromptCase]:
    if not numbers:
        return cases
    return [case for case in cases if case.number in numbers]


def parse_numbers(raw: str | None) -> set[int] | None:
    if not raw:
        return None

    out: set[int] = set()
    for chunk in raw.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "-" in chunk:
            start_s, end_s = chunk.split("-", 1)
            start = int(start_s)
            end = int(end_s)
            out.update(range(start, end + 1))
        else:
            out.add(int(chunk))
    return out


def extract_session_id(transcript_text: str) -> str | None:
    match = re.search(r"session id:\s*([0-9a-f-]{36})", transcript_text)
    return match.group(1) if match else None


def fenced(text: str) -> str:
    return f"```\n{text.rstrip()}\n```"


def build_results_markdown(
    runs: list[RunResult],
    prompts_path: Path,
    workspace: Path,
    codex_home: Path,
    model: str | None,
    reasoning_effort: str | None,
    sandbox: str,
    approval: str,
    title: str,
) -> str:
    lines: list[str] = []
    lines.append(f"# {title}")
    lines.append("")
    lines.append(f"- Workspace: `{workspace}`")
    lines.append(f"- CODEX_HOME: `{codex_home}`")
    lines.append(f"- Prompts source: `{prompts_path}`")
    if model:
        lines.append(f"- Model: `{model}`")
    if reasoning_effort:
        lines.append(f"- Reasoning effort: `{reasoning_effort}`")
    lines.append(f"- Sandbox: `{sandbox}`")
    lines.append(f"- Approval policy: `{approval}`")
    lines.append("- Session mode: fresh `codex exec --ephemeral` run per prompt")
    lines.append("")

    for run in runs:
        lines.append(f"## Prompt {run.case.number}")
        lines.append("")
        lines.append(f"- Category: `{run.case.category}`")
        lines.append(f"- Exit code: `{run.exit_code}`")
        lines.append(f"- Session id: `{run.session_id or 'unknown'}`")
        lines.append(f"- Prompt: `{run.case.prompt}`")
        lines.append(f"- Transcript: `{run.transcript_path}`")
        lines.append(f"- Final message file: `{run.final_message_path}`")
        lines.append(f"- Command file: `{run.command_path}`")
        lines.append("")
        lines.append("### Final Response")
        lines.append("")
        lines.append(fenced(run.final_message or "[no final message captured]"))
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def run_case(
    case: PromptCase,
    workspace: Path,
    runs_dir: Path,
    codex_home: Path,
    model: str | None,
    reasoning_effort: str | None,
    color: str,
    sandbox: str,
    approval: str,
) -> RunResult:
    case_dir = runs_dir / f"prompt_{case.number:02d}"
    case_dir.mkdir(parents=True, exist_ok=True)

    transcript_path = case_dir / "codex_exec_stdout.txt"
    final_message_path = case_dir / "final_message.txt"
    command_path = case_dir / "command.txt"

    cmd = [
        "codex",
        "-a",
        approval,
        "-s",
        sandbox,
        "exec",
        "--skip-git-repo-check",
        "--ephemeral",
        "--color",
        color,
        "-C",
        str(workspace),
        "-o",
        str(final_message_path),
    ]
    if model:
        cmd += ["-m", model]
    if reasoning_effort:
        cmd += ["-c", f"model_reasoning_effort={json.dumps(reasoning_effort)}"]
    cmd.append(case.prompt)

    command_path.write_text(" ".join(json.dumps(part) for part in cmd) + "\n")

    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        check=False,
        env=env,
    )

    transcript_path.write_text(result.stdout)
    final_message = final_message_path.read_text() if final_message_path.exists() else ""
    session_id = extract_session_id(result.stdout)

    return RunResult(
        case=case,
        exit_code=result.returncode,
        session_id=session_id,
        final_message=final_message,
        transcript_path=transcript_path,
        final_message_path=final_message_path,
        command_path=command_path,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run prompt-based skill tests through fresh Codex sessions."
    )
    parser.add_argument("--prompts-file", type=Path, default=DEFAULT_PROMPTS)
    parser.add_argument("--results-file", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--runs-dir", type=Path, default=DEFAULT_RUNS_DIR)
    parser.add_argument("--workspace", type=Path, default=DEFAULT_WORKSPACE)
    parser.add_argument("--codex-home", type=Path, default=DEFAULT_CODEX_HOME)
    parser.add_argument(
        "--numbers",
        help="Comma-separated prompt numbers and/or ranges, e.g. 1,3,5-8",
    )
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--reasoning-effort", default=DEFAULT_REASONING_EFFORT)
    parser.add_argument("--sandbox", default=DEFAULT_SANDBOX)
    parser.add_argument("--approval", default=DEFAULT_APPROVAL)
    parser.add_argument("--color", default="never")
    parser.add_argument("--results-title", default=DEFAULT_RESULTS_TITLE)
    args = parser.parse_args()

    markdown_text = args.prompts_file.read_text()
    cases = parse_prompts(markdown_text)
    selected = choose_cases(cases, parse_numbers(args.numbers))

    if not selected:
        print("No prompt cases selected.", file=sys.stderr)
        return 1

    args.runs_dir.mkdir(parents=True, exist_ok=True)

    runs: list[RunResult] = []
    for case in selected:
        runs.append(
            run_case(
                case=case,
                workspace=args.workspace,
                runs_dir=args.runs_dir,
                codex_home=args.codex_home,
                model=args.model,
                reasoning_effort=args.reasoning_effort,
                color=args.color,
                sandbox=args.sandbox,
                approval=args.approval,
            )
        )

    results_markdown = build_results_markdown(
        runs=runs,
        prompts_path=args.prompts_file,
        workspace=args.workspace,
        codex_home=args.codex_home,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        sandbox=args.sandbox,
        approval=args.approval,
        title=args.results_title,
    )
    args.results_file.write_text(results_markdown)

    print(f"Wrote results to {args.results_file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
