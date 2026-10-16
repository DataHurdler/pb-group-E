# 05 Test and Refine

Status: ready
Time: 2:05–2:50 (45 min) · Talk 12 / do 33
Objectives: LO4 · Refine prompts through iterative testing and evaluation. (LO1, SU reinforced)

## Purpose

Replace "try again until it looks better" with a method: decide what good means
first, in terms someone else could check, test on more than one input, change
one thing at a time, and verify by hand before trusting the result.

## By the end of this block, participants can…

- Turn vague quality words into checkable pass/fail criteria
- Test a prompt on a normal input, a hard input, and an out-of-scope probe
- Improve a prompt one change at a time and keep a log of what helped
- Apply the verification checklist, and explain the limits of AI checking AI

## Timed outline

| Min | Segment | Format | What happens |
| --- | --- | --- | --- |
| 0–3 | Hook | Whole-room vote | [Two summaries](../../materials/slides/hook-summaries.md) side by side. "Which is better?" The room splits, or agrees for different reasons. "You can't answer yet. You haven't said what better means." |
| 3–12 | The method | Lecture | Talking points |
| 12–15 | Make it checkable | Whole room | Rewrite three vague criteria (below) |
| 15–37 | Test and refine | Pairs or individual | [Activity 05](../../activities/05-test-and-refine.md) |
| 37–42 | Debrief | Whole room | Which single change helped most? Did any make it worse? What did the probe input reveal? Did the checklist catch anything your criteria missed? |
| 42–45 | Bridge | Instructor | Reveal what's wrong with Summary A. "Open your own prompt. Next it becomes something you can reuse." |

## Talking points (9 min)

1. **Criteria first.** Write three to five pass/fail checks before you run it.
   Otherwise you'll judge by fluency, and AI is always fluent.
2. **Checkable means someone else could check it and agree.** "Clear" isn't
   checkable; "every sentence under 25 words" is.
3. **Test on more than one input.** A normal case, a hard case, and a probe:
   a question the source *can't* answer ("Can I expense a rideshare?" against
   the telework policy). A prompt that works only on the example you wrote it
   for isn't finished.
4. **One change at a time.** Change five things and it improves: which one
   helped? A change that made it worse is a finding too.
5. **Results vary; run it twice.** A change that helped once might be luck. For
   anything you'll reuse, run the final version at least twice in new chats.
6. **The verification checklist.** Walk through
   [verify-checklist.md](../../handouts/verify-checklist.md): the five kinds of
   error, then read it as the audience, including fairness and accessibility.
7. **AI checking AI is useful, not sufficient.** "Quote the source for every
   claim, or write NOT IN SOURCE" catches real errors. But AI graders miss
   errors, flag correct statements, favour longer answers and the first option
   shown, and flip when you ask "are you sure?" You still check.
8. **Re-test when the tool changes.** Vendors update models without notice; a
   prompt that worked in March may behave differently in June.

## Make it checkable (3 min)

| Vague | Checkable |
| --- | --- |
| "Clear" | Main point in the first sentence; no sentence over 25 words |
| "Accurate" | Every number matches the source; counts add up to 17 |
| "Professional" | No exclamation marks; no promises the facts don't support; signed with the office name |

## Materials

- Slides: section 05, and [hook-summaries.md](../../materials/slides/hook-summaries.md)
- [verify-checklist.md](../../handouts/verify-checklist.md), one per person
- Activity 05 sheet with the iteration log
- [Answer key for the comment counts](../../instructor/answer-keys.md#park-comments)

## Check for understanding

Look at iteration logs while circulating. A good log has one change per row,
scores that go up *and sometimes down*, and at least one test on a second
input.

## Common problems

| Problem | Response |
| --- | --- |
| Criteria are vague | "How would two people check that and agree?" |
| Editing in the same chat each round | Fine for small fixes; for the log, a new chat per round keeps rounds comparable |
| Version 0 already passes everything | Raise the bar: run the hard input, or the probe |

## Instructor notes

- The hook summaries are ready in
  [hook-summaries.md](../../materials/slides/hook-summaries.md): one fluent but
  wrong, one plain but accurate.
- If the day is late, shorten the hook and debrief, never the activity.
