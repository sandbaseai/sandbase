# Douyin Material Center Related Videos API: pricing, parameters and code examples

`douyin/creator/creator-material-center-related` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns related videos for a specific topic, hot spot, prop, or music entry from the Douyin creator material center. Supports pagination controls and filtering by billboard type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-material-center-related", "query_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-material-center-related', {'query_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-material-center-related", {
  "query_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-material-center-related", sandbase.Params{
	"query_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-material-center-related` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Items per page (default 20, range 1-100) range 1–100 |
| `offset` | integer |  | Offset (starting position for pagination) range 0– |
| `query_id` | string | yes | Query ID (topic_id / hot_id obtained from billboard endpoints)  |
| `billboard_type` | integer |  | Billboard type  |

## Details

Returns a page of related videos for one topic, hot spot, prop, or music entry from the Douyin creator material center. Each item has a video ID and a cover image. The only required input is `query_id`.

### Use cases

- Pull the videos linked to a trending topic to see which clips represent it.
- Collect cover images and video IDs for a hot spot to build a reference board.
- Page through all videos tied to a music or prop entry to review how creators use it.
- Pass the returned `item_id` values to a video detail API to get full video data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-material-center-related" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query_id": "2488260"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query_id` | string | Yes | Query ID (topic_id / hot_id obtained from billboard endpoints) |
| `billboard_type` | integer | No | Billboard type |
| `limit` | integer | No | Items per page (default 20, range 1-100) |
| `offset` | integer | No | Offset (starting position for pagination) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "has_more": true,
  "item_list": [
    {
      "cover": {
        "uri": "tos-cn-i-0813/oMBvhpgRAAPibABGCovoqEAAgIaa4kiwCwAKI",
        "url_list": [
          "https://p11-sign.douyinpic.com/tos-cn-i-0813/oMBvhpgRAAPibABGCovoqEAAgIaa4kiwCwA…"
        ]
      },
      "item_id": "7638565167143477106",
      "sec_item_id": "@ifZv67JOREr5tclG6L3ots14py+WYSjzLKkqOKVpjpj5rnq+EGQpezfFbyAFrlLw"
    }
  ],
  "status_code": 0,
  "status_msg": "",
  "total": 500
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_list[]` | The list of related videos on this page. |
| `item_list[].item_id` | The ID of the video, as a numeric string. |
| `item_list[].sec_item_id` | An encoded form of the video ID. It starts with `@`. |
| `item_list[].cover.uri` | The storage path of the cover image. |
| `item_list[].cover.url_list[]` | Signed cover image URLs for the same image. The URLs use different hosts and include an expiry value. |
| `has_more` | `true` when more videos are available after this page. |
| `total` | The total count of related videos for this `query_id`. The sample shows `500`. |
| `status_code / status_msg` | The status of the call. `0` with an empty message appears on success. |

### Notes

- Get `query_id` from a billboard endpoint. It is the `topic_id` or `hot_id` of an entry. Try [Douyin Creator Material Center Billboard](/apis/douyin/creator/creator-material-center-billboard) or [Douyin Creator Hot Topic Billboard](/apis/douyin/creator/creator-hot-topic-billboard).
- Page with `limit` (1 to 100, default 20) and `offset`. Keep requesting while `has_more` is `true`.
- The response gives only IDs and covers. Call [Douyin Single Video Details](/apis/douyin/app-v3/one-video) with `item_id` to get more about a video.
- `billboard_type` is an optional integer filter.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-material-center-related.json`](../../../../catalog/models/douyin/creator/creator-material-center-related.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-material-center-related
