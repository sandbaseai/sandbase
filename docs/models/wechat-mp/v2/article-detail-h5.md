# WeChat MP Article Detail (H5, Recommended) API: pricing, parameters and code examples

`wechat-mp/v2/article-detail-h5` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get WeChat MP Article Detail (H5, Recommended) on WeChat MP. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/article-detail-h5", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/article-detail-h5', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/article-detail-h5", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/article-detail-h5", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/article-detail-h5` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | True=raw response; False=simplified parsed structure default `true` |
| `url` | string | yes | /mp.weixin.qq.com/s/WeChat MP article URL (https://mp.weixin.qq.com/s/… or long URL with __biz)  |

## Details

Returns the details of one WeChat MP (official account) article as JSON. It includes the article's author, account info, engagement counts and album links. You pass the article URL in `url`.

### Use cases

- Track read, like, share and collect counts for a single article.
- Identify which account published an article by reading its nickname, alias and `bizuin`.
- Walk through an article series by following the previous and next article links in the album info.
- Save the cover image URL and author name of an article for a content archive.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/article-detail-h5" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw", "raw": true}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | /mp.weixin.qq.com/s/WeChat MP article URL (https://mp.weixin.qq.com/s/… or long URL with __biz) |
| `raw` | boolean | No | True=raw response; False=simplified parsed structure |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "bizUin": 3236757533,
  "content": {
    "_content_type": "article",
    "_fields_from": "cgiDataNew",
    "_via": "h5",
    "ad_mark_status": 0,
    "advertisement_info": [],
    "ai_chat_info": {
      "ai_chat_status": 0,
      "room_info": ""
    },
    "ai_chat_status": 0,
    "aigc_pictures": [],
    "ainfos": [],
    "album_id": "1865468163396517889",
    "album_id_str": "1865468163396517889",
    "album_needpay": 0
  },
  "debug_id": "8cb4e28d",
  "debug_info": "gAAAAABq6ZE4GYK6HwtXMOKwwlRiVoQL60YmFG5wMevNjy3ouQJJNK66HmnybPYQL0IgnvQj9f_hI2Ie…",
  "itemIdx": 1,
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `content.appmsg_bar_data.read_num` | Number of reads for the article. |
| `content.appmsg_bar_data.like_count / content.appmsg_bar_data.old_like_count` | Two like counters. `like_count` is the newer like type and `old_like_count` is the older one. Compare both with `appmsg_like_type` before you use either. |
| `content.appmsg_bar_data.share_count / content.appmsg_bar_data.collect_count / content.appmsg_bar_data.comment_count` | Number of shares, collects and comments on the article. |
| `content.author` | Author name shown on the article. |
| `content.biz_card.list[].nickname / content.biz_card.list[].alias` | Display name and account ID of the publishing account. |
| `content.biz_card.list[].orignal_num` | Number of original articles listed for the account on its card. |
| `content.bizuin` | Encoded account ID (the `__biz` value) of the publishing account. |
| `content.cdn_url` | URL of the article cover image. |
| `content.appmsgalbuminfo.title` | Title of the album (article series) this article belongs to. |
| `content.appmsgalbuminfo.pre_article_title / content.appmsgalbuminfo.pre_article_link` | Title and link of the previous article in the album. |
| `content.appmsgalbuminfo.next_article_title / content.appmsgalbuminfo.next_article_link` | Title and link of the next article in the album. |

### Notes

- Pass a short link (`https://mp.weixin.qq.com/s/…`) or a long link that contains `__biz` in `url`.
- Set `raw` to `true` (the default) for the full response shown here. Set it to `false` for a simplified parsed structure.
- Links in the album info contain `&amp;` in place of `&`. Replace it before you open the link.
- For comments on the article, call [WeChat MP Article Comments](/apis/wechat-mp/v2/article-comments). For account details, call [WeChat MP Account Profile](/apis/wechat-mp/v2/account-profile).

### Pricing

$0.01 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/v2/article-detail-h5.json`](../../../../catalog/models/wechat-mp/v2/article-detail-h5.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/article-detail-h5
