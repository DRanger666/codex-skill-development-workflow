# Boundary And Scope

This reference captures the preferred boundary logic for custom skills in this environment.

## Core Principle

Skills should be narrow, but not artificially fragmented.

The target is:

- non-competing scope
- clear authority
- full user guidance across the skill set

## Preferred Split

Split a workflow into multiple skills when the tasks are genuinely different, for example:

- intake and path selection
- operational procedure
- maintenance or recovery
- domain navigation
- artifact generation

The Playwright skill pair is the main example:

- intake skill decides whether Playwright is the right first path and what readiness conditions apply
- connected-tab workflow owns the exact operational procedure once Playwright is chosen

## Bad Split Pattern

Do not split if the result is:

- two skills that answer the same user need from slightly different angles
- unclear authority over the same prompt
- a first-contact skill that no longer guides a user far enough to succeed

## Bad Merge Pattern

Do not merge if the result is:

- one large skill with multiple competing operational surfaces
- a skill that becomes both intake and full workflow essay at once
- a document that is too broad to trigger cleanly or stay readable

## Deliberate Limited Duplication

Not all duplication is bad.

A fact may need to appear in more than one skill if it serves different functions.

The main accepted case is:

- readiness in one skill
- diagnosis in another

When duplication is necessary, keep it asymmetric:

- one skill gets the first-contact version
- another gets the operational or troubleshooting version

## Entry-Point Completeness Rule

Assume the user may enter from more than one related skill.

Therefore:

- neither skill should omit a fact that would cause silent failure from that entry point

This does not justify full duplication.
It justifies enough coverage to prevent a broken handoff.

## Practical Questions To Ask

Before deciding the scope:

- what exact user problem does this skill own
- what prompts should clearly trigger it
- what prompts should clearly belong elsewhere
- if a related skill exists, what remains this skill's authority after the split
- what blocking facts must still be visible from this entry point

## Good Outcome

A good boundary design produces a skill set where:

- each skill has a recognizable authority surface
- mixed prompts can still be handled without conceptual collision
- patching one skill does not require rewriting the whole set
