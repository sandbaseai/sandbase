# WeChat MP Comment Replies API: pricing, parameters and code examples

`wechat-mp/v2/comment-replies` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns second-level replies under a specific WeChat MP article comment using the article url and comment identifiers. Supports pagination offset and raw output formats.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/comment-replies", "url": "http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/comment-replies', {'url': 'http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/comment-replies", {
  "url": "http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/comment-replies", sandbase.Params{
	"url": "http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=full raw reply objects; False=simplified replies.  |
| `url` | string | yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). E.g. `http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd`  |
| `offset` | integer |  | Optional, default 0 (>=0). Reply pagination offset; 0 for the first page, pass `next_offset` from the previous response when `has_more=true`. Ignored when `all_pages=true`. range 0– |
| `comment_id` |  |  | 文章的评论 id（可选，**性能捷径**）：不传时上游要先抓并解析整篇文章 HTML 才能拿到它，约占本接口耗时的一半；已有该值时传进来可显著加快。取自 /fetch_article_detail 或 /fetch_article_detail_h5 响应的 `$.data.content.comment_id`/Article comment id (optional, performance shortcut): when…  |
| `content_id` |  |  | Optional (numeric). `content_id` of the target first-level comment, from `$.data.comments[N].content_id` of the `fetch_article_comments` response; **defaults to the first comment that has replies when omitted**. E.g.…  |

## Details

Fetch second-level comment replies for a WeChat MP article by providing the article `url`. Specify `content_id` to target a specific comment thread.

### Use cases

- Retrieve nested reply threads under top-level article comments.
- Paginate through reader responses on popular WeChat MP posts.
- Speed up reply retrieval by supplying a pre-fetched comment_id.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "http://mp.weixin.qq.com/s?__biz=Mzk3NTA0MzM5NA==&mid=2247483745&idx=1&sn=3f34e768cf457a501038991ed30be1f4#rd"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…`). |
| `raw` | boolean | No | Optional, default True. |
| `offset` | integer | No | Optional, default 0 (>=0). |
| `comment_id` | string | No | 文章的评论 id（可选，性能捷径）：不传时上游要先抓并解析整篇文章 HTML 才能拿到它，约占本接口耗时的一半；已有该值时传进来可显著加快。取自 /fetch_article_detail 或 /fetch_article_detail_h5 响应的 `$.data.content.comment_id`/Artic… |
| `content_id` | string | No | Optional (numeric). |

### Notes

- Pass `comment_id` from article detail responses to avoid upstream HTML parsing and improve response latency.
- Target a specific comment thread by passing `content_id` obtained from comment listing endpoints; defaults to the first comment with replies when omitted.
- Page through replies by passing `next_offset` into `offset` when more results are available.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat MP Account Articles](/apis/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Account Profile](/apis/wechat-mp/v2/account-profile): Retrieves the profile details of an official WeChat account, including name, avatar, signature, and verification entity type using its official account ID.
- [WeChat MP Article Ads](/apis/wechat-mp/v2/article-ad): Returns embedded ad slot information for a specified WeChat MP article URL.

---
Machine-readable: [`catalog/models/wechat-mp/v2/comment-replies.json`](../../../../catalog/models/wechat-mp/v2/comment-replies.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/comment-replies
