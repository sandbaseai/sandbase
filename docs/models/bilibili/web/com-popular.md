# Bilibili Comprehensive Popular Videos API: pricing, parameters and code examples

`bilibili/web/com-popular` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a comprehensive list of trending videos on Bilibili, including video metadata, author details, and engagement statistics across pages.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/com-popular"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/com-popular', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/com-popular", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/com-popular", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/web/com-popular` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `pn` | integer |  | Page number default `1` |

## Details

Access the comprehensive list of trending Bilibili videos by specifying the target page index with `pn`.

### Use cases

- Track trending video topics and categories on Bilibili.
- Monitor engagement statistics such as views and likes on popular clips.
- Discover high-performing video creators across different genres.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/com-popular" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pn` | integer | No | Page number |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "list": [
      {
        "ctime": 1791286688,
        "desc": "嘻嘻嘻嘻我就是想看你这个表情啊嘻嘻嘻嘻我就是想看你这个表情啊嘻嘻嘻嘻我就是想看你这个表情啊嘻嘻嘻嘻我就是想看你这个表情啊嘻嘻嘻嘻我就是想看你这嘻嘻嘻嘻我就是想看你这个表情啊嘻嘻嘻…",
        "duration": 962,
        "pid_name_v2": "二次元",
        "pubdate": 1791286688,
        "season_id": 19833,
        "season_type": 0,
        "short_link_v2": "https://b23.tv/BV1Uppw6yEMr",
        "title": "啊啊7月新番你到底给我下了什么药啊！！【泛式】",
        "tname": "动漫杂谈",
        "owner": {
          "name": "泛式"
        },
        "rights": {
          "ugc_pay_preview": 0
        },
        "stat": {
          "dislike": 0,
          "his_rank": 0,
          "like": 31112,
          "now_rank": 0,
          "view": 180230
        }
      }
    ]
  }
}
```

### Notes

- Use `pn` to specify the page number for paginated results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/com-popular.json`](../../../../catalog/models/bilibili/web/com-popular.json) · Store page: https://www.sandbase.ai/model/bilibili/web/com-popular
