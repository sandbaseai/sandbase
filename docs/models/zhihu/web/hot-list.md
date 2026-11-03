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

Zhihu's current hot list (知乎热榜): the trending questions with their heat score, excerpt, answer count and follower count, in ranking order.

### Use cases

- Track trending topics in China for content planning or PR monitoring.
- Collect daily snapshots of Zhihu trends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/hot-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `desktop` | string | No | Is it a desktop |
| `limit` | string | No | Number of articles per page |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "detail_text": "2160 万热度",
      "target": {
        "id": 2099419745036650047,
        "title": "如何看待10元快剪正暴打全国的「设计总监」？",
        "excerpt": "近期，全国多地出现10元快剪排队潮，没有收银员，没有洗头台，没有推销办卡。反观传统理发店则因推销办卡等问题大量关停。此前，理发店因“头衔通胀”、预付卡纠纷频发被…",
        "answer_count": 530,
        "follower_count": 856,
        "created": 1793320672,
        "url": "https://api.zhihu.com/questions/2099419745036650047"
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | Hot items in rank order. |
| `data[].detail_text` | Heat, e.g. "2160 万热度" (21.6 million). |
| `data[].target.id / title / url` | Question ID, title and link. |
| `data[].target.excerpt` | Excerpt of the top answer or question detail. |
| `data[].target.answer_count / follower_count` | Answers and followers of the question. |
| `data[].target.created` | Question creation time, Unix seconds. |

### Notes

- `limit` sets how many items are returned.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…
- [Get Zhihu AI Search (v2)](/apis/zhihu/web/ai-search-stream): Get Zhihu AI Search results (new endpoint).
- [Get Zhihu Answer Detail](/apis/zhihu/web/answer-detail): Get a single Zhihu answer's detail (content / stats / author / question, etc.).

---
Machine-readable: [`catalog/models/zhihu/web/hot-list.json`](../../../../catalog/models/zhihu/web/hot-list.json) · Store page: https://www.sandbase.ai/model/zhihu/web/hot-list
