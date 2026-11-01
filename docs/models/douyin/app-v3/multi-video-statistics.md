# Douyin Video Statistics (Batch)

`douyin/app-v3/multi-video-statistics` · api · Douyin

Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.

## Pricing

- **$0.0375 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/multi-video-statistics", "aweme_ids": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/multi-video-statistics', {'aweme_ids': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/multi-video-statistics", {
  "aweme_ids": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/multi-video-statistics", sandbase.Params{
	"aweme_ids": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/multi-video-statistics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_ids` | string | yes | Video id, supports multiple video ids, separated by commas, no more than 50, single is also possible, no need for commas.  |

## Details

Pass one or more Douyin video IDs (`aweme_id`) and get each video's play, like, share and download counts in a single call.

### Use cases

- Track performance of a list of campaign videos daily.
- Compare engagement across many videos at once.
- Enrich search results with up-to-date statistics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/multi-video-statistics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_ids": "7565738211130035491"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_ids` | string | Yes | Video id, supports multiple video ids, separated by commas, no more than 50, single is also possible, no need for comma… |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "statistics_list": [
    {
      "aweme_id": "7565738211130035491",
      "digg_count": 86131,
      "download_count": 27,
      "play_count": 2461544,
      "share_count": 161
    }
  ]
}
```

### Notes

- Separate multiple IDs with commas, up to 50 per request.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Hot Search List](/model/douyin/app-v3/hot-search-list): Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.
- [Douyin User Videos](/model/douyin/app-v3/user-post-videos): Get the videos on a Douyin user's profile with descriptions, publish time and play, like, comment and share counts.
- [Get Douyin brand hot search list data](/model/douyin/app-v3/brand-hot-search-list): Get Douyin brand hot search category data.

---
Machine-readable: [`catalog/models/douyin/app-v3/multi-video-statistics.json`](../../../../catalog/models/douyin/app-v3/multi-video-statistics.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/multi-video-statistics
