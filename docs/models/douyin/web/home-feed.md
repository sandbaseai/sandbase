# Douyin Web Home Feed API: pricing, parameters and code examples

`douyin/web/home-feed` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves the Douyin web home feed containing video listings and media metadata. Supports setting the item count and pagination index.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/home-feed", "count": 10, "refresh_index": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/home-feed', {'count': 10, 'refresh_index': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/home-feed", {
  "count": 10,
  "refresh_index": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/home-feed", sandbase.Params{
	"count": 10,
	"refresh_index": 0,
})
```

Same call via the path form: `POST /v1/api/douyin/web/home-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number, default is 10, it is recommended to keep it unchanged.  |
| `refresh_index` | integer |  | Refresh/paging index, start at 0 and +1 per page.  |

## Details

This API returns a page of videos from the Douyin web home feed. It needs no input, and you can set `count` and `refresh_index` to control the batch size and the page.

### Use cases

- Collect a sample of recommended Douyin videos with their captions and author IDs.
- Page through the home feed by raising `refresh_index` to build a list of video IDs for later lookups.
- Track which hashtags appear in feed captions by reading `desc` and `caption`.
- Check which feed videos allow comments or sharing using the `aweme_control` flags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number, default is 10, it is recommended to keep it unchanged. |
| `refresh_index` | integer | No | Refresh/paging index, start at 0 and +1 per page. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_list": [
    {
      "ad_candidates": null,
      "ai_follow_images": null,
      "authentication_token": "MS4wLjAA…",
      "author": {
        "avatar_thumb": {
          "height": 720,
          "uri": "100x100/aweme-avatar/tos-cn-avt-0015_b0561efc1a4d84e5ec492deaac6c1f28",
          "url_list": [
            "https://p3-pc.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_b0561efc1…"
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
        "is_ad_fake": false
      },
      "author_user_id": 3207689576654832,
      "aweme_control": {
        "can_comment": true,
        "can_forward": true,
        "can_share": true,
        "can_show_comment": true
      },
      "aweme_id": "7674483865485987108",
      "aweme_listen_struct": {
        "trace_info": "{\"copyright_not_speech\":\"false\",\"copyright_reason\":\"not_intercept\",\"copyright_ta…"
      },
      "aweme_type": 0,
      "can_cache_to_local": true,
      "caption": "#原创动漫 #原创漫剧 #二次元 #甜文 #ai漫剧",
      "chapter_abstract": ""
    }
  ],
  "has_more": 1,
  "log_pb": {
    "impr_id": "2026110315322802C13721EFCFF357478D"
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_list[]` | The list of feed items. Each item is one Douyin video. |
| `aweme_list[].aweme_id` | The ID of the video, as a string. Use it to look up the video in other APIs. |
| `aweme_list[].desc / aweme_list[].caption` | The video text. `desc` is the full description and `caption` is the hashtag line. |
| `aweme_list[].create_time` | When the video was created, as a Unix timestamp in seconds. |
| `aweme_list[].author_user_id` | The numeric user ID of the video author. |
| `aweme_list[].author.avatar_thumb.url_list[]` | Links to the author's avatar image. |
| `aweme_list[].aweme_control.can_comment / aweme_list[].aweme_control.can_share` | Flags that show whether comments and sharing are allowed on the video. |
| `aweme_list[].chapter_list[]` | Chapter markers for the video, when present. Each has a `desc` title, a `timestamp` and an image `url`. |
| `has_more` | Shows whether more items are available. The value `1` means you can request the next page. |
| `log_pb.impr_id` | The impression ID of this feed request. |

### Notes

- Start with `refresh_index` set to `0` and add `1` for each next page.
- Keep `count` at its default of `10`, as the parameter documentation recommends.
- Some items have `null` for fields such as `chapter_list`, so check for null before you read them.
- Pass an `aweme_id` to [Douyin Single Video Details (V1)](/apis/douyin/web/one-video) to get more detail on one video.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/home-feed.json`](../../../../catalog/models/douyin/web/home-feed.json) · Store page: https://www.sandbase.ai/model/douyin/web/home-feed
