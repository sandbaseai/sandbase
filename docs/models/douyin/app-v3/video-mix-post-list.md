# Douyin Video Mix Post List API: pricing, parameters and code examples

`douyin/app-v3/video-mix-post-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of video posts belonging to a specific Douyin video compilation or mix. Query by mix_id with cursor-based pagination to retrieve post details and metadata.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-mix-post-list", "mix_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-mix-post-list', {'mix_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-mix-post-list", {
  "mix_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-mix-post-list", sandbase.Params{
	"mix_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-mix-post-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG.  |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response.  |
| `mix_id` | string | yes | Mix id  |

## Details

Returns the video posts that belong to one Douyin mix (a video compilation). You send a `mix_id` and get a page of posts with author, hashtag and permission data. Paging uses `cursor`.

### Use cases

- List every episode in a Douyin compilation to build a full watch order.
- Collect the `aweme_id` values of a mix, then fetch each video's details or statistics.
- Check which hashtags a creator attaches to the videos in one series.
- Check whether the posts in a mix allow comments, forwarding and sharing.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-mix-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mix_id": "7384792941870450726"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mix_id` | string | Yes | Mix id |
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "activity_video_type": -1,
      "admire_auth": {
        "admire_button": 1,
        "author_can_admire": 0,
        "exit_admire_in_aweme_post": 0,
        "is_admire": 0,
        "is_click_admire_icon_recently": 0,
        "is_fifty_admire_author_stable_fans": 0,
        "is_iron_fans_in_aweme_post": 0,
        "is_show_admire_button": 0
      },
      "ai_follow_images": null,
      "ancestor_info": {
        "gid": 7384475272541635072,
        "product_id": 32,
        "uid": 3326402489
      },
      "anchors": null,
      "authentication_token": "MS4wLjAA…",
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
        }
      },
      "author_mask_tag": 0,
      "author_user_id": 2557909361237356,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7384478157656673562",
      "aweme_listen_struct": {
        "listen_diversion": {
          "extra": [
            {
              "key": "new_guide_prefix",
              "val": "下载汽水"
            }
          ],
          "popup_scene": 4,
          "side_desc": "听更多精彩内容",
          "sub_title_type": "relation"
        },
        "music_cover_listen": 1,
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"has_listen_cp_new\",\"copyrigh…"
      }
    }
  ],
  "cursor": 15,
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103153142D21BE2032677DA43D82A",
    "now": 1793691102000
  },
  "has_more": 1,
  "item_id_to_episode": "{\"7384477694525836595\":2,\"7384478157656673562\":1,\"7384480323989556506\":3,\"738479…",
  "log_pb": {
    "impr_id": "20261103153142D21BE2032677DA43D82A"
  },
  "min_cursor": 0,
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | One entry per video post in the mix. |
| `aweme_list[].aweme_id` | ID of the video post, returned as a string. |
| `aweme_list[].author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_list[].author.avatar_168x168.url_list / avatar_300x300.url_list` | Avatar image URLs for the author at the 168x168 and 300x300 sizes. Each list holds a `webp` and a `jpeg` link. |
| `aweme_list[].cha_list[].cha_name / cid` | Name and ID of a hashtag attached to the video. |
| `aweme_list[].aweme_control.can_comment / can_forward / can_share` | Flags that show whether viewers can comment on, forward or share the post. |
| `aweme_list[].commerce_info.is_ad` | Shows whether the post is marked as an ad. |
| `aweme_list[].aweme_type` | Numeric post type code. The sample posts all return `0`. |
| `aweme_list[].comment_gid` | ID used for the comments of the post. It matches `aweme_id` in the sample. |

### Notes

- `mix_id` is a string of digits, for example `7384792941870450726`.
- Send `cursor` as `0` for the first page. For the next page, pass the cursor value from the previous response.
- Leave `count` at its default value. The parameter description warns that changing it causes bugs.
- To look at the mix itself, call [Douyin Video Mix Detail](/apis/douyin/app-v3/video-mix-detail). To get numbers for a single post, pass its `aweme_id` to [Douyin Video Statistics](/apis/douyin/app-v3/video-statistics).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-mix-post-list.json`](../../../../catalog/models/douyin/app-v3/video-mix-post-list.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-mix-post-list
