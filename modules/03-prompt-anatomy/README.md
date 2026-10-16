# 03 Anatomy of a Prompt

Status: ready
Time: 10:45–12:00 (75 min) · Talk 20 / do 55
Objectives: LO2 · Write clear, structured prompts that produce more useful and relevant outputs. (SU reinforced)

## Purpose

Give participants one structure, the six slots, that fixes most weak prompts,
the habit of diagnosing a disappointing output by asking which slot is empty,
and a version 1 prompt for their own job.

## By the end of this block, participants can…

- Name the six slots and what goes wrong when each is empty
- Diagnose a weak output by naming the empty slot
- Rebuild a weak prompt one slot at a time and see what each slot changed
- Recognize that vendor frameworks (Microsoft, Google, OpenAI, GovTech
  Singapore) cover the same core as the slots
- Write a version 1 prompt for a recurring task of their own, with stand-in data

## Timed outline

| Min | Segment | Format | What happens |
| --- | --- | --- | --- |
| 0–5 | Hook | Tables | **Worst prompt contest:** the vaguest possible prompt for *reply to a resident complaint*. Run it; read out the best-worst result. Write the room's "what's missing?" answers on the flip chart; they turn out to be the slots |
| 5–17 | Six slots, built live | Demo | Talking points A; build the hydrant prompt one slot at a time, the room calling out what to add (below) |
| 17–21 | Diagnose the output | Whole room | [Three prepared outputs](../../materials/slides/diagnose-outputs.md) on screen; name the empty slot in a sentence |
| 21–27 | What else matters | Lecture | Talking points B: principles, Role, the vendor-framework map |
| 27–49 | Rebuild a weak prompt | Pairs | [Activity 03a](../../activities/03a-rebuild-a-weak-prompt.md) |
| 49–55 | Debrief | Whole room | Each pair, as a sentence: "The output was ___, so our ___ slot was empty." Tally on the flip chart |
| 55–57 | Set up your own task | Instructor | Introduce 03b; repeat the before-you-paste rule and the not-today list |
| 57–72 | Your task, v1 | Individual | [Activity 03b](../../activities/03b-your-task-v1.md) |
| 72–75 | Turn and tell | Pairs | Tell a neighbour your task and which slot was weakest in v1. Bridge: "After lunch, ten techniques for exactly that." |

## Talking points A: the six slots (12 min, built live)

| Slot | What goes in it | When it's empty, the output is… |
| --- | --- | --- |
| **Task** | One job, starting with a verb | the wrong thing entirely |
| **Context** | What the AI can't guess: who you are, the situation, the purpose (*why*), the source material | generic, or invented |
| **Audience** | Who reads it, what they already know, reading level | pitched at the wrong person |
| **Constraints** | Length, tone, what must stay exactly as written, what's off limits | too long, wrong tone, breaks a rule |
| **Format** | The shape: sections, table, email, bullets, a form to fill | unusable shape |
| **Examples** | One good sample of what you want | right content, wrong voice or style |

Build it live with [hydrant-notice.md](../../materials/data/hydrant-notice.md).
New chat each step; ask the room "what would you add?" before each.

| Step | Add | What the room should notice |
| --- | --- | --- |
| 1 | **Task:** "Rewrite this notice in plain language." + paste | Better, still long and formal |
| 2 | **+ Audience:** residents, on phones, some with limited English, 6th-grade level | Shorter words |
| 3 | **+ Constraints:** under 150 words; keep every date, time, boundary, and phone number exactly; friendly, not casual | Facts preserved |
| 4 | **+ Format:** headline, then "What's happening", "What you should do", "Questions?" | Scannable |
| 5 | **+ Context:** "I work in Public Works. This goes on the city website and the utility-bill insert, so residents will read it in a hurry." Source in `<notice>` tags | Small change here, since the notice carried most of the context. Context matters most when there's no source to paste |

Examples come in Module 04 ("Show one example"). Mention that they're a slot.

## Talking points B: what else matters (6 min)

1. **Explain why.** "Spell out every acronym" works; "Spell out every acronym,
   because readers are residents who don't know our department's shorthand"
   works better and generalizes to cases you didn't list.
2. **Say what to do, not only what not to do.** "Write in short paragraphs"
   beats "Don't use bullet points." Keep hard "don'ts" for real boundaries:
   "Don't promise a refund."
3. **One job per prompt.** Two jobs, two prompts.
4. **Mark your material.** Put pasted text between tags or quotes, so the
   AI can tell your instructions from the material, and so instructions hidden
   in the material are less likely to be followed.
5. **No magic words.** ALL CAPS, "this is very important," threats, and
   tips don't reliably help and can make the AI over-strict. Contradictions
   hurt more than missing detail. Clear and lean beats long and anxious.
6. **Role is optional.** "You are an experienced communications officer"
   nudges tone and vocabulary. Research finds that expert personas don't
   reliably improve accuracy. Use a role for voice; never instead of Context.
7. **Every vendor's framework covers the same core.** None is identical, and
   few name Audience or Examples separately, but they all ask for the task, the
   context, and the shape of the output. One slide:

| Vendor framework | Maps to |
| --- | --- |
| Microsoft Copilot: Goal, Context, Source, Expectations | Task · Context · Context (source) · Constraints + Format |
| Google Gemini: Persona, Task, Context, Format | Role · Task · Context · Format |
| OpenAI: Goal, Context, Output, Boundaries | Task · Context · Format · Constraints |
| GovTech Singapore CO-STAR: Context, Objective, Style, Tone, Audience, Response | Context · Task · Constraints · Constraints · Audience · Format |

"Use whichever your tool's help pages use. They all ask for the same core."

## Diagnose the output (4 min)

Use [diagnose-outputs.md](../../materials/slides/diagnose-outputs.md): three
requests and outputs, with the answers (Context, Constraints, Format) and the
fix for each. Show one at a time; the room names the empty slot.

## Materials

- Slides: section 03
- [prompt-anatomy-cheat-sheet.md](../../handouts/prompt-anatomy-cheat-sheet.md), one per person
- Activity sheets 03a and 03b

## Check for understanding

While circulating in 03a, ask a pair to point to their **Audience** and
**Constraints** slots. If they can't, they've written a longer Task.

## Common problems

| Problem | Response |
| --- | --- |
| The prompt is a wall of text | Fine. Length isn't the problem; vagueness is. One line per slot helps |
| "Which slot is it?" (Audience vs Constraints) | Doesn't matter. The slots are a checklist for what's missing, not a filing system |
| Can't think of a task for 03b | "The email you answer most often" works for almost everyone |
| Own task involves decisions about people | Redirect to the writing around it: the letter explaining a decision, not the decision |
| Someone pastes real data in 03b | Quietly stop them, help make a stand-in; never make an example of them |

## Instructor notes

- Expect Context and Constraints to win the tally.
- 03b must not be cut. It seeds the afternoon and the capstone.
- If someone insists their framework (RTF, RISEN, CRAFT…) is better: "Great.
  Check it has these six things in it." Most acronyms are a subset or reshuffle.
