# AI and LLM Prompt Engineering for Public Service: A First Day with AI

A one-day, hands-on course for **government employees who are new to AI**:
six instructional hours, 8:30–4:00, with two breaks and a lunch. It is the
government edition of *AI and LLM Prompt Engineering*, the first course in a
five-course AI series. The approved learning objectives are kept word for word,
and a safe-use standard is added for public employees.

By 4:00, participants understand how AI assistants use prompts and context, and
how they fail. They know what may and may not go into a prompt, and can write
structured prompts with the six slots. They can apply ten techniques, test and
refine a prompt instead of retrying, and save it as a reusable template. Each
leaves with a tested template for a task from their own job, one a colleague
has already run cold.

**Status: ready to teach**, once the host-agency details in
[COURSE-BRIEF.md](COURSE-BRIEF.md#assumptions-to-confirm-with-the-host-agency)
are filled in, along with the placeholders in the slides and emails. Find
what's left with:

```sh
grep -rn "TODO" --include="*.md" .
grep -on "\[[A-Z][A-Z /]*\]" slides/course-day.qmd participants/*.md instructor/after-action.md
```

The second command also lists `[BRACKETS]` that are deliberately part of
prompt templates; fill only the logistics ones (`[DATE]`, `[APPROVED TOOL]`,
`[RECORDS OFFICER]`, and so on).

## The day at a glance

| Time | Min | Block | Objectives |
| --- | --- | --- | --- |
| 8:30 | 30 | [00 Welcome and first prompt](modules/00-welcome/README.md) | — |
| 9:00 | 60 | [01 How AI uses prompts and context](modules/01-how-ai-uses-prompts/README.md) | LO1 |
| 10:00 | 15 | **Break** | |
| 10:15 | 30 | [02 Safe and accountable use](modules/02-safe-use/README.md) | SU |
| 10:45 | 75 | [03 Anatomy of a prompt](modules/03-prompt-anatomy/README.md) | LO2 |
| 12:00 | 60 | **Lunch** | |
| 1:00 | 65 | [04 Techniques](modules/04-techniques/README.md) | LO3 |
| 2:05 | 45 | [05 Test and refine](modules/05-test-and-refine/README.md) | LO4 |
| 2:50 | 15 | **Break** | |
| 3:05 | 40 | [06 Reuse, efficiency, and capstone](modules/06-reuse-and-capstone/README.md) | LO5 |
| 3:45 | 15 | [07 Wrap-up](modules/07-wrap-up/README.md) | All |

**360 instructional minutes**: 105 of instructor talk (29%) and 255 of
participants doing (71%). `python3 tools/check_timing.py` verifies the arithmetic.
Pacing rules and the cut list are in [schedule.md](schedule.md).

## Objectives

1. **LO1** Explain how large language models use prompts and context to generate responses.
2. **LO2** Write clear, structured prompts that produce more useful and relevant outputs.
3. **LO3** Apply prompting techniques to improve accuracy, consistency, format, and usefulness.
4. **LO4** Refine prompts through iterative testing and evaluation.
5. **LO5** Use prompting strategies that improve efficiency while maintaining output quality.

**SU, safe use** (course-wide standard): decide what may go into a prompt,
recognize pasted text that tries to give orders, and verify output before it
leaves your desk.

## Repo layout

```
COURSE-BRIEF.md   Charter: description, audience, objectives, scope, design decisions
schedule.md       Minute budget, timed plan, pacing rules, cut list, coverage
modules/          Instructor guide per block: timed outline, talking points, demos
activities/       Participant activity sheets, ready to print or project
handouts/         Job aids participants keep (cheat sheet, technique reference,
                  safe-to-paste, verify checklist, prompt library, cases, reading, glossary)
materials/data/   Fictional "City of Brookfall" practice files, incl. a planted prompt injection
materials/slides/ Prepared demo material (Module 05 hook)
slides/           Quarto reveal.js deck for the whole day (source + rendered HTML)
assessment/       Pre/post check, capstone rubric, feedback form
instructor/       Prep checklist, run sheet, facilitator guide, setup, answer keys, after-action
participants/     Pre-course and follow-up emails
tools/            check_timing.py: verifies every module's minutes add up
web/              Self-paced web edition of the whole course (one HTML page)
docs/             Where the design came from: research, sources, ideas adopted
```

## To teach it

1. **3–4 weeks out:** fill in the host-agency fields in
   [COURSE-BRIEF.md](COURSE-BRIEF.md); get the agency's AI policy and the
   records officer's answers; confirm access to the approved tool with work
   accounts. Then follow [instructor/prep-checklist.md](instructor/prep-checklist.md).
2. **2 weeks out:** run every activity and station yourself in the approved
   tool; render the slides.
3. **On the day:** [instructor/run-sheet.md](instructor/run-sheet.md) and
   [slides/course-day.html](slides/course-day.html) (press `S` for speaker notes).
4. **After:** [participants/follow-up-email.md](participants/follow-up-email.md),
   [instructor/after-action.md](instructor/after-action.md), and the 30-day
   check-in.

To rebuild the slides after editing: `quarto render slides/course-day.qmd`.

## Design principles

- **Name the failure before the technique.** Every technique runs against the
  plain version first.
- **Six slots, not an acronym;** Role is optional.
- **Tool-neutral.** Tool-specific notes live only in
  [instructor/setup-and-tech.md](instructor/setup-and-tech.md).
- **Fictional data all day.** The data rule is modelled, not just taught.
- **Safety early, then everywhere.** Data rules at 10:15, then a
  before-you-paste line on every activity sheet.
- **Variability is curriculum.** Never promise a demo output.
- **One prompt grows all day,** from the 8:34 index card to the 3:25 cold test.

How the design was researched and what it borrows is recorded in
[docs/design-notes.md](docs/design-notes.md).
