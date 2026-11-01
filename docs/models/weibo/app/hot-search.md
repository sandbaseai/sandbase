# Weibo Hot Search Rankings

`weibo/app/hot-search` · api · Weibo

Returns current Weibo hot search rankings across various categories. Supports filtering by category such as realtime trends or by city name for regional topics.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/hot-search", "category": "realtimehot", "count": 20, "page": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/hot-search', {'category': 'realtimehot', 'count': 20, 'page': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/hot-search", {
  "category": "realtimehot",
  "count": 20,
  "page": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/hot-search", sandbase.Params{
	"category": "realtimehot",
	"count": 20,
	"page": 1,
})
```

Same call via the path form: `POST /v1/api/weibo/app/hot-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starts from 1 (default 1) default `1`; range 1– |
| `count` | integer |  | Items per page, default 20, max 50 default `20`; range 1–50 |
| `category` | string |  | Hot search category default `"realtimehot"` |
| `region_name` | string |  | City name for local hot search, only effective when category=region, default Beijing  |

## Details

Retrieve trending search topics on Weibo filtered by `category` and optional `region_name`. It also supports pagination via `page` and `count`.

### Use cases

- Track trending discussions and viral topics across Weibo.
- Monitor regional trending searches for specific city locations.
- Analyze popular search terms categorized by realtime relevance.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/hot-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | No | Page number, starts from 1 (default 1) |
| `count` | integer | No | Items per page, default 20, max 50 |
| `category` | string | No | Hot search category |
| `region_name` | string | No | City name for local hot search, only effective when category=region, default Beijing |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "channelInfo": {
    "channels": [
      {
        "pageDataType": "flow",
        "title": "我的",
        "actionlog": {
          "act_type": 1
        },
        "params": {
          "transType": "pageinfo"
        }
      }
    ]
  }
}
```

### Notes

- `region_name` is only effective when `category` is set to region, defaulting to Beijing.
- `count` accepts a maximum of 50 items per page with a default of 20.
- `page` starts from 1 with a default value of 1.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Categories](/model/weibo/app/hot-search-categories): Returns all available hot search categories from Weibo.

---
Machine-readable: [`catalog/models/weibo/app/hot-search.json`](../../../../catalog/models/weibo/app/hot-search.json) · Store page: https://www.sandbase.ai/model/weibo/app/hot-search
