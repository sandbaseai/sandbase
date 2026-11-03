# China Social Media Search API: pricing, parameters and code examples

`cn-social/search` · data API · China Social Media · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search recent posts and articles across Chinese news sites, Weibo, WeChat, Zhihu, Douyin, Xiaohongshu, Bilibili and Kuaishou by keyword, with source and time-range filters. Results come from a cached index, so rare keywords can return few items.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "cn-social/search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('cn-social/search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("cn-social/search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "cn-social/search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/cn-social/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end` | string |  | End time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request.  |
| `start` | string |  | Start time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request.  |
| `source` | string |  | Target social media platform for search filtering. one of: `ALL`, `NEWS`, `WEIBO`, `WEIXIN`, `ZHIHU`, `DOUYIN`, `XIAOHONGSHU`, `BILIBILI`, `KUAISHOU`; default `"ALL"` |
| `keyword` | string |  | Search query string. Supports these five syntax forms: - AND (&&): A && B matches content containing both A and B. - OR (\|\|): A \|\| B matches content containing A or B. - Exclusion (-): -A matches content that does not…  |
| `nextCursor` | string |  | Pagination cursor provided by the 'nextCursor' field in the previous response.  |

## Details

Returns a list of recent posts and articles that match a keyword across Chinese news sites and social platforms such as Weibo, WeChat, Zhihu, Douyin, Xiaohongshu, Bilibili and Kuaishou. It needs a `keyword` and a time range set by `start` and `end`. You can limit results to one platform with `source`.

### Use cases

- Track how often a topic such as 人工智能 appears in Chinese news and social posts over a two-week window.
- Collect WeChat official account articles that mention a brand or product name.
- Build a news feed for one keyword by combining `title`, `url` and `sourceName`.
- Exclude noisy terms with the `-` syntax to monitor a narrow topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/cn-social/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能", "source": "ALL", "start": "2026-10-19 00:00:00", "end": "2026-11-02 00:00:00"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end` | string | No | End time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request. |
| `keyword` | string | No | Search query string. Supports these five syntax forms: - AND (&&): A && B matches content containing both A and B. - OR (//): A // B matches content containing A or B. - Exclusion (-): -A matches content that does not co |
| `nextCursor` | string | No | Pagination cursor provided by the 'nextCursor' field in the previous response. |
| `source` | string | No | Target social media platform for search filtering. |
| `start` | string | No | Start time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "list": [
    {
      "author": {
        "avatar": "http://wx.qlogo.cn/mmhead/0nn3FBrD9a32s1WibMMeS0gAAyXicFNonzp9kicxpmfqYF5q7ODcrp…",
        "id": "gh_e3feebbd6659",
        "nickname": "阳城文学编辑部",
        "username": "gh_e3feebbd6659"
      },
      "content": "<img src=\"https://mmbiz.qpic.cn/mmbiz_png/QrAzOGRiaZD7AT8ubbRkChwq3s0LhQGZaRRNib…",
      "createTime": 1792339200001,
      "image": [
        "https://mmbiz.qpic.cn/mmbiz_png/QrAzOGRiaZD7AT8ubbRkChwq3s0LhQGZaRRNibPFf5BoZe11…"
      ],
      "sourceName": "微信公众号",
      "title": "张红胜/“中国好人”郝三铁",
      "url": "https://mp.weixin.qq.com/s?__biz=MzU4NDkzMTc0Mg==&amp;mid=2247515237&amp;idx=1&a…",
      "video": []
    }
  ],
  "nextCursor": "AgsnJl5KTvicfhdQZ00Z7nCYyNiKXocL",
  "totalNumber": 447606
}
```

### Response fields

| Field | Meaning |
|---|---|
| `list[]` | One matching post or article. Each item has the author, content, media and link. |
| `list[].title` | Title of the article or post. |
| `list[].url` | Link to the original page. In the WeChat items the link contains `&amp;` in place of `&`. |
| `list[].sourceName` | Name of the site or platform the item came from, for example `微信公众号` or `壹点`. |
| `list[].createTime` | Creation time as a number. The values look like Unix time in milliseconds. |
| `list[].content` | Body of the item as an HTML string. It can include `<p>` and `<img>` tags, and long bodies may be cut. |
| `list[].image[] / list[].video[]` | Lists of image and video URLs attached to the item. An item without media can return an empty list, or a list holding one empty string. |
| `list[].author.nickname / list[].author.username` | Display name and account name of the author. Both are empty strings for some news items. |
| `list[].author.id / list[].author.avatar` | Author account ID and avatar image URL. Both can be empty strings. |
| `nextCursor` | Cursor string for the next page of results. |
| `totalNumber` | Total number of items that match the query. |

### Notes

- To get the next page, send the `nextCursor` value from the response as the `nextCursor` parameter, with the same `keyword`, `source`, `start` and `end`.
- Write `start` and `end` as `yyyy-MM-dd HH:mm:ss`. They are required on the first request.
- `source` accepts `ALL`, `NEWS`, `WEIBO`, `WEIXIN`, `ZHIHU`, `DOUYIN`, `XIAOHONGSHU`, `BILIBILI` and `KUAISHOU`. The default is `ALL`.
- `keyword` supports `&&` for AND, `||` for OR, `-` for exclusion, parentheses for grouping, and English double quotes for an exact match.

### Pricing

$0.028571 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/cn-social/search.json`](../../../catalog/models/cn-social/search.json) · Store page: https://www.sandbase.ai/model/cn-social/search
