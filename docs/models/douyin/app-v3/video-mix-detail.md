# Douyin Video Mix Detail API: pricing, parameters and code examples

`douyin/app-v3/video-mix-detail` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information about a specific Douyin video compilation playlist based on the provided mix identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-mix-detail", "mix_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-mix-detail', {'mix_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-mix-detail", {
  "mix_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-mix-detail", sandbase.Params{
	"mix_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-mix-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mix_id` | string | yes | Mix id  |

## Details

Returns details for one Douyin video compilation (mix), including its name, description, author, play and collect counts, and share link. It needs a `mix_id`, the numeric ID of the mix.

### Use cases

- Check how many episodes a Douyin mix has and how many plays it has reached.
- Track the growth of a learning or series mix by comparing `statis.play_vv` and `statis.collect_vv` over time.
- Get the share link and cover image of a mix for a content catalog.
- Identify the creator of a mix from the author profile attached to it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-mix-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mix_id": "7384792941870450726"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mix_id` | string | Yes | Mix id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "202611031531421E24DA0C17973011DE31",
    "now": 1793691102000
  },
  "log_pb": {
    "impr_id": "202611031531421E24DA0C17973011DE31"
  },
  "mix_info": {
    "author": {
      "accept_private_policy": false,
      "account_region": "",
      "ad_cover_url": null,
      "allow_story_normal_like": false,
      "apple_account": 0,
      "authority_status": 0,
      "avatar_168x168": {
        "height": 720,
        "uri": "168x168/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0…"
        ],
        "width": 720
      },
      "avatar_300x300": {
        "height": 720,
        "uri": "300x300/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/img/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0…"
        ],
        "width": 720
      },
      "avatar_larger": {
        "height": 720,
        "uri": "1080x1080/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/aweme/1080x1080/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVF…"
        ],
        "width": 720
      },
      "avatar_medium": {
        "height": 720,
        "uri": "720x720/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFAp…"
        ],
        "width": 720
      },
      "avatar_schema_list": null,
      "avatar_thumb": {
        "height": 720,
        "uri": "100x100/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFApMfIA8eW6A0AfIFfANnCa8h1D",
        "url_list": [
          "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_ooQ2tkQ4kDVFAp…"
        ],
        "width": 720
      }
    },
    "cover_url": {
      "height": 720,
      "uri": "tos-cn-i-dy/3c8e3cda77604466a0686b9c368ea4a9",
      "url_list": [
        "https://p3-sign.douyinpic.com/obj/tos-cn-i-dy/3c8e3cda77604466a0686b9c368ea4a9?l…"
      ],
      "width": 720
    },
    "create_time": 1719406093,
    "desc": "直观理解计算机技术",
    "extra": "{\"content_sub_type\":0,\"sub_type\":0,\"game_content_collection_id\":\"\",\"top_item_con…",
    "has_recommend_mix": 1,
    "ids": null,
    "is_iaa": 0,
    "is_serial_mix": 0,
    "mix_id": "7384792941870450726",
    "mix_name": "直观理解计算机技术 coredumped",
    "mix_pic_type": 0
  },
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `mix_info.mix_id` | ID of the mix. It matches the `mix_id` you sent. |
| `mix_info.mix_name / mix_info.desc` | Title and short description of the mix. |
| `mix_info.statis.play_vv` | Total play count of the mix. |
| `mix_info.statis.collect_vv` | Number of times users have collected the mix. |
| `mix_info.statis.updated_to_episode` | Number of the latest episode in the mix. |
| `mix_info.create_time / mix_info.update_time` | Unix timestamps in seconds for when the mix was created and last updated. |
| `mix_info.cover_url.url_list[]` | Cover image URLs for the mix. The URLs are signed and carry an `x-expires` value. |
| `mix_info.share_info.share_url` | Public share link for the mix page. |
| `mix_info.share_info.share_title / mix_info.share_info.share_desc` | Text Douyin shows when a user shares the mix. |
| `mix_info.author.avatar_larger.url_list[]` | Avatar image URLs of the mix author. Smaller sizes are in `avatar_300x300`, `avatar_168x168` and `avatar_thumb`. |

### Notes

- `mix_id` is a numeric string, for example `7384792941870450726`. Send it as a string.
- A successful call returns `status_code` `0` and the data under `mix_info`.
- To list the videos inside a mix, call [Douyin Video Mix Post List](/apis/douyin/app-v3/video-mix-post-list) with the same mix ID.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-mix-detail.json`](../../../../catalog/models/douyin/app-v3/video-mix-detail.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-mix-detail
