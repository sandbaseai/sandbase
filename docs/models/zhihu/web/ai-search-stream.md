# Zhihu AI Search Stream API: pricing, parameters and code examples

`zhihu/web/ai-search-stream` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns streaming AI search results from Zhihu based on a query prompt. Supports conversational multi-turn sessions and chat modes.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/ai-search-stream", "message_content": "test"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/ai-search-stream', {'message_content': 'test'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/ai-search-stream", {
  "message_content": "test"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/ai-search-stream", sandbase.Params{
	"message_content": "test",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/ai-search-stream` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `chat_mode` | string |  | Chat mode, default FAST  |
| `session_id` | string |  | Session ID for multi-turn  |
| `message_content` | string | yes | Search Content  |

## Details

Query Zhihu AI search stream by passing `message_content`. Optionally supply `session_id` for multi-turn conversations and specify `chat_mode`.

### Use cases

- Retrieve AI-synthesized answers from Zhihu content.
- Maintain multi-turn AI search dialogs using session identifiers.
- Stream Zhihu search output in fast or alternative chat modes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/ai-search-stream" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"message_content": "<message_content>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `message_content` | string | Yes | Search Content |
| `chat_mode` | string | No | Chat mode, default FAST |
| `session_id` | string | No | Session ID for multi-turn |

### Notes

- `message_content` is required to provide the search text.
- `session_id` enables multi-turn conversation tracking.
- `chat_mode` defaults to FAST if omitted.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…
- [Zhihu Column Article Detail](/apis/zhihu/web/column-article-detail): Returns detailed information and metadata for a specific Zhihu column article, including author profile details, using a provided article ID.

---
Machine-readable: [`catalog/models/zhihu/web/ai-search-stream.json`](../../../../catalog/models/zhihu/web/ai-search-stream.json) · Store page: https://www.sandbase.ai/model/zhihu/web/ai-search-stream
