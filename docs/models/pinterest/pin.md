# Pinterest Pin Details API: pricing, parameters and code examples

`pinterest/pin` · data API · Pinterest · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.018 per call · **Modes:** sync

Returns detailed information for a single Pinterest pin using its page URL. Supports an optional setting to return a trimmed response payload.

## Pricing

- **$0.018 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pinterest/pin", "url": "https://www.pinterest.com/pin/99360735500167749/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pinterest/pin', {'url': 'https://www.pinterest.com/pin/99360735500167749/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pinterest/pin", {
  "url": "https://www.pinterest.com/pin/99360735500167749/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pinterest/pin", sandbase.Params{
	"url": "https://www.pinterest.com/pin/99360735500167749/",
})
```

Same call via the path form: `POST /v1/api/pinterest/pin` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The Pinterest pin URL to fetch details for.  |
| `trim` | boolean |  | Set to true for a trimmed down version of the response.  |

## Details

Returns details for one Pinterest pin, including its title, description, creation date, source attribution, the board it sits on and save and comment counts. It needs the pin page URL in `url`. Set `trim` to `true` to get a smaller response.

### Use cases

- Pull the title, description and source link of a saved pin to build a content catalog.
- Track the save and comment counts of a pin over repeated calls.
- Find which board and which user attribution a pin belongs to.
- Read the source domain and original author of an image to check where it came from.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pinterest/pin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.pinterest.com/pin/99360735500167749/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The Pinterest pin URL to fetch details for. |
| `trim` | boolean | No | Set to true for a trimmed down version of the response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "__typename": "Pin",
  "adData": null,
  "adMatchReason": 0,
  "adTargetingAttribution": null,
  "adTargetingAttributionReasons": null,
  "advertiserId": null,
  "affiliateDisclosure": null,
  "affiliateLink": null,
  "aggregatedPinData": {
    "aggregatedStats": {
      "saves": 101674
    },
    "commentCount": 30,
    "didItData": {
      "imagesCount": 142
    },
    "entityId": "4793404135709870511",
    "id": "QWdncmVnYXRlZFBpbkRhdGE6NDc5MzQwNDEzNTcwOTg3MDUxMQ==",
    "isShopTheLook": false
  },
  "attribution": {
    "__typename": "Attribution",
    "authorName": "kentbrew",
    "authorUrl": "http://www.flickr.com/photos/kentbrew/",
    "ccUrl": null,
    "embed": null,
    "providerName": "flickr",
    "url": "http://www.flickr.com/photos/kentbrew/6851755809/"
  },
  "board": {
    "boardOrderModifiedAt": "Sun, 14 Mar 2021 17:38:05 +0000",
    "collaboratedByMe": false,
    "collaboratorPermissions": null,
    "coverImageSpec_216x146": {
      "url": "https://i.pinimg.com/216x146/e4/e1/fc/e4e1fc7076e459ff87604d5a0b392f77.jpg"
    },
    "coverImageSpec_236x": {
      "url": "https://i.pinimg.com/236x/e4/e1/fc/e4e1fc7076e459ff87604d5a0b392f77.jpg"
    },
    "coverImageSpec_400x300": {
      "url": "https://i.pinimg.com/400x300/e4/e1/fc/e4e1fc7076e459ff87604d5a0b392f77.jpg"
    },
    "entityId": "99360804217844427",
    "followedByMe": false,
    "id": "Qm9hcmQ6OTkzNjA4MDQyMTc4NDQ0Mjc=",
    "imageCoverHdUrl": "https://i.pinimg.com/474x/e4/e1/fc/e4e1fc7076e459ff87604d5a0b392f77.jpg",
    "imageCoverUrl": "https://i.pinimg.com/200x150/e4/e1/fc/e4e1fc7076e459ff87604d5a0b392f77.jpg",
    "imageThumbnailUrl": "https://i.pinimg.com/upload/99360804217844427_board_thumbnail_2021-03-14-17-38-0…"
  },
  "boostAdsData": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `closeupUnifiedTitle / closeupUnifiedDescription` | Title and description shown on the pin's closeup page. `gridTitle` and `gridDescription` hold the versions shown in the grid. |
| `createdAt` | Date and time the pin was created, as an RFC 2822 style string such as `Thu, 04 Oct 2012 21:50:37 +0000`. |
| `entityId` | Numeric ID of the pin. It matches the number in the pin URL. |
| `domain` | Domain of the site the pin links to, such as `flickr.com`. |
| `attribution.authorName / attribution.authorUrl / attribution.url` | Name of the original author, their profile link, and the link to the original source item. |
| `aggregatedPinData.aggregatedStats.saves` | Number of times the pin has been saved. |
| `aggregatedPinData.commentCount` | Number of comments on the pin. |
| `board.name / board.url / board.pinCount` | Name of the board holding the pin, its relative URL path, and the number of pins on it. |
| `board.owner.entityId` | ID of the user who owns the board. |
| `closeupUnifiedAttribution.username / closeupUnifiedAttribution.followerCount` | Username and follower count of the account the pin is credited to. |

### Notes

- Copy the pin URL from the browser address bar. It has the form `https://www.pinterest.com/pin/<id>/`.
- Many fields, such as `adData` and `affiliateLink`, come back as `null` when the pin has no such data.
- To see more pins from the same board, use [Pinterest Board Pins](/apis/pinterest/board). To find pins by keyword, use [Pinterest Search](/apis/pinterest/search).

### Pricing

$0.018 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/pinterest/pin.json`](../../../catalog/models/pinterest/pin.json) · Store page: https://www.sandbase.ai/model/pinterest/pin
