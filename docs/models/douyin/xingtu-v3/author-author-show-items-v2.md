# Douyin Xingtu Showcase Items API: pricing, parameters and code examples

`douyin/xingtu-v3/author-author-show-items-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) showcase items for a creator, with content-channel, assignment, and flow filters. Use it to review a creator's marketplace showcase during commerce campaign planning.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/author-author-show-items-v2", "oAuthorId": "6870161898013196295"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/author-author-show-items-v2', {'oAuthorId': '6870161898013196295'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/author-author-show-items-v2", {
  "oAuthorId": "6870161898013196295"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/author-author-show-items-v2", sandbase.Params{
	"oAuthorId": "6870161898013196295",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/author-author-show-items-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `flowType` | string |  | Flow type filter. one of: `EXCLUDE`, `INCLUDE`; default `"EXCLUDE"` |
| `platform` | string |  | Platform type. one of: `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT`, `SHORT_DRAMA`; default `"SHORT_VIDEO"` |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `onlyAssign` | boolean |  | Whether to only include assigned items. default `false` |

## Details

Returns a creator's recent Douyin videos and Xingtu showcase videos, plus summary performance ratios for the creator. It needs the Xingtu author ID in `oAuthorId`, and you can filter by `platform`, `onlyAssign` and `flowType`.

### Use cases

- Review a creator's most recent videos and their play, like and share counts before you plan a commerce campaign.
- Check which videos the creator has listed in their Xingtu showcase and how each one performed.
- Compare a creator's play, interaction and view-rate ratios against the average in `data_description`.
- Pull video URLs and cover URIs to preview a creator's content style for a brand brief.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/author-author-show-items-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `oAuthorId` | string | Yes | Author's unique ID. |
| `flowType` | string | No | Flow type filter. |
| `onlyAssign` | boolean | No | Whether to only include assigned items. |
| `platform` | string | No | Platform type. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": "Success"
  },
  "data_description": {
    "interaction": {
      "compare_author": 0.48,
      "compare_avg": -0.0194,
      "rate": 0.0335
    },
    "interaction_enrollment": {
      "compare_author": 0,
      "compare_avg": -0.0806,
      "rate": 0
    },
    "play_medium": {
      "compare_author": 1,
      "compare_avg": 1397.0922421295331,
      "rate": 21350728
    },
    "play_medium_enrollment": {
      "compare_author": 0,
      "compare_avg": -1,
      "rate": 0
    },
    "video_view_rate": {
      "compare_author": 0.95,
      "compare_avg": 0.2292,
      "rate": 0.3797
    },
    "video_view_rate_enrollment": {
      "compare_author": 0,
      "compare_avg": -0.1214,
      "rate": 0
    }
  },
  "latest_item_info": [
    {
      "comment": 88,
      "core_user_id": "66598046050",
      "create_time": 1793546692,
      "create_timestamp": 1793546692,
      "duration": 21,
      "duration_min": 0,
      "head_image_uri": "tos-cn-i-dy/a3d2faae1be84a4ca329974e1accbdfd",
      "is_hot": false,
      "is_playlet": 0,
      "item_animated_cover": "tos-cn-i-dy/a3d2faae1be84a4ca329974e1accbdfd",
      "item_cover": "tos-cn-i-dy/a3d2faae1be84a4ca329974e1accbdfd",
      "item_date": "2026-11-01"
    }
  ],
  "latest_item_statics_antispam": {},
  "latest_star_item_info": [
    {
      "comment": 84,
      "core_user_id": "66598046050",
      "create_time": 1793421043,
      "create_timestamp": 1793421043,
      "duration": 235,
      "duration_min": 3,
      "head_image_uri": "tos-cn-i-dy/64c6cb23275c44adba8a6f1dfbbe1525",
      "is_hot": false,
      "is_playlet": 0,
      "item_animated_cover": "tos-cn-i-dy/64c6cb23275c44adba8a6f1dfbbe1525",
      "item_cover": "tos-cn-i-dy/64c6cb23275c44adba8a6f1dfbbe1525",
      "item_date": "2026-10-31"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `latest_item_info[]` | Recent videos from the creator. Each row holds the title, counts and IDs of one video. |
| `latest_star_item_info[]` | Videos from the creator's Xingtu showcase. These rows use the same fields as `latest_item_info[]`. |
| `latest_item_info[].item_id / latest_item_info[].video_id` | Identifiers of the video. `item_id` is a numeric string and `video_id` is a longer string key. |
| `latest_item_info[].item_title` | Title text of the video. It often holds hashtags and @mentions. |
| `latest_item_info[].play / like / comment / share` | Play, like, comment and share counts for the video. The same keys appear in `latest_star_item_info[]`. |
| `latest_item_info[].create_timestamp` | Creation time of the video as a Unix timestamp in seconds. `item_date` gives the same day as a `YYYY-MM-DD` string. |
| `latest_item_info[].duration` | Length of the video. `duration_min` is the minute part, shown as a whole number. |
| `latest_item_info[].url` | Share link to the video on Douyin. The response cuts long values, so the link may carry extra query parameters. |
| `data_description.interaction.rate / compare_avg` | Interaction `rate` for the creator and its difference from the average (`compare_avg`). Other blocks such as `play_medium` and `video_view_rate` use the same layout. |
| `base_resp.status_code / base_resp.status_message` | Call status. `0` with `Success` means the call worked. |

### Notes

- Get `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square).
- `platform` accepts `SHORT_VIDEO`, `LIVE_STREAMING`, `PICTURE_TEXT` and `SHORT_DRAMA`. The default is `SHORT_VIDEO`.
- `flowType` accepts `EXCLUDE` or `INCLUDE`. The default is `EXCLUDE`. `onlyAssign` defaults to `false`.
- Call [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info) for the creator's profile details.

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/author-author-show-items-v2.json`](../../../../catalog/models/douyin/xingtu-v3/author-author-show-items-v2.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/author-author-show-items-v2
