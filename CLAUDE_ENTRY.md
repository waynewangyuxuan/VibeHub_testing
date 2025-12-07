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
    skill.session_prep.v1.md      # 准备阶段 skill
    skill.session_start.v1.md     # 开 session skill
    skill.session_execute.v1.md   # 执行 session skill
    ...（慢慢加）

  templates/               # 可复制的 markdown 模板
    session_prep.md        # session 前整理信息用
    project_session.md
    feature_session.md

  sessions/                # 每个 session 一个文件夹
    2025-12-06-1430-sunset-pipeline/
      prep/                # prep 阶段的工作区
        raw_dump.md        # 原始信息整理
        to_upload/         # 待上传到 Drive 的内容
      session.md           # 正式的 session 文件
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
>
> **核心 Skills（详见 `prompts/` 目录）：**
>
> | Skill | 使用位置 | 用途 |
> |-------|----------|------|
> | `skill.session_prep.v1.md` | vibehub | 整理零散信息（可选） |
> | `skill.session_start.v1.md` | vibehub | 生成启动 prompt |
> | `skill.session_execute.v1.md` | **项目 repo** | 配合启动 prompt 干活 |

### 5.0 当我说「我有一堆东西要整理」或「帮我准备一个 session」时

**→ 使用 `skill.session_prep.v1.md`**（可选步骤）

这是 **session 前的 intake 阶段**。

你（Claude）应该：

1. 创建 session 文件夹：`sessions/{timestamp}-{project}/`
2. 在 `prep/` 子目录下整理信息
3. 帮我分类、建议 Drive 结构、生成待上传内容
4. 完成后进入 `skill.session_start` 生成启动 prompt

**文件夹结构：**
```
sessions/2025-12-06-1430-sunset/
  prep/
    raw_dump.md
    to_upload/
  session.md    # 下一步生成
```

### 5.1 当我说「我要在某个项目上开一个 session」时

**→ 使用 `skill.session_start.v1.md`**

你（Claude）应该：

1. 如果已有 prep，从 `prep/raw_dump.md` 提取信息
2. 如果没有 prep，通过对话问我几个关键问题
3. 生成 `session.md`
4. **输出「启动 Prompt」**——这是核心产出，用户会复制到项目 repo 使用

**流程：**
```
vibehub-testing                      实际项目 repo
───────────────                      ──────────────
1. (可选) prep
2. session_start
3. 生成启动 prompt  ─────────────→   4. 用户贴入启动 prompt
                                      5. 配合 session_execute 干活
```

### 5.2 关于 `skill.session_execute.v1.md`

**注意：这个 skill 是在实际项目 repo 里使用的，不是在 vibehub 里。**

它定义了 Claude 在项目 repo 里的工作方式：
- 先理解，再行动
- 制定计划，逐步执行
- 保持沟通，及时汇报

用户会把这个 skill 复制到项目 repo，或者启动 prompt 里会引用它。

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