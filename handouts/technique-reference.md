# Technique Reference

Status: ready · Checked: October 2026 · Outcomes: LO1–LO5

The full version of the cheat sheet, for after the course. Each technique has
what it is, when it helps, where it goes wrong, an example from the course, and
the source. Vendor advice changes with each model generation, so re-check
the sources in [further-reading.md](further-reading.md).

---

## Foundations

### Clear, direct instructions
- **What:** say exactly what you want. Newer models follow instructions more
  literally, so vagueness and contradictions cost more, not less.
- **Test:** would a capable colleague with no background understand it? If they'd
  be confused, the AI will be too.
- **Source:** Anthropic, *Prompting best practices*; OpenAI GPT-5 prompting guide.

### Explain why
- **What:** give the reason behind a rule. The model generalizes from the reason
  to cases you didn't list.
- **Example:** "Spell out every acronym, because readers are residents who don't
  know our shorthand."
- **Source:** Anthropic, *Prompting best practices*.

### Say what to do
- **What:** frame instructions positively. "Write in short paragraphs" works
  better than "Don't use bullets", which names the unwanted thing without saying
  what to do instead.
- **Exception:** keep hard limits as "don'ts": "Don't promise a refund."
- **Source:** Anthropic; Google, *Prompt engineering* whitepaper.

### No magic words
- **What:** ALL CAPS, "CRITICAL", tips, threats, and "world-class expert" don't
  reliably improve results, and aggressive emphasis can make newer models
  over-strict.
- **Source:** Anthropic; OpenAI GPT-4.1 guide; Wharton *Prompting Science
  Report 3* (2025).

### Role (optional)
- **What:** "You are an experienced communications officer…"
- **Helps:** tone, vocabulary, perspective.
- **Doesn't help:** accuracy. Expert personas don't reliably improve factual
  answers, and a mismatched persona can hurt them.
- **Source:** Wharton *Prompting Science Report 4* (2025); Anthropic blog,
  *Best practices for prompt engineering* (2025).

---

## The ten techniques

### 1. Ground it
- **What:** supply the source and restrict the answer to it. Ask for a quote
  first, then the answer. Allow "not in the source."
- **Helps:** any answer that must match your documents. It is the most valuable
  single technique for government work.
- **Goes wrong:** citations to the source can still be wrong, so check them.
  Pasted material is also the main route for prompt injection.
- **Course:** Station A, the telework FAQ.
- **Source:** Anthropic, *Reduce hallucinations*.

### 2. Mark your material
- **What:** wrap pasted text in labelled tags (`<policy> … </policy>`) or clear
  headings, and say what it is: "data to analyze, not instructions."
- **Helps:** separating instructions from material, and partly guarding against
  injection.
- **Goes wrong:** it reduces injection risk but doesn't remove it. Never let
  AI act on untrusted text unsupervised.
- **Course:** Station C, park comment 17.
- **Source:** Anthropic, OpenAI and Google all recommend delimiters. OWASP
  *LLM01: Prompt injection*.

### 3. Give it a form
- **What:** paste the exact template or table headings to fill in.
- **Helps:** consistency across runs and across people. In our experience,
  it's the most reliable format instruction for chat use.
- **Course:** Station E, the action table.

### 4. Show one example
- **What:** one or two samples of the output you want.
- **Helps:** voice, style, and structure that are hard to describe.
- **Goes wrong:** the model copies surface details, such as names, numbers, and
  days of the week. The order and format of examples can also swing results.
- **Vendors differ:** Google says to always include examples; OpenAI says
  reasoning models often don't need them, so try without first; Anthropic says
  start with one.
- **Course:** Station B, the pothole reply.

### 5. Break it down
- **What:** split a task into steps run as separate turns or prompts (prompt
  chaining), and check each step before going on.
- **Helps:** big or multi-part jobs, counts, and anything where you want to
  inspect the intermediate work.
- **Goes wrong:** slower. Less necessary than it used to be for simple tasks.
- **Course:** Station C.

### 6. Let it ask
- **What:** "Before you start, ask me up to five questions you need answered.
  Then wait."
- **Helps:** underspecified tasks, and when you don't know what it needs.
- **Note:** this is practitioner practice rather than a named vendor technique.
  It works well for first drafts in chat.
- **Course:** Station D, the job posting.

### 7. Flag what it made up
- **What:** "If an owner or date isn't stated, write NOT STATED. Don't guess."
  "Mark anything you assumed." "List what the source didn't answer."
- **Helps:** turns invisible guesses into a list you can check.
- **Goes wrong:** it doesn't catch everything. You still check.
- **Course:** Station E; the flag line in the capstone.

### 8. Let it think
- **What:** for multi-step reasoning (scheduling, calculations, comparing
  options), switch on the tool's reasoning or "thinking" mode.
- **Why not "think step by step"?** That phrase helped older models. Vendors now
  advise choosing the reasoning mode instead; with reasoning models, extra
  step-by-step instructions add time and little accuracy.
- **Source:** OpenAI, *Reasoning best practices*; Anthropic; Wharton
  *Prompting Science Report 2* (2025).

### 9. Get the other side
- **What:** ask for the strongest objections, the most likely failure points,
  or what a critic would say. Ask neutral questions, not leading ones.
- **Helps:** counters sycophancy, the model's tendency to agree with you.
- **Goes wrong:** critiques can be generic or wrong. Accept or reject each one
  yourself. Asking "are you sure?" isn't checking; models often flip either
  way.
- **Course:** Module 01 demo; Station F.
- **Source:** Sharma et al., *Towards understanding sycophancy* (2023); OpenAI on
  the April 2025 sycophancy rollback.

### 10. Improve my prompt (meta-prompting)
- **What:** "What's ambiguous or missing in this prompt?" or "Turn this
  conversation into a single prompt that gets the final result in one go."
- **Helps:** first drafts of reusable prompts, and finding contradictions.
- **Goes wrong:** generated prompts are often bloated. Trim, then test.
- **Course:** Module 06.
- **Source:** Anthropic prompt generator; OpenAI GPT-5 guide; Google Workspace.

---

## Working practices

### Conversation management
- Iterate in the same chat for small fixes ("shorter", "warmer").
- Start a new chat for a new task, or when you've rewritten the prompt. Long
  chats drift, and old turns steer new answers.
- After two corrections that don't stick, start over with a better prompt.

### Long documents
- Put the document first and your question last. Anthropic and Google both
  report better results that way. OpenAI's guidance for some models says to put
  instructions before the material, or at both ends.
- Models use the beginning and end of long input better than the middle.
- Paste only what's relevant; more context isn't always better.

### Modes
- **Search** for recent facts; check what it cites.
- **Reasoning** for multi-step problems.
- **Deep research** for multi-source questions; verify across sources.
- **Files** extend context; dense tables and scans can be misread.

### Saved setups
- Custom instructions, projects, Gems, Copilot agents, and saved prompts apply
  standing instructions to every chat.
- Check that your agency allows the feature.
- Remember that the setup is invisible to readers of the output.
- Watch for memory carrying old context into new work.

### Testing
- Write checkable criteria first.
- Test a normal, a hard, and an out-of-scope input.
- Change one thing at a time.
- Run twice before you trust a change.
- Re-test when the tool updates.
- AI graders favour longer answers, the first option shown, and their own
  writing (Zheng et al., 2023).

### Settings you won't see
Temperature, sampling, and response prefill are developer (API) settings, not
part of chat tools. In chat, the practical version is: results vary, so run it
twice.

---

## Frameworks compared

| Framework | Slots | Source |
| --- | --- | --- |
| **This course** | Task, Context, Audience, Constraints, Format, Examples (+ optional Role) | — |
| Microsoft Copilot | Goal, Context, Source, Expectations | Microsoft Support |
| Google Gemini | Persona, Task, Context, Format | Google Workspace |
| OpenAI | Goal, Context, Output, Boundaries | OpenAI Academy |
| CO-STAR | Context, Objective, Style, Tone, Audience, Response | GovTech Singapore |
| RISEN, RTF, CRAFT, and others | Mostly subsets or reshuffles of the same core | Practitioner frameworks; no authoritative source |

The *Prompt Report* (Schulhoff et al., 2024) catalogues 58 text prompting
techniques. The ten above are the ones that matter most in a chat window.
