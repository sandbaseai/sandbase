# Weibo User Timeline API: pricing, parameters and code examples

`weibo/app/user-timeline` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the posts on a Weibo user's timeline: text, publish time, region, images and repost, comment and like counts, with page and month filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-timeline", "filter_type": "all", "month": null, "page": 1, "uid": "7648703289"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-timeline', {'filter_type': 'all', 'month': None, 'page': 1, 'uid': '7648703289'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-timeline", {
  "filter_type": "all",
  "month": null,
  "page": 1,
  "uid": "7648703289"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-timeline", sandbase.Params{
	"filter_type": "all",
	"month": nil,
	"page": 1,
	"uid": "7648703289",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `page` | integer |  | Page number, starts from 1 (default 1) default `1`; range 1– |
| `month` |  |  | Time filter parameter, format YYYYMMDD (only used when filter_type=month)  |
| `filter_type` | string |  | Filter type (default "all") default `"all"` |

## Details

Pass a Weibo user ID and get that user's posts page by page, with full engagement counts.

### Use cases

- Monitor posts from brands, media or public figures.
- Analyze posting frequency and engagement.
- Archive an account's posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "7648703289"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `page` | integer | No | Page number, starts from 1 (default 1) |
| `month` | string | No | Time filter parameter, format YYYYMMDD (only used when filter_type=month) |
| `filter_type` | string | No | Filter type (default "all") |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "category": "feed",
      "data": {
        "id": 5019473113516768,
        "mblogid": "O8aAfeKS4",
        "created_at": "Thu Apr 04 16:25:10 +0800 2024",
        "reposts_count": 796,
        "comments_count": 11619,
        "attitudes_count": 38445,
        "region_name": "发布于 浙江",
        "pic_num": 0,
        "text": "<post text>",
        "user": {
          "screen_name": "<user>"
        }
      }
    }
  ],
  "pageData": {
    "page": 1
  }
}
```

### Notes

- `filter_type` filters the timeline (default `all`); use `month` (YYYYMMDD) with `filter_type=month`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [AI Smart Search](/model/weibo/app/ai-smart-search): App Ai Smart Search provides a focused capability for applications, automation, and data workflows.
- [Get home recommend feed](/model/weibo/app/home-recommend-feed): Get the home recommend feed from Weibo.
- [Get hot search](/model/weibo/app/hot-search): Get Weibo hot search ranking, supports multiple categories.

---
Machine-readable: [`catalog/models/weibo/app/user-timeline.json`](../../../../catalog/models/weibo/app/user-timeline.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-timeline
