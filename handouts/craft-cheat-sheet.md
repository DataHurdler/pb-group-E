# CRAFT: A Five-Part Prompt Checklist

*Keep this next to your keyboard. Not every prompt needs all five, but every
weak prompt is missing at least one.*

| | Ask yourself | Write something like |
| --- | --- | --- |
| **C — Context** | What does the AI need to know that it can't guess? Who am I, what's the situation, what source should it use? | "I work in the permits office of a mid-sized city. Below is our current notice, between the `<notice>` tags." |
| **R — Request** | What exactly do I want done? One main job, starting with a verb. | "Rewrite the notice so a resident can understand it in under a minute." |
| **A — Audience** | Who will read the result? What do they already know? What tone? | "Readers are residents, many reading on a phone, some with limited English. Aim for a 6th-grade reading level. Friendly, not bureaucratic." |
| **F — Format** | What should the result look like? Length, structure, what to include or leave out. | "Under 150 words. A one-line headline, then 'What's happening', 'What you should do', and 'Questions?' sections. Keep every date, time, and phone number." |
| **T — Test** | How should it check itself, and what should it flag for me? | "Use only facts in the notice. Don't add anything. After the rewrite, list any information you left out." |

## The whole prompt, assembled

> I work in the Public Works department of a mid-sized city. Below is our
> current notice about water-main flushing, between the `<notice>` tags.
>
> Rewrite it so a resident can understand it in under a minute. Readers are
> residents, many reading on a phone, some with limited English. Aim for a
> 6th-grade reading level, friendly but not casual.
>
> Format: under 150 words. A one-line headline, then three short sections:
> "What's happening", "What you should do", and "Questions?". Keep every date,
> time, area boundary, and phone number exactly as written.
>
> Use only facts in the notice; don't add anything. After the rewrite, list any
> information from the original that you left out.
>
> `<notice>` …paste here… `</notice>`

## Four moves for when CRAFT isn't enough

| Move | When | Say |
| --- | --- | --- |
| **Ground it** | The answer must come from a specific document | "Answer only from the text below. If it isn't there, say 'Not in the source.'" |
| **Show it** | You need a particular style or structure | "Here are two examples of the style I want: …" |
| **Break it down** | The task has several steps, or the output keeps coming back muddled | Do it in turns: "First, list the themes. … Now count them. … Now write the memo." |
| **Let it ask** | You're not sure what information it needs | "Before you start, ask me up to five questions you need answered to do this well." |

## Three habits

1. **Start a new chat for a new task.** Old conversation steers new answers.
2. **Change one thing at a time** when refining, so you know what helped.
3. **You sign it, you own it.** Check facts, numbers, names, and citations
   before anything leaves your desk.
