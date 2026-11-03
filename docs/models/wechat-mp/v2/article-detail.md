# WeChat MP Article Detail API: pricing, parameters and code examples

`wechat-mp/v2/article-detail` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get a WeChat official account (MP) article from its URL: title, author, account, publish time, cover, full text and HTML content, and album info.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/article-detail", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/article-detail', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/article-detail", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/article-detail", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/article-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw response; False=simplified projection.  |
| `url` | string | yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…` or long URL with `__biz`). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw`  |

## Details

Fetch a WeChat Official Account article from its `mp.weixin.qq.com` link: title, author, account, publish time, cover, the article body and album navigation.

### Use cases

- Archive or index Official Account articles for search and monitoring.
- Feed article text to an LLM for summaries or classification.
- Follow an account's album by walking the previous and next article links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/article-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL (`https://mp.weixin.qq.com/s/…` or long URL with `__biz`). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw` |
| `raw` | boolean | No | Optional, default True. True=raw response; False=simplified projection. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "bizUin": 3236757533,
  "content": {
    "ad_mark_status": 0,
    "advertisement_info": [],
    "ai_chat_info": {
      "ai_chat_status": 0,
      "room_info": ""
    },
    "aigc_pictures": [],
    "ainfos": [],
    "alias": "QbitAI",
    "anchor_tree": [],
    "app_id": "wx2f0fbcc28597dbce",
    "appmsg_ext_get": {
      "func_flag": 0
    },
    "appmsg_fe_filter": "contenteditable",
    "appmsg_like_type": 2,
    "appmsg_listen_id": "150401723788215308"
  },
  "debug_id": "76bcf329",
  "debug_info": "gAAAAABq6TvHOF0gUZr0UtGRNNjD4W-NNP-IT4lPPio5Dwex8GR_nFBUjeaR1hbn-qVXS0Vv-38ZkNLU…",
  "itemIdx": 1,
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `content.title / content.author / content.nick_name` | Article title, author and account name. |
| `content.content / content_noencode` | Article body HTML. |
| `content.create_time` | Publish time. |
| `content.appmsgalbuminfo` | Album (series) info with `pre_article_link` and `next_article_link`. |
| `bizUin` | Numeric ID of the Official Account. |

### Notes

- Set `raw: true` to get the unprocessed page payload.
- Read counts and likes are not included; use [WeChat MP Article Stats (H5)](/apis/wechat-mp/v2/article-stats-h5) for those.
- Deleted or blocked articles fail and are not charged.

### Pricing

$0.01 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat MP Account Articles](/apis/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [Get WeChat MP Account Profile](/apis/wechat-mp/v2/account-profile): Pass a `gh_username` to get the official account profile: name / avatar / description / verification entity type, etc..
- [Get WeChat MP Article Ads](/apis/wechat-mp/v2/article-ad): Pass an article URL to get the embedded ad slot info of the article..

---
Machine-readable: [`catalog/models/wechat-mp/v2/article-detail.json`](../../../../catalog/models/wechat-mp/v2/article-detail.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/article-detail
