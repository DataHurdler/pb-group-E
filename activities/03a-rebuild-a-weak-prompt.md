# Activity 03a: Rebuild a Weak Prompt, One Slot at a Time

Module 03 · 22 min · Pairs · LO2

## Goal

Watch what each slot does by adding them one at a time, then use the slots to
diagnose and fix a second weak prompt in one go.

## You need

- [../handouts/prompt-anatomy-cheat-sheet.md](../handouts/prompt-anatomy-cheat-sheet.md)
- Your AI tool, and the Brookfall files in [../materials/data/](../materials/data/)

## Part 1: the telework announcement (15 min)

The real need: an email to all Parks and Recreation staff, from their director,
announcing the new telework policy and getting every fact right.

Each version adds **one** slot to the last. Run each version in a **new chat**.
After each run, write one line: what changed? To save time, split the work: one
of you runs v0, v2, v4 while the other writes the next version, then swap.
**v5 is optional** if you're short of time.

| Version | Add | What changed? |
| --- | --- | --- |
| v0 | "Write an email about the new telework policy." | |
| v1 | **+ Context:** who's sending it and why; paste [telework-policy.md](../materials/data/telework-policy.md) between `<policy>` tags | |
| v2 | **+ Audience:** who reads it and what they already know | |
| v3 | **+ Constraints:** length, tone, what must be exactly right | |
| v4 | **+ Format:** subject line, sections, a bullet list of eligibility rules? You decide | |
| v5 (optional) | **+** "Before you write, ask me any questions you need answered." Answer them, with made-up details if needed | |

Look back at v0. What did it invent: dates, forms, rules?

## Part 2: diagnose and fix (7 min)

Weak prompt: **"Summarize these notes."** with
[meeting-notes.md](../materials/data/meeting-notes.md) pasted.

The real need: an action list the chair can send to staff today: who does what,
by when.

1. **(2 min)** Run it. Finish this sentence: *"The output was ___, so the ___
   slot was empty."*
2. **(4 min)** Fix every empty slot in one rewrite. Run it in a new chat.
3. **(1 min)** Did it assign an owner to something the notes say nobody owns?
   (Module 04 has the fix.)

**You're done when** your v0–v5 table is filled in and you have a diagnosis
sentence for Part 2.

## Before you paste

Everything here is fictional and Green. Say it out loud anyway; it's the habit.

## If you finish early

Take your v4 and remove one slot at a time. Which removal hurts most?
