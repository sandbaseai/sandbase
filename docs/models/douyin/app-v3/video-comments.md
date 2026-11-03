# Douyin Video Comments API: pricing, parameters and code examples

`douyin/app-v3/video-comments` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the comments on a Douyin video: comment text, publish time, like count, reply count and commenter location, with cursor pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-comments", "aweme_id": "7448118827402972455", "count": 20, "cursor": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-comments', {'aweme_id': '7448118827402972455', 'count': 20, 'cursor': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-comments", {
  "aweme_id": "7448118827402972455",
  "count": 20,
  "cursor": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-comments", sandbase.Params{
	"aweme_id": "7448118827402972455",
	"count": 20,
	"cursor": 0,
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG. default `20` |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. default `0` |
| `aweme_id` | string | yes | Video id  |

## Details

Returns the first-level comments on a Douyin video, with text, publish time, like count, reply count and the commenter's IP location. It needs the video ID in `aweme_id`. Results come in pages with a cursor.

### Use cases

- Read what viewers say about a product or campaign video and score the sentiment.
- Collect the questions viewers ask under a video to build an FAQ.
- Compare commenter regions using `ip_label` to see where an audience is based.
- Find comments with replies and call the replies API to read the threads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7565738211130035491"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comment_common_data": "MS4wLjAAAAAAK94fZypbcSoKKAxk0SidLyyXg0ilf_OVZdvKpflgNmdnEVcwf9dcRv6n68LYu5sDbbke…",
  "comment_config": {},
  "comment_insert_bars": null,
  "comments": [
    {
      "aweme_id": "7565738211130035491",
      "can_collect": false,
      "cid": "7703557083483915008",
      "comment_audio": {
        "content": "{\"status\":10,\"message\":\"success\",\"version\":3,\"video_id\":\"v03423g10003dbk8feq7dld…",
        "duration": 9571,
        "timbre_text": "识别到萌音",
        "timbre_type": "萌音",
        "vid": "v03423g10003dbk8feq7dldde24v8c80",
        "wave": "0.25079367,0.7111111,0.7619048,0.4936508,0.6333333,0.3857143,0.43650794,0.628571…"
      },
      "comment_token": "MS4wLjAA…",
      "content_type": 8,
      "create_time": 1793624155,
      "decorated_emoji_info": null,
      "digg_count": 0,
      "ent_parachute_tip": 0,
      "enter_from": "general_search",
      "image_list": null
    }
  ],
  "cursor": 20,
  "extra": {
    "fatal_item_ids": null,
    "now": 1793691105000,
    "scenes": null
  },
  "fast_response_comment": {
    "constant_response_words": [
      "赞"
    ],
    "timed_response_words": [
      "早上好"
    ]
  },
  "folded_comment_count": 0,
  "general_comment_config": {
    "survey_info": {
      "stay_duration": 10000,
      "survey_detail": "{\"icon_url_dark\":\"https://lf3-static.bytednsdoc.com/obj/eden-cn/wpozuvpahsly_lm_…",
      "survey_id": "1789370631",
      "survey_index": 0,
      "survey_lynx_uri": "aweme://lynxview/?surl=https%3A%2F%2Flf-dy-sourcecdn-tos.bytegecko.com%2Fobj%2Fb…",
      "survey_type": 2
    }
  },
  "has_more": 1,
  "hotsoon_filtered_count": 0,
  "log_pb": {
    "impr_id": "20261103153145C624057C7A1A9E123BFA"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `total` | Total number of comments on the video (5092 in this response). |
| `has_more` | Shows whether another page exists. `1` means more comments are available. |
| `cursor` | Value to send as `cursor` to get the next page. It was `20` after the first page. |
| `comments[].cid` | ID of the comment. |
| `comments[].text` | Comment text. It is an empty string for voice comments. |
| `comments[].create_time` | Publish time of the comment as a Unix timestamp in seconds. |
| `comments[].digg_count` | Number of likes on the comment. |
| `comments[].reply_comment_total` | Number of replies to the comment. |
| `comments[].ip_label` | Province-level location label of the commenter, such as `河南`. |
| `comments[].comment_audio.timbre_type / comments[].comment_audio.duration` | Present on voice comments. They give the voice style label and the audio length, with `duration` as a number in the response. |

### Notes

- Get `aweme_id` from a video list or detail API, for example [Douyin Video Detail](/apis/douyin/app-v3/one-video-v3).
- Send `cursor` as `0` for the first page. For the next page, pass the `cursor` value from the previous response.
- Keep `count` at the default `20`. The parameter notes say other values can cause bugs.
- To read replies under a comment, call [Douyin Video Comment Replies (App V3)](/apis/douyin/app-v3/video-comment-replies).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Hot Search List](/apis/douyin/app-v3/hot-search-list): Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.
- [Douyin Video Statistics (Batch)](/apis/douyin/app-v3/multi-video-statistics): Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.
- [Douyin Video Detail](/apis/douyin/app-v3/one-video-v3): Get the full data of a single Douyin post by ID (video, photo or article): description, author, hashtags, music, statistics and play URLs.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-comments.json`](../../../../catalog/models/douyin/app-v3/video-comments.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-comments
