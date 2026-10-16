# Course Brief

Status: ready for review

## Title

**AI and LLM Prompt Engineering for Public Service: A First Day with AI**

The course is the government edition of *AI and LLM Prompt Engineering*, the
first course in a five-course AI series. It keeps the series' approved learning
objectives word for word and adds what public employees need on top: the rules
for what may go into a prompt, and who answers for what comes out.

## Catalog description

Generative AI tools like Microsoft Copilot, ChatGPT, Claude, and Gemini can
draft, summarize, and rewrite in seconds, but only if you know how to ask, and
only if you know when not to. This one-day, hands-on course is for government
employees who are new to AI. You'll learn how these tools use your prompt and
context to produce an answer, and the predictable ways they go wrong. You'll
learn what you can and cannot put into a prompt. You'll practise a six-part
structure for writing prompts and ten techniques for harder tasks. You'll learn
how to test and refine a prompt instead of retrying until it looks right, and
how to save it so it keeps saving you time. All practice uses realistic
public-sector tasks: plain-language notices, resident replies, public-comment
summaries, policy FAQs, meeting notes, and job postings. You'll leave with a
tested, reusable prompt for a task from your own job. No technical background
is required.

## Audience

- **Who:** Government employees at any level (federal, state, county, or city)
  in administrative, program, communications, HR, and frontline roles.
- **Assumed:** Comfortable with email, a web browser, and word processing.
- **Not assumed:** Regular use of AI chat tools, any coding, any statistics.
  Most participants will have tried a chatbot at least once. Some will never
  have used one at work, and a few will be skeptical or anxious. Design for
  them.
- **Size:** 12–30 participants at tables of 3–4. One instructor; a second
  helper is strongly recommended above 20.

## Learning objectives

The approved objectives for the series course, unchanged:

| ID | Objective | Taught | Checked by |
| --- | --- | --- | --- |
| LO1 | Explain how large language models use prompts and context to generate responses. | 01 | Pre/post Q1–3; Activity 01 |
| LO2 | Write clear, structured prompts that produce more useful and relevant outputs. | 03 | Pre/post Q6; Activity 03a; capstone row 1 |
| LO3 | Apply prompting techniques to improve accuracy, consistency, format, and usefulness. | 04 | Pre/post Q7–8; Activity 04 stations; capstone row 2 |
| LO4 | Refine prompts through iterative testing and evaluation. | 05 | Pre/post Q9; Activity 05 iteration log; capstone row 3 |
| LO5 | Use prompting strategies that improve efficiency while maintaining output quality. | 06 | Pre/post Q10; capstone row 4 |

Plus one **course-wide standard** for government participants. It is not a
sixth objective; it's a condition on all five.

| ID | Standard | Taught | Checked by |
| --- | --- | --- | --- |
| SU | **Safe use.** Participants decide what may go into a prompt under their agency's rules, recognize pasted text that tries to give orders, and verify output before it leaves their desk, because they are accountable for it. | 02, then every activity | Pre/post Q4–5; Activity 02; capstone row 5 |

## What "comprehensive" means in six hours

Every participant meets the whole field, not just a checklist:

| Area | Covered |
| --- | --- |
| **How it works** | Prediction; context (everything the model can see); context windows and drift; training cutoff; search, reasoning, and deep-research modes; why answers vary |
| **How it fails** | Confabulation; sycophancy; counting and arithmetic; lost caveats and overstatement; prompt injection; automation bias on our side |
| **Structure** | Six slots (Task, Context, Audience, Constraints, Format, Examples), with Role as an optional extra; diagnosing a weak prompt from its output; how Microsoft's, Google's, OpenAI's, and GovTech Singapore's frameworks cover the same core |
| **Techniques** | Ground it (quote first), mark your material, give it a form, show one example, break it down, let it ask, flag what it made up, let it think, get the other side, improve my prompt |
| **Testing** | Criteria first and checkable; test cases including a hard one and an out-of-scope probe; one change at a time; run twice; the verification checklist; the limits of AI checking AI |
| **Efficiency** | Templates with brackets; a prompt library; saved setups (custom instructions, projects, Gems, agents); turning a conversation into a reusable prompt; when *not* to use AI |
| **Safe use** | Approved accounts; the traffic light; records; disclosure; high-impact uses; real cases |

The sources behind each claim are in
[handouts/further-reading.md](handouts/further-reading.md) and
[handouts/technique-reference.md](handouts/technique-reference.md).

## Scope

**In scope.** Chat-based AI assistants used through a web or desktop interface:
writing, summarizing, rewriting, extracting, organizing, critiquing, and
brainstorming. Safe and accountable use at the level of the person writing the
prompt. Techniques that work in any major tool.

**Out of scope**, and where it goes instead:

| Topic | Response |
| --- | --- |
| How models are trained; types of machine learning; choosing a model | *Introduction to AI and Machine Learning* (series course) |
| Agents, automation, connecting AI to other systems | *Building an AI Agent* (series course). "An agent's instructions are a prompt, so today is the foundation." |
| Organizational AI governance, policy writing, bias audits | *AI Ethics and Governance* (series course); agency CIO / AI governance office |
| Spreadsheet analysis and charts | *Data Analytics, Cleaning and Visualization in Excel* (series course) |
| Legal questions on specific use cases | Agency counsel and records officer; parking lot |
| Buying an AI product | Agency CIO / procurement |
| Image, audio, and video generation | Mention only |

## Design decisions

1. **Approved objectives, government standard.** The series objectives are fixed.
   Safe use is a standard every objective is practised under, not a sixth
   objective that competes for time.
2. **Six slots, not an acronym.** Plain slot names are easier to apply
   correctly than a memorable acronym, and they map onto every vendor's
   framework. Role is optional, because the evidence is that personas change
   tone, not accuracy.
3. **Name the failure before the technique.** Every technique is introduced by
   the problem it fixes, and every station runs the plain version first.
4. **Tool-neutral.** Agencies approve different tools. Tool-specific setup lives
   only in [instructor/setup-and-tech.md](instructor/setup-and-tech.md).
5. **Fictional data only, all day.** All practice material is set in the
   fictional *City of Brookfall*, [materials/data/](materials/data/), including
   a planted prompt injection. The data rule is modelled, not just taught.
6. **One prompt grows all day.** Each participant's own task runs from the
   8:34 introductions through to the capstone.
7. **Safety early, then everywhere.** Data rules come at 10:15, then recur as
   a "before you paste" line on every activity sheet.
8. **Variability is curriculum.** Different answers to the same prompt are
   taught, not apologized for. Instructors never promise a demo output.
9. **Read the prompt, not just the output.** Share-outs show prompts, so the
   room learns what caused a result.

## Assumptions to confirm with the host agency

| # | Assumption | If different |
| --- | --- | --- |
| A1 | 8:30–4:00: six instructional hours, two 15-minute breaks, a 60-minute lunch | Shift all clock times; the minute budget in [schedule.md](schedule.md) holds |
| A2 | In person, one laptop per participant, Wi-Fi | Online: see [instructor/setup-and-tech.md](instructor/setup-and-tech.md#running-it-online) |
| A3 | Every participant can sign in to an agency-approved AI tool with an agency account before the day | **Biggest risk.** Without it, pair participants, or run demo-only for blocked participants. Never send them to personal accounts |
| A4 | The agency has a written AI use policy the instructor can quote | If none exists, teach the conservative default in [handouts/safe-to-paste.md](handouts/safe-to-paste.md) and say so |
| A5 | No credit or certification attached | If there is one, the post-check and capstone rubric become graded |

Fill in before the day:

- **Host agency:** [TODO]
- **Approved AI tool(s) and account type:** [TODO]
- **Agency AI policy link and owner:** [TODO]
- **Disclosure rule for AI-assisted documents:** [TODO]
- **Records officer / privacy contact to name in Module 02:** [TODO]
- **Date, venue, instructor(s):** [TODO]
