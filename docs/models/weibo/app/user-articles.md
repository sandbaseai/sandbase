# Weibo User Articles API: pricing, parameters and code examples

`weibo/app/user-articles` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of articles released by a specified Weibo user. Supports pagination via a cursor parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-articles", "uid": "1725941200"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-articles', {'uid': '1725941200'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-articles", {
  "uid": "1725941200"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-articles", sandbase.Params{
	"uid": "1725941200",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `since_id` |  |  | Pagination cursor, don't pass for first request, use returned since_id for subsequent requests  |

## Details

Returns a list of feed items posted by a Weibo user, based on the user's `uid`. Each item carries post data such as like counts and image URLs, and the response includes a cursor for the next page.

### Use cases

- Pull the latest feed items from a Weibo account to review what it has published.
- Collect like counts for a user's posts to compare which ones got the most reaction.
- Page through a user's feed with the returned cursor to build an archive of their posts.
- Extract image URLs from a user's posts to gather the pictures they shared.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "1725941200"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `since_id` | string | No | Pagination cursor, don't pass for first request, use returned since_id for subsequent requests |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "__profile_card_server__": {
    "from": "SHANHAI-SERVER"
  },
  "config": "{}",
  "items": [
    {
      "category": "cell",
      "span": {
        "style": {
          "height": 10
        }
      },
      "type": "span"
    }
  ],
  "loadedInfo": "{}",
  "moreInfo": {
    "error": "网络加载失败，请稍后尝试",
    "loading": "正在加载更多",
    "moreType": "default",
    "pagingType": "cursor",
    "params": {
      "count": 20,
      "max_id": 0,
      "since_id": "5344278831435751_0_0"
    }
  },
  "navInfo": "{}",
  "pageData": "{}",
  "refreshInfo": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | List of entries on the page. Entries with `category` set to `feed` are posts. Entries with `category` set to `cell` and `type` set to `span` are spacing elements with no post data. |
| `items[].category / items[].type` | Kind of entry. Use `category` to tell post entries (`feed`) apart from layout entries (`cell`). |
| `items[].data.attitudes_count` | Number of likes on the post. |
| `items[].data.bmiddle_pic` | URL of the medium-size picture attached to the post, when the post has one. |
| `items[].data.ad_marked` | Boolean that shows whether the post is marked as an ad. |
| `items[].data.annotations[]` | List of small objects with extra post details, such as `client_mblogid`. The keys differ from one object to the next. |
| `items[].itemExt.anchorId / items[].itemExt.extraItemId` | Identifiers for the entry within the feed, for example `2319121725941200_-_ordinary`. |
| `moreInfo.params.since_id` | Cursor value for the next page, for example `5344278831435751_0_0`. |
| `moreInfo.params.count` | Page size that the cursor uses. The sample value is `20`. |
| `moreInfo.pagingType` | Paging method. The value `cursor` means you page with `since_id`. |

### Notes

- Leave out `since_id` on the first request. For the next page, pass the value from `moreInfo.params.since_id` as `since_id`.
- Some fields in the response, such as `config`, `loadedInfo`, `navInfo`, `pageData` and `refreshInfo`, are JSON strings that hold `{}` in the sample.
- Filter `items[]` on `category` equal to `feed` to skip the spacing entries.
- To read the full content of one post, call [Weibo Post Detail (App)](/apis/weibo/app/status-detail). To get the account's profile, call [Weibo User Profile Information](/apis/weibo/app/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-articles.json`](../../../../catalog/models/weibo/app/user-articles.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-articles
