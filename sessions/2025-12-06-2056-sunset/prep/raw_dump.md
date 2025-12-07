---
prep_id: 2025-12-06-2056-sunset
status: organized
---

# Session 准备：SUnSET Pipeline

## 1. 论文核心信息

**论文标题**: SUnSET: Synergistic Understanding of Stakeholder, Events and Time for Timeline Generation

**作者**: Tiviatis Sim (NUS/A*STAR), Yang Kaiwen, Shen Xin, Kenji Kawaguchi (NUS)

**任务**: Timeline Summarization (TLS) - 从新闻文章集合生成事件时间线摘要

**核心创新**:
1. 首次在 TLS 中引入 stakeholder（利益相关者）信息
2. SET triplet: (Stakeholder, Event, Time) 三元组表示
3. 基于 stakeholder 的 Relevance 评分机制
4. 比现有 SOTA 更快（无需 pairwise LLM 比较）

---

## 2. Pipeline 架构（三阶段）

### Stage 1: SET Generation
- **输入**: 新闻文章 + 发布时间
- **LLM 提取**:
  - 事件摘要 + 预估日期 → `{date: event_summary}`
  - 每个事件的 stakeholders（最多5个）→ 人物/组织
- **Coreference Resolution**: 用 Wikidata KG 统一实体名称
  - 例: "POTUS" → "President of America" → Q ID

### Stage 2: Event Clustering
- **Embedding**: GTE-Modernbert-Base 对事件编码
- **相似度**: Cosine similarity + Relevance score
- **Relevance 公式**:
  ```
  Rel(ς, d) = β × P(ς, d) × R(count(ς_d))

  P (Penalty): 惩罚跨 topic 常见的 stakeholder
  R (Reward): 奖励 topic 内高频出现的 stakeholder (tanh dampened)
  ```
- **Edge 建立**: Top-20 相似事件 + 可选 Exact Matching (EM)

### Stage 3: Timeline Generation
- **Cluster Ranking**: 基于 cluster 大小 + stakeholder relevance
  ```
  Significance = [1 + ln(|C|)] × (Σ Rel / |S_C|)
  ```
- **TextRank**: 从重要 cluster 中提取核心事件
- **输出**: Date-Event pairs 组成的 timeline

---

## 3. 技术栈

| 组件 | 工具/模型 |
|------|----------|
| LLM | Qwen2.5-72B-Instruct (主), GPT-4o (对比) |
| Embedding | GTE-Modernbert-Base |
| 部署 | VLLM |
| Coreference | Wikidata API + spaCy NER |
| Clustering | Cosine similarity + custom Relevance |
| Ranking | TextRank |

---

## 4. 数据集

| Dataset | Topics | Timelines | 特点 |
|---------|--------|-----------|------|
| Timeline17 (T17) | 9 | 19 | 2005-2013, 多源 |
| Crisis | 4 | 22 | 危机事件, 大量文章 |

---

## 5. 评估指标

- **AR-1**: Alignment-based ROUGE-1 F1
- **AR-2**: Alignment-based ROUGE-2 F1
- **Date-F1**: 日期匹配 F1 分数

---

## 6. 关键超参数

- **β**: Relevance 权重 (0-1, 越大 stakeholder 影响越大)
- **EM (Exact Matching)**: 0/1/2 个共同 stakeholder 才能建边
- 最佳配置: β=1.0, EM=0 或 EM=1

---

## 7. 实现要点

### Prompts (Appendix A)
1. **Event+Time Extraction**: 让 LLM 输出 `{date: event_summary}` dict
2. **Stakeholder Extraction**: 针对每个 event 提取最多 5 个 stakeholder

### Wikidata Coreference (Appendix B)
- 多级搜索: label → 去 title → 去空格 → interface search
- 检查 "Position Held By" 属性做实体链接

### 公式细节
- P (Penalty): 用 Coefficient of Variation 衡量跨 topic 分布
- R (Reward): `tanh(x/10)` 限制在 [0,1]，x~21 时饱和

---

## 8. 待实现模块清单

1. [ ] SET Extraction (LLM prompting)
2. [ ] Wikidata Coreference Resolution
3. [ ] GTE Embedding
4. [ ] Relevance Scoring (P, R, Rel)
5. [ ] Event Clustering
6. [ ] Cluster Ranking (Significance)
7. [ ] TextRank Timeline Generation
8. [ ] Evaluation (AR-1, AR-2, Date-F1)

---

## 9. 相关文件清单

| 文件名 | 位置 | 类型 | 备注 |
|--------|------|------|------|
| SUnSET paper | prep/to_upload/ | PDF | 原论文 |
| qwen-service.md | prep/to_upload/ | MD | Qwen 服务配置 |
| starter_plan.md | prep/to_upload/ | MD | 初始计划（空） |

---

## 10. 决策记录

- [x] **数据集**: T17 (Timeline17)
- [x] **LLM**: Qwen service (待补充 endpoint)
- [x] **Coreference**: 完整 Wikidata（通过 proxy 访问）
- [x] **范围**: 完整复现论文

---

## 11. 服务配置

### Proxy Service (访问 Wikipedia/Wikidata)
- **文档**: https://proxy.frederickpi.com/doc
- **用途**: Coreference resolution 时访问 Wikidata API
- **端点**:
  - `GET /proxies/normal` - 获取代理列表 (`ip:port:user:pass`)
  - `GET /proxy/random/normal` - 随机单个代理

### Qwen Service (VLLM, OpenAI-compatible)

**Text Generation (SET Extraction)**
- **URL**: `http://ds-serv11.ucsd.edu:18000/v1`
- **Model**: `Qwen/Qwen3-32B`
- **API**: OpenAI-compatible (`/v1/chat/completions`)
- **Auth**: `api_key="dummy"`

**Embedding (Event Clustering)**
- **URL**: `http://ds-serv11.ucsd.edu:18003/v1`
- **Model**: `qwen3-embed-0.6b`
- **API**: OpenAI-compatible (`/v1/embeddings`)

> **Note**: 论文用 Qwen2.5-72B + GTE-Modernbert-Base，我们用 Qwen3-32B + qwen3-embed-0.6b
