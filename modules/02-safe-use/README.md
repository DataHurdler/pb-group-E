# 02 Safe and Accountable Use

Status: ready
Time: 10:15–10:45 (30 min) · Talk 12 / do 18
Objectives: SU (safe-use standard); LO1 reinforced (pasted text is context too)

## Purpose

Give government participants the concrete rules for what may go into a prompt
and who answers for what comes out, before they write a serious prompt, and
show that pasted material can try to give the AI orders.

## By the end of this block, participants can…

- Apply the five before-you-paste questions and the traffic light
- Remove or replace identifying details so a task can still be done
- Explain records, disclosure, and high-impact-use rules at the level of the
  person writing the prompt
- Recognize prompt injection, and mark pasted material to reduce it

## Timed outline

| Min | Segment | Format | What happens |
| --- | --- | --- | --- |
| 0–3 | Hook | Instructor | Teaching case 5: Washington cities' ChatGPT logs released under public-records requests, including an AI summary that described broadly supportive public comments as raising "significant concerns." "Would your chats survive that?" |
| 3–11 | The rules | Lecture | Talking points |
| 11–19 | Safe to paste? | Groups | [Activity 02](../../activities/02-safe-to-paste.md) Part A: card sort |
| 19–25 | Clean this prompt | Pairs | Activity 02 Part B: rewrite a risky prompt with placeholders, **without running the original** |
| 25–29 | Debrief | Whole room | The most-argued card; what each pair removed and what they kept. Settle cards 2, 4, 6, 8, 11 with the [key](../../instructor/answer-keys.md#02-safe-to-paste) |
| 29–30 | Bridge | Instructor | "Now you know what goes in. Next: how to structure it." |

## Talking points (8 min)

Fill in the agency specifics from
[COURSE-BRIEF.md](../../COURSE-BRIEF.md#assumptions-to-confirm-with-the-host-agency)
first. Where the agency's policy is stricter than these points, it wins.

1. **Agency account, approved tool.** Personal and free accounts often let the
   vendor keep or train on what you type. Many governments, New York City among
   them, prohibit them for work outright. And an approved tool may still not
   be approved for every kind of data: CJIS, HIPAA, and federal tax data each
   need their own approvals.
2. **Five questions and the traffic light**, from
   [safe-to-paste.md](../../handouts/safe-to-paste.md). One example of each
   colour.
3. **Records.** Prompts and outputs used for government business may be public
   records, even in a personal account. As of October 2026 we know of no court
   ruling squarely on AI chats, but agencies have already released them in
   response to requests (teaching case 5); ask counsel for your jurisdiction.
   Federal staff: NARA's August 2026 guidance (AC 11.2026) says using AI does
   not "in and of itself" create federal records, but what you rely on,
   circulate, or keep may be one. Name
   the records officer. Don't use logged-out or temporary chats to avoid
   recordkeeping.
4. **Disclosure.** Many governments require you to say when content was
   generated or substantially assisted by AI. State the agency's rule.
5. **Decisions about people.** Our rule: don't use a general-purpose chatbot
   to make, recommend, or substantially inform a decision about a person's
   eligibility, benefits, employment, discipline, or enforcement. For
   comparison, federal agencies under OMB M-25-21 must apply minimum risk
   practices (testing, an impact assessment, human oversight, a chance to
   appeal) to "high-impact" AI whose output is a principal basis for such
   decisions. State and local rules vary; state the host's.
   **Public-facing tools need testing too.** Teaching case 4: NYC's MyCity
   chatbot told businesses things that were illegal.
6. **Pasted text can give orders.** *Demo, 1 minute:* show comment 17 in
   [park-comments.md](../../materials/data/park-comments.md). "If you paste this
   into a summary prompt, the AI may obey it. That's prompt injection. OWASP
   ranks it number one in its Top 10 risks for AI applications." Defence: mark where pasted
   material starts and ends, say it's data, read the output for signs it obeyed
   the material, and never let AI act on untrusted text unsupervised. Station C
   this afternoon tests it.
7. **You sign it, you own it.**

## Materials

- Slides: section 02
- [safe-to-paste.md](../../handouts/safe-to-paste.md), one per person
- Activity 02 cards, printed and cut, one set per group
- [teaching-cases.md](../../handouts/teaching-cases.md), cases 4 and 5

## Check for understanding

Part B is the check. A good rewrite keeps everything needed for the task (the
issue, the amount, the approved waiver) and nothing that identifies anyone.
If a pair deleted the details the AI actually needed, that's a useful finding
too: "What's the least it needs to know?"

## Common problems

| Problem | Response |
| --- | --- |
| "Then I can't use it for anything" | Most writing tasks don't need the real name. Show the placeholder rewrite |
| "Our agency hasn't said anything" | Then use the conservative default, and ask your supervisor which tool is approved. Parking lot for the policy owner |
| Questions you can't answer about agency law | Parking lot; promise a written answer, and get one |
| Participants want to debate whether AI is good for government | Valid, and that's the *AI Ethics and Governance* course. Today: the practitioner's rules |

## Instructor notes

- This is the most important 30 minutes for the host agency. If the morning
  runs late, cut the card sort to six cards, never the talking points.
- Keep the tone factual: "here's how to do this right," not "AI is dangerous."
- Don't state a disclosure rule as government-wide; it varies. State the host's.
