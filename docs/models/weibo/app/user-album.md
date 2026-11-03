# Weibo User Album API: pricing, parameters and code examples

`weibo/app/user-album` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the photo and media album content of a specified Weibo user. Supports cursor-based pagination using the since_id parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-album", "uid": "7648703289"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-album', {'uid': '7648703289'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-album", {
  "uid": "7648703289"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-album", sandbase.Params{
	"uid": "7648703289",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-album` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `since_id` |  |  | Pagination cursor, don't pass for first request, use returned since_id for subsequent requests  |

## Details

Returns the photo album of a Weibo user as a list of layout cards. Each card holds image links in several sizes and the post data tied to each photo. It needs the user's numeric `uid`.

### Use cases

- Collect image URLs from a creator's Weibo album for an archive.
- List the album categories of a profile, such as selfies and avatars, with a cover image for each.
- Page through a user's older album photos with the `since_id` cursor.
- Match each album photo to its source post through the `mblog` object.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-album" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "7648703289"}'
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
      "since_id": "5012154263666753_4990205358511630|1034:4990204960768042_20240328_-1"
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
| `items[].items[].data.pics[].pic_title` | Name of an album category, for example `自拍` (selfies) or `头像` (avatars). It appears in the album index card. |
| `items[].items[].data.pics[].pic` | Cover image URL for that album category. |
| `items[].items[].data.pics[].scheme` | App deep link that opens the album category. Its `containerid` value names the album. |
| `items[].items[].data.pics[].pic_id` | ID of one photo. It is also the file name in the image URLs. |
| `items[].items[].data.pics[].pic_big / pic_middle / pic_mw2000` | Image URLs of the same photo in different sizes. `pic_big` is the original-size link. |
| `items[].items[].data.pics[].mblog.attitudes_count` | Like count of the post the photo belongs to. |
| `items[].items[].data.pics[].mblog.bmiddle_pic` | Medium-size image URL of the post's picture. |
| `items[].items[].data.pics[].object_id` | Object ID of the photo, in the form `1042018:<hash>`. |
| `moreInfo.params.since_id` | Cursor for the next page. Send it back as `since_id`. |
| `moreInfo.params.count` | Page size reported for the next request, `20` in this response. |

### Notes

- Leave out `since_id` on the first call. For later pages, pass the value from `moreInfo.params.since_id`.
- `moreInfo.pagingType` is `cursor`, so pages follow the cursor and not a page number.
- The first page starts with album category cards. Photo cards follow in groups with `card_type` `47`.
- Several fields, such as `config` and `loadedInfo`, come back as JSON strings and are empty (`{}`) in this response.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-album.json`](../../../../catalog/models/weibo/app/user-album.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-album
