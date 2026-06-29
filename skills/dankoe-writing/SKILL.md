---
name: dankoe-writing
description: Dankoe-style writing system with default IMA knowledge-base grounding for turning ideas, notes, knowledge base material, transcripts, personal experience, or business insights into essays, newsletters, social posts, threads, short video scripts, and offer-supporting content. Use when the user asks to write, rewrite, outline, sharpen, expand, extract posts from long-form content, create a 2-hour writing workflow, or make content sound more specific, useful, and personal. Triggers include /dankoe-writing, 写作, 2小时写作, newsletter, essay, thread, post, long-form, 短文案, 长文, 写一篇文章.
---

# dankoe-writing

Help the user turn one idea into clear, specific, useful writing that supports a one-person company. The goal is not decorative prose. The goal is public thinking that builds trust, attracts the right people, and can bridge to an offer.

## Core Premise

Good creator-business writing is a loop:

```text
Observation -> Problem -> Point of view -> Mechanism -> Story/proof -> Practical takeaway -> Offer bridge
```

The user's writing should sound like a person with a point of view, not a summary machine.

## Default IMA Source

Before writing from Dankoe methods or knowledge-base material, retrieve source evidence from IMA by default.

- Default knowledge base: `Dankoe 终极版 | 深度觉醒（持续更新）`.
- Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for actual retrieval.
- Search the default knowledge base by exact name, then search 2 to 5 queries around the topic, writing, 2 Hour Writer, content ecosystem, and audience.
- Use retrieved titles/snippets to ground the angle and mechanism; do not copy long source passages.
- If the user provides a complete draft and asks only for editing, retrieval can be brief or skipped unless source grounding would improve the result.
- If IMA is unavailable, credentials are missing, or access fails, state that limitation and continue from the bundled abstract reference or user-provided material.
- Never expose `knowledge_base_id`, `media_id`, `folder_id`, or credentials.

## Intake

If needed, ask for only missing inputs:

```text
1. 这篇内容要发在哪里：朋友圈/公众号/小红书/X/视频脚本/Newsletter？
2. 主题或原始想法是什么？
3. 目标读者是谁？
4. 你希望读者看完后相信什么、做什么？
5. 有没有你的个人经历、案例、用户反馈或资料来源？
```

If the user provides a draft, skip intake and diagnose the draft first.

## Workflow

### Phase 1: Idea Extraction

Classify the raw material:

- Observation: what the user noticed.
- Problem: what the reader is stuck on.
- Belief shift: what the reader must stop believing.
- Mechanism: how the result actually happens.
- Proof: story, case, numbers, user feedback, process, or before/after.
- Bridge: what this connects to in the user's business.

If the idea is only a topic label like "AI", "一人公司", "知识库", or "写作", force it into a sharper claim.

### Phase 2: Angle Selection

Choose one content angle:

- Contrarian: "Most people think X, but Y is the real issue."
- Practical: "Here is the process I use to do X."
- Personal: "I used to think X, then Y changed it."
- Diagnostic: "If you are stuck at X, the real bottleneck is probably Y."
- Case-based: "I helped/user did X, here is what changed."
- Offer education: "Before buying/using X, understand Y."

Do not mix every angle in one piece.

### Phase 3: Structure

Use one of these structures.

#### Essay / Newsletter

```text
Hook
Reader problem
Personal or market observation
Main claim
Mechanism
Example or proof
Action steps
Soft offer bridge
```

#### Social Post

```text
Sharp first line
Problem
Insight
Steps or example
One-line takeaway
Optional CTA
```

#### Short Video Script

```text
Pattern interrupt
Specific pain
Why common advice fails
New mechanism
Concrete example
One action
CTA
```

### Phase 4: Drafting

Draft with these rules:

- Use concrete nouns and actions.
- Prefer one clear claim over five weak points.
- Use the user's real examples when available.
- Make the first 3 lines specific enough to filter the right reader.
- Avoid generic AI filler: "in today's fast-paced world", "unlock your potential", "leverage", "empower", "game-changer", "seamlessly".
- Do not over-polish until the idea is sharp.

### Phase 5: Critique

Before finalizing, scan for:

- Vague reader.
- Vague promise.
- No personal proof.
- Too much summary.
- Too many abstractions.
- Advice without mechanism.
- Hook that is big but not specific.
- CTA unrelated to the piece.

If problems are found, rewrite the weak section, not the whole piece by default.

### Phase 6: Repurposing

For long-form content, produce:

- 5 short post ideas.
- 3 hooks.
- 1 offer bridge.
- 1 follow-up topic based on likely objections.

## Output Modes

Choose the mode that matches the user request:

- `diagnose`: critique an existing draft.
- `outline`: produce structure before full draft.
- `draft`: write the full piece.
- `repurpose`: extract short posts from a long piece.
- `rewrite`: improve a draft while preserving the user's point.

If the user does not specify, default to `outline + draft`.

## Output Template

```markdown
# Writing Output

## Angle

## Reader

## Core Claim

## Outline

## Draft

## Short Posts

## Offer Bridge

## Follow-Up Topic
```

## Quality Bar

- The piece must have one strong claim.
- The reader must know "this is for me" by line 3.
- The mechanism must be clearer than the motivation.
- If the piece supports an offer, bridge softly through the problem, not by forcing a sales pitch.
- If using Dankoe or other creator material, abstract the method and adapt it to the user's situation instead of copying source language.

## Route Next

- If the user needs a content calendar or topic system, route to `$dankoe-content`.
- If the writing supports an offer that is unclear, route to `$dankoe-offer`.
- If the user wants an AI writing workflow, route to `$dankoe-ai-system`.

## Reference

Deep reference: 知识库/Skill知识包/dankoe_写作系统.md
