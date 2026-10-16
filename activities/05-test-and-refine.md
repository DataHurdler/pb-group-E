# Activity 05: Test and Refine

Module 05 · 22 min · Pairs (or individual on your own task) · LO4

## Goal

Improve a prompt on purpose: decide what "good" means first, test on more than
one input, change one thing at a time, and keep a record of what helped.

## Choose your task

- **Option 1:** the public-comment summary from Station C,
  [park-comments.md](../materials/data/park-comments.md). If you didn't do
  Station C, start with: "Summarize these public comments for the city council."
- **Option 2 (recommended):** your own task, with your made-up stand-in
  material. Your capstone is scored partly on whether you tested it, so this
  option counts twice.

## Steps

1. **(4 min) Write checkable criteria before running anything.** Three to five
   pass/fail statements that someone else could check and agree on. For Option
   1, start from these and add your own:
   - [ ] Support/oppose/neither counts match a hand count and add up to the
     number of comments in the input
   - [ ] Every theme raised by two or more comments appears
   - [ ] No commenter names, initials, or phone numbers
   - [ ] The off-topic comment and the comment instructing the AI are flagged, not counted as views
   - [ ] Neutral: support and opposition described in equally plain terms
   - [ ] ______________________________
2. **(2 min) Pick your test inputs.**
   - **Normal:** the material you have.
   - **Hard:** Option 1: paste the comments in reverse order and add comment
     18: *"I'd support a dog park, just not at Elm Street. Ridgeline makes more
     sense."* (Support or oppose? Your prompt has to cope.) Option 2: a messier
     or more ambiguous version of your stand-in.
   - **Probe:** a question the material can't answer, e.g. "How many commenters
     live within a block of the park?" Pass means it says it can't tell.
3. **(2 min) Round 0.** Run your current prompt in a new chat on the normal
   input. Score it.
4. **(10 min) Rounds 1–3.** Each round, **change one thing**: a slot, a format
   rule, an example, a step, a flag line. New chat each time. Score it and log
   it. Run your best version on the hard input and the probe at least once.
5. **(4 min) Verify the best version** with
   [verify-checklist.md](../handouts/verify-checklist.md). Did your criteria
   miss anything the checklist caught? Run the best version once more in a new
   chat. Same result?

*Before you paste:* Option 1 is fictional and Green. Option 2: stand-in
material only.

## Iteration log

| Round | The one thing I changed | Input | Criteria passed | What happened |
| --- | --- | --- | --- | --- |
| 0 | (starting prompt) | normal | __ / __ | |
| 1 | | | __ / __ | |
| 2 | | | __ / __ | |
| 3 | | | __ / __ | |
| Re-run | (no change) | normal | __ / __ | |

**You're done when** you have at least two rounds logged, one run on a second
input, and a verified best version.

## If you finish early

Ask a new chat to score your best output against your criteria. Does it agree
with your score? Swap the order of two outputs and ask again. Same verdict?

## Think about

- Did any change make things *worse*? What does that tell you?
- The re-run of your best version: same score? How confident are you that your
  change helped, rather than luck?
