# vibehub-testing · MVP 说明（给我本人 & Claude 看）

> 核心设定：
> - **Google Drive = 我的内容数据库**：结构可以是乱的，允许 AI 在我的确认下创建/移动/改名/编辑文件。
> - **vibehub-testing = Cloud / Prompt Hub**：
>   - 集中放各种 Claude skill / prompt 模板（可跨项目复用）。
>   - 管理「当前在搞什么项目 / feature」的 session 文件。
>   - 记录重要的 Drive 改动 & 原因（实验日志）。

---

## 1. VibeHub（对我个人）的目标（超简版）

对我个人来说，这个阶段的 VibeHub 想解决这几件事：

1. **我不想手动设计 Drive 目录结构**
   - Drive 就当一个「不限 schema 的数据库」。
   - AI 可以帮我建目录、拆文件、重命名，只要最后在某个地方记录一下"为什么这么改"。

2. **我想要一个集中管理 Claude prompt / skill 的地方**
   - 比如：
     - 某个 PR review 的标准 prompt
     - 某种「读项目文档再写代码」的 skill
     - 某个「跑一条数据 pipeline」的 script-like prompt
   - 这些东西要可以「一键拉来复用、稍微改改就能用在新项目」。

3. **我希望 AI 能"长一点的生命周期 & 更自主一点"地跟 Drive 互动**
   - 它知道：
     - 去 Drive 找哪些文件 / 用什么关键词搜索
     - 可以主动提议「要不要把这类东西拆成一个新文件」「这个目录太乱，要不要重组」
   - 但每次实际变动 Drive 前，会在一个 session 文件里写清楚计划和理由，让我确认。

一句话：
> **vibehub-testing = 我个人的「AI 驱动知识库的控制台 + prompt 中心」。**

---

## 2. 这个 repo 现在在做什么？

当前 MVP，这个 repo 只做 3 件事：

1. **`prompts/`：集中管理 Claude skill / prompt 模板**
   - 例子：
     - `prompts/skill.pr_review.v1.md`
     - `prompts/skill.feature_dev.v1.md`
     - `prompts/skill.data_pipeline.v1.md`
   - 每个文件里写清楚：
     - 这个 skill 是干嘛的
     - 需要用户提供什么（代码 / 文档 / 路径 / 关键词）
     - 推荐怎么在 Claude Code 里调用

2. **`templates/`：存放可以 copy 的 markdown 模板**
   - 比如：
     - `templates/session_prep.md`：**session 前的准备阶段**——把零散信息整理好、推到 Drive。
     - `templates/project_session.md`：我要开始搞某个项目时复制一份出来。
     - `templates/feature_session.md`：对某个 feature 的一次工作 session。
   - 这些模板会告诉 Claude：
     - 这次 session 要干嘛
     - 去 Drive 找东西的大致线索（关键词 / 可能的路径）
     - 怎么记录这次对 Drive 的修改

3. **`sessions/`：每次「我要认真搞点东西」时，新建一个 session 文件**
   - 命名示例：`sessions/2025-12-06-sunset-pipeline.md`
   - 内容一般来源于 `templates/project_session.md`，然后由 Claude 填充。
   - 里面会包含：
     - 这次要做什么（project / feature / 任务）
     - 相关 Drive 搜索关键词 / 可能的文档
     - Claude 生成的「在目标项目中启动 Claude Code 的 prompt」
     - 这次 session 做过的 Drive 改动记录

**日志（为什么要这么改 Drive）就放在每个 session 里即可。**
以后如果需要，可以再搞 `logs/` 目录，现在先不用。

---

## 3. 推荐的最小目录结构（可以慢慢长）

```text
vibehub-testing/
  CLAUDE_ENTRY.md          # 本文件

  prompts/                 # Claude skill / prompt 模板
    skill.pr_review.v1.md
    skill.feature_dev.v1.md
    ...（慢慢加）

  templates/               # 可复制的 markdown 模板
    session_prep.md        # session 前整理信息用
    project_session.md
    feature_session.md

  sessions/                # 具体某次"我要干活"的 session
    2025-12-06-sunset-pipeline.md
    ...

  prep/                    # session 准备文件（可选，也可以直接放 sessions/）
    2025-12-06-sunset-prep.md
    ...
```

---

## 4. `templates/project_session.md` 的约定（v0）

> 这是一个「我要开始在某个项目上干活」的 session 模板。
> 我会复制它到 `sessions/` 下面，然后让 Claude 帮我填。

详见 `templates/project_session.md`。

---

## 5. Claude：当我在这个 repo 里找你时，你要怎么做？

> 下面是给 Claude 的行为约定。

### 5.0 当我说「我有一堆东西要整理」或「帮我准备一个 session」时

这是 **session 前的 intake 阶段**。典型入口：

> 我有一堆关于 XXX 的信息/文件/想法，帮我整理一下，然后我们再正式开 session。

你（Claude）应该：

1. 基于 `templates/session_prep.md` 创建一个 prep 文件。
2. 让我把零散信息 dump 到「第 1 节」。
3. 帮我：
   - **分类整理**：提取核心概念、参考资料、待办事项、不确定项
   - **建议 Drive 结构**：这些东西应该怎么放到 Drive 里
   - **生成待上传内容**：比如项目 README、整理好的笔记
4. 等我确认 Drive 结构后，告诉我要上传什么、放哪里。
5. 上传完成后，**自动生成正式的 `project_session.md`**，里面的 `drive_search_hints` 就是刚整理好的路径。

**流程图：**
```
零散信息 → session_prep.md → 整理 & 上传 Drive → project_session.md → 开始干活
```

### 5.1 当我说「我要在某个项目上开一个 session」时

典型对话入口会像这样（我说）：

> 我现在想开始搞一个叫"sunset-pipeline"的东西。
> 请你帮我在 `templates/project_session.md` 的基础上，
> 生成一个适合这个项目的 session 文件内容，我会存到 `sessions/2025-12-06-sunset-pipeline.md` 里。

你（Claude）应该：

1. 阅读 `CLAUDE_ENTRY.md` 和 `templates/project_session.md`。
2. 问我几个最关键的问题（如果你需要的话），比如：
   * 这个项目的名字 / 代号
   * 我大概记得它在 Drive 里有什么线索（关键词 / 大概路径）
3. 在当前对话中生成一份填写好的 `project_session.md` 内容，包括：
   * `session_id` / `project_handle`
   * 初始的 `drive_search_hints`
   * 第 3 节「Claude：请你做的第一步」里你打算怎么搜 / 看
4. 把这份 markdown 输出给我，让我复制到 `sessions/xxxx.md` 文件里。

### 5.2 当我已经有一个 session 文件，并把它贴给你 / 附给你的时候

如果我说：

> 这是 `sessions/2025-12-06-sunset-pipeline.md` 的最新内容，
> 里面有「Drive 搜索线索」，你按照里面的指示，帮我真正开始做事。

你应该：

1. 阅读 session 内容，**严格按照里面写好的流程** 来：
   * 设计你在 Drive 里的搜索策略
   * 告诉我「接下来你需要我从 Drive 打开的文档/搜索结果」
2. 当你想改 Drive（创建/重命名/移动/拆文档）时：
   * 先在 session 的「第 6 节」里写出**计划中的改动列表**
   * 让我确认
   * 再让我去 Drive 里实际执行（或者用集成功能）
3. 每次重要改动之后：
   * 把「第 6 节」里对应项打勾，并追加简短说明（你帮我生成文本，我复制回去）

### 5.3 你也可以帮我维护 prompts/skills

当我们在某个项目里，用出了一套「很好用的 prompt」时（例如 PR review / feature 开发），你可以：

1. 提醒我：
   * 这可以沉淀成一个可复用的 Claude skill 模板
2. 帮我生成一个 `prompts/skill.xxx.v1.md` 文件内容，里面包括：
   * skill 的用途
   * 需要的输入（代码、说明、diff 等）
   * 在 Claude Code 里的使用步骤
3. 我会把这段文本放进 `prompts/`，以后新项目可以直接拿来复用。

---

## 6. 对我本人来说，实际操作的一条「最小路径」

第一次使用这个 MVP，我可以只做这几步：

1. 在 Drive 里什么都不用动，只要确保我之前的笔记/文档已经在那里。
2. 在这个 repo 加上：
   * `CLAUDE_ENTRY.md`（本文件）
   * `templates/project_session.md`（用上面那份模板）
3. 在 Claude Code 里打开 `vibehub-testing`，对 Claude 说：
   > 「按 `CLAUDE_ENTRY.md` 里的约定，我想为一个叫 sunset-pipeline 的东西开一个 project session，
   > 先帮我生成 `project_session` 的内容。」
4. 把 Claude 生成的 session 内容保存为 `sessions/2025-12-06-sunset-pipeline.md`。
5. 再把这个 session 文件 + 一些 Drive 搜索结果贴给 Claude，让它真正开始工作。

从这里开始，我就可以一边做真实项目，一边感受：

* 这个 session 模板好不好用
* prompt 该怎么拆成可复用的 skill
* AI 帮我乱搞 Drive 的体验如何（以及如何记录）