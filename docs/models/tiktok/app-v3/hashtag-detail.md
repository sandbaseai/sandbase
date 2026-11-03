# TikTok Hashtag Detail API: pricing, parameters and code examples

`tiktok/app-v3/hashtag-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information for a specified TikTok hashtag. Queries require a hashtag identifier and accept an optional country region code.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/hashtag-detail", "ch_id": "7551"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/hashtag-detail', {'ch_id': '7551'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/hashtag-detail", {
  "ch_id": "7551"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/hashtag-detail", sandbase.Params{
	"ch_id": "7551",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/hashtag-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ch_id` | string | yes | Hashtag id  |
| `region` | string |  | Region, supports US, GB, FR, JP, VN, SG, default US default `"US"` |

## Details

Returns details for one TikTok hashtag, including its name, ID, share link, and usage and view counts. It needs the hashtag ID as `ch_id` and accepts an optional `region` code.

### Use cases

- Read the total view count of a hashtag such as `cat` to compare it with other tags.
- Store the `use_count` of a hashtag over time to see how fast its use grows.
- Get the share URL and share text of a hashtag to build a link in a report or app.
- Check whether a hashtag is flagged as commercial before you plan a campaign around it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/hashtag-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ch_id": "7551"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ch_id` | string | Yes | Hashtag id |
| `region` | string | No | Region, supports US, GB, FR, JP, VN, SG, default US |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ch_info": {
    "allow_upload_cover": true,
    "author": {
      "account_labels": null,
      "ad_cover_url": null,
      "advance_feature_item_order": null,
      "advanced_feature_info": null,
      "bold_fields": null,
      "can_message_follow_status_list": null,
      "can_set_geofencing": null,
      "cha_list": null,
      "cover_url": null,
      "events": null,
      "followers_detail": null,
      "geofencing": null
    },
    "banner_list": null,
    "cha_attrs": null,
    "cha_name": "cat",
    "cid": "7551",
    "collect_stat": 0,
    "connect_music": [],
    "desc": "",
    "extra_attr": {
      "is_live": false
    },
    "hashtag_profile": "https://p16-common-sign.tiktokcdn-us.com/musically-maliva-obj/2e13829d6e18167082…",
    "is_challenge": 0
  },
  "dynamic_list": null,
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110307435349CFD9AA1E8F98029FC1",
    "now": 1793691833000
  },
  "log_pb": {
    "impr_id": "2026110307435349CFD9AA1E8F98029FC1"
  },
  "rec_list": null,
  "slide_list": null,
  "status_code": 0,
  "status_msg": "",
  "version": "v2"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ch_info.cha_name` | Name of the hashtag, without the `#` sign. The sample value is `cat`. |
| `ch_info.cid` | ID of the hashtag as a string. It matches the `ch_id` you sent. |
| `ch_info.view_count` | Total number of views counted for the hashtag. |
| `ch_info.use_count / ch_info.user_count` | Counts tied to the hashtag's usage. In the sample both have the same value. |
| `ch_info.desc` | Hashtag description text. It can be an empty string. |
| `ch_info.hashtag_profile` | URL of the hashtag's profile image. |
| `ch_info.is_commerce` | Boolean flag that shows whether the hashtag is marked as commercial. |
| `ch_info.share_info.share_url` | Public TikTok web link to the hashtag page. |
| `ch_info.share_info.share_desc / ch_info.share_info.share_title` | Text TikTok uses when someone shares the hashtag. |
| `ch_info.schema` | App deep link that opens the hashtag detail page in the TikTok app. |

### Notes

- `ch_id` is a numeric ID sent as a string, for example `7551`. Find IDs with [TikTok Hashtag Search Results](/apis/tiktok/app-v3/hashtag-search-result).
- `region` supports `US`, `GB`, `FR`, `JP`, `VN`, `SG`. The default is `US`.
- To list videos that use the hashtag, call [TikTok Hashtag Video List](/apis/tiktok/app-v3/hashtag-video-list) next.
- Many fields, such as those under `ch_info.author`, return `null` for this hashtag.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/hashtag-detail.json`](../../../../catalog/models/tiktok/app-v3/hashtag-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/hashtag-detail
