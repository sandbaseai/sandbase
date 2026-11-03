# TikTok Video Comment Keywords API: pricing, parameters and code examples

`tiktok/analytics/comment-keywords` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns extracted keywords and topics from user comments on a TikTok video. Queries are filtered by the unique video identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/analytics/comment-keywords", "item_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/analytics/comment-keywords', {'item_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/analytics/comment-keywords", {
  "item_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/analytics/comment-keywords", sandbase.Params{
	"item_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/analytics/comment-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video ID, required parameter, can be obtained from video sharing links or TikTok Studio  |

## Details

Returns keywords and short phrases pulled from the comments on one TikTok video. Each keyword comes with example comments that contain it. The only input is the video ID in `item_id`.

### Use cases

- Find the phrases viewers repeat most in the comments of a single video.
- Read sample comments behind each phrase to see how viewers talk about a topic.
- Spot the most liked comments that mention a phrase.
- Compare the keyword lists of several videos to see which topics come up again.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/analytics/comment-keywords" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7350810998023949599"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video ID, required parameter, can be obtained from video sharing links or TikTok Studio |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "item_id": "7350810998023949599",
  "key_words": {
    "comment_key_words": [
      {
        "comments": [
          {
            "channel_id": 0,
            "cid": "7350994816208044831",
            "comment_author": {
              "cover": {
                "url_list": [
                  "https://p16-common-sign.tiktokcdn-us.com/tos-useast8-avt-0068-tx2/83a239de10dcb0…"
                ]
              },
              "nick_name": "Itsmellow",
              "uid": "7312929108468139054"
            },
            "comment_type": 0,
            "create_date": 1711536918,
            "digg_count": 0,
            "text": "Yo if you look again I’m pretty sure she made it"
          }
        ],
        "key_word": "pretty sure"
      }
    ],
    "message": {
      "data_source": 1,
      "status": 1,
      "timestamp": 1793691831
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `item_id` | The video ID that was queried. It matches the `item_id` in the request. |
| `key_words.comment_key_words[].key_word` | An extracted keyword or phrase, such as `pretty sure` or `long way`. |
| `key_words.comment_key_words[].comments[].text` | The text of a comment that contains the keyword. |
| `key_words.comment_key_words[].comments[].cid` | The ID of the comment. |
| `key_words.comment_key_words[].comments[].digg_count` | The like count of the comment. |
| `key_words.comment_key_words[].comments[].create_date` | The time the comment was posted, as a Unix timestamp in seconds. |
| `key_words.comment_key_words[].comments[].comment_author.nick_name / key_words.comment_key_words[].comments[].comment_author.uid` | The display name and the user ID of the person who wrote the comment. |
| `key_words.comment_key_words[].comments[].comment_author.cover.url_list[]` | Image URLs for the comment author's avatar. |

### Notes

- Get `item_id` from a TikTok video sharing link or from TikTok Studio. It is a numeric string such as `7350810998023949599`.
- Each keyword in the response holds a short list of comments, not every comment on the video.
- To see views, likes and other metrics for the same video, call [TikTok Video Metrics](/apis/tiktok/analytics/video-metrics).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Creator Info and Milestones](/apis/tiktok/analytics/creator-info-and-milestones): Returns creator details and milestone history for a specified TikTok account.
- [Detect fake views in video](/apis/tiktok/analytics/detect-fake-views): Check whether a TikTok video has fake views.
- [TikTok Video Metrics](/apis/tiktok/analytics/video-metrics): Retrieve detailed analytics for TikTok videos, including total views, likes, comments, favorites, and 14-day daily performance trends using a video identifier.

---
Machine-readable: [`catalog/models/tiktok/analytics/comment-keywords.json`](../../../../catalog/models/tiktok/analytics/comment-keywords.json) · Store page: https://www.sandbase.ai/model/tiktok/analytics/comment-keywords
