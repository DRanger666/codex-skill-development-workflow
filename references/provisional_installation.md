# Provisional Installation

This reference captures when and how provisional installation should be used.

## Core Idea

Sometimes real failures will not surface until a skill is installed and starts shaping behavior in normal use.

So provisional installation is a legitimate stage, not a mistake.

It is also not a one-time exception to an otherwise terminal lifecycle.

In this environment, provisional installation is one possible entry into a longer revision loop.

## When Provisional Installation Is Reasonable

Provisional installation is appropriate when:

- the skill has a coherent scope
- the structure is sound enough to validate
- the current draft is already useful
- further progress likely depends on real use rather than more abstract drafting

## What Must Be True

If a skill is installed provisionally:

- the staged version should exist first
- the staged history should be preserved
- the skill should say it is provisional
- the difference between structural validity and behavioral maturity should be stated honestly

## What Provisional Does Not Mean

It does not mean:

- unstructured improvisation
- skipping validation
- skipping staging
- pretending the installed copy is final

## Recommended Promotion Sequence

The preferred order is:

1. create or patch the staged skill
2. commit the staged changes descriptively
3. run structural validation if available
4. decide whether provisional installation is justified
5. install into `CODEX_HOME`
6. treat later failures as patch input, not as embarrassment

## Archive-Native Symlink Exception

The normal installation shape is a copied runtime package under `CODEX_HOME`.

A symlink from `CODEX_HOME/skills/<name>` to a repo-local skill folder is an exception, not a shortcut. Use it only for archive-native skills where the repo is part of the runtime boundary: for example, when the skill depends on local archive indexes, source snapshots, recovered transcripts, large assets, or repo-pinned navigation that should not be duplicated into `CODEX_HOME`.

Archive-native does not mean merely large, fast-moving, or inconvenient to copy.

Before using this route, verify that:

- the staged repo exists and preserves descriptive history
- the symlink target is stable, intentional, and repo-local
- the linked skill folder still exposes a clean runtime surface
- copying would create stale duplicated archive state or broken references
- the exception is documented in the relevant repo or workspace policy

This exception does not permit skipping staging, validation, maturity labeling, or artifact hygiene. It also does not permit development notes, patch logs, test output, or scratch material to become runtime material.

When an archive-native skill matures, reassess whether a copied runtime package has become practical. If the symlink remains the right shape, treat the target repo commit as the deployed revision when precise reproducibility matters.

## Why This Matters

This keeps two truths visible at once:

- the skill is useful enough to use now
- the skill is still expected to change

That honesty improves later patching because future sessions can recognize the installed skill as provisional rather than assuming it is already hardened.

## Continuous Improvement Implication

Provisional installation should be understood as:

- one current revision entering normal use

not as:

- the last meaningful step before a fixed final version

Later installed revisions may still go through:

- `v2`
- `v3`
- later patch cycles

for reasons such as:

- real failures surfacing during use
- changing Codex behavior
- evolving MCP tools
- new workflow needs
- stronger competing solutions

Even a later refined installed revision may re-enter the same loop.

The important distinction is:

- provisional labels early uncertainty honestly
- continuous improvement remains possible for every later installed revision too
