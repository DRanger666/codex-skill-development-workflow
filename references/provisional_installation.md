# Provisional Installation

This reference captures when and how provisional installation should be used.

## Core Idea

Sometimes real failures will not surface until a skill is installed and starts shaping behavior in normal use.

So provisional installation is a legitimate stage, not a mistake.

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

## Why This Matters

This keeps two truths visible at once:

- the skill is useful enough to use now
- the skill is still expected to change

That honesty improves later patching because future sessions can recognize the installed skill as provisional rather than assuming it is already hardened.
