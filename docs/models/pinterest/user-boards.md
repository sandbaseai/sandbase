# Pinterest User Boards API: pricing, parameters and code examples

`pinterest/user-boards` · data API · Pinterest · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.018 per call · **Modes:** sync

Get a Pinterest user's boards by username: board name, URL, description, pin and follower counts, cover images and creation date.

## Pricing

- **$0.018 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pinterest/user-boards", "handle": "example"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pinterest/user-boards', {'handle': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pinterest/user-boards", {
  "handle": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pinterest/user-boards", sandbase.Params{
	"handle": "example",
})
```

Same call via the path form: `POST /v1/api/pinterest/user-boards` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `trim` | boolean |  | Set to true for a trimmed down version of the response.  |
| `handle` | string | yes | The Pinterest username to get boards for (e.g. 'broadstbullycom' from https://www.pinterest.com/broadstbullycom/).  |

## Details

This API returns the boards on a Pinterest profile. Each board has a name, URL, description, pin count, follower count, cover image and creation date. It needs the Pinterest username as `handle`.

### Use cases

- Compare how a brand groups its content into boards and which boards draw the most followers.
- Rank a creator's boards by `follower_count` to find the topics that attract the most attention.
- Collect board URLs for a profile, then pull the pins from each board.
- Track the size of a board over time by saving `pin_count` and `follower_count` on a schedule.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pinterest/user-boards" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "pinterest", "trim": true}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | The Pinterest username to get boards for (e.g. 'broadstbullycom' from https://www.pinterest.com/broadstbullycom/). |
| `trim` | boolean | No | Set to true for a trimmed down version of the response. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "boards": [
    {
      "created_at": "Fri, 23 Oct 2026 23:04:28 +0000",
      "description": "Thoughtful finds for a slower, softer life — candles, journals and self-care tre…",
      "follower_count": 4233328,
      "id": "424605139808129209",
      "image_cover_hd_url": "https://i.pinimg.com/474x/57/4d/64/574d645321687c7bb1ab8d1163daae9b.jpg",
      "name": "Grounding gifts to romanticize your life",
      "pin_count": 59,
      "url": "https://www.pinterest.com/pinterest/grounding-gifts-to-romanticize-your-life/"
    }
  ],
  "credits_charged": 1,
  "credits_remaining": 409649,
  "cursor": "LT40MjQ2MDUxMzk4MDgxMjc3NDN8MTB8NDUyNDcwNTM2ODQ2ODIwMipHUUwqfDA1NmI5M2UyMzZhNGFl…",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `boards[]` | List of boards that belong to the user. |
| `boards[].name` | Title of the board. |
| `boards[].description` | Text the owner wrote to describe the board. |
| `boards[].url` | Full Pinterest URL of the board. |
| `boards[].id` | Numeric board ID, returned as a string. |
| `boards[].pin_count / boards[].follower_count` | Number of pins saved on the board and number of users who follow it. |
| `boards[].image_cover_hd_url` | URL of the board's cover image. |
| `boards[].created_at` | Creation date and time of the board, in a format like `Fri, 23 Oct 2026 23:04:28 +0000`. |
| `cursor` | Token that points to the next page of boards. |

### Notes

- Take `handle` from the profile URL. For https://www.pinterest.com/pinterest/ the value is `pinterest`.
- Pass the returned `cursor` to request more boards, if your plan of use supports paging with it. The response carries it when more results may exist.
- Set `trim` to `true` for a smaller response, as used in the example.
- To list the pins on a board, call [Pinterest Board Pins](/apis/pinterest/board) next.

### Pricing

$0.018 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/pinterest/user-boards.json`](../../../catalog/models/pinterest/user-boards.json) · Store page: https://www.sandbase.ai/model/pinterest/user-boards
