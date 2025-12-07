---
prep_id: {{日期-项目代号，比如 2025-12-06-sunset}}
target_session: {{之后会生成的 session 文件名}}
status: gathering | organizing | uploaded | session_created
---

# Session 准备：{{项目名}}

> 这个文件用于：在正式开 session 之前，把零散的信息、文件、想法先 dump 在这里，
> 让 Claude 帮你整理成结构化内容，然后推到 Drive，最后生成正式的 session。

---

## 1. 原始信息 Dump（随便贴）

> 把你手头的东西全部丢在这里，不用管格式：
> - 聊天记录片段
> - 笔记截图的文字
> - 想法、TODO
> - 相关链接
> - 文件名 / 路径

```
（在这里随便贴）



```

---

## 2. 相关文件清单

> 列出你手头有的文件（本地 or 已经在 Drive 的）

| 文件名 | 位置 | 类型 | 备注 |
|--------|------|------|------|
| example.pdf | 本地 ~/Downloads | 文档 | 需要上传到 Drive |
| 旧笔记.gdoc | Drive/某个文件夹 | Google Doc | 已存在 |
| ... | | | |

---

## 3. Claude：请帮我整理

> 这一节由 Claude 填写。

### 3.1 信息分类

我把你 dump 的内容整理成以下几类：

**核心概念 / 目标：**
- （Claude 提取）

**关键参考资料：**
- （Claude 提取）

**待办 / 行动项：**
- （Claude 提取）

**不确定 / 需要澄清：**
- （Claude 提取）

### 3.2 建议的 Drive 结构

基于你提供的内容，我建议在 Drive 里这样组织：

```
My Drive/
  {{项目名}}/
    README.md          # 项目概览（我帮你生成）
    references/        # 参考资料
    notes/             # 笔记和想法
    assets/            # 相关文件
```

### 3.3 需要你确认的事项

- [ ] 这个 Drive 结构 OK 吗？
- [ ] 哪些文件需要我帮你生成内容？
- [ ] 有没有敏感信息不应该放 Drive？

---

## 4. 准备上传到 Drive 的内容

> Claude 帮你生成的、或你手动准备的，准备推到 Drive 的东西。

### 4.1 项目 README（待上传）

```markdown
# {{项目名}}

## 概述
（Claude 根据你的 dump 生成）

## 关键文档
- ...

## 当前状态
- ...
```

### 4.2 其他待上传文件

| 文件 | 目标 Drive 路径 | 状态 |
|------|-----------------|------|
| README.md | My Drive/{{项目}}/README.md | [ ] 待上传 |
| ... | | |

---

## 5. 上传完成后：生成 Session

> 当 Drive 整理好之后，Claude 会帮你生成正式的 `project_session.md` 内容。

**生成的 session 将包含：**
- 明确的 `drive_search_hints`（基于刚上传的文件）
- 第一步行动计划
- Claude Code 启动 prompt

---

## 6. 状态追踪

- [ ] 原始信息已 dump
- [ ] Claude 已整理分类
- [ ] Drive 结构已确认
- [ ] 文件已上传到 Drive
- [ ] 正式 session 已生成 → `sessions/{{session_id}}.md`
