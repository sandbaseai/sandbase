# Zhihu Answer Comments API: pricing, parameters and code examples

`zhihu/web/comment-v5` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the comments on a Zhihu answer: comment text, author, time, like and reply counts, with sorting and pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/comment-v5", "answer_id": "2023560406912770519"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/comment-v5', {'answer_id': '2023560406912770519'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/comment-v5", {
  "answer_id": "2023560406912770519"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/comment-v5", sandbase.Params{
	"answer_id": "2023560406912770519",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/comment-v5` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of comments per page  |
| `offset` | string |  | Offset/Page Number  |
| `order_by` | string |  | Sort  |
| `answer_id` | string | yes | Answer ID  |

## Details

Returns the top-level comments on a Zhihu answer, each with its text, author, creation time, like and dislike counts, and a few preview replies. It needs an `answer_id`. Paging and sort order are optional.

### Use cases

- Pull the most liked comments on an answer to see which views the readers agree with.
- Track how the comment count on an answer changes by reading `counts.total_counts` over time.
- Collect comment text with the author's city tag for a study of how opinions differ by region.
- Find comments with many replies, then fetch their full reply threads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/comment-v5" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"answer_id": "2023560406912770519"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `answer_id` | string | Yes | Answer ID |
| `limit` | string | No | Number of comments per page |
| `offset` | string | No | Offset/Page Number |
| `order_by` | string | No | Sort |

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
    "total_counts": 269
  },
  "data": [
    {
      "_": null,
      "author": {
        "avatar_url": "https://picx.zhimg.com/v2-27bc715d780ecfc2402e01ada9c0e98f_l.jpg?source=06d4cd63",
        "avatar_url_template": "https://pic1.zhimg.com/v2-27bc715d780ecfc2402e01ada9c0e98f_l.jpg?source=06d4cd63",
        "badge_v2": {
          "detail_badges": null,
          "merged_badges": null,
          "title": ""
        },
        "exposed_medal": {
          "avatar_url": "https://pica.zhimg.com/v2-0cbfd5688630e180e5732c71b9935608_r.jpg?source=06d4cd63",
          "can_click": true,
          "description": "赞同 30 次",
          "medal_avatar_frame": "",
          "medal_id": "972460827463282688",
          "medal_name": "表示赞同",
          "mini_avatar_url": "https://pica.zhimg.com/v2-0cbfd5688630e180e5732c71b9935608_r.jpg?source=06d4cd63"
        },
        "gender": 1,
        "headline": "",
        "id": "318f3f9198703cf6aff20e05b75ca635",
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
    "toast": "彼此欣赏让讨论更加充实"
  },
  "header": [],
  "is_content_author": false,
  "is_content_rewardable": true,
  "paging": {
    "is_end": false,
    "is_start": true,
    "next": "https://www.zhihu.com/api/v4/comment_v5/answers/2023560406912770519/root_comment…",
    "previous": "https://www.zhihu.com/api/v4/comment_v5/answers/2023560406912770519/root_comment…",
    "totals": 269
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
| `counts.total_counts` | Total number of comments on the answer. |
| `data[].id` | ID of the comment, as a string. |
| `data[].content` | Comment text. Some comments contain HTML such as `<p>` and `<a>` tags. |
| `data[].created_time` | Time the comment was created, as a Unix timestamp in seconds. |
| `data[].like_count / dislike_count` | Number of likes and dislikes on the comment. |
| `data[].child_comment_count` | Number of replies under the comment. |
| `data[].child_comments[]` | A short preview of replies to the comment. Each item has the same shape as a top-level comment. |
| `data[].child_comment_next_offset` | Cursor value for the next page of replies to this comment. |
| `data[].author.id / author.headline` | ID and profile headline of the comment author. |
| `data[].comment_tag[].text` | Tag shown on the comment. Tags with `type` set to `ip_info` hold a place name such as `上海`. |
| `paging.is_end` | `false` when more pages of comments are available. |

### Notes

- Get the `answer_id` from a Zhihu answer URL, or from [Zhihu Question Answers](/apis/zhihu/web/question-answers).
- Use `limit` and `offset` to page through comments. `paging.is_end` shows whether you have reached the last page.
- To read all replies under one comment, call [Zhihu Sub Comments](/apis/zhihu/web/sub-comment-v5).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…
- [Zhihu Hot List](/apis/zhihu/web/hot-list): Get the Zhihu hot list: trending questions with title, excerpt, heat, answer and follower counts, and links.
- [Get Zhihu AI Search (v2)](/apis/zhihu/web/ai-search-stream): Get Zhihu AI Search results (new endpoint).

---
Machine-readable: [`catalog/models/zhihu/web/comment-v5.json`](../../../../catalog/models/zhihu/web/comment-v5.json) · Store page: https://www.sandbase.ai/model/zhihu/web/comment-v5
