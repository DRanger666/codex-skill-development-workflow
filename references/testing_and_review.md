# Testing And Review

This reference captures the preferred way to test and review custom skills in this environment.

## Main Principle

Testing and evaluation are not the same thing.

The preferred model is:

- use scripts or harnesses to generate evidence
- use manual review to interpret that evidence

Do not let the harness pretend to be the reviewer.

## When Harness Testing Makes Sense

Harness-style testing is especially useful when a skill is:

- prompt-triggerable
- sensitive to wording or boundary ambiguity
- expected to load in some prompts and not in others
- vulnerable to side effects during response generation

## Preferred Harness Shape

The established pattern from the Playwright work is:

- one prompt per fresh isolated session
- capture exact command used
- capture raw transcript
- capture final response
- preserve per-prompt artifacts
- write a summary report separately

Prompt sets should vary:

- trigger strength
- specificity
- boundary ambiguity
- operational demands

## Review Standard

When reviewing results, do not default to binary pass/fail.

Use categories such as:

- content failure
- workflow failure
- wording or framing issue
- trigger weakness
- boundary blur but acceptable
- side-effect risk
- harness artifact
- not an issue

These categories make patching more precise.

## Important Review Questions

When interpreting a result, ask:

- did the response actually harm the user-facing workflow
- was the oddity caused by the skill, by the prompt, or by the harness/runtime
- is the problem patch-worthy or only inelegant
- did the skill boundary hold up under a mixed prompt

## Structural Validation Versus Behavioral Testing

Structural validation is still useful, but it checks only basics such as:

- frontmatter
- required files
- naming rules

It does not prove:

- trigger reliability
- user-facing clarity
- correct boundary behavior
- absence of side-effect drift

So do not stop at structural validation for non-trivial skills.

## Live Interactive Testing

Some skills cannot be tested well with prompt harnesses alone.

Examples include skills that depend on:

- live browser state
- user-selected pages
- account-specific context
- interactive switching during the run

In those cases, the test plan must include:

- setup preconditions
- user involvement points
- environment caveats
- interpretation rules that separate setup failures from skill failures

## Patch Loop

After review:

- write a precise issue or patch note
- name the actual failure mode
- decide whether the fix belongs in scope, wording, trigger design, or architecture
- patch the staged skill first
- only then consider updating the installed copy
