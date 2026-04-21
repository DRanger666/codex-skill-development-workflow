# Artifact Placement

This reference captures where different kinds of skill-related material should live.

## Main Distinction

The central placement rule is:

- runtime-internal material belongs inside the skill
- development material around the skill belongs outside the runtime skill

## Inside The Skill Folder

Keep only materials that the skill may need at runtime or that define the runtime skill surface.

Typical examples:

- `SKILL.md`
- runtime `references/`
- runtime `assets/`
- `agents/openai.yaml` when used
- scripts that the skill may actually invoke as part of its intended operation

## Runtime `references/`

Use `references/` for:

- workflow notes
- domain references
- condensed findings
- examples that support actual runtime use of the skill

Do not use `references/` for:

- testing plans
- patch notes
- postmortems
- review memos
- broad development planning around the skill

Those are development-side artifacts, not runtime skill knowledge.

## Outside The Skill Folder

Keep development artifacts outside the skill when they are about:

- building the skill
- testing the skill
- reviewing the skill
- patch planning
- issue tracking
- architecture redesign

Appropriate locations include:

- workspace development-note folders
- dedicated issue or patch-note folders, usually at workspace level
- testing or validation directories
- staging-repo level notes only when they are stable, clean, and appropriate to
  the staged repo as a public-facing development container

Do not read this list as meaning that patch-note folders and staged-repo notes
are equally appropriate in the staged repo.

Patch-analysis notes, fork-local review artifacts, and similar development
materials should usually remain at workspace level unless they have been
deliberately curated into clean repo-appropriate notes.

## Staging Repo Level

At the staging-repo or staging-directory level, it is appropriate to keep:

- a repo `README.md`
- notes about scope of the staged repo
- deployment-vs-staging explanation
- development history and commit structure

That material explains the development surface, not the runtime skill behavior.

A staging repo may be a clean, publishable, versioned development container.
Messy transient notes, test outputs, review artifacts, and patch records often
live outside that repo even when the skill itself is being actively developed.

The staged repo should be clean enough that it would not feel misplaced or
embarrassing if pushed to a public GitHub repo for that skill.

That means the question is not merely:

- does this note have a legitimate role somewhere

The real question is:

- does this note belong inside the clean staged repo for this skill

Some development artifacts are useful and legitimate but still belong outside
the staged repo at workspace level.

Examples that usually stay outside the staged repo:

- session spawn notes
- workspace-lineage artifacts
- transient review scratch notes
- patch-analysis notes tied to one local forked session

Examples that may belong in the staged repo when kept clean:

- a repo `README.md`
- a short note explaining a critical design decision
- a clearly written TODO or testing note that materially supports future skill
  development

Two staging shapes are acceptable:

- a repo that contains one or more skill folders
- a repo whose root is the skill root

Both preserve version history correctly. The important boundary is not the shape
itself, but the distinction between the staged development container and the
runtime skill package.

## Portability Versus Relocation

A good staged repo should be portable.

That means it should remain clean and self-contained enough that moving it to a
new parent workspace is feasible when hygiene requires it.

But portability does not imply that relocation is always the right move.

If the staged repo already lives under a stable, relevant parent workspace,
keeping it there is a coherent route.

Moving is preferred when the current parent directory is:

- unrelated to the skill
- misleading about the repo's purpose
- transient enough to create future maintenance confusion

So the rule is:

- portability is a capability requirement
- relocation is a situational hygiene decision

## Installed Skill Level

The installed copy under `CODEX_HOME` should contain runtime material only.

Do not install development notes into `CODEX_HOME` just because they were useful while building the skill.

If repo root equals skill root, do not treat a naive repository archive as the
runtime skill package. Install or export only the runtime subset and exclude
repository metadata such as `.git`.

Reusable testing scaffolds may live inside a runtime skill only when they support
that skill's runtime job of helping design or scaffold testing. Keep
skill-specific harnesses, test plans, run outputs, review notes, and patch
records outside the runtime skill.

## Practical Placement Heuristic

Ask:

- would the skill load or need this material while helping the user do the actual task

If yes:

- it may belong inside the skill

If no, and the material is about designing, testing, or patching the skill itself:

- it belongs outside

If it belongs outside the runtime skill but is still under consideration for the
staged repo, ask:

- does it materially support the skill's professional development
- would it feel at home in a clean public repo for this skill

If not:

- keep it outside the staged repo at workspace level

## Naming Direction

The user's current pattern favors descriptive development-note names such as:

- `<skill_or_topic>_development_notes`

That is a good fit for artifacts that are not runtime-internal to the skill.
