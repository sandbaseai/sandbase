# Zhihu Hot Recommendations API: pricing, parameters and code examples

`zhihu/web/hot-recommend` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns hot recommendation items and content snippets from Zhihu Web. Supports pagination through offset and page_number alongside an optional session_token.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/hot-recommend"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/hot-recommend', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/hot-recommend", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/hot-recommend", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zhihu/web/hot-recommend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string |  | Offset default `"0"` |
| `page_number` | string |  | Page Number default `"1"` |
| `session_token` | string |  | Session Token default `""` |

## Details

Returns a page of recommended feed items from the Zhihu web home feed. Each item holds an answer with its author, text excerpt and comment count. All inputs are optional: `offset`, `page_number` and `session_token`.

### Use cases

- Collect the answers Zhihu currently recommends to build a content curation feed.
- Store answer excerpts and author details to study which topics and writers appear in the feed.
- Collect answer IDs from the feed and fetch full answers with a second call.
- Compare feed pages across `page_number` values to see how the recommendation list changes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/hot-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `offset` | string | No | Offset |
| `page_number` | string | No | Page Number |
| `session_token` | string | No | Session Token |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "action_card": false,
      "attached_info": "CpIGCMS6qfuZhIW7vAEQBBoJODAyNzYwNDY5IOjBgdcGKAEwAUABSkIKLVRTX1NPVVJDRV9UV09UT1dF…",
      "brief": "{\"source\": \"TS\", \"type\": \"answer\", \"id\": 2098451264585704463}",
      "created_time": 1793692132,
      "id": "1_1793692132.933",
      "offset": 1,
      "target": {
        "allow_segment_interaction": true,
        "answer_type": "normal",
        "author": {
          "avatar_url": "https://pic1.zhimg.com/50/v2-abed1a8c04700ba7d72b45195223e0ff_l.jpg?source=b6762…",
          "followers_count": 1,
          "gender": -1,
          "headline": "",
          "id": "438712683e436fb415549acab460ed58",
          "is_followed": false,
          "is_following": false,
          "is_org": false
        },
        "comment_count": 1,
        "content": "<p data-pid=\"gonXIEys\">会降价并且已经降价完了，现在先不要买，等第二波看看吧</p><p data-pid=\"oemngc15\">抖音10…",
        "created_time": 1793089768,
        "excerpt": "会降价并且已经降价完了，现在先不要买，等第二波看看吧 抖音10月15日-10月18日是第一波，店铺本身降价且有平台消费券领，我看到好多装机博主，都降价了，97x…",
        "excerpt_new": "会降价并且已经降价完了，现在先不要买，等第二波看看吧 抖音10月15日-10月18日是第一波，店铺本身降价且有平台消费券领，我看到好多装机博主，都降价了，97x…"
      },
      "type": "feed",
      "updated_time": 1793692132,
      "verb": "TOPIC_ACKNOWLEDGED_ANSWER"
    }
  ],
  "fresh_text": "推荐已更新",
  "paging": {
    "is_end": false,
    "is_start": false,
    "next": "https://www.zhihu.com/api/v3/feed/topstory/recommend?action=down&ad_interval=-10…",
    "previous": "https://www.zhihu.com/api/v3/feed/topstory/recommend?action=pull&ad_interval=-10…",
    "totals": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One recommended feed item. The list holds several items per page. |
| `data[].target.content` | Answer body as HTML. Long answers may be cut, so use the excerpt for plain text. |
| `data[].target.excerpt / data[].target.excerpt_new` | Plain text excerpt of the answer, with paragraphs joined by spaces. |
| `data[].target.author.id / data[].target.author.headline` | Author ID and the profile headline the author set. The headline can be empty. |
| `data[].target.author.followers_count` | Number of followers of the answer author. |
| `data[].target.comment_count` | Number of comments on the answer. |
| `data[].target.created_time / data[].created_time / data[].updated_time` | Unix timestamps in seconds. `target.created_time` is for the answer, the other two are for the feed item. |
| `data[].brief` | JSON string that holds the content `type` (such as `answer`), the `source` and the numeric `id` of the answer. |
| `data[].offset` | Position of the item in the feed, starting at 1. |
| `paging.next / paging.is_end` | `next` is a ready-made URL for the next feed page. `is_end` shows whether the feed has ended. |

### Notes

- Send `{}` to get the first page. Raise `page_number` and `offset` to move forward.
- The `next` URL in `paging` contains a `session_token` value. Pass the same value as `session_token` to continue the same feed session.
- Read the answer ID from `data[].brief` and pass it to [Zhihu Answer Details](/apis/zhihu/web/answer-detail) for the full answer.
- For a ranked list of topics instead of a personal-style feed, use [Zhihu Hot List](/apis/zhihu/web/hot-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/hot-recommend.json`](../../../../catalog/models/zhihu/web/hot-recommend.json) · Store page: https://www.sandbase.ai/model/zhihu/web/hot-recommend
