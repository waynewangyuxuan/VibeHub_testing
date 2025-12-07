# Qwen Services Guide

## Available Services (curl localllm.frederickpi.com/report)

| Service | URL | Model |
|---------|-----|-------|
| Text (32B) | `http://ds-serv11.ucsd.edu:18000` | `Qwen/Qwen3-32B` |
| Embedding | `http://ds-serv11.ucsd.edu:18003` | `qwen3-embed-0.6b` |
| Text (30B-A3B) | `http://ds-serv11.ucsd.edu:18005` | `Qwen/Qwen3-30B-A3B` (offline) |

## .env Configuration
```bash
VLLM_QWEN_32B_URL=http://ds-serv11.ucsd.edu:18000
VLLM_QWEN_32B_MODEL=Qwen/Qwen3-32B
VLLM_EMBEDDING_URL=http://ds-serv11.ucsd.edu:18003
DEFAULT_EMBEDDING_MODEL=qwen3-embed-0.6b
```

## Quick Test
```bash
# Check service status
curl -s http://ds-serv11.ucsd.edu:18000/v1/models | jq .

# Chat completion
curl -s http://ds-serv11.ucsd.edu:18000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"Qwen/Qwen3-32B","messages":[{"role":"user","content":"Hello"}],"max_tokens":50}'

# Embedding
curl -s http://ds-serv11.ucsd.edu:18003/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{"model":"qwen3-embed-0.6b","input":["Hello world"]}'
```

## Python Usage
```python
from openai import OpenAI

client = OpenAI(base_url="http://ds-serv11.ucsd.edu:18000/v1", api_key="dummy")
resp = client.chat.completions.create(
    model="Qwen/Qwen3-32B",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=100
)
print(resp.choices[0].message.content)
```