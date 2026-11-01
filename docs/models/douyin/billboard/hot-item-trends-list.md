# Douyin Billboard Post Trends

`douyin/billboard/hot-item-trends-list` · api · Douyin

Returns engagement trend metrics for a specific Douyin post across hourly or daily time windows, covering likes, shares, and comments.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-item-trends-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-item-trends-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-item-trends-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-item-trends-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-item-trends-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `option` | integer |  | Option, 7 Like 8 Share 9 Comment  |
| `aweme_id` | string |  | Work id  |
| `date_window` | integer |  | Time window, 1 by hour 2 by day  |

## Details

Access historical trend metrics for a Douyin post using `aweme_id`, with options to filter by metric type using `option` and time scale using `date_window`.

### Use cases

- Track hourly like and comment growth for a trending Douyin video.
- Analyze share velocity over daily time intervals for marketing reports.
- Monitor engagement performance curves following a video release.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-item-trends-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `option` | integer | No | Option, 7 Like 8 Share 9 Comment |
| `aweme_id` | string | No | Work id |
| `date_window` | integer | No | Time window, 1 by hour 2 by day |

### Notes

- Set `option` to 7 for likes, 8 for shares, or 9 for comments.
- Use `date_window` with 1 for hourly intervals or 2 for daily intervals.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-item-trends-list.json`](../../../../catalog/models/douyin/billboard/hot-item-trends-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-item-trends-list
