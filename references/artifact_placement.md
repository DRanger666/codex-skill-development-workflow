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
- staging-repo level notes
- dedicated issue or patch-note folders
- testing or validation directories

## Staging Repo Level

At the staging-repo or staging-directory level, it is appropriate to keep:

- a repo `README.md`
- notes about scope of the staged repo
- deployment-vs-staging explanation
- development history and commit structure

That material explains the development surface, not the runtime skill behavior.

## Installed Skill Level

The installed copy under `CODEX_HOME` should contain runtime material only.

Do not install development notes into `CODEX_HOME` just because they were useful while building the skill.

## Practical Placement Heuristic

Ask:

- would the skill load or need this material while helping the user do the actual task

If yes:

- it may belong inside the skill

If no, and the material is about designing, testing, or patching the skill itself:

- it belongs outside

## Naming Direction

The user's current pattern favors descriptive development-note names such as:

- `<skill_or_topic>_development_notes`

That is a good fit for artifacts that are not runtime-internal to the skill.
