# Zhihu Pin Comments API: pricing, parameters and code examples

`zhihu/web/pin-comments` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comments for a Zhihu pin, including author details, like counts, and reply counts. Supports sorting by score or newest timestamp.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/pin-comments", "pin_id": "2050290260991534603"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/pin-comments', {'pin_id': '2050290260991534603'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/pin-comments", {
  "pin_id": "2050290260991534603"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/pin-comments", sandbase.Params{
	"pin_id": "2050290260991534603",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/pin-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of comments per page default `"20"` |
| `offset` | string |  | Offset, take the cursor from the response for paging default `""` |
| `pin_id` | string | yes | Pin ID  |
| `order_by` | string |  | Sort, score=default, ts=newest one of: `score`, `ts`; default `"score"` |

## Details

Returns the top-level comments on a Zhihu pin, with author details, like counts, reply counts and creation times. It needs one input, the `pin_id` of the pin.

### Use cases

- Collect reader feedback under a Zhihu pin for review or analysis.
- Rank comments by `score` or list the newest ones first with `order_by`.
- Find which commenters on a pin have replies by checking `child_comment_count`.
- Build a list of commenters with their headlines and medals for outreach research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/pin-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"pin_id": "2050290260991534603"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pin_id` | string | Yes | Pin ID |
| `limit` | string | No | Number of comments per page |
| `offset` | string | No | Offset, take the cursor from the response for paging |
| `order_by` | string | No | Sort, score=default, ts=newest |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_plugin_infos": [],
  "atmosphere_voting_config": {
    "daily_frequency": 1,
    "detail": [
      {
        "emoji_level": "dissatisfied",
        "normal_icon": "https://picx.zhimg.com/v2-1d5d094f0cd71f7da08e7e54d037c0b5.png",
        "selected_icon": "https://picx.zhimg.com/v2-9af3c8aa46b63f2f840138b0ee6b0a99.png",
        "title": "不满"
      }
    ],
    "frequency_interval": 3,
    "location": 3,
    "min_num_of_root_comment": 10,
    "title": "你对该内容下的评论氛围是否满意？"
  },
  "comment_status": {
    "induce_text": "",
    "text": "",
    "type": 0
  },
  "counts": {
    "collapsed_counts": 0,
    "reviewing_counts": 0,
    "segment_comment_counts": 0,
    "total_counts": 13
  },
  "data": [
    {
      "_": null,
      "author": {
        "avatar_url": "https://pic1.zhimg.com/v2-06e80e5b987155fd91c0b48c35fea502_l.jpg?source=06d4cd63",
        "avatar_url_template": "https://picx.zhimg.com/v2-06e80e5b987155fd91c0b48c35fea502_l.jpg?source=06d4cd63",
        "badge_v2": {
          "detail_badges": null,
          "merged_badges": null,
          "title": ""
        },
        "exposed_medal": {
          "avatar_url": "https://picx.zhimg.com/v2-388966b5f4af924b2610a8f9e9001dc4_r.jpg?source=06d4cd63",
          "can_click": true,
          "description": "连续答题 15 天",
          "medal_avatar_frame": "",
          "medal_id": "972481762269622272",
          "medal_name": "笔耕不辍",
          "mini_avatar_url": "https://picx.zhimg.com/v2-388966b5f4af924b2610a8f9e9001dc4_r.jpg?source=06d4cd63"
        },
        "gender": 0,
        "headline": "拥抱AI，做AI知识的传播者，做AI应用的实践者。",
        "id": "bee34cad7542c3006331794fb0e69bf6",
        "is_advertiser": false
      },
      "author_tag": [],
      "can_annotation": false,
      "can_author_top": false,
      "can_collapse": false,
      "can_delete": false,
      "can_dislike": true,
      "can_hot": false,
      "can_like": true,
      "can_more": true,
      "can_reply": true
    }
  ],
  "edit_status": {
    "can_reply": true,
    "toast": "多元视角碰撞无限可能"
  },
  "header": [],
  "is_content_author": false,
  "is_content_rewardable": false,
  "paging": {
    "is_end": true,
    "is_start": true,
    "next": "https://www.zhihu.com/api/v4/comment_v5/pins/2050290260991534603/root_comment?li…",
    "previous": "https://www.zhihu.com/api/v4/comment_v5/pins/2050290260991534603/root_comment?li…",
    "totals": 13
  },
  "sorter": [
    {
      "text": "默认",
      "type": "score"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].content` | Text of the comment. |
| `data[].id` | ID of the comment, as a string. |
| `data[].created_time` | Time the comment was created. The value is a Unix timestamp in seconds. |
| `data[].like_count / dislike_count` | Number of likes and dislikes on the comment. |
| `data[].child_comment_count` | Number of replies under the comment. `child_comments` holds the reply items. |
| `data[].author.id / author.headline` | ID and profile headline of the commenter. |
| `data[].comment_tag[].text` | Tag shown with the comment. Items of type `ip_info` show a place name such as a province or country. |
| `counts.total_counts` | Total number of comments on the pin. |
| `paging.next / paging.previous` | URLs for the next and previous page. The `offset` value inside each URL is the cursor for paging. |
| `paging.is_end` | Tells you whether this page is the last one. |

### Notes

- Get the `pin_id` from a pin link or from [Zhihu User Pins](/apis/zhihu/web/user-pins). Use [Zhihu Pin Detail](/apis/zhihu/web/pin-detail) for the pin itself.
- To page, copy the `offset` value from `paging.next` into the `offset` parameter. Use `limit` to set the page size.
- Set `order_by` to `score` for the default ranking or `ts` for the newest comments. The `sorter` array lists both options.
- To read replies to a comment, call [Zhihu Sub Comments](/apis/zhihu/web/sub-comment-v5).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/pin-comments.json`](../../../../catalog/models/zhihu/web/pin-comments.json) · Store page: https://www.sandbase.ai/model/zhihu/web/pin-comments
