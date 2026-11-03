# Douyin Video Index Interpretation API: pricing, parameters and code examples

`douyin/index/item-index-interpret` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns index breakdown metrics for a specified Douyin video across a date range. It provides sub-index interpretations using a video ID with start and end dates.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-index-interpret", "end_date": "20260710", "item_id": "7660090930283744575", "start_date": "20260704"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-index-interpret', {'end_date': '20260710', 'item_id': '7660090930283744575', 'start_date': '20260704'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-index-interpret", {
  "end_date": "20260710",
  "item_id": "7660090930283744575",
  "start_date": "20260704"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-index-interpret", sandbase.Params{
	"end_date": "20260710",
	"item_id": "7660090930283744575",
	"start_date": "20260704",
})
```

Same call via the path form: `POST /v1/api/douyin/index/item-index-interpret` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video ID (Douyin aweme id, numeric string)  |
| `end_date` | string | yes | End date YYYYMMDD  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Returns index interpretation scores for one Douyin video over a date range. It needs a video ID (`item_id`), a `start_date`, and an `end_date`. The response scores three sub-indexes: play, interaction, and fan rise.

### Use cases

- Compare how a video scores on play, interaction, and fan rise over one week.
- Check which sub-index is weakest for a video before deciding what to change in the next post.
- Store the sub-index scores for a set of videos to rank them side by side.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-index-interpret" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260710", "item_id": "7660090930283744575", "start_date": "20260704"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD |
| `item_id` | string | Yes | Video ID (Douyin aweme id, numeric string) |
| `start_date` | string | Yes | Start date YYYYMMDD |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "interpretRadar": {
    "itself": {
      "fanRise": {
        "ratio": null,
        "score": "0"
      },
      "interaction": {
        "ratio": null,
        "score": "0"
      },
      "play": {
        "ratio": null,
        "score": "0"
      }
    }
  },
  "interpretRank": {
    "fanRise": {
      "score": "0"
    },
    "interaction": {
      "score": "0"
    },
    "play": {
      "score": "0"
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `interpretRank.play.score / interpretRank.interaction.score / interpretRank.fanRise.score` | Rank score for each sub-index of the video: play, interaction, and fan rise. Values are strings, for example `"0"`. |
| `interpretRadar.itself.play.score / interpretRadar.itself.interaction.score / interpretRadar.itself.fanRise.score` | Radar chart score for the video itself on each of the three sub-indexes. Values are strings. |
| `interpretRadar.itself.play.ratio / interpretRadar.itself.interaction.ratio / interpretRadar.itself.fanRise.ratio` | Ratio value for each sub-index in the radar data. It is `null` in the sample response. |
| `BaseResp.StatusCode` | Status code of the call. `0` in the sample response. |
| `BaseResp.StatusMessage` | Status message of the call. It is an empty string in the sample response. |

### Notes

- `item_id` is the Douyin aweme ID, a numeric string such as `7660090930283744575`. You can find it with [Douyin Index Video Search](/apis/douyin/index/item-query).
- Write `start_date` and `end_date` as `YYYYMMDD`, for example `20260704`. Call [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date) to see the dates that have data.
- The sample response returned `"0"` scores and `null` ratios, so a video or date range can return empty values.
- For the daily index values of the same video, call [Douyin Video Index Trend](/apis/douyin/index/item-index).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-index-interpret.json`](../../../../catalog/models/douyin/index/item-index-interpret.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-index-interpret
