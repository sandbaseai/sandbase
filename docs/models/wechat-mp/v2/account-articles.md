# WeChat MP Account Articles API: pricing, parameters and code examples

`wechat-mp/v2/account-articles` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audio tabs.

## Pricing

- **$0.01 per call** (USD)
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

This API returns one page of published posts from a WeChat official account. It needs the account's `gh_` username and returns each post's title, link, cover images and timestamps. You can switch between the articles, videos, audios and image-text tabs.

### Use cases

- Check an official account every day for new posts and alert your team when one appears.
- Back-fill a full archive of an account's posts page by page for search or analysis.
- Collect article `url` values and send them to an article detail API to fetch full text.
- Pull cover images in several aspect ratios to build a media preview board.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/account-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "gh_363b924965e9", "raw": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Official account `gh_username` (`gh_…`). E.g. `gh_363b924965e9` |
| `item_show_type` | string | No | Optional content tab (matches the "Articles / Videos / Audios" tabs on the account homepage). Empty / `0`=articles (default), `5`=videos, `7`=audios, `8`=image-text posts. Omitting it = articles, behavior unchanged. |
| `offset` | string | No | Optional pagination cursor (base64), **leave empty for the first page**; for the next page pass `next_offset` from the previous response. E.g. `CAMQChiS5KfRBiAKOJLkp9EGQABIAVgAYABwAQ==` |
| `page_size` | integer | No | Optional, default 20, range **10-20**. Articles per page. |
| `raw` | boolean | No | Optional, default True. True=raw; False=simplified parsing. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "articles": [
    {
      "app_msg_id": 2667043262,
      "cover": "https://mmbiz.qpic.cn/sz_mmbiz_jpg/QaRWjMxooXuuJvoef2xYDJDM1gT68bahKtzZW8icwkhMD…",
      "covers": {
        "16_9": "https://mmbiz.qpic.cn/sz_mmbiz_jpg/QaRWjMxooXuuJvoef2xYDJDM1gT68bahKtzZW8icwkhMD…",
        "1_1": "https://mmbiz.qpic.cn/sz_mmbiz_jpg/QaRWjMxooXuPF9A7Lbmgk30txKLibicJhkKnnWHNPUYp6…",
        "235_1": "https://mmbiz.qpic.cn/sz_mmbiz_jpg/QaRWjMxooXuuJvoef2xYDJDM1gT68bahKtzZW8icwkhMD…",
        "3_4": "https://mmbiz.qpic.cn/sz_mmbiz_jpg/QaRWjMxooXuuJvoef2xYDJDM1gT68bahKtzZW8icwkhMD…"
      },
      "create_time": 1793687341,
      "digest": "",
      "idx": 1,
      "is_paid": 0,
      "is_pay_subscribe": 0,
      "item_show_type": 0,
      "msg_type": 9,
      "pic_count": 0,
      "source_url": "https://www.peopleapp.com/"
    }
  ],
  "biz_username": "gh_363b924965e9",
  "count": 10,
  "debug_id": "3abf1131",
  "debug_info": "gAAAAABq6ZEyXemFYbNluN88EMaiChiAu1gBtoObz7ewpDqb_YwtslUuVI9cFGFJ77gF3uk2Fs5o8NUT…",
  "is_end": 0,
  "next_offset": "WABgAGiBpOW+74vB9Go=",
  "pages": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `articles[].title` | Title of the post. |
| `articles[].url` | Link to the post on mp.weixin.qq.com. Use it to open the post or pass it to an article API. |
| `articles[].app_msg_id` | Numeric ID of the post. It also appears as `mid` in the post `url`. |
| `articles[].create_time / update_time` | Unix timestamps in seconds for when the post was created and last updated. |
| `articles[].cover` | URL of the main cover image. |
| `articles[].covers` | Object with cover image URLs cropped to different aspect ratios. Each key is named after its ratio. |
| `articles[].idx` | Position of the post within its publish batch. A value of `1` is the first post in that batch. |
| `articles[].is_paid / is_pay_subscribe` | Flags for paid content. In this response both are `0`. |
| `articles[].source_url` | The external link attached to the post, when there is one. |
| `count / is_end / next_offset` | `count` is the number of posts on this page. `is_end` shows whether this is the last page. `next_offset` is the cursor for the next page. |

### Notes

- Leave `offset` empty for the first page. For the next page, pass the `next_offset` value from the previous response as `offset`.
- Stop paging when `is_end` is truthy. In this response `is_end` is `0`, so more pages exist.
- `page_size` accepts 10 to 20. `item_show_type` picks the tab: empty or `0` for articles, `5` for videos, `7` for audios, `8` for image-text posts.
- To read the full text of a post, send its `url` to [WeChat MP Article Detail](/apis/wechat-mp/v2/article-detail). To look up the account itself, use [WeChat MP Account Profile](/apis/wechat-mp/v2/account-profile).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat MP Article Detail](/apis/wechat-mp/v2/article-detail): Get a WeChat official account (MP) article from its URL: title, author, account, publish time, cover, full text and HTML content, and album info.
- [Get WeChat MP Account Profile](/apis/wechat-mp/v2/account-profile): Pass a `gh_username` to get the official account profile: name / avatar / description / verification entity type, etc..
- [Get WeChat MP Article Ads](/apis/wechat-mp/v2/article-ad): Pass an article URL to get the embedded ad slot info of the article..

---
Machine-readable: [`catalog/models/wechat-mp/v2/account-articles.json`](../../../../catalog/models/wechat-mp/v2/account-articles.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/account-articles
