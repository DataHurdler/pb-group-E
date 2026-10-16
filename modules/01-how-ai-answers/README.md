# 01 How AI Answers, and Using It Safely

Status: ready
Time: 9:30–10:30 (60 min) · Talk 22 / do 38
Outcomes: LO1, LO2

## Purpose

Give participants one accurate mental model of what an AI assistant is doing,
so that its failures stop being surprising, and the rules for what never goes
into a prompt, before they write a serious one.

## By the end of this block, participants can…

- Explain that an LLM predicts likely text rather than looking up facts, and
  name three resulting failure modes (LO1)
- Find fabricated and changed claims by checking output against a source (LO1)
- Sort information into green, yellow, and red for prompting, and say who is
  accountable for the output (LO2)

## Timed outline

| Min | Segment | Format | What happens |
| --- | --- | --- | --- |
| 0–4 | Hook | Whole room vote | "When you ask an AI a question, where does the answer come from?" (a) it searches the web, (b) it looks it up in a database, (c) it predicts what words should come next. Hands up, no answer yet |
| 4–14 | How it works | Lecture | Talking points A |
| 14–29 | Spot the fabrication | Groups | [Activity 1A](../../activities/1A-spot-the-fabrication.md) |
| 29–34 | Debrief | Whole room | Each group names its most harmful error; reveal the [answer key](../../instructor/answer-keys.md#1a-spot-the-fabrication) |
| 34–42 | Using it safely | Lecture | Talking points B |
| 42–52 | Safe to paste? | Groups | [Activity 1B](../../activities/1B-safe-to-paste-sort.md) |
| 52–58 | Debrief | Whole room | Each group shares its most-argued card; settle 2, 6, 8, and 11 using the [key](../../instructor/answer-keys.md#1b-safe-to-paste) |
| 58–60 | Bridge | Instructor | "It writes well and checks nothing, so the quality of what you get depends on what you give it. That's the next block." |

## Talking points A: how it works (10 min)

1. **Answer to the hook: (c), mostly.** The model has read an enormous amount of
   text and learned which words tend to follow which. It writes one piece at a
   time, picking a likely next piece. Some tools can also search the web or read
   your files, but the writing is still prediction.
2. **So it's good at** anything where "sounds like good writing" is most of the
   job: drafting, rewriting, summarizing *text you give it*, changing tone or
   reading level, organizing messy notes, brainstorming options.
3. **And it fails in predictable ways:**
   - **Fabrication.** When it doesn't know, it still produces something that
     looks like an answer: a policy section, a statistic, a court case. It
     doesn't feel uncertain the way you would.
   - **It doesn't know your world.** Not your agency's policies, not last
     month's council vote, not what "the usual form" means, unless you tell it.
     Its knowledge stops at a training date.
   - **Agreeable and inconsistent.** It tends to go along with your framing
     ("Why is this policy good?") and can give a different answer if you ask
     again.
   - **Weak at exact counts and arithmetic** without a calculator tool.
4. **Mental model:** a very fast, very well-read new hire on their first day,
   who never says "I don't know." Brilliant for a first draft; you'd never send
   their work out unchecked.
5. **It only knows what's in this conversation**, plus whatever memory or
   custom-instruction features you've turned on. That's why a new chat for a
   new task matters.

Keep this at intuition level. If someone asks about neural networks, tokens, or
training, give one sentence and offer to talk at the break.

## Talking points B: using it safely (8 min)

Before this block, fill in the agency specifics in
[COURSE-BRIEF.md](../../COURSE-BRIEF.md#assumptions-to-confirm-with-the-host-agency).

1. **Approved tools only.** Name the agency's approved tool(s) and policy. A
   personal account on a public website has different data terms from an
   agency-licensed one, even under the same brand name.
2. **The traffic light** from [safe-to-paste.md](../../handouts/safe-to-paste.md).
   Walk through one example of each colour.
3. **Records.** In many jurisdictions, prompts and outputs created for public
   business can be public records and may be discoverable. Name the records
   officer. Rule of thumb: write prompts you'd be comfortable seeing published.
4. **You own the output.** "The AI wrote it" is not a defence for an error in
   a letter you sent.
5. **Not for decisions about people.** Eligibility, hiring, discipline,
   enforcement, benefits. Bias, explainability, and due process make these
   legally and ethically different.
6. **The fix is usually easy:** remove or make up the identifying details. You
   rarely need the real name to get help with the wording.

## Materials

- Slides: [deck](../../slides/course-day.qmd), section 01
- [telework-policy.md](../../materials/data/telework-policy.md),
  [flawed-memo.md](../../materials/data/flawed-memo.md), printed one per group
- 1B cards, printed and cut, one set per group
- [safe-to-paste.md](../../handouts/safe-to-paste.md), one per person

## Check for understanding

During the 1A debrief, ask: "Where did the FLSA citation come from?" You want to
hear "it predicted something that sounded like a legal basis." If you hear "it
looked it up wrong," revisit talking point 1.

## Common problems

| Problem | Response |
| --- | --- |
| "But mine gave a correct answer" | Good, and it would have sounded the same if it were wrong. That's the point |
| Groups find only 2–3 memo errors | Hint: "Check every number." Then: "Check the legal citation." |
| Card-sort argument about public comments (card 11) | Good argument. They're public records, but you still don't need the phone numbers to summarize them. Remove them |
| Questions about agency policy you can't answer | Parking lot; promise an answer in the follow-up email, and get one |

## Instructor notes

- Talking points B is the most important 8 minutes of the day for the agency.
  Don't let it slip to save time; cut the card sort to six cards instead.
- Avoid scare stories. The tone is "here's how to do this right," not "AI is
  dangerous."
