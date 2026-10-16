# Schedule

Status: ready

## Budget

| | Minutes |
| --- | --- |
| On site, 8:30–4:00 | 450 |
| Lunch, 12:00–1:00 | −60 |
| Two breaks, 10:00 and 2:50 | −30 |
| **Instructional time** | **360 (6 hours)** |
| Instructor talk and demos | 105 (29%) |
| Participants doing: activities, practice, debriefs, checks | 255 (71%) |

Run `python3 tools/check_timing.py` after editing any module. It checks that
every module's timed outline adds up to its slot and that the day totals 360.

## The day

| Time | Min | Block | Talk / do | Objectives |
| --- | --- | --- | --- | --- |
| 8:30 | 30 | [**00 Welcome and first prompt**](modules/00-welcome/README.md): before/after demo, introductions, pre-check, sign in to the *work* account | 11 / 19 | — |
| 9:00 | 60 | [**01 How AI uses prompts and context**](modules/01-how-ai-uses-prompts/README.md): prediction, context, modes, variability, confabulation, sycophancy | 22 / 38 | LO1 |
| 10:00 | 15 | **Break** | | |
| 10:15 | 30 | [**02 Safe and accountable use**](modules/02-safe-use/README.md): approved accounts, the traffic light, records, disclosure, high-impact uses, prompt injection | 12 / 18 | SU |
| 10:45 | 75 | [**03 Anatomy of a prompt**](modules/03-prompt-anatomy/README.md): six slots, diagnose from the output, vendor frameworks, your own task v1 | 20 / 55 | LO2 |
| 12:00 | 60 | **Lunch** | | |
| 1:00 | 65 | [**04 Techniques**](modules/04-techniques/README.md): ten techniques, six stations, plain version first | 16 / 49 | LO3 |
| 2:05 | 45 | [**05 Test and refine**](modules/05-test-and-refine/README.md): checkable criteria, test cases, one change at a time, verification, AI checking AI | 12 / 33 | LO4 |
| 2:50 | 15 | **Break** | | |
| 3:05 | 40 | [**06 Reuse, efficiency, and capstone**](modules/06-reuse-and-capstone/README.md): templates, library, saved setups, when not to use AI; build and cold-test your template | 8 / 32 | LO5 |
| 3:45 | 15 | [**07 Wrap-up**](modules/07-wrap-up/README.md): post-check, Monday card, close, feedback | 4 / 11 | All |
| 4:00 | | End | | |

## Pacing rules

- **No instructor talk longer than 12 minutes** before participants do something.
- **After lunch, hands on within two minutes.** Module 04 opens with the warm-up
  already on screen.
- **Stop activities on time.** Debrief what groups have.
- **Clock checks at 10:00, 12:00, and 2:50.** More than 10 minutes behind:
  apply the cut list immediately, not later.
- **Parking lot** for policy, legal, and "what about tool X" questions.
  Answered in Module 07 or in the follow-up email.

## If the day runs long: cut in this order

1. Module 04: two stations instead of three; *Ground it* stays required (−12).
2. Module 03: Part 2 of Activity 03a becomes optional (−7).
3. Module 01: the sycophancy check becomes an instructor demo (−4).
4. Module 02: the card sort uses 6 cards instead of 12 (−4).
5. Module 00: drop the experience poll and shorten "The day" to 3 minutes (−3).

**Never cut:** the Module 02 safe-use talk, the Module 03 own-task version 1,
the Module 05 activity, the Module 06 partner test, or the Module 07
post-check.

## If there's extra time

1. **Prompt bake-off** (+20): every table writes a prompt for the same brief
   (a road-closure notice); outputs are judged blind against the Module 05
   criteria; then the winning *prompt* is revealed and the room explains why it
   won. Optionally, have an AI judge the same outputs and compare.
2. **Reverse-engineer the prompt** (+10): show three outputs; tables guess the
   prompt that produced each, slot by slot.
3. **Share-outs** (+5): two volunteers show their capstone template.

## Coverage

| | Introduced | Practised | Checked |
| --- | --- | --- | --- |
| LO1 How LLMs use prompts and context | 01 | 01, 04 (warm-up), 05 | Pre/post Q1–3, Activity 01 |
| LO2 Clear, structured prompts | 03 | 03, 04, 06 | Pre/post Q6, Activity 03a, capstone row 1 |
| LO3 Techniques | 04 | 04, 06 | Pre/post Q7–8, Activity 04 stations, capstone row 2 |
| LO4 Testing and refining | 05 | 05, 06 | Pre/post Q9, Activity 05 log, capstone row 3 |
| LO5 Efficiency | 06 | 06 | Pre/post Q10, capstone row 4 |
| SU Safe use | 02 | 02, every "before you paste", 04 station C, 06 | Pre/post Q4–5, Activity 02, capstone row 5 |
