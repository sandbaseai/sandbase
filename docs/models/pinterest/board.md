# Pinterest Board Pins API: pricing, parameters and code examples

`pinterest/board` · data API · Pinterest · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.018 per call · **Modes:** sync

Returns a paginated list of pins from a specified Pinterest board URL, including pin metadata, images, and aggregated pin metrics.

## Pricing

- **$0.018 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pinterest/board", "url": "https://www.pinterest.com/pinterest/official-news/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pinterest/board', {'url': 'https://www.pinterest.com/pinterest/official-news/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pinterest/board", {
  "url": "https://www.pinterest.com/pinterest/official-news/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pinterest/board", sandbase.Params{
	"url": "https://www.pinterest.com/pinterest/official-news/",
})
```

Same call via the path form: `POST /v1/api/pinterest/board` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The URL of the Pinterest board to fetch pins from.  |
| `trim` | boolean |  | Set to true for a trimmed down version of the response.  |
| `cursor` | string |  | Pagination cursor from a previous response to get the next page.  |

## Details

Returns a page of pins from a public Pinterest board. Each pin includes its description, image URLs in several sizes, the source domain, board and owner details, and save counts. The only required input is the board `url`.

### Use cases

- Download pin images and descriptions from a curated board to build a visual reference library.
- Track `aggregated_pin_data.aggregated_stats.saves` across pins to see which board content gets saved most.
- Check which domains a board links to by reading `domain` on each pin.
- Page through a brand's board to archive its pins with their IDs and dominant colors.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pinterest/board" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.pinterest.com/pinterest/official-news/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The URL of the Pinterest board to fetch pins from. |
| `cursor` | string | No | Pagination cursor from a previous response to get the next page. |
| `trim` | boolean | No | Set to true for a trimmed down version of the response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "credits_charged": 1,
  "credits_remaining": 409647,
  "cursor": "Y2JZakk0ZUU1WWR6Qk9SRmw1VDBSVk1rNXFRVEZPUkVVMFRYcHJkMHRyWkZKVVEzQTRUVWRWTlU5RVNY…",
  "pins": [
    {
      "access": [],
      "aggregated_pin_data": {
        "aggregated_stats": {
          "done": 1,
          "saves": 99
        },
        "creator_analytics": null,
        "did_it_data": {
          "details_count": 1,
          "images_count": 1,
          "rating": -1,
          "recommend_scores": [
            {
              "count": 0,
              "score": 1
            }
          ],
          "recommended_count": 1,
          "responses_count": 0,
          "tags": [],
          "type": "aggregateddiditdata"
        },
        "id": "4932015542193108810",
        "is_shop_the_look": false,
        "node_id": "QWdncmVnYXRlZFBpbkRhdGE6NDkzMjAxNTU0MjE5MzEwODgxMA=="
      },
      "alt_text": null,
      "attribution": null,
      "auto_alt_text": "a room filled with lots of yellow stools next to a table and shelves on the wall",
      "board": {
        "collaborated_by_me": false,
        "followed_by_me": false,
        "id": "424605139806979476",
        "is_collaborative": false,
        "layout": "default",
        "name": "Official news",
        "node_id": "Qm9hcmQ6NDI0NjA1MTM5ODA2OTc5NDc2",
        "owner": {
          "full_name": "Pinterest",
          "id": "424605208526455283",
          "image_medium_url": "https://i.pinimg.com/75x75_RS/1c/b5/61/1cb561c8e7b9c709f78d110a4b5f0863.jpg",
          "image_small_url": "https://i.pinimg.com/30x30_RS/1c/b5/61/1cb561c8e7b9c709f78d110a4b5f0863.jpg",
          "is_primary_website_verified": true,
          "is_verified_merchant": false,
          "node_id": "VXNlcjo0MjQ2MDUyMDg1MjY0NTUyODM=",
          "username": "pinterest"
        }
      },
      "call_to_action_text": null,
      "campaign_id": null,
      "carousel_data": null,
      "category": "",
      "collection_pin": null,
      "creator_analytics": null
    }
  ],
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `pins[].id` | Identifier of the pin. |
| `pins[].description / pins[].grid_title` | The pin description text and the title shown in the grid. `grid_title` can be an empty string. |
| `pins[].domain` | Domain the pin links to. Pins uploaded directly show `Uploaded by user`. |
| `pins[].images.orig.url / pins[].images.orig.width / pins[].images.orig.height` | URL of the original-size image, with its width and height. The `images` object also lists smaller versions, each with its own `url`, `width` and `height`. |
| `pins[].dominant_color` | Main color of the pin image as a hex code. |
| `pins[].auto_alt_text` | Generated text describing the image. It can be `null`. |
| `pins[].aggregated_pin_data.aggregated_stats.saves / pins[].aggregated_pin_data.aggregated_stats.done` | Number of saves and the `done` count for the pin. |
| `pins[].board.name / pins[].board.id` | Name and ID of the board that holds the pin. |
| `pins[].board.owner.username / pins[].board.owner.full_name` | Username and display name of the board owner. |
| `cursor` | Token for the next page of pins. |

### Notes

- Pass the `cursor` value from a response as the `cursor` parameter to get the next page.
- Set `trim` to `true` to get a smaller response.
- The `url` must be a full board address, for example `https://www.pinterest.com/pinterest/official-news/`.
- To get more detail on one pin, use [Pinterest Pin Details](/apis/pinterest/pin). To list the boards of a user, use [Pinterest User Boards](/apis/pinterest/user-boards).

### Pricing

$0.018 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/pinterest/board.json`](../../../catalog/models/pinterest/board.json) · Store page: https://www.sandbase.ai/model/pinterest/board
