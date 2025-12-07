---
session_id: 2025-12-06-2056-sunset
project_handle: sunset
target_repo: /Users/waynewang/SUnSET
status: ready
created_at: 2025-12-06T20:56:00
---

# Session: SUnSET Pipeline

## 目标

完整复现 SUnSET 论文 (Synergistic Understanding of Stakeholder, Events and Time for Timeline Generation)，实现一个 Timeline Summarization (TLS) pipeline。

## 背景信息

### 论文核心
- **任务**: 从新闻文章集合生成事件时间线摘要
- **创新点**: 首次在 TLS 中引入 stakeholder 信息，通过 SET (Stakeholder-Event-Time) triplet 和 Relevance 评分提升效果
- **结果**: 在 T17 和 Crisis 数据集上达到 SOTA

### Pipeline 三阶段
1. **SET Generation**: LLM 提取事件+时间+stakeholders，Wikidata coreference
2. **Event Clustering**: Embedding + Cosine similarity + Relevance scoring
3. **Timeline Generation**: Cluster ranking + TextRank

### 服务配置
- **LLM**: Qwen3-32B @ `http://ds-serv11.ucsd.edu:18000/v1`
- **Embedding**: qwen3-embed-0.6b @ `http://ds-serv11.ucsd.edu:18003/v1`
- **Proxy**: `https://proxy.frederickpi.com` (访问 Wikidata)

### 数据集
- Timeline17 (T17): 9 topics, 19 timelines, 2005-2013

## 工作范围

**要做：**
- 完整复现论文的三阶段 pipeline
- 使用 T17 数据集评估
- 实现 AR-1, AR-2, Date-F1 评估指标

**不做：**
- Crisis 数据集（可选后续）
- 对比 baseline (LLM-TLS, CHRONOS)

## 参考资料

- **论文 PDF**: `sessions/2025-12-06-2056-sunset/prep/to_upload/SUnSET*.pdf`
- **Prep 文档**: `sessions/2025-12-06-2056-sunset/prep/raw_dump.md`
- **服务配置**: `sessions/2025-12-06-2056-sunset/prep/to_upload/qwen-service.md`

## 启动 Prompt

见下方独立输出
