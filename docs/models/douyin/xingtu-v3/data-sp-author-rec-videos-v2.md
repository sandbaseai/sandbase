# Douyin Xingtu Recommended Videos API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-rec-videos-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) recommended videos for a specified creator and content channel. Use it to inspect representative content during creator research.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-rec-videos-v2", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-rec-videos-v2', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-rec-videos-v2", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-rec-videos-v2", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-rec-videos-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |

## Details

Returns four lists of recommended videos for one creator on Douyin Creator Marketplace (Xingtu): masterpiece, newest, order hot and personal hot. It needs the creator's `oAuthorId` and optionally a `platform` channel such as `SHORT_VIDEO`.

### Use cases

- Pull a creator's top-played videos to judge their best work before a brand deal.
- Check the newest videos to see how recent posts perform compared with older hits.
- Compare the order hot list with the personal hot list to see which videos did well in paid work versus organic posts.
- Collect `item_id` values to look up full video details in another API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-rec-videos-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `platform` | string | No | Platform type. |

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
      "create_time": 1790522586,
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
      "create_time": 1793659647,
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
      "create_time": 1779884754,
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
      "create_time": 1787229615,
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
| `masterpiece_videos[] / newest_videos[] / order_hot_videos[] / personal_hot_videos[]` | The four video lists. Each list holds video objects with the same fields. The names suggest masterpiece, latest, order-related hot and personal hot videos. |
| `masterpiece_videos[].item_id` | The video's ID, returned as a string. Use it to identify the video in other calls. |
| `masterpiece_videos[].play` | Play count of the video. In this sample it is the main metric with real values. |
| `masterpiece_videos[].create_time` | Creation time of the video as a Unix timestamp in seconds. |
| `masterpiece_videos[].item_title` | The video's title. It can be an empty string. |
| `masterpiece_videos[].item_cover` | Cover image field of the video. It can be empty. |
| `masterpiece_videos[].like / comment / share / favorite` | Engagement counts for the video. Many of these are `0` in the sample, so check for missing data before using them. |
| `masterpiece_videos[].interact_rate` | Interaction rate field of the video. It is `0` in this sample. |
| `masterpiece_videos[].duration` | Duration field of the video. It is `0` in this sample. |
| `base_resp.status_code` | Status code of the call. `0` appears on a successful response. |

### Notes

- Use `platform` to pick the content channel: `SHORT_VIDEO` (default), `LIVE_STREAMING`, `PICTURE_TEXT` or `SHORT_DRAMA`.
- Find a creator's `oAuthorId` with [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- Many metric fields return `0` or an empty string in the sample. Only `item_id`, `create_time` and `play` held values.
- For more of a creator's posts, call [Douyin Xingtu Creator Homepage Videos](/apis/douyin/xingtu-v3/aggregator-author-homepage-videos).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-rec-videos-v2.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-rec-videos-v2.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-rec-videos-v2
