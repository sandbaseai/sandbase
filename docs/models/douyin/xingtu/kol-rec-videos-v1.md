# Douyin Xingtu KOL Recommended Videos API: pricing, parameters and code examples

`douyin/xingtu/kol-rec-videos-v1` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns recommended videos for a Douyin Xingtu creator based on the provided creator ID. Useful for discovering high-performing content from specific influencers.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu/kol-rec-videos-v1", "kolId": "7048929565493690398"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu/kol-rec-videos-v1', {'kolId': '7048929565493690398'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu/kol-rec-videos-v1", {
  "kolId": "7048929565493690398"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu/kol-rec-videos-v1", sandbase.Params{
	"kolId": "7048929565493690398",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu/kol-rec-videos-v1` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `kolId` | string | yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id`  |

## Details

Returns lists of videos tied to a Douyin Xingtu creator: masterpiece videos, newest videos and order hot videos. It needs one input, the creator's `kolId`.

### Use cases

- Pull a creator's newest videos to check how recent posts are performing.
- Compare `play` counts across masterpiece and order hot videos to see which content earns the most views.
- Collect `item_id` values to look up full details for a creator's best videos.
- Screen a creator's recent output before you shortlist them for a campaign.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu/kol-rec-videos-v1" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"kolId": "7048929565493690398"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `kolId` | string | Yes | User kolId, can be obtained from the following interfaces: `douyin/xingtu/xingtu-kolid-by-uid`; `douyin/xingtu/xingtu-kolid-by-sec-user-id`; `douyin/xingtu/xingtu-kolid-by-unique-id` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "masterpiece_videos": [
    {
      "acu": 0,
      "avg_watch": 0,
      "barrage": 0,
      "biz_id": "0",
      "comment": 0,
      "core_user_id": "0",
      "create_time": 1734027222,
      "create_timestamp": 0,
      "duration": 0,
      "duration_min": 0,
      "fans_club": 0,
      "favorite": "0"
    }
  ],
  "newest_videos": [
    {
      "acu": 0,
      "avg_watch": 0,
      "barrage": 0,
      "biz_id": "0",
      "comment": 0,
      "core_user_id": "0",
      "create_time": 1734515396,
      "create_timestamp": 0,
      "duration": 0,
      "duration_min": 0,
      "fans_club": 0,
      "favorite": "0"
    }
  ],
  "order_hot_videos": [
    {
      "acu": 0,
      "avg_watch": 0,
      "barrage": 0,
      "biz_id": "0",
      "comment": 0,
      "core_user_id": "0",
      "create_time": 1734082828,
      "create_timestamp": 0,
      "duration": 0,
      "duration_min": 0,
      "fans_club": 0,
      "favorite": "0"
    }
  ],
  "personal_hot_videos": []
}
```

### Response fields

| Field | Meaning |
|---|---|
| `masterpiece_videos[]` | List of videos the creator is known for. Each item uses the same video fields as the other lists. |
| `newest_videos[]` | List of the creator's most recent videos. |
| `order_hot_videos[]` | List of videos in the order hot group. The name suggests top videos from sponsored orders, but the response does not say so. |
| `personal_hot_videos[]` | List of personal hot videos. It can be empty, as in the sample. |
| `masterpiece_videos[].item_id` | ID of the video, as a string. Use it to identify the video in other calls. |
| `masterpiece_videos[].play` | Play count of the video. In the sample it is the most filled-in metric. |
| `masterpiece_videos[].create_time` | Creation time of the video as a Unix timestamp in seconds. |
| `masterpiece_videos[].like / comment / share / repin` | Engagement counts for the video. Many items return `0` here, so check `play` first. |
| `masterpiece_videos[].item_title / item_cover` | Title and cover image of the video. These can be empty strings. |
| `base_resp.status_code` | Status code of the response. `0` in the sample, with an empty `status_message`. |

### Notes

- Get `kolId` from [Douyin XingTu KOL ID by User ID](/apis/douyin/xingtu/xingtu-kolid-by-uid), [Douyin XingTu kolId Lookup](/apis/douyin/xingtu/xingtu-kolid-by-sec-user-id) or [Douyin XingTu KOL ID by Unique ID](/apis/douyin/xingtu/xingtu-kolid-by-unique-id).
- The request has no pagination parameter. Each list returns only a few videos.
- Many metric fields come back as `0` or an empty string in the sample, so `play`, `item_id` and `create_time` are the most reliable fields.

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Xingtu Author Hot Comment Keywords](/apis/douyin/xingtu/author-content-hot-comment-keywords-v1): Returns hot comment keywords from content produced by a Douyin Xingtu creator.
- [Douyin Xingtu Author Hot Comment Tokens (Xingtu)](/apis/douyin/xingtu/author-hot-comment-tokens-v1): Returns hot comment tokens for a Douyin Xingtu creator based on the specified creator ID.
- [Douyin Xingtu KOL Audience Portrait (V1)](/apis/douyin/xingtu/kol-audience-portrait-v1): Returns audience demographic and portrait insights for a Douyin Xingtu creator.

---
Machine-readable: [`catalog/models/douyin/xingtu/kol-rec-videos-v1.json`](../../../../catalog/models/douyin/xingtu/kol-rec-videos-v1.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu/kol-rec-videos-v1
