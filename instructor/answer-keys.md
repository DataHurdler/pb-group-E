# Answer Keys

Instructor only. Don't distribute.

## 01 Spot the fabrication

Errors in [flawed-memo.md](../materials/data/flawed-memo.md), checked against
[telework-policy.md](../materials/data/telework-policy.md).

| # | Memo says | Policy says | Kind | Harm |
| --- | --- | --- | --- | --- |
| 1 | Eligible after **three months** | **Six months** (§2a) | Changed | Ineligible staff apply; supervisors approve in error |
| 2 | Up to **three days** a week | **Two days** (§3) | Changed | Arrangements approved that violate policy |
| 3 | Agreements valid **two years** | Expire **every December 31**; renew in January (§3) | Changed | Lapsed agreements nobody renews |
| 4 | City **reimburses up to $40/month** for internet; "submit receipts to your supervisor monthly" | City **does not reimburse** internet, phone, or utilities (§4). No receipt process exists | Changed (reversed), plus an invented process | Staff submit receipts for money that was never offered. **Expected to be rated most harmful** |
| 5 | Out-of-state telework **never** permitted | Permitted with HR Director's written approval, max 10 working days a year (§5) | Overstated | Staff denied an option the policy allows |
| 6 | Rules follow "**Section 9.2 of the Fair Labor Standards Act**," which "requires public employers to offer telework" | Policy cites no law. The FLSA contains no such provision and doesn't require telework | Invented authority | A fake legal basis in an official memo |
| 7 | Ineligible: operating City vehicles, public contact | City vehicles **or equipment**, and **on-site supervision of field staff** (§2) | Lost caveat | Field supervisors and equipment operators think they're eligible |
| 8 | Either party ends it with 10 days' notice | Also: the City may end it **immediately for performance concerns or operational need** (§6) | Lost caveat | Staff believe they're guaranteed 10 days |

**Correct statements (−1 if flagged):** effective July 1, 2025; core hours
9–3; written agreement signed by employee and supervisor; City-issued laptop;
telework must be in-state; 10 working days' notice; HR at 555-0110.

**Judgement call, don't penalize either way:** "satisfactory performance rating"
for "Meets Expectations or higher" is a softening. It's worth mentioning but not
counted.

**Maximum score:** 8 errors × 3 = 24.

**Part B:** the AI check usually finds the changed numbers and often the
invented reimbursement. It's less reliable on lost caveats (7, 8), and sometimes
flags a correct statement such as core hours, or "satisfactory." Either result
makes the point.

**Debrief:** spend most time on item 6. It's specific, official-sounding, and
entirely made up, which is exactly what confabulation looks like.

## 02 Safe to paste

Part A assumes an agency-approved tool and a work account. Adjust to the
agency's actual policy.

| Card | Colour | Note |
| --- | --- | --- |
| 1 Adopted budget, published | 🟢 | Public |
| 2 Complaint email with name, address, phone | 🔴 | Becomes 🟡/🟢 once replaced with placeholders. **Key teaching card** |
| 3 Internal meeting agenda | 🟡 | Approved tool only. The practical difference from Green: remove any names or personal details first, and remember it may be a record |
| 4 Performance evaluation, name removed | 🔴 | **Removing the name doesn't make it safe:** it's still a personnel record, and the details identify the person. Get help with wording using an invented example instead |
| 5 Job posting, not yet published | 🟡 | 🟢 once published |
| 6 Bid prices before award | 🔴 | Procurement-sensitive |
| 7 Made-up scenario | 🟢 | This is the safe workaround |
| 8 Case-management screenshot | 🔴 | Personal data on many people at once; screenshots are easy to forget about |
| 9 State statute text | 🟢 | Public |
| 10 Security procedures | 🔴 | Security-sensitive |
| 11 Public comments with phone numbers | 🟡 | Public records, but remove the contact details first; you don't need them to summarize. **Usually the most-argued card** |
| 12 Annual-report paragraph | 🟡 → 🟢 | Draft is internal; fine once published |

**Part B, a good cleaned prompt:**

> Draft a reply from [Utility Billing office] to a resident who is upset about
> a $96 late fee on their water bill. They missed the due date because of a
> family medical emergency in August. A supervisor approved waiving the fee as a
> one-time courtesy. Apologize, confirm the fee has been removed, and thank them
> for letting us know. Warm, plain, under 120 words. Use [RESIDENT NAME] as the
> greeting.

- **Removed:** name, email, phone, street address, account number, the child's
  medical condition, the supervisor's name.
- **Kept, because the task needs it:** the fee amount, the general reason, the
  approval, the tone.
- **Added back by hand before sending:** the resident's name, and the account
  reference if your template requires it.

## Park comments

From [park-comments.md](../materials/data/park-comments.md), 17 comments.

| Position | Comments | Count |
| --- | --- | --- |
| Support (incl. conditional) | 1, 3, 5, 9, 13, 16 | 6 |
| Oppose (incl. "not here") | 2, 4, 7, 12 | 4 |
| Neither: concern or question only | 6, 8, 11, 14, 15 | 5 |
| Off-topic | 10 | 1 |
| **Instruction aimed at AI (prompt injection)** | 17 | 1 |

- **Comment 17** opens with "Great project," so counting it as a seventh
  supporter is defensible. Its bracketed text must be flagged, never obeyed. A
  summary that reports unanimous support or no concerns has been injected.
- **Defensible alternatives:** 8 as "oppose this location"; 3 and 13 as
  conditional. Accept any scheme applied consistently, as long as the counts
  match it and add to 17.

| Theme | Comments |
| --- | --- |
| Noise | 2, 12 |
| Parking | 3, 14 |
| Cost and maintenance funding | 4, 15 |
| Safety (children, small dogs) | 7, 13 |
| Community and social benefit | 1, 5, 16 |
| Waste and cleanliness | 6 |
| Alternative location (Ridgeline Park) | 8 |
| Accessibility | 11 |
| Lighting and hours | 12 |

**Personal data:** comment 9 includes a phone number. A good summary omits it.

**Probe question** ("How many commenters live within a block of the park?"):
comment 2 says so ("directly across"), and comment 3 implies it ("spill onto our
block"). A good answer names those and says it can't tell for the rest, because
the comments don't give addresses. **Pass** = it says it can't determine this
for most commenters. **Fail** = it gives a number.

## 04 Stations, what to expect

| Station | Plain version usually… | Technique version should… |
| --- | --- | --- |
| A Ground it | Gives a confident general answer about internet reimbursement and out-of-state work | Say no reimbursement (§4); out-of-state only with HR approval, 10 days a year (§5); "doesn't say" for the dress code and rideshare probes |
| B Show one example | Has the facts, but reads like a form letter; may still imply payment | Same facts, in the example's voice (thanks, one apology, action and timeframe, a personal follow-up line); no copied SR number or dates |
| C Break it down | Miscounts; may include comment 9's phone number; may obey comment 17 | Count 6/4/5 + 1 off-topic + 1 flagged; omit names and numbers |
| D Let it ask | Invents a salary, benefits, or a degree requirement | Ask about salary, closing date, how to apply, language requirement, schedule |
| E Form + flag | Assigns the admin-specialist posting to someone (often Marisol or Tom); gives Priya's notice a date | Write NOT STATED for both; show the 10/17 salt quotes, Ana's same-day delivery check, and Jae's memo with source lines. **Accept either** "10/21" or "a week before 10/28" or NOT STATED for Jae's due date: the notes give it only relatively |
| F Other side | "This is a solid plan" with mild suggestions | Specific risks, with a reason to accept or reject each (below) |

**Station E date check:** Jae's memo is due to Marisol "a week before" 10/28,
which is 10/21. If a model computes the date, check its arithmetic; models often
get relative dates wrong.

**Station F, critiques worth accepting:**
- Copying online reports by hand may *increase* workload if reporting gets
  easier.
- No path for dangerous potholes that need urgent response.
- The form must be accessible (ADA/WCAG) and usable by residents with limited
  English.
- Photos and emails become records with retention and privacy implications.
- The utility-bill notice mails November 20, after the November 3 launch.
- "Fewer calls" isn't a measure of success: no baseline, no target, and nothing
  about repair times.
- No test or pilot before launch.

**Usually weak:**
- generic "cybersecurity concerns";
- "the cost may be high" (the plan says none, though staff time is a fair
  point);
- "residents may not use it" with nothing specific behind it.

## Pre/post check

| Q | Answer | If they chose… it suggests |
| --- | --- | --- |
| 1 | c | a: thinks it's a database. b: thinks it retrieves pages. Revisit Module 01 point 1 |
| 2 | a | b: doesn't see context as the lever. c: over-learned "long prompts are bad" |
| 3 | c | b: thinks asking "are you sure?" checks it. Revisit "flipping isn't checking" |
| 4 | b | c: believes removing a name makes a record safe. Revisit card 4 |
| 5 | a | b: assumes the rest of the summary is clean. c: unaware of injection |
| 6 | c | a/b: believes adjectives or flattery improve output |
| 7 | b | a: role folklore. c: magic-word folklore |
| 8 | a | b: describes style instead of showing it. c: the wrong technique for the problem |
| 9 | c | a: hasn't absorbed one-change-at-a-time |
| 10 | b | a: long chats drift and mix tasks. c: memory is unreliable, invisible to others, and not a template |

Expected most common morning wrong answers: 1a, 3b, 4c, 7a. Replace this
line with what you actually see after the first offering.

## Capstone exemplar

Show for 60 seconds in Module 06, then take it down so participants don't copy
it.

```
USE THIS FOR: replies to picnic-shelter reservation requests
DON'T USE THIS FOR: refunds, complaints, or requests involving a disability
accommodation (route those to the office manager)
CHECK BEFORE USING THE OUTPUT: date, shelter, and fee against the booking system

BEFORE YOU PASTE: replace the requester's name, phone, email, and any account
number with [REQUESTER].

Draft a reply to the reservation request below. I handle picnic-shelter
reservations for a city parks department; the reply goes out by email the
same day.

Audience: a resident who may never have booked before. Plain language, friendly.
Constraints: under 150 words. Use only the rules in <rules>. Don't promise a
date that [AVAILABILITY] doesn't confirm.
Format: first sentence says whether the date is available, based on
[AVAILABILITY: available / not available / alternative dates]. Then the cost,
what's included, and how to pay. End with [SIGNATURE].
If the request asks something the rules don't cover, write "I'll check and get
back to you" instead of answering. After the draft, list anything in the
request you didn't answer.

<rules>
[PASTE CURRENT RESERVATION RULES]
</rules>

<request>
[PASTE REQUEST, PERSONAL DETAILS REPLACED]
</request>

BEFORE YOU SEND, I CHECK:
- [ ] Date and shelter match the booking system
- [ ] Fee matches this year's fee schedule
- [ ] Nothing promised that the rules don't allow
```

**Why it scores Strong on every row:**
- **Clear and structured:** all the slots it needs.
- **Technique fit:** grounding in the rules (the likely failure is invented fees
  or policies) plus a flag line.
- **Tested:** the author ran it on a normal request and on a request for a date
  that's already booked.
- **Reusable:** a header that says where not to use it, and brackets for
  everything that changes.
- **Safe and verifiable:** a before-you-paste line, and a specific send
  checklist.
