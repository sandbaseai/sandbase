# Douyin Video Search Suggestions API: pricing, parameters and code examples

`douyin/index/item-sug` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns search suggestions and related video items based on a keyword query. Includes video titles, URLs, like counts, and author nicknames.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-sug", "query": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-sug', {'query': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-sug", {
  "query": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-sug", sandbase.Params{
	"query": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/index/item-sug` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword  |

## Details

Returns a list of Douyin videos that match a search keyword. Each item has the video title, URL, like count, author nickname, category and thumbnail. It needs one input, the `query` keyword.

### Use cases

- Find popular Douyin videos that mention a topic such as `人工智能`.
- Collect video URLs and `itemId` values to feed into other Douyin video lookups.
- Compare which content categories a keyword appears in, using `category_name`.
- Rank videos for a keyword by `likes` to spot the most engaging posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-sug" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "data": [
    {
      "avatarUrl": "https://p6-byteindex-sign.byteimg.com/aweme-avatar/tos-cn-avt-0015_c71d4aad59827…",
      "category_name": "美食",
      "index": "173099",
      "itemId": "7703073570793225579",
      "likes": "5052",
      "nickname": "康喜搞笑社",
      "thumbnail": "https://p6-byteindex-sign.byteimg.com/tos-cn-p-0015c000-ce/oMgVNnCfoAzND7BfgIWwz…",
      "title": "“人工智能打饭机”#万万想不到 #当代大学生精神状态 #哈哈哈哈哈哈我要笑死了 #人类迷惑行为 #剪映 视频中是可使用食材 可能引人不适谨慎观看 视频效果无不良…",
      "url": "https://www.douyin.com/video/7703073570793225579"
    }
  ],
  "itemSugResult": [
    {
      "avatarUrl": "https://p6-byteindex-sign.byteimg.com/aweme-avatar/tos-cn-avt-0015_c71d4aad59827…",
      "category_name": "美食",
      "index": "173099",
      "itemId": "7703073570793225579",
      "likes": "5052",
      "nickname": "康喜搞笑社",
      "thumbnail": "https://p6-byteindex-sign.byteimg.com/tos-cn-p-0015c000-ce/oMgVNnCfoAzND7BfgIWwz…",
      "title": "“人工智能打饭机”#万万想不到 #当代大学生精神状态 #哈哈哈哈哈哈我要笑死了 #人类迷惑行为 #剪映 视频中是可使用食材 可能引人不适谨慎观看 视频效果无不良…",
      "url": "https://www.douyin.com/video/7703073570793225579"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | List of matching video items for the keyword. Each entry holds the fields below. |
| `data[].title` | Video caption text, including hashtags. |
| `data[].url` | Link to the video page on Douyin. |
| `data[].itemId` | ID of the video. It is also the last part of `url`. |
| `data[].likes` | Like count for the video, returned as a string. |
| `data[].nickname` | Display name of the video author. |
| `data[].category_name` | Content category of the video, for example `美食` or `教育校园`. |
| `data[].index` | Numeric index value for the video, returned as a string. |
| `data[].avatarUrl / data[].thumbnail` | Signed image URLs for the author avatar and the video cover. |
| `itemSugResult[]` | Same list of video items as `data[]`, with the same fields. |

### Notes

- Pass the search keyword in `query`. The request has no pagination parameter.
- `data` and `itemSugResult` hold the same items in this response, so read either one.
- `likes` and `index` arrive as strings. Convert them to numbers before sorting.
- To search videos with more filters, try [Douyin Index Video Search](/apis/douyin/index/item-query).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-sug.json`](../../../../catalog/models/douyin/index/item-sug.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-sug
