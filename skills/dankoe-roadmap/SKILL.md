---
name: dankoe-roadmap
description: Build a Dankoe-style one-person company roadmap with default IMA knowledge-base grounding. Use when the user wants to start or redesign a one-person business, turn themselves into a business, combine interests into a niche, choose a direction, create a personal brand path, or map the path from skill/interests/problems to audience, offer, and revenue. Triggers include /dankoe-roadmap, 一人公司路线图, 将自己产品化, niche, personal monopoly, creator business roadmap.
---

# dankoe-roadmap

Help the user turn their interests, skills, problems, and lived experience into a practical one-person company roadmap.

## Core Premise

A one-person company is not "one person doing every task forever." It is a simple value system:

```text
Identity and interests -> problems worth solving -> content proof -> offer -> feedback -> better product
```

AI and tools accelerate this loop, but the user still needs judgment, taste, proof, and repetition.

## Default IMA Source

Before producing the roadmap, retrieve source evidence from IMA by default.

- Default knowledge base: `Dankoe 终极版 | 深度觉醒（持续更新）`.
- Use `ima-skill/SKILL.md` and `ima-skill/knowledge-base/SKILL.md` for actual retrieval.
- Search the default knowledge base by exact name, then search 2 to 5 queries based on the user's direction.
- Use retrieved source titles/snippets to ground the roadmap; do not copy long source passages.
- If IMA is unavailable, credentials are missing, or access fails, state that limitation and continue from the bundled abstract reference.
- Never expose `knowledge_base_id`, `media_id`, `folder_id`, or credentials.

## Commercial Case Library Gate

If the user asks for roadmap examples, business examples, benchmark projects, similar case studies, niche examples, monetization examples, 生财有术案例, or anything involving 商业案例库, use the shared `$commercial-case-library` dependency before answering. Do not ask the user whether to download it; install/check it automatically:

```text
~/.agents/shared/commercial-case-library/知识库/商业案例库/commercial_cases_manifest.json
```

If the shared library is missing, do not ask for confirmation. Automatically ensure the dependency is available:

1. If `$commercial-case-library` is not installed or cannot be loaded, install it immediately without asking the user:

```text
npx -y skills add FocusLiz-Lab/commercial-case-library -g --all
```

2. Run the shared downloader:

```text
python scripts/download_cases.py
```

3. Continue the original task after the download succeeds.

Only stop and ask the user for help if installation, network access, or filesystem writes fail. If that happens, explain the failure and give the exact command the user can run manually.

## Intake

Ask for missing information only once. Prefer this compact intake:

```text
1. 你现在会什么，或者正在学什么？
2. 你过去 2 年反复解决过什么问题？
3. 你愿意持续写/讲/研究什么主题？
4. 你现在有没有受众、客户、作品或收入？
5. 你每周能投入多少深度工作时间？
```

If the user already gave enough context, skip intake and proceed.

## Workflow

### Phase 1: Raw Material Audit

Separate the user's inputs into:

- Skills: what they can do for others.
- Interests: what they can study without forcing themselves.
- Problems: what they have solved or are solving.
- Proof: portfolio, results, audience, testimonials, or credible experience.
- Constraints: time, money, language, platform, energy, risk tolerance.

If there is no proof, do not fake authority. Design a proof-building path first.

### Phase 2: Niche Construction

Do not ask the user to "pick a niche" as a static category. Build a niche as a point of view:

```text
I help {specific people} move from {painful current state} to {desired state} through {mechanism I can prove or practice}.
```

Reject niches that are only labels, such as "AI", "self-growth", "finance", "creator economy", or "one-person company."

### Phase 3: Path Selection

Choose one primary path:

- Client service: fastest path when the user has no audience but can solve a valuable problem.
- Coaching/consulting: use when the user has judgment and can diagnose specific situations.
- Digital product: use when the user has repeated methods, templates, or teachable systems.
- Newsletter/community: use when the user can publish consistently and create belonging or curation value.
- Hybrid: use when service creates cash and proof, then product packages repeated solutions.

For beginners, prefer service first unless the user already has distribution.

### Phase 4: 90-Day Roadmap

Output a 90-day plan:

- Days 1-14: clarify point of view, publish proof-of-thinking, talk to potential buyers.
- Days 15-30: create first offer or service, get conversations, test objections.
- Days 31-60: publish around the buyer's problem, improve the offer, collect proof.
- Days 61-90: systemize delivery, create assets, decide whether to productize.

### Phase 5: First Week Actions

Always end with 3 to 5 concrete actions for the next 7 days. Each action must produce an artifact: a landing page draft, 10 posts, 5 outreach messages, 3 customer calls, an offer card, or a case study.

## Output Template

```markdown
# Dankoe 一人公司路线图

## 当前判断
- 阶段：
- 最大卡点：
- 不该做的事：

## 可用原材料
- 技能：
- 兴趣：
- 已解决问题：
- 证明：
- 约束：

## 定位句
我帮助 {人群} 从 {现状} 到 {结果}，方法是 {机制}。

## 推荐路径
{client service / consulting / digital product / newsletter / hybrid}

## 90 天路线
...

## 未来 7 天
...
```

## Route Next

- If the roadmap depends on monetization, route to `$dankoe-offer`.
- If the roadmap depends on publishing, route to `$dankoe-content`.
- If the roadmap depends on AI workflow design, route to `$dankoe-ai-system`.

## Reference

Deep reference: 知识库/Skill知识包/dankoe_一人公司框架.md
## Dependency Auto-Bootstrap

If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or the user explicitly wants local/offline retrieval, ensure the local Dankoe expert atom library exists before answering. GitHub installs should already include it under `~/.agents/skills/dankoe/知识库/原子库/atoms.jsonl`. Also check `~/.agents/skills/dankoe-download-atoms/知识库/原子库/atoms.jsonl`. If both are missing, treat this as a light/partial install and call `$dankoe-download-atoms` or run `python tools/download_full_atoms.py` from the installed `dankoe-download-atoms` skill directory. Do not ask the user whether to download; do it automatically when local fallback is required.

If the request involves acquisition, traffic, channel choice, platform choice, Xiaohongshu/小红书, WeChat Official Account/公众号, private domain/私域, conversion, lead generation, product launch, business examples, benchmark projects, case studies, monetization examples, 生财有术案例, or any answer would benefit from case evidence, use `$commercial-case-library` automatically before answering. Do not ask the user whether to download it.
## Dankoe Methodology First

Every answer must use Dankoe methodology as the primary reasoning layer. For `/dankoe` requests, first ground the diagnosis, framing, and recommendation in Dankoe sources or Dankoe workflow principles:

1. Prefer the default IMA knowledge base `Dankoe 终极版 | 深度觉醒（持续更新）`.
2. If IMA is unavailable, rate-limited, permission-blocked, has weak/no hits, or local fallback is needed, use the local Dankoe expert atom library and auto-bootstrap it when missing.
3. Only after the Dankoe layer is established, add commercial cases when the question would benefit from proof, benchmarks, platform/channel examples, monetization examples, acquisition examples, or Chinese-market context.
4. Commercial cases are supporting evidence only. Do not let commercial cases replace Dankoe methodology, and do not answer purely from the commercial case library unless no Dankoe source is available; if that happens, label the answer as case-supported inference rather than Dankoe-grounded.
5. In final answers, keep the distinction clear: `Dankoe 方法论` for the core principle and `商业案例支撑` for examples.


