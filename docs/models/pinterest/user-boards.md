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

Pass a Pinterest username and get the boards on that profile.

### Use cases

- Analyze how brands organize content on Pinterest.
- Find popular boards in a niche.
- Track board growth.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pinterest/user-boards" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "pinterest", "trim": true}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | The Pinterest username to get boards for (e.g. 'broadstbullycom' from https://www.pinterest.com/broadstbullycom/). |
| `trim` | boolean | No | Set to true for a trimmed down version of the response. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "boards": [
    {
      "description": "Inspired by the Pinterest Predicts trend, Wilderkind, this limited-edition collection is …",
      "follower_count": 8323,
      "id": "1136033143445898365",
      "name": "The Wilderkind Collection",
      "pin_count": 45,
      "url": "https://www.pinterest.com/chamberlaincoffeepins/the-wilderkind-collection/"
    }
  ]
}
```

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/pinterest/user-boards.json`](../../../catalog/models/pinterest/user-boards.json) · Store page: https://www.sandbase.ai/model/pinterest/user-boards
