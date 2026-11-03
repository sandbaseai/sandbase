# Douyin Video Statistics (Batch) API: pricing, parameters and code examples

`douyin/app-v3/multi-video-statistics` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.025 per call · **Modes:** sync

Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.

## Pricing

- **$0.025 per call** (USD)

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

Returns play, like, share and download counts for Douyin videos. Pass one or more video IDs in `aweme_ids`, separated by commas, up to 50 per request.

### Use cases

- Track the play and like counts of a list of campaign videos over time.
- Rank a batch of videos by `play_count` or `digg_count` to find the top performers.
- Compare how often viewers share or download videos in the same set.
- Refresh the counts for videos you already stored from a user or hashtag listing.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/multi-video-statistics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_ids": "7565738211130035491"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_ids` | string | Yes | Video id, supports multiple video ids, separated by commas, no more than 50, single is also possible, no need for commas. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "statistics_list": [
    {
      "aweme_id": "7565738211130035491",
      "digg_count": 88106,
      "download_count": 29,
      "play_count": 2553057,
      "share_count": 165
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `statistics_list` | List of results, one object per video ID in the request. |
| `statistics_list[].aweme_id` | ID of the Douyin video. Use it to match each result to the ID you sent. |
| `statistics_list[].play_count` | Number of plays for the video. |
| `statistics_list[].digg_count` | Number of likes (diggs) on the video. |
| `statistics_list[].share_count` | Number of times the video was shared. |
| `statistics_list[].download_count` | Number of times the video was downloaded. |

### Notes

- Send `aweme_ids` as one string with IDs separated by commas, for example `7565738211130035491,7565738211130035492`. A single ID needs no comma.
- Do not send more than 50 IDs per request.
- Match each result to your input by `aweme_id`, not by position.
- To get descriptions, authors or play URLs, call [Douyin Batch Video Information (App V3)](/apis/douyin/app-v3/multi-video). To list a user's videos and their IDs first, use [Douyin User Videos](/apis/douyin/app-v3/user-post-videos).

### Pricing

$0.025 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Hot Search List](/apis/douyin/app-v3/hot-search-list): Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.
- [Douyin User Videos](/apis/douyin/app-v3/user-post-videos): Get the videos on a Douyin user's profile with descriptions, publish time and play, like, comment and share counts.
- [Get Douyin brand hot search list data](/apis/douyin/app-v3/brand-hot-search-list): Get Douyin brand hot search category data.

---
Machine-readable: [`catalog/models/douyin/app-v3/multi-video-statistics.json`](../../../../catalog/models/douyin/app-v3/multi-video-statistics.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/multi-video-statistics
