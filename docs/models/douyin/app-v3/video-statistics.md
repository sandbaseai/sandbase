# Douyin Video Statistics API: pricing, parameters and code examples

`douyin/app-v3/video-statistics` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns statistical metrics including like counts, play counts, and share counts for specified Douyin videos by ID.

## Pricing

- **$0.001 per call** (USD)
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

Returns like, play and share counts for one or two Douyin videos. You pass the video IDs in `aweme_ids`, separated by a comma.

### Use cases

- Check the play and like counts of a single Douyin post.
- Compare engagement between two Douyin videos in one call.
- Read `share_count` to see how often a video was shared.
- Check `download_count` on videos that report it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-statistics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_ids": "7448118827402972455,7126745726494821640"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_ids` | string | Yes | Video id, supports multiple video ids, separated by commas, no more than 2, single is also possible, no need for commas. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "statistics_list": [
    {
      "aweme_id": "7448118827402972455",
      "digg_count": 4553,
      "play_count": 239913,
      "share_count": 69
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `statistics_list[]` | One entry per video ID you sent. |
| `statistics_list[].aweme_id` | The ID of the video these counts belong to. Use it to match each entry to your input. |
| `statistics_list[].digg_count` | Number of likes on the video. |
| `statistics_list[].play_count` | Number of plays on the video. |
| `statistics_list[].share_count` | Number of shares of the video. |
| `statistics_list[].download_count` | Number of downloads of the video. It appears only for some videos, so the first video in the example does not have it. |

### Notes

- Send at most two IDs in `aweme_ids`. For one video, send the ID without a comma.
- `aweme_id` values are long numeric strings. Keep them as strings.
- `download_count` can be missing from an entry, so check for it before you read it.
- To count more than two videos at once, use [Douyin Video Statistics (Batch)](/apis/douyin/app-v3/multi-video-statistics).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-statistics.json`](../../../../catalog/models/douyin/app-v3/video-statistics.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-statistics
