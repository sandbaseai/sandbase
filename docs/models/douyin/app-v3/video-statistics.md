# Douyin Video Statistics API: pricing, parameters and code examples

`douyin/app-v3/video-statistics` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns statistical metrics including like counts, play counts, and share counts for specified Douyin videos by ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-statistics", "aweme_ids": "7448118827402972455,7126745726494821640"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-statistics', {'aweme_ids': '7448118827402972455,7126745726494821640'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-statistics", {
  "aweme_ids": "7448118827402972455,7126745726494821640"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-statistics", sandbase.Params{
	"aweme_ids": "7448118827402972455,7126745726494821640",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-statistics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_ids` | string | yes | Video id, supports multiple video ids, separated by commas, no more than 2, single is also possible, no need for commas.  |

## Details

Fetch performance metrics for Douyin videos by providing one or two video identifiers in `aweme_ids`.

### Use cases

- Track engagement metrics such as play and like counts for specific Douyin posts.
- Compare statistical performance across multiple Douyin videos.
- Monitor video share counts to evaluate content reach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-statistics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_ids": "7448118827402972455,7126745726494821640"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_ids` | string | Yes | Video id, supports multiple video ids, separated by commas, no more than 2, single is also possible, no need for commas. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "statistics_list": [
    {
      "aweme_id": "7448118827402972455",
      "digg_count": 4554,
      "play_count": 239764,
      "share_count": 69
    }
  ]
}
```

### Notes

- The `aweme_ids` parameter accepts a single video ID or up to two IDs separated by commas.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-statistics.json`](../../../../catalog/models/douyin/app-v3/video-statistics.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-statistics
