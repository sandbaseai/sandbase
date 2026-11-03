# WeChat MP Article Details API: pricing, parameters and code examples

`wechat-mp/article-detail` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get a WeChat Official Account article by URL with selectable plain-text or rich-text content mode. Use it to collect a known article in the preferred representation for reading, extraction, or storage.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/article-detail", "articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/article-detail', {'articleUrl': 'http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/article-detail", {
  "articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/article-detail", sandbase.Params{
	"articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/article-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mode` | string |  | Article body format. TEXT returns plain text, and RICH_TEXT returns rich text when supported. one of: `TEXT`, `RICH_TEXT`; default `"TEXT"` |
| `articleUrl` | string | yes | WeChat Official Account article URL used to fetch article detail content and metadata.  |

## Details

Returns the content and metadata of one WeChat Official Account article. It needs the article URL as `articleUrl`, and an optional `mode` of `TEXT` or `RICH_TEXT` to choose the body format.

### Use cases

- Archive the full body and images of a known article for storage or offline reading.
- Extract article text for translation, summarization, or keyword analysis.
- Identify the publishing account of an article from its `nick_name`, `alias` and `biz` values.
- Collect the image URLs of an article to download its pictures.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/article-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"articleUrl": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `articleUrl` | string | Yes | WeChat Official Account article URL used to fetch article detail content and metadata. |
| `mode` | string | No | Article body format. TEXT returns plain text, and RICH_TEXT returns rich text when supported. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "alias": "people_rmw",
  "app_id": "wx020d85a0aef80286",
  "appmsg_link": "",
  "author": "人民网",
  "biz": "MjM5NzI3NDg4MA==",
  "cdn_url": "https://mmbiz.qpic.cn/sz_mmbiz_jpg/XvpojIRrhdsyicO44PY4KBDO38CdYO8ibR6G1vDpBibT3…",
  "cdn_url_16_9": "",
  "cdn_url_1_1": "https://mmbiz.qpic.cn/mmbiz_jpg/XvpojIRrhdtYoKJAt9gpOfEewclvkplGicoF0BKYP99k961i…",
  "cdn_url_235_1": "https://mmbiz.qpic.cn/sz_mmbiz_jpg/XvpojIRrhdsyicO44PY4KBDO38CdYO8ibR6G1vDpBibT3…",
  "claim_source_info": {
    "aigc_type": "",
    "aigc_wording": "",
    "claim_source": "1",
    "claim_source_type": "",
    "media_source_type_info": {
      "biz_headimgurl": "",
      "biz_link_url": "",
      "biz_nickname": "",
      "media_source_from": "",
      "news_position_info": {
        "city": "",
        "country": "",
        "province": ""
      },
      "news_time": "",
      "other_from_account": ""
    }
  },
  "collect_count": -1,
  "comment_count": -1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `content` | Article body. In the sample response it holds HTML-style markup with `<p>` and `<img>` tags. |
| `content_multi_text` | Another form of the article body, with inline styles and links in HTML-style markup. |
| `author` | Author name shown on the article. |
| `nick_name / alias / biz / app_id` | Identifiers of the Official Account that published the article: display name, account alias, `biz` ID and app ID. |
| `create_time / create_time_str / pubtime` | Publish time of the article. `create_time` and `pubtime` use the format `YYYY-MM-DD HH:MM:SS`. `create_time_str` stops at minutes. |
| `mid / idx / hashid` | Article identifiers. `mid` is the message ID, `idx` is the article position in that message, and `hashid` matches the `sn` value in the URL. |
| `picture_page_info_list[].cdn_url` | Image URL for each picture found in the article. |
| `picture_page_info_list[].width / picture_page_info_list[].height` | Dimensions of each picture. |
| `cdn_url / cdn_url_1_1 / cdn_url_235_1` | Cover image URLs in different aspect ratios. Some ratios can be empty strings. |
| `ip_wording / provinceName / countryName` | Location text shown for the article, such as province and country. |
| `read / comment_count / share_count / collect_count / looking` | Engagement counters. The sample returns `-1` for all of them, so use the metrics API for these numbers. |

### Notes

- Copy `articleUrl` from a WeChat article link. The sample URL contains the `__biz`, `mid`, `idx` and `sn` parameters, which match `biz`, `mid`, `idx` and `hashid` in the response.
- Set `mode` to `RICH_TEXT` to ask for rich text. The default is `TEXT`.
- For view and like counts, call [WeChat MP Article Metrics](/apis/wechat-mp/article-metrics). For reader comments, call [WeChat MP Article Comments](/apis/wechat-mp/article-comment).
- A newer version of this endpoint is available as [WeChat MP Article Detail (H5, Recommended)](/apis/wechat-mp/v2/article-detail-h5).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/article-detail.json`](../../../catalog/models/wechat-mp/article-detail.json) · Store page: https://www.sandbase.ai/model/wechat-mp/article-detail
