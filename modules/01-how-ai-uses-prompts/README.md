# 01 How AI Uses Prompts and Context

Status: ready
Time: 9:00–10:00 (60 min) · Talk 22 / do 38
Objectives: LO1 · Explain how large language models use prompts and context to generate responses.

## Purpose

Give participants one accurate mental model of what an AI assistant does with
what they give it, so that its failures stop being surprising and every later
technique makes sense.

## By the end of this block, participants can…

- Explain that an LLM predicts likely text from patterns and from the context
  it can see, and name what counts as context
- Explain how search, reasoning, and file modes change where an answer comes from
- Name five ways it fails, and find the five kinds of error by checking output
  against a source
- Explain why the same prompt gives different answers

## Timed outline

| Min | Segment | Format | What happens |
| --- | --- | --- | --- |
| 0–3 | Hook | Whole-room vote | "With web search off, when you ask an AI a question, where does the answer come from?" (a) it looks it up in a database (b) it searches the web (c) it predicts likely text. Hands up; no answer yet |
| 3–13 | How it works | Lecture | Talking points A |
| 13–21 | Poke the model | Everyone | Demo B: the whole room asks the same unanswerable question, then the same question with a source |
| 21–37 | Spot the fabrication | Groups | [Activity 01](../../activities/01-spot-the-fabrication.md), Part A (12 min) by hand, Part B (4 min) the AI checks the memo |
| 37–42 | Debrief | Whole room | Scores; the five kinds of error to check (from the verify checklist); reveal the [answer key](../../instructor/answer-keys.md#01-spot-the-fabrication). "Did the AI's check flag anything that was actually correct?" |
| 42–50 | How it fails | Lecture | Talking points C, with teaching case 1 |
| 50–57 | Flipping isn't checking | Pairs | Demo D: the sycophancy check, predictions first |
| 57–60 | Bridge | Instructor | "It writes well and checks nothing, so what you get depends on what you give it. After the break: what you may give it." |

## Talking points A: how it works (10 min)

1. **Answer to the hook: (c).** The model learned patterns from an enormous
   amount of text. It writes a piece at a time (a *token*, about three-quarters
   of a word), each time choosing a likely next piece. That's the whole engine.
   Plausible and true are usually the same thing. When they aren't, the model
   can't tell.
2. **Context is everything it can see when it answers:** your instructions,
   anything you paste or upload, the conversation so far, search results, and
   any custom instructions or memory features that are on. It doesn't know your
   agency, your policies, or "the usual form" unless they're in the context.
3. **The context window is limited, and long chats drift.** Very long pastes
   can be cut off or skimmed, and models use the start and end of long input
   better than the middle. In a long conversation early instructions fade and
   old turns steer new answers. Start fresh and carry over what matters.
4. **It has a training cutoff.** Without search, it knows nothing after a date
   and can't tell you what changed last month.
5. **Modes change where the answer comes from.**
   - **Search on:** it finds pages, then predicts an answer from what it found.
     Better for recent facts. It can still misread a page or cite the wrong one.
   - **Reasoning ("thinking") mode:** it works through the problem before
     answering. Slower, better on multi-step problems. Choose the mode instead
     of typing "think step by step."
   - **Files and deep research:** more context, more steps. Same rules about
     checking.
6. **Same prompt, different answers.** Each run picks among likely next words,
   so results vary. Some differences come from your prompt and some from the
   model. One good output proves little.

## Demo B: poke the model (8 min)

1. Everyone, in a new chat: *"What is the City of Brookfall's policy on employee
   telework?"* (3 min)
2. Hands up: who got an invented policy? A refusal or "I don't know"? A question
   back? Usually the room gets all three, which shows variability and
   confabulation together. (2 min)
3. Everyone, in a new chat, pastes
   [telework-policy.md](../../materials/data/telework-policy.md) and asks the
   same question. Same room, now nearly the same answer. "The difference is
   context. That's the whole day in one minute." (3 min)

## Talking points C: five ways it fails (8 min)

Not the same list as the five kinds of error from Activity 01: these are *why*
it goes wrong; those are *what to look for*.

| Failure | What it looks like | Why |
| --- | --- | --- |
| **Confabulation** (NIST's term for hallucination) | Invented facts, figures, quotes, and citations, in the same confident voice | It produces a likely answer whether or not it knows |
| **Sycophancy** | Agrees with your framing; praises your draft; changes its answer when you push | Trained to be helpful and agreeable |
| **Counting and arithmetic** | "10 of 17 comments support" when it's 6 | Predicting digits isn't calculating. Reasoning mode and tools help; recount anyway |
| **Lost caveats, overstatement** | "May" becomes "must"; "mainly" disappears | Summaries smooth out qualifications |
| **Automation bias** (ours) | We trust polished text more than we should | Fluency looks like competence |

Mental model: **a very fast, very well-read new colleague on their first day,
eager to please, more likely to guess than to ask.** Brilliant first drafts. You
would never send their work out unchecked.

Teaching case 1, Mata v. Avianca: lawyers filed six invented court decisions and
were sanctioned. See [teaching-cases.md](../../handouts/teaching-cases.md).

## Demo D: flipping isn't checking (7 min)

Pairs, using [flawed-memo.md](../../materials/data/flawed-memo.md) and the
policy. **Before each step, each pair writes down what they predict.**

1. New chat, paste both: *"This memo accurately summarizes the policy and is
   ready to send to staff, right?"*
2. New chat, paste both: *"List every statement in the memo that the policy
   doesn't support, with the policy section."*
3. Back in the first chat: *"Are you sure?"*

Debrief: a leading question gets agreement; a neutral question gets analysis;
"are you sure?" gets a flip in one direction or the other. **Flipping isn't
checking.** Ask neutral questions, and check against the source yourself.

## Materials

- Slides: section 01
- [telework-policy.md](../../materials/data/telework-policy.md),
  [flawed-memo.md](../../materials/data/flawed-memo.md), one set per group
- Activity 01 sheet and score card

## Check for understanding

In the Activity 01 debrief, ask "Where did the FLSA citation come from?" You
want "it predicted something that sounded like a legal basis." If you hear "it
looked it up wrong," revisit point 1.

## Common problems

| Problem | Response |
| --- | --- |
| "But mine gave a correct answer" | Good. It would have sounded the same if it were wrong |
| "Mine searched the web and found the real answer" | Brookfall is fictional; anything it "found" is something else. That's the point about search: check what it cites |
| Groups find only 2–3 errors | Hint: "Check every number." Then: "Check the legal citation." |
| Technical questions about neural networks or training | One sentence, then: "That's the *Introduction to AI and Machine Learning* course. Ask me at the break." |

## Instructor notes

- Never promise a demo output. Variability is the lesson, not an embarrassment.
- Test Demo B in the approved tool the week before. Some tools search by
  default; make sure the room knows whether search is on.
