# Prompt Engineering for Public Service: A First Day with AI

A one-day, six-hour, hands-on course for **government employees who are new to
AI**. Participants learn how AI assistants produce their answers and where they
go wrong, what may and may not go into a prompt, a five-part method for writing
prompts (CRAFT), four techniques for harder tasks, and how to verify and refine
output. Each participant leaves with a tested, reusable prompt for a task from
their own job.

This repo has everything needed to prepare, teach, and follow up: schedule,
module guides, activities, handouts, fictional practice data, slides,
assessment, and instructor materials.

**Status: ready to teach**, once the host-agency details in
[COURSE-BRIEF.md](COURSE-BRIEF.md#assumptions-to-confirm-with-the-host-agency)
are filled in. Find what's left with:

```sh
grep -rn "TODO\|\[APPROVED TOOL\]\|\[POLICY" --include="*.md" --include="*.qmd" .
```

## The day at a glance

9:00–4:00 · 360 contact minutes · 330 instructional · about one quarter
instructor talk, three quarters participants doing.

| Time | Min | Block | Outcomes |
| --- | --- | --- | --- |
| 9:00 | 30 | [00 Welcome and first prompt](modules/00-welcome/README.md) | — |
| 9:30 | 60 | [01 How AI answers, and using it safely](modules/01-how-ai-answers/README.md) | LO1, LO2 |
| 10:30 | 15 | Break | |
| 10:45 | 75 | [02 The CRAFT prompt](modules/02-craft/README.md) | LO3 |
| 12:00 | 60 | Lunch | |
| 13:00 | 60 | [03 Technique stations](modules/03-techniques/README.md) | LO4 |
| 14:00 | 45 | [04 Test, verify, refine](modules/04-test-and-refine/README.md) | LO5 |
| 14:45 | 15 | Break | |
| 15:00 | 40 | [05 Capstone: your reusable prompt](modules/05-capstone/README.md) | LO3–LO5 |
| 15:40 | 20 | [06 Wrap-up](modules/06-wrap-up/README.md) | All |

Minute budget, pacing rules, and the cut list are in [schedule.md](schedule.md).

## Learning outcomes

By the end of the day, participants can:

1. **Explain** how an LLM produces an answer and name three ways that leads to errors
2. **Decide** what may go into a prompt and who is accountable for the result
3. **Write** a complete prompt using CRAFT: Context, Request, Audience, Format, Test
4. **Choose and apply** a technique: ground it, show it, break it down, let it ask
5. **Verify and refine** output against criteria, and save it as a reusable template

## Repo layout

```
COURSE-BRIEF.md   Charter: description, audience, outcomes, scope, assumptions
schedule.md       Timed plan, minute budget, cut list, outcome coverage
modules/          Instructor guide per block: timed outline, talking points, demos
activities/       Participant activity sheets, ready to print or project
handouts/         Job aids participants keep: CRAFT, safe-to-paste, verify, prompt library, glossary
materials/data/   Fictional "City of Brookfall" practice documents, safe to paste anywhere
materials/slides/ Prepared demo material (Module 04 hook)
slides/           Quarto reveal.js deck for the whole day (source + rendered HTML)
assessment/       Pre/post check, capstone rubric, feedback form
instructor/       Prep checklist, run sheet, facilitator guide, setup, answer keys, after-action
participants/     Pre-course and follow-up emails
```

## To teach it

1. **3–4 weeks out:** fill in the host-agency fields in
   [COURSE-BRIEF.md](COURSE-BRIEF.md), get the agency's AI policy, and confirm
   how participants get access to the approved tool. Then work through
   [instructor/prep-checklist.md](instructor/prep-checklist.md).
2. **1 week out:** run every activity yourself in the approved tool; print
   from the list in the checklist.
3. **On the day:** [instructor/run-sheet.md](instructor/run-sheet.md) and
   [slides/course-day.html](slides/course-day.html) (press `S` for speaker notes).
4. **After:** [participants/follow-up-email.md](participants/follow-up-email.md)
   and [instructor/after-action.md](instructor/after-action.md).

To rebuild the slides after editing: `quarto render slides/course-day.qmd`.

## Design principles

- **Tool-neutral.** Every technique works in Copilot, ChatGPT, Claude, and
  Gemini. Tool-specific notes live only in
  [instructor/setup-and-tech.md](instructor/setup-and-tech.md).
- **Fictional data, all day.** Practice uses the City of Brookfall files, so the
  data rule is modelled, not just taught.
- **Safety is a thread, not a lecture.** Data rules come at 10:00, then recur as
  a "before you paste" check in every activity.
- **Plain version first.** Every technique is run against the version without
  it, so participants see the difference themselves.
- **One thread on their own job,** from introductions to the capstone, so the
  day ends with something they'll use on Monday.
