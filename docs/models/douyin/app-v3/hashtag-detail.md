# Douyin Hashtag Details API: pricing, parameters and code examples

`douyin/app-v3/hashtag-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves comprehensive information and metadata for a specific Douyin hashtag using its unique challenge identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/hashtag-detail", "ch_id": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/hashtag-detail', {'ch_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/hashtag-detail", {
  "ch_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/hashtag-detail", sandbase.Params{
	"ch_id": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/hashtag-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ch_id` | integer | yes | Hashtag id  |

## Details

Returns metadata for one Douyin hashtag (also called a challenge), including its name, creation time, participant count and total view count. It needs the numeric hashtag id in `ch_id`.

### Use cases

- Track the total `view_count` and `user_count` of a Douyin hashtag over repeated calls.
- Resolve a hashtag id to its readable name, such as `深海`, for reports and dashboards.
- Build a share link or app deep link for a hashtag from its `share_info.share_url` or `schema` value.
- Check whether a hashtag is on a billboard by reading its `billboard_rank` and `billboard_name`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/hashtag-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ch_id": 1575791821492238}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ch_id` | integer | Yes | Hashtag id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ch_info": {
    "allow_upload_cover": true,
    "author": {
      "accept_private_policy": false,
      "account_region": "",
      "ad_cover_url": null,
      "allow_story_normal_like": false,
      "apple_account": 0,
      "authority_status": 0,
      "avatar_168x168": {
        "height": 720,
        "uri": "168x168/aweme-avatar/tos-cn-avt-0015_e92dd08ff04ba878a6104672877eece4",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_e92dd08ff04ba878a61046…"
        ],
        "width": 720
      },
      "avatar_300x300": {
        "height": 720,
        "uri": "300x300/aweme-avatar/tos-cn-avt-0015_e92dd08ff04ba878a6104672877eece4",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-avt-0015_e92dd08ff04ba878a61046…"
        ],
        "width": 720
      },
      "avatar_larger": {
        "height": 720,
        "uri": "1080x1080/aweme-avatar/tos-cn-avt-0015_e92dd08ff04ba878a6104672877eece4",
        "url_list": [
          "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-avt-0015_e92dd08ff0…"
        ],
        "width": 720
      },
      "avatar_medium": {
        "height": 720,
        "uri": "720x720/aweme-avatar/tos-cn-avt-0015_e92dd08ff04ba878a6104672877eece4",
        "url_list": [
          "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_e92dd08ff04b…"
        ],
        "width": 720
      },
      "avatar_schema_list": null,
      "avatar_thumb": {
        "height": 720,
        "uri": "100x100/aweme-avatar/tos-cn-avt-0015_e92dd08ff04ba878a6104672877eece4",
        "url_list": [
          "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_e92dd08ff04b…"
        ],
        "width": 720
      }
    },
    "banner_list": null,
    "billboard_name": "",
    "billboard_rank": 0,
    "billboard_type": 0,
    "billboard_url": "",
    "cha_attrs": null,
    "cha_name": "深海",
    "challenge_status": 1,
    "cid": "1575791821492238",
    "collect_stat": 0
  },
  "dynamic_list": null,
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110315313535B3DB839B42701199A0",
    "now": 1793691095000
  },
  "log_pb": {
    "impr_id": "2026110315313535B3DB839B42701199A0"
  },
  "rec_list": null,
  "shoot_mob_extras": {},
  "slide_list": null,
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `ch_info.cha_name` | Display name of the hashtag, without the # sign. |
| `ch_info.cid` | Hashtag id as a string. It matches the `ch_id` you sent. |
| `ch_info.view_count` | Total views recorded for the hashtag. |
| `ch_info.user_count` | Number of users counted as participating in the hashtag. |
| `ch_info.create_time / ch_info.update_time` | Unix timestamps in seconds for when the hashtag was created and last updated. |
| `ch_info.desc` | Hashtag description text. It can be an empty string. |
| `ch_info.share_info.share_url / ch_info.schema` | Web share link and Douyin app deep link for the hashtag. |
| `ch_info.share_info.share_title` | Share text that includes the hashtag name. |
| `ch_info.billboard_name / ch_info.billboard_rank` | Billboard name and rank for the hashtag. Empty and `0` values mean no billboard entry is shown. |
| `ch_info.author.avatar_larger.url_list[]` | Image URLs for the avatar of the user attached to the hashtag in `ch_info.author`. |

### Notes

- The hashtag id is the `cid` value inside the `schema` link, for example `aweme://aweme/challenge/detail?cid=1575791821492238`.
- Image URLs in the response carry `x-expires` and `x-signature` parameters, so download images soon after the call.
- To list videos under a hashtag, call [Douyin Hashtag Video List](/apis/douyin/app-v3/hashtag-video-list).
- To see trending hashtags, try [Douyin Hot Challenge List](/apis/douyin/billboard/hot-challenge-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/hashtag-detail.json`](../../../../catalog/models/douyin/app-v3/hashtag-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/hashtag-detail
