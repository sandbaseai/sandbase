# Douyin Author Recommended Videos V2 API: pricing, parameters and code examples

`douyin/xingtu-v2/author-rec-videos-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call · **Modes:** sync

Get Author Recommended Videos V2 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.002 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/author-rec-videos-v2", "o_author_id": "7112600044674482187"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/author-rec-videos-v2', {'o_author_id': '7112600044674482187'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/author-rec-videos-v2", {
  "o_author_id": "7112600044674482187"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/author-rec-videos-v2", sandbase.Params{
	"o_author_id": "7112600044674482187",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/author-rec-videos-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `o_author_id` | string | yes | Creator ID  |
| `platform_source` | integer |  | Platform source, 1=Douyin default `1` |
| `platform_channel` | integer |  | Platform channel, 1=Douyin video default `1` |

## Details

Returns four lists of videos for one Douyin creator in Xingtu: masterpiece, newest, order hot and personal hot videos. Each video carries its `item_id`, `create_time` and `play` count. The only required input is the creator ID in `o_author_id`.

### Use cases

- Pull a creator's most played videos to judge their best past content before a brand deal.
- Check the newest videos of a creator to see how recently and how often they post.
- Collect `item_id` values from the hot lists to feed into video-level report APIs.
- Compare the order hot list with the personal hot list to see which videos performed in sponsored work and which in organic posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/author-rec-videos-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"o_author_id": "7112600044674482187", "platform_source": 1, "platform_channel": 1}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `o_author_id` | string | Yes | Creator ID |
| `platform_channel` | integer | No | Platform channel, 1=Douyin video |
| `platform_source` | integer | No | Platform source, 1=Douyin |

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
      "create_time": 1791057423,
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
      "create_time": 1791979120,
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
      "create_time": 1792948058,
      "create_timestamp": 0,
      "duration": 0,
      "duration_min": 0,
      "fans_club": 0,
      "favorite": "0"
    }
  ],
  "personal_hot_videos": [
    {
      "acu": 0,
      "avg_watch": 0,
      "barrage": 0,
      "biz_id": "0",
      "comment": 0,
      "core_user_id": "0",
      "create_time": 1791015055,
      "create_timestamp": 0,
      "duration": 0,
      "duration_min": 0,
      "fans_club": 0,
      "favorite": "0"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `masterpiece_videos[]` | Videos listed as the creator's masterpieces. Each item has the same video fields as the other lists. |
| `newest_videos[]` | The creator's latest videos. |
| `order_hot_videos[] / personal_hot_videos[]` | Two lists of hot videos for the creator, named order hot and personal hot. The names suggest sponsored-order videos and the creator's own videos, but the response does not define them. |
| `masterpiece_videos[].item_id` | ID of the video, as a string. The same field appears in every list. |
| `masterpiece_videos[].play` | Play count of the video. In the sample, values run from about 3.5 million to 36 million. |
| `masterpiece_videos[].create_time` | Creation time of the video as a Unix timestamp in seconds. |
| `masterpiece_videos[].like / comment / share` | Interaction counts for the video. They were `0` in the sample, so they may be empty for some videos. |
| `masterpiece_videos[].item_title / item_cover` | Title and cover image of the video. Both were empty strings in the sample. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means success. |

### Notes

- Get the creator ID for `o_author_id` from a lookup such as [Douyin XingTu kolId by Douyin ID](/apis/douyin/xingtu-v2/xingtu-kolid-by-unique-id) or [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator).
- Keep `platform_source` and `platform_channel` at `1` for Douyin video.
- Many numeric fields, such as `duration`, `impression` and `avg_watch`, were `0` in the sample. Rely on `item_id`, `play` and `create_time` for these videos.
- Use the `item_id` values with [Douyin Item Report Detail](/apis/douyin/xingtu-v2/item-report-detail) to look deeper at a single video.

### Pricing

$0.002 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/author-rec-videos-v2.json`](../../../../catalog/models/douyin/xingtu-v2/author-rec-videos-v2.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/author-rec-videos-v2
