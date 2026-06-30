# dkskill

Dan Koe 风格一人公司 Skill 工具箱。

本仓库打包了一组面向 Agent 的 skills，用于学习 Dan Koe 风格资料、搭建一人公司、设计 offer、创建内容系统、撰写长短内容，并设计 AI 辅助工作流。

可在 Codex、Claude Code、Cursor、Trae Solo 等支持 skill / system prompt 的 Agent 上使用。

**最新版本：v0.3.6**

**v0.3.6 更新**：项目更名为 `dkskill`，GitHub 仓库同步更名。README 新增更新方式和知识库加入说明。

**v0.3.5 更新**：整套 Dankoe workflow skills 默认使用 IMA 知识库「Dankoe 终极版 | 深度觉醒（持续更新）」作为资料来源。用户不需要单独调用 `$dankoe-ima`；`$dankoe-content`、`$dankoe-writing`、`$dankoe-learning-map` 等原有 skill 会默认先检索 IMA，再输出工作流结果。

---

## 如何安装 dkskill

### 通用安装方式（适用于 Codex / Claude Code）

```bash
npx -y skills add FocusLiz-Lab/dkskill -g --all
```

安装后可以直接使用：

```text
$dankoe-content 我是做自媒体的，帮我做内容地图
```

```text
$dankoe-writing 帮我把“普通人如何建立个人品牌”扩展成一篇公众号文章，再拆成5条短内容
```

```text
$dankoe-offer 帮我把个人成长陪跑设计成可卖的offer
```

### Trae Solo / 手动上传

从 GitHub Releases 下载最新的 `dkskill-版本号.zip`。

解压后里面是多个独立 skill zip：

- `dankoe.zip`
- `dankoe-learning-map.zip`
- `dankoe-roadmap.zip`
- `dankoe-offer.zip`
- `dankoe-content.zip`
- `dankoe-writing.zip`
- `dankoe-ai-system.zip`
- `dankoe-ima.zip`

每个 zip 解压后根级都是 `SKILL.md`，可以逐个上传到支持 skill 的客户端。

### 本地构建

Codex-style skill zips：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build-skills.ps1
```

Claude-style skill zips：

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\build-claude-skills.ps1
```

产物目录：

```text
dist/
claude-dist/
```

---

## 如何更新 dkskill

### 通过 `npx skills add` 安装的用户

重新运行一次安装命令即可。安装和更新用的是同一条命令：

```bash
npx -y skills add FocusLiz-Lab/dkskill -g --all
```

然后重启或刷新你的 Agent 客户端，让新的 skill 配置生效。

### 手动 zip 安装的用户

到 GitHub Releases 下载最新版本：

```text
https://github.com/FocusLiz-Lab/dkskill/releases
```

重新导入最新的 skill zip。Trae Solo 这类一个 zip 一个 skill 的客户端，需要逐个替换旧 skill。

### 本地源码用户

```powershell
git pull
powershell -ExecutionPolicy Bypass -File .\tools\build-skills.ps1
```

---

## IMA 配置

整套 Dankoe workflow skills 默认读取 IMA 知识库：

```text
Dankoe 终极版 | 深度觉醒（持续更新）
```

用户不需要在每次提问时写这个知识库名。只要 IMA skill 和凭证配置完成，下面这些命令都会默认先检索 IMA：

```text
$dankoe-learning-map 我是做自媒体的，先看哪些？
$dankoe-content 我是做自媒体的，帮我做内容地图
$dankoe-writing 帮我写一篇关于个人品牌的公众号文章
$dankoe-offer 帮我设计一个数字产品 offer
```

如果要使用其他 IMA 知识库，在问题里直接写知识库名称即可。

### 加入知识库

如果你想加入或获取「Dankoe 终极版 | 深度觉醒（持续更新）」知识库，可以联系我。

![加入知识库二维码](docs/knowledge-base-qrcode.png)

### 安装 IMA skill

```text
请安装 ima 技能
下载地址：https://app-dl.ima.qq.com/skills/ima-skills-1.1.7.zip
API Key 获取：https://ima.qq.com/agent-interface
```

需要满足：

- 已安装官方 `ima-skill`
- 已配置自己的 IMA `Client ID` 和 `API Key`
- 当前 IMA 账号能访问目标知识库

本仓库不包含、也不会保存任何 IMA API Key。

---

## 工具箱

| Skill | 做什么 |
|---|---|
| `$dankoe` | 主入口。根据用户问题自动路由到合适的 Dankoe workflow。 |
| `$dankoe-learning-map` | 学习地图。回答“先看哪些、从哪里开始、不同目标怎么学”。 |
| `$dankoe-roadmap` | 一人公司路线图。把兴趣、技能、问题、受众、offer 串成 90 天路径。 |
| `$dankoe-offer` | Offer 设计。把技能、知识、服务、课程、模板、社群设计成可卖产品。 |
| `$dankoe-content` | 内容地图。设计个人品牌定位、内容支柱、选题系统和 30 天发布计划。 |
| `$dankoe-writing` | 写作系统。把想法、笔记、材料扩展成长文，并拆成短内容。 |
| `$dankoe-ai-system` | AI 工作流。为一人公司设计研究、内容、offer、交付、复盘等工作流。 |
| `$dankoe-ima` | 可选 IMA 检索入口。用于显式搜索、排错、查看检索摘要。普通 workflow 不需要单独调用它。 |

---

## 常见主线

### 自媒体学习路径

```text
dankoe-learning-map
    ↓
dankoe-content
    ↓
dankoe-writing
```

### 一人公司路径

```text
dankoe-roadmap
    ↓
dankoe-offer
    ↓
dankoe-content
```

### 写作与内容复用

```text
dankoe-content
    ↓
dankoe-writing
    ↓
dankoe-ai-system
```

### 显式 IMA 检索

```text
dankoe-ima
    ↓
对应 workflow skill
```

---

## 知识库

本仓库的 `知识库/Skill知识包/` 只包含抽象后的方法论说明，用于让 skill 在没有 IMA 的情况下仍可运行基础流程。

```text
知识库/
└── Skill知识包/
    ├── dankoe_学习地图.md
    ├── dankoe_一人公司框架.md
    ├── dankoe_offer框架.md
    ├── dankoe_内容地图.md
    ├── dankoe_写作系统.md
    ├── dankoe_AI工作流.md
    └── dankoe_IMA桥接.md
```

这些文件不是 Dan Koe 原始课程、书籍、Newsletter、视频或转录稿；只是工作流抽象。

---

## 版权边界

本仓库不包含 Dan Koe 的原始付费课程、书籍、Newsletter、YouTube 视频、转录稿或其他受版权保护的原文内容。

如果用户有自己的 IMA 知识库或本地资料，可以在自己的 Agent 环境里配置使用；这些资料不会随本仓库发布。

请不要把以下内容提交到 GitHub：

- IMA API Key
- `SOURCE_MAP.local.md`
- 本地私有资料路径
- 原始 PDF / 视频 / 转录稿
- 任何无授权的第三方内容

---

## 许可证

本项目采用 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) 许可证。

- 个人使用、学习、研究、非商业项目：允许使用
- 公开发布衍生作品：请注明来源
- 商业用途：需要单独确认授权

本许可证只覆盖本仓库原创的 skill instructions、workflow 和抽象知识包，不授权任何第三方原始资料。
