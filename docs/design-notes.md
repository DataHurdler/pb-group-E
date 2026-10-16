# Design Notes: Where This Course Came From

Status: ready

## Revision of October 16, 2026

The first version (commit `037c886`) was a 330-minute course built around a
five-part acronym (CRAFT). It was revised for three reasons:

- to give first-time users a **comprehensive** understanding of prompt
  engineering;
- to fit **six instructional hours with two breaks and a lunch**;
- to align with the instructor's series course and with what the other groups
  built.

### What changed

| | Before | After |
| --- | --- | --- |
| Day | 9:00–4:00, 330 instructional minutes | 8:30–4:00, **360**, two breaks + lunch |
| Objectives | Six rewritten objectives | The five **approved** series objectives, verbatim, + a safe-use standard |
| Framework | CRAFT (no Constraints or Examples slot) | **Six slots** + diagnose-from-output + map of vendor frameworks |
| Techniques | 4 | **10**, each introduced by the failure it fixes |
| Safety | Inside Module 01 | Its own block at 10:15, plus a thread through every activity; prompt injection; corrected wording on records, high-impact uses, accounts |
| Testing | Criteria, one change at a time | + checkable criteria, test inputs (normal / hard / probe), run twice, limits of AI checking AI |
| Reuse | Template | + library entries, saved setups, meta-prompting, efficiency including checking time, when not to use AI |
| Evidence | — | Real cases, sources for every claim, a timing checker |

## Research basis

Three research passes, October 16, 2026. The sources are listed in
[../handouts/further-reading.md](../handouts/further-reading.md) and
[../handouts/technique-reference.md](../handouts/technique-reference.md).

1. **Prompt-engineering practice.**
   - Vendor guides: Anthropic, OpenAI, Google, Microsoft, and GovTech
     Singapore's CO-STAR.
   - Surveys and studies: the *Prompt Report*; Wharton's *Prompting Science
     Reports* on personas, chain-of-thought, and tips/threats; work on
     sycophancy, long context, and LLM-as-judge bias.

   Main conclusions:
   - Every framework shares one core, so plain slots are taught and the
     frameworks are mapped onto them.
   - Personas change tone, not accuracy.
   - With reasoning models, choosing the mode beats typing "think step by step."
   - ALL CAPS and threats don't help.
   - Grounding is the most valuable single technique.
   - Prompt injection is ranked #1 in OWASP's Top 10 for LLM applications, and
     it matters to anyone pasting documents.
2. **Government guidance.**
   - Federal: OMB M-25-21 ("high-impact" AI), NIST AI 600-1, NARA AC 11.2026.
   - State and city employee policies: NJ, NYC, Boston, Seattle, San Jose,
     Washington, California, Pennsylvania, Utah.
   - Public-records reporting and commentary.

   It led to three corrected statements:
   - **Records:** "may be public records, even in a personal account"; no court
     has yet ruled squarely, as far as we found in October 2026; federal records
     status depends on use (NARA AC 11.2026, verified).
   - **People decisions:** "high-impact," allowed only through approved systems
     with safeguards, not "never."
   - **Accounts:** personal accounts are often prohibited and don't escape
     records law; an approved tool isn't approved for every data type.

   It also produced five teaching cases, and the note that EO 13166 on language
   access was revoked in 2025 (so the course says "qualified human translator"
   without citing it).
3. **The instructor's reference design** (`prompt-engineering` repo). Taken
   from it:
   - the approved objectives;
   - slots over acronyms, with Role marked as overrated;
   - diagnose from the output;
   - name the failure before the technique;
   - "give it a form";
   - marking material as an injection defence;
   - checkable criteria;
   - library entries with "what good looks like / where it goes wrong";
   - "when not to use AI";
   - efficiency rules (reuse beats rewriting; a fresh chat beats arguing);
   - "read the prompt, not the output";
   - never promising a demo;
   - series forward references.

## Ideas adopted from the other groups

All five sibling repos were reviewed after their October 16 updates.

| From | Idea | Where it went |
| --- | --- | --- |
| pb-group-A | One prompt that grows all day | Index card at 8:34 → capstone |
| pb-group-A | Prompt bake-off with blind judging | Extra-time option in [schedule.md](../schedule.md) |
| pb-group-A | "Clean this prompt": show a risky prompt, don't run it, rewrite with placeholders | Activity 02 Part B |
| pb-group-B | Typed error taxonomy incl. lost caveat; AI claim-check with "NOT IN SOURCE" and "did it flag anything correct?" | Activity 01; verify checklist |
| pb-group-B | Cumulative one-slot-at-a-time rebuild, new chat per version | Activity 03a |
| pb-group-B | Cold template swap: write down every question you wanted to ask | Activity 06 |
| pb-group-B | Monday card item: a task you've decided *not* to use AI for; 30-day follow-up | Module 07; follow-up email |
| pb-group-B | "Removing names doesn't make it releasable" | Card 4 in Activity 02 |
| pb-group-C | Use-case split: AI does · AI helps, I decide · Me only; time saved *including checking* | Module 06; Activity 06 |
| pb-group-C | Template header `USE THIS FOR / DON'T USE THIS FOR / CHECK BEFORE USING` | Activity 06 skeleton |
| pb-group-C | Reading pre/post results: items too easy in the morning get replaced | Feedback form notes |
| pb-group-D | "Poke the model" with a fictional organization's policy: invented vs refusal | Module 01 Demo B |
| pb-group-D | Out-of-scope probe question as a test case | Station A; Activity 05 |
| pb-group-D | Navigator/driver/checker roles | Activities 01 and 04 |
| pb-group-D | "I don't know yet" option on the pre/post check | Pre/post check |
| pb-group-D | "Turn this conversation into a single prompt" | Technique 10; Module 06 |
| pb-group-D | A script that checks the timing adds up | [tools/check_timing.py](../tools/check_timing.py) |
| pb-group-F | Fabrication-hunt scoring with a penalty for false accusations | Activity 01 |
| pb-group-F | "Are you sure?" sycophancy demo with predictions first: "flipping isn't checking" | Module 01 Demo D |
| pb-group-F | Red-team with accept/reject for each critique | Station F |
| pb-group-F | Reverse-engineer the prompt | Extra-time option |

### Pitfalls seen elsewhere and avoided

| Pitfall | Seen in | How this course avoids it |
| --- | --- | --- |
| "It predicts; it doesn't look things up" as an absolute | A, B, C | Taught alongside search, reasoning, and file modes |
| Role as a required element | D | Role is optional, with the evidence |
| "Think step by step" taught without reference to reasoning models | A | Technique 8 explains the change |
| "Are you sure?" offered as a check | A | Shown as a flip, not a check |
| Self-critique presented as verification | B, C, D | Self-checks presented as useful but not sufficient |
| Personal or free accounts recommended for government work | A | Agency-managed accounts only |
| Pre/post codes built from personal details | D | Neutral code words |

## Review and verification

After the rewrite, an independent read-only review checked every file against
every other one: clock times, activity minutes, data counts, cross-references,
leftovers, and policy wording. Its findings were fixed, including:

- **Station logistics:** pairs now stay at their tables, with a full set of
  sheets on every table.
- **Pre/post check:** the options were shuffled so the answer key isn't
  predictable.
- **Federal policy wording:** OMB M-25-21 is no longer presented as the course's
  own rule.
- **Error definitions:** a reversed fact is now classed as "Changed."
- **Station B:** now changes one variable.
- **Station D:** its answers moved to a face-down card.
- **New materials:** a score card for Activity 01 and prepared outputs for the
  Module 03 diagnose drill.

Claims checked against primary sources on October 16, 2026:

| Claim | Source | Result |
| --- | --- | --- |
| New York City prohibits personal accounts for city GenAI work | NYC OTI *Use Guidance: Generative AI* | Verified: "Using personal accounts is prohibited by citywide cybersecurity policies" |
| NARA: AI use alone doesn't create a federal record | NARA AC 11.2026 (Aug 21, 2026) and its PDF guidance | Verified: use does not "in and of itself, result in the creation of federal records" |
| Washington cities' ChatGPT logs, comment-summary error, undisclosed grant letter | Cascade PBS, Aug 2025 | Verified; case 5 corrected to the reported details (Everett, Bellingham) |

Not independently re-verified here, so check them before teaching:

- the other case links;
- the vendor documentation pages, which change with each model;
- OMB M-25-21 still being in force.
