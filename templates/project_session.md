---
session_type: project
session_id: {{自动填，比如 2025-12-06-sunset}}
project_handle: {{我给这个项目起的名字，比如 sunset-pipeline}}
drive_search_hints:
  - "关键词1"
  - "关键词2"
  - "某个关键术语"
ai_can_modify_drive: true
---

# 1. 本次想做什么？

> 由我用自然语言写：
> 比如：
> - 复刻一个叫 sunset 的数据 pipeline，
> - 希望 AI 帮我：
>   - 找到 Drive 里所有相关的说明 / 笔记 / 设计；
>   - 把信息汇总成一份"起步说明"；
>   - 生成一个可以放进 Claude Code（连接代码仓库）的启动 prompt。

# 2. 与这个项目相关的 Drive 线索（初始版本）

> 由我先粗略写一点，Claude 可以补充/修正。

- 可能的关键词：keyword1, keyword2, XXX
- 可能的目录/文件（如果我记得的话）：
  - `My Drive/old-notes/...`
  - ...

# 3. Claude：请你做的第一步

> 这一节由 Claude 填。

- 根据我提供的关键词 / 线索，规划你在 Drive 里要怎么搜：
  - 建议搜索词列表
  - 建议要打开阅读的前 N 个文档类型
- 读完之后，帮我输出：
  1. 一份「项目起步说明」（包括该看哪些文档、先做什么）
  2. 一段「给这个项目的 Claude Code 用的启动 prompt」

# 4. Claude 生成的「项目起步说明」

> Claude 在这里写：
> - 总结项目是什么
> - Drive 里哪些文档是关键入口
> - 建议的工作流（写代码 / 写文档 / 改结构）

# 5. Claude 生成的「Claude Code 启动 prompt」

> Claude 在这里写一段完整的 prompt：
> - 目标：在 *另一个* Claude Code 会话里使用
> - 内容包括：
>   - 这个项目是啥
>   - 建议先从 Drive 哪些文件读起（可以用自然语言描述 + 关键词）
>   - 怎么配合后续 skill（比如 PR review skill / feature dev skill）

# 6. 本次 session 对 Drive 的改动记录（非常重要）

> 每次 AI 想改 Drive，请先写在这里，让我确认，再去执行。

- [ ] （Claude 填）计划中的 Drive 改动列表，例如：
  - 创建新文档：`...`
  - 重命名：`旧名 -> 新名`
  - 移动：`A 文件夹 -> B 文件夹`
  - 拆分某个过长文档为两个

> 改完之后打勾，并在后面备注"已执行"。

# 7. 备注 / 下一步想法

> 我用来记：
> - 这个工作流有什么感觉
> - 下次想改进什么（模板、prompt、Drive 组织方式等）
