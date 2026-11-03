# Douyin Related Posts Recommendations API: pricing, parameters and code examples

`douyin/web/related-posts` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended related posts for a specific Douyin video. Supports pagination using a refresh index and customizable post count limits.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/related-posts", "aweme_id": "7393365489105358132"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/related-posts', {'aweme_id': '7393365489105358132'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/related-posts", {
  "aweme_id": "7393365489105358132"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/related-posts", sandbase.Params{
	"aweme_id": "7393365489105358132",
})
```

Same call via the path form: `POST /v1/api/douyin/web/related-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, default is 20, it is recommended to keep it unchanged. default `20` |
| `aweme_id` | string | yes | Video id  |
| `refresh_index` | integer |  | Paging index, default is 1, then increase by 1 each time for paging. default `1` |

## Details

Returns a list of recommended Douyin videos related to one video. The input is the video's `aweme_id`. Each item in `aweme_list` holds the post text, author, hashtags, chapters and danmaku settings.

### Use cases

- Find videos that Douyin links to a given post, to study what content sits near it.
- Collect hashtags from related posts to see which topics cluster around a video.
- Read the AI chapter summaries of related long videos without opening each one.
- Page through more suggestions by raising `refresh_index` to build a larger set of related videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/related-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7393365489105358132"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number, default is 20, it is recommended to keep it unchanged. |
| `refresh_index` | integer | No | Paging index, default is 1, then increase by 1 each time for paging. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "ad_candidates": null,
      "ai_follow_images": null,
      "anchors": null,
      "authentication_token": "MS4wLjAA…",
      "author": {
        "avatar_thumb": {
          "height": 720,
          "uri": "100x100/aweme-avatar/tos-cn-i-0813c001_oEBnlHYiAAAuA9FHgEFru1CDJfHqfg9EAACC7I",
          "url_list": [
            "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c001_oEBnlHY…"
          ],
          "width": 720
        },
        "common_interest": null,
        "cover_url": [
          {
            "height": 720,
            "uri": "c8510002be9a3a61aad2",
            "url_list": [
              "https://p3-pc-sign.douyinpic.com/obj/c8510002be9a3a61aad2?lk3s=138a59ce&x-expire…"
            ],
            "width": 720
          }
        ],
        "custom_verify": "",
        "enterprise_verify_reason": "",
        "follow_status": 0,
        "follower_status": 0,
        "followers_detail": null
      },
      "author_user_id": 3935848376315614,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7703155542465842482",
      "aweme_listen_struct": {
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"not_intercept\",\"copyright_ta…"
      },
      "aweme_type": 0,
      "can_cache_to_local": true,
      "caption": "#历史 #美国 #人文星闪耀计划 #人物 #二战"
    }
  ],
  "chime_video_list": null,
  "filter_infos": null,
  "has_more": 1,
  "log_pb": {
    "impr_id": "202611031532293DB8359BA9C2541C2D10"
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[].aweme_id / aweme_list[].group_id` | ID of the related video. In this response both fields hold the same value. |
| `aweme_list[].desc` | Full post text, including hashtags. |
| `aweme_list[].caption` | Short caption of the post. It can differ from `desc`, which may have an extra title in front. |
| `aweme_list[].create_time` | Publish time of the video as a Unix timestamp in seconds. |
| `aweme_list[].duration` | Length of the video. Values such as `2920491` suggest milliseconds, but the response does not state the unit. |
| `aweme_list[].author_user_id` | Numeric ID of the account that posted the video. |
| `aweme_list[].author.avatar_thumb.url_list` | Image URLs for the author's small avatar. |
| `aweme_list[].cha_list[].cha_name / aweme_list[].cha_list[].cid` | Name and ID of each hashtag attached to the video. |
| `aweme_list[].chapter_abstract` | Text summary of the video content. It is an empty string when the video has none. |
| `aweme_list[].chapter_list[].desc / aweme_list[].chapter_list[].timestamp` | Title of each chapter and its start position in the video. Values such as `83000` suggest milliseconds. |
| `aweme_list[].danmaku_control.danmaku_cnt` | Number of danmaku (scrolling comments) on the video. |

### Notes

- Send the target video ID in `aweme_id`. Get it from a video link with [Douyin Video ID Extractor](/apis/douyin/web/aweme-id).
- To page, raise `refresh_index` by 1 on each call, starting at 1. `count` defaults to 20 and the docs advise leaving it unchanged.
- Many fields are `null` for some videos, such as `comment_list` and `anchors`. Check for `null` before you read them.
- Image URLs such as `cover_url` contain `x-expires` and `x-signature` query values, so save the image if you need it long term.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/related-posts.json`](../../../../catalog/models/douyin/web/related-posts.json) · Store page: https://www.sandbase.ai/model/douyin/web/related-posts
