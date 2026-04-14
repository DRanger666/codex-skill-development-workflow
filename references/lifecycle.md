# Lifecycle

This reference captures the preferred maturity model for a custom skill in this environment.

## Default Development Loop

The recurring development loop is:

1. problem note
2. design or boundary note
3. staged draft
4. structural validation
5. provisional installation
6. behavioral testing
7. review and patch planning
8. current installed revision

Not every skill will need the same amount of ceremony, but this is the default loop.

Important point:

- this is not a one-way waterfall
- stage 8 is not a terminal end state
- any installed skill may re-enter the loop when new evidence arrives

The practical model is continuous improvement by revision.

That means a skill may go through multiple staged revisions such as:

- `v1`
- `v2`
- `v3`

without that implying the earlier stages were mistakes. It simply means the skill kept improving as the environment, evidence, or requirements changed.

## Re-entry Triggers

An installed skill should re-enter the development loop when any of the following happens:

- real use exposes a workflow failure
- a trigger weakness becomes visible
- wording causes user confusion
- the boundary between related skills proves unstable
- Codex behavior changes
- MCP tool behavior changes
- the available toolset changes
- the user's workflow or standards change
- a better public or local skill for the same purpose appears
- the skill's complexity grows enough to justify scripts or structured backing data

So the right mindset is:

- install a current best revision
- keep it open to later refinement

## Stage Meanings

### Problem Note

Use this stage when the user has identified:

- a repeated workflow need
- a real failure
- a recurring ambiguity
- or a pattern that is currently being rediscovered manually

The goal is to name the problem precisely before creating the skill.

### Design Or Boundary Note

Use this stage when the main uncertainty is:

- whether the workflow should be one skill or multiple skills
- where the authority boundary should be drawn
- whether a fact should appear in more than one skill
- whether the eventual solution should remain text-only or grow scripts and structured state

### Staged Draft

This is the first runnable or installable skill candidate.

Expected properties:

- exists outside `CODEX_HOME`
- has a real `SKILL.md`
- is self-contained for runtime materials
- has descriptive history from the beginning

### Structural Validation

At this stage:

- frontmatter is valid
- required files are present
- the basic skill structure is syntactically sound

Important warning:

- structural validation does not prove behavioral maturity

### Provisional Installation

This is appropriate when:

- the skill is useful already
- its main structure is sound
- real-world use is likely to surface the next set of failures

At this stage, the skill should explicitly say it is provisional.

### Behavioral Testing

Behavioral testing may include:

- manual interactive use
- prompt-set testing
- isolated-session harness testing
- live-environment testing

Testing should match the actual risk surface of the skill.

### Review And Patch Planning

After testing, capture:

- what failed
- what was acceptable
- what was only a harness artifact
- what patch direction is justified

### Current Installed Revision

This is the current best deployed revision, not the final version forever.

At this stage, the skill:

- has survived at least one round of evidence-based revision
- its boundaries and language are more trustworthy than the first install

But it still remains eligible for later re-entry into the loop.

It is better to think of this stage as:

- the current stable deployed revision

rather than:

- the finished skill

## Practical Rule

If there is pressure to install early, install early honestly.

That means:

- label the skill as provisional
- preserve the staged history
- keep testing and patching notes outside the runtime skill

This is better than pretending a first-draft installed skill is mature.

Likewise, it is better to treat a current installed revision as:

- currently trustworthy

rather than:

- permanently complete
