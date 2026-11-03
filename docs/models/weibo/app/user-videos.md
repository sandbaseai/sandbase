# Weibo User Videos API: pricing, parameters and code examples

`weibo/app/user-videos` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the video feed for a specified Weibo user in a waterfall layout. Accepts a user identifier and an optional cursor for paginated results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-videos", "uid": "8431518763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-videos', {'uid': '8431518763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-videos", {
  "uid": "8431518763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-videos", sandbase.Params{
	"uid": "8431518763",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `since_id` |  |  | Pagination cursor, don't pass for first request, use returned since_id for subsequent requests  |

## Details

Returns the video feed for a Weibo user as a list of layout items, using the user's `uid`. The response is a waterfall-style list of cells and cards, and you can pass `since_id` to get the next page.

### Use cases

- Check whether a Weibo account has published any videos.
- Page through a creator's video feed once the account has video cards.
- Find the link to an account's liked-video stream from the `scheme` value in the first card.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
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
  "navInfo": "{}",
  "pageData": "{}",
  "refreshInfo": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[]` | List of layout items. Each item is a cell (spacing) or a card (content). |
| `items[].category` | Item kind, such as `cell` or `card`. |
| `items[].type` | Subtype of a cell item. The sample shows `span`, a spacer. |
| `items[].data.card_type` | Numeric card type. The sample shows `156` for the tab card and `58` for the empty-state card. |
| `items[].data.name` | Text shown on a card. In the sample it reads "该博主还未发布任何视频" (this blogger has not posted any videos), so the account has no videos. |
| `items[].data.commend_info[].text / items[].data.commend_info[].scheme` | Label and app link for a profile action. The sample shows the label `赞` (like) and a `sinaweibo://svideo_like_stream` link for the user's liked videos. |
| `items[].data.commend_info[].icon` | Image URL for the action icon. |
| `items[].itemExt.anchorId` | Anchor ID attached to a card item. |

### Notes

- Send `uid` only on the first request. For later pages, pass the returned `since_id` cursor.
- The sample response has no video cards. The account returned a `card_type` `58` card saying it has not posted any videos, and no `since_id` appeared.
- Several top-level fields, such as `config`, `loadedInfo`, `navInfo`, `pageData` and `refreshInfo`, come back as the string `"{}"` in this response.
- To get account details for a `uid`, call [Weibo User Profile Information](/apis/weibo/app/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-videos.json`](../../../../catalog/models/weibo/app/user-videos.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-videos
