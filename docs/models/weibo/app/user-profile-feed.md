# Weibo App User Profile Feed API: pricing, parameters and code examples

`weibo/app/user-profile-feed` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves the profile feed cards for a specified user on Weibo. Query by target user identifier with support for cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-profile-feed", "uid": "8431518763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-profile-feed', {'uid': '8431518763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-profile-feed", {
  "uid": "8431518763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-profile-feed", sandbase.Params{
	"uid": "8431518763",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-profile-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `since_id` |  |  | Pagination cursor, don't pass for first request, use returned since_id for subsequent requests  |

## Details

Returns the profile feed cards for a Weibo user as a list of card objects. It needs the target user ID in `uid` and accepts an optional `since_id` cursor for the next page.

### Use cases

- Check whether a Weibo account has any feed cards before you call a timeline API.
- Page through an account's profile feed by passing the returned `since_id` back in the next request.
- Read card layout and styling values to see how the Weibo app renders a profile feed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-profile-feed" \
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
      "category": "card",
      "data": {
        "button_background_color": "#FFFFFF",
        "button_dark_background_color": "#242424",
        "button_scheme": "",
        "button_selected_background_color": "#F7F7F7",
        "button_selected_dark_background_color": "#1E1E1E",
        "button_selected_dark_text_color": "#EA8011",
        "button_selected_text_color": "#FF8200",
        "card_type": 58
      },
      "itemExt": null,
      "style": {
        "margin": [
          0
        ],
        "padding": [
          0
        ]
      }
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
| `items[]` | List of feed cards for the profile. Each entry holds one card. |
| `items[].category` | Type of the entry. The sample value is `card`. |
| `items[].data.card_type` | Numeric card type. The sample value is `58`. |
| `items[].data.button_background_color / items[].data.button_selected_background_color` | Hex background colors for a button in the card, in its normal and selected states. |
| `items[].data.button_selected_text_color` | Hex text color for the selected button state. |
| `items[].data.button_dark_background_color / items[].data.button_selected_dark_background_color` | Hex background colors for the same button in dark mode. |
| `items[].style.margin / items[].style.padding` | Lists of spacing numbers the app uses to lay out the card. |
| `items[].itemExt` | Extra item data. It is `null` in the sample response. |
| `config / loadedInfo / navInfo / pageData / refreshInfo` | Strings that hold JSON. All of them are `"{}"` in the sample response. |

### Notes

- Get the `uid` from a user lookup, for example [Weibo User Profile Information](/apis/weibo/app/user-info).
- Leave `since_id` out on the first request. For later pages, pass the `since_id` value that the previous response returned.
- For the posts themselves, call [Weibo User Timeline](/apis/weibo/app/user-timeline).
- The sample response holds a single card with no post data, so check `items[].data` for the card contents.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-profile-feed.json`](../../../../catalog/models/weibo/app/user-profile-feed.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-profile-feed
