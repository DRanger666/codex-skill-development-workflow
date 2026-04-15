---
name: codex-skill-development-local-workflow
description: "Use this skill when Codex skill work should follow the user's local development workflow on this machine: scope and boundary design, staged development outside CODEX_HOME, runtime-vs-development artifact placement, provisional installation decisions, behavioral testing, and evidence-driven patching."
---

# MPR Skill Development Workflow

Use this skill when the task is about developing or refining a Codex skill under the user's own standards rather than only following generic skill-creation advice.

This skill is about custom workflow discipline:

- scope and boundary design
- staging and versioning
- runtime-vs-development artifact placement
- provisional installation decisions
- testing and review strategy
- patch-note driven refinement

Read these as needed:

- [references/lifecycle.md](references/lifecycle.md)
- [references/boundary_and_scope.md](references/boundary_and_scope.md)
- [references/artifact_placement.md](references/artifact_placement.md)
- [references/testing_and_review.md](references/testing_and_review.md)
- [references/provisional_installation.md](references/provisional_installation.md)

## Status

This skill is provisional.

It is a first operational draft distilled from prior skill-building work across multiple sessions and workspaces. Treat it as an early codification of the user's standards, not as a fully hardened process document.

## Authority Boundary

This skill owns:

- identifying the right development stage for a skill
- deciding whether a workflow should become one skill or multiple non-overlapping skills
- preserving a clean authority boundary between related skills
- choosing where runtime material versus development material should live
- deciding when provisional installation is reasonable
- choosing an appropriate testing and review strategy
- recommending patch-note and issue-note driven refinement

This skill does not own:

- generic Codex skill syntax rules by itself
- the canonical `init_skill.py` or `quick_validate.py` mechanics by itself
- broad generic advice that ignores the user's local standards

For canonical Codex packaging mechanics, validation scripts, and baseline folder conventions, also use the system `skill-creator` guidance.

This skill complements `skill-creator`. It does not replace it.

## Core Model

The user's skill-development process is not:

- write `SKILL.md`
- install immediately
- hope for the best

The actual working model is:

1. define the problem and desired operational surface
2. decide the right scope boundary
3. stage the skill outside `CODEX_HOME`
4. preserve descriptive version history from the beginning
5. keep runtime materials self-contained
6. keep development and testing artifacts outside the runtime skill
7. validate structurally
8. install provisionally when useful and label that status honestly
9. test behavior with prompts, harnesses, and manual review
10. patch from real failures

This is a recurring loop, not a one-way sequence.

The installed skill at any moment should be treated as the current best deployed revision, not as a permanently finished artifact.

This skill should also be treated as a hand-holding workflow, not as a rigid protocol.

Its default sequence is the preferred route because it protects important outcomes such as:

- proper staging
- descriptive version history
- clean runtime-vs-development artifact placement
- explicit maturity labeling
- meaningful testing and review
- overall development hygiene

But if the user intentionally takes a different coherent route, do not force the default sequence mechanically.

Instead:

- adapt to the route the user is actually taking
- keep track of which protections or deliverables that route may skip
- surface the tradeoffs explicitly
- help the user recover missing safeguards where needed

## When To Use This Skill

Use this skill when the user is doing any of the following:

- creating a new custom skill
- deciding whether to split one skill into two or more skills
- patching a skill after real failures or ambiguity
- setting up a staging repo or staged skill folder
- deciding what belongs inside `references/`, `assets/`, or outside the skill
- designing a prompt-testing harness for a skill
- interpreting skill-test results
- deciding whether a skill is only a draft, provisionally installable, or mature enough for promotion

## Operating Posture

Use this skill as a consultation frame for skill-development work.

Its job is to:

- identify where the user is in the skill-development lifecycle
- identify the real decision or problem being worked on
- apply the relevant doctrine from this skill and its references
- recommend the next concrete move
- state what remains uncertain, user-owned, or still unvalidated

Do not treat this as a rigid executor skill.

Use the flow below as the default guidance path, while adapting when the user is
already following a different coherent route.

## Default Guidance Flow

### Phase 1. Resolve The Development Task

First identify which kind of skill-development task is actually happening:

- brand-new skill design
- boundary redesign
- patching after a failure
- staging and packaging
- testing and review planning
- promotion into `CODEX_HOME`

Do not jump straight into editing until that is clear.

Also determine whether the user is already following a non-default but coherent route.

If they are, do not snap back to the canonical flow automatically.

Instead, identify:

- which stage they are effectively in
- which expected deliverables already exist
- which expected deliverables are still missing
- what risks or losses may follow if the current route continues unchanged

### Phase 2. Decide The Scope Boundary

Before drafting or patching the skill, decide:

- should this be one skill or multiple skills
- what the authority boundary is
- whether any shared facts need deliberate asymmetric duplication across skills

Prefer narrow, non-competing skills.

Do not split only for elegance if the split makes first-contact guidance incomplete.

Do not merge only for convenience if the merged skill collapses distinct operational surfaces.

### Phase 3. Choose Artifact Placement

Before writing files, decide which materials are:

- runtime-internal to the skill
- development-side notes around the skill
- testing and review artifacts
- staging-repo level documents

Runtime material belongs inside the skill folder.

Development notes, testing plans, review notes, and patch notes should generally live outside the runtime skill folder.

### Phase 4. Stage Before Installing

Develop the skill in a staged area before promoting it into `CODEX_HOME`.

The staged area should:

- preserve descriptive git history
- explain its relation to installed skills
- keep the skill self-contained at runtime

If a staged repo or directory does not exist yet, create one first rather than improvising directly in the installed skill location.

### Phase 5. Mark Maturity Honestly

Every skill draft should be treated as being in one of these states:

- draft
- structurally valid
- provisionally installed
- behaviorally tested
- current installed revision

If the skill is not behaviorally tested, say so plainly.

If it is installed early for practical use, label it as provisional.

Even a behaviorally tested installed skill may later re-enter the loop because of:

- real failures
- tool changes
- Codex or MCP behavior changes
- changing user needs
- stronger competing local or public skills

### Phase 6. Validate And Test Appropriately

Run structural validation when available.

Then decide whether behavioral testing is needed and what form it should take:

- simple manual testing
- prompt-set testing
- isolated-session harness testing
- live interactive testing
- review against real failures from use

Do not let structural validation be mistaken for behavioral maturity.

### Phase 7. Patch From Evidence

When failures happen, write down:

- what happened
- why it matters
- whether the issue is scope, wording, trigger, workflow, artifact placement, or architecture
- what patch direction follows

Prefer patch-note driven refinement over vague “improve the skill” editing.

## Output Expectations

When using this skill, produce:

- a clear statement of the skill-development stage
- a clear statement of whether the user is on the default route or a coherent alternative route
- a clear scope and boundary decision
- the correct artifact placement decision
- a staged-draft or patch recommendation
- an explicit maturity label such as `provisional` when appropriate
- a testing and review recommendation proportionate to the skill's current state
- explicit warnings about any missing safeguards or deliverables the current route may be skipping

## Anti-Patterns

Do not:

- invent skills directly in `CODEX_HOME` without staging
- blur development notes into runtime `references/`
- overfit to one session and present the result as mature
- collapse related skills into one file when they own different operational surfaces
- forbid all duplication even when one fact is needed for both readiness and diagnosis
- force the canonical sequence mechanically when the user is already following a different but coherent route
- fail to notice when the user's chosen route is skipping important protections such as staging, version history, testing, or hygiene
- let harness output stand in for human review
- pretend structural validation proves behavioral reliability
