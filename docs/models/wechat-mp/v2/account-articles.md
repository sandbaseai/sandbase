# WeChat MP Account Articles

`wechat-mp/v2/account-articles` · api · WeChat MP

Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audio tabs.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/account-articles", "raw": false, "username": "gh_363b924965e9"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/account-articles', {'raw': False, 'username': 'gh_363b924965e9'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/account-articles", {
  "raw": false,
  "username": "gh_363b924965e9"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/account-articles", sandbase.Params{
	"raw": false,
	"username": "gh_363b924965e9",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/account-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw; False=simplified parsing.  |
| `offset` |  |  | Optional pagination cursor (base64), **leave empty for the first page**; for the next page pass `next_offset` from the previous response. E.g. `CAMQChiS5KfRBiAKOJLkp9EGQABIAVgAYABwAQ==`  |
| `username` | string | yes | Official account `gh_username` (`gh_…`). E.g. `gh_363b924965e9`  |
| `page_size` | integer |  | Optional, default 20, range **10-20**. Articles per page. range 10–20 |
| `item_show_type` |  |  | Optional content tab (matches the "Articles / Videos / Audios" tabs on the account homepage). Empty / `0`=articles (default), `5`=videos, `7`=audios, `8`=image-text posts. Omitting it = articles, behavior unchanged.  |

## Details

Pass an official account `gh_…` username and get a page of its historical posts with title, URL, cover and publish time. Paginate with `next_offset`.

### Use cases

- Monitor new articles from competitor or media accounts.
- Back-fill an account's archive for analysis or search.
- Feed article URLs into the Article Detail API for full text.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/account-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "gh_363b924965e9", "raw": false}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Official account `gh_username` (`gh_…`). |
| `raw` | boolean | No | Optional, default True. |
| `offset` | string | No | Optional pagination cursor (base64), leave empty for the first page; for the next page pass `next_offset` from the prev… |
| `page_size` | integer | No | Optional, default 20, range 10-20. |
| `item_show_type` | string | No | Optional content tab (matches the "Articles / Videos / Audios" tabs on the account homepage). |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "count": 10,
  "is_end": 0,
  "next_offset": "<next_offset>",
  "articles": [
    {
      "app_msg_id": 2667038019,
      "title": "谁家的龙，一直坐着啊？",
      "create_time": 1791276963,
      "item_show_type": 0,
      "is_paid": 0,
      "url": "http://mp.weixin.qq.com/s?__biz=MjM5MjAxNDM4MA==&mid=266703…",
      "cover": "https://mmbiz.qpic.cn/mmbiz_jpg/QaRWjMxooXtjiaLui…"
    }
  ]
}
```

### Notes

- `is_end` truthy means the last page.
- `item_show_type`: empty or 0 = articles, 5 = videos, 7 = audio.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat MP Article Detail](/model/wechat-mp/v2/article-detail): Get a WeChat official account (MP) article from its URL: title, author, account, publish time, cover, full text and HTML content, and album info.
- [Get WeChat MP Account Profile](/model/wechat-mp/v2/account-profile): Pass a `gh_username` to get the official account profile: name / avatar / description / verification entity type, etc..
- [Get WeChat MP Article Ads](/model/wechat-mp/v2/article-ad): Pass an article URL to get the embedded ad slot info of the article..

---
Machine-readable: [`catalog/models/wechat-mp/v2/account-articles.json`](../../../../catalog/models/wechat-mp/v2/account-articles.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/account-articles
