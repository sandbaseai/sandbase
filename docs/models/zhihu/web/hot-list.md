# Zhihu Hot List API: pricing, parameters and code examples

`zhihu/web/hot-list` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the Zhihu hot list: trending questions with title, excerpt, heat, answer and follower counts, and links.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/hot-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/hot-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/hot-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/hot-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zhihu/web/hot-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of articles per page default `"50"` |
| `desktop` | string |  | Is it a desktop default `"true"` |

## Details

Fetch the current Zhihu hot list. Each item includes the trending question, an excerpt, heat value, and answer and follower counts.

### Use cases

- Track trending discussions on Zhihu.
- Find popular questions to answer for content marketing.
- Build daily trend digests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/hot-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | string | No | Number of articles per page |
| `desktop` | string | No | Is it a desktop |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "fresh_text": "热榜已更新",
  "data": [
    {
      "type": "hot_list_feed",
      "detail_text": "163 万热度",
      "target": {
        "id": 26705971,
        "type": "question",
        "title": "Adobe Photoshop 是否已经过时？",
        "answer_count": 286,
        "follower_count": 4005,
        "created": 1416488544,
        "excerpt": "时代在发展，Photoshop 软件是否已经过时了？ 感谢各位热心以及耐心的回答，在此深表感谢。关…",
        "url": "https://api.zhihu.com/questions/26705971"
      }
    }
  ],
  "paging": {
    "is_end": false
  }
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…
- [Get Zhihu AI Search (v2)](/model/zhihu/web/ai-search-stream): Get Zhihu AI Search results (new endpoint).
- [Get Zhihu Answer Detail](/model/zhihu/web/answer-detail): Get a single Zhihu answer's detail (content / stats / author / question, etc.).

---
Machine-readable: [`catalog/models/zhihu/web/hot-list.json`](../../../../catalog/models/zhihu/web/hot-list.json) · Store page: https://www.sandbase.ai/model/zhihu/web/hot-list
