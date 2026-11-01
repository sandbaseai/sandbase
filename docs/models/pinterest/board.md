# Pinterest Board Pins

`pinterest/board` · api · Pinterest

Returns a paginated list of pins from a specified Pinterest board URL, including pin metadata, images, and aggregated pin metrics.

## Pricing

- **$0.018 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pinterest/board", "url": "<url>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pinterest/board', {'url': '<url>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pinterest/board", {
  "url": "<url>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pinterest/board", sandbase.Params{
	"url": "<url>",
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

Retrieve pins and associated metadata from a Pinterest board using its `url`. The endpoint also supports pagination via `cursor` and lightweight responses via `trim`.

### Use cases

- Extract pin images and descriptions from a target Pinterest board.
- Monitor board content additions and aggregate pin metrics over time.
- Collect creative assets from curated boards for visual reference libraries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pinterest/board" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "<url>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The URL of the Pinterest board to fetch pins from. |
| `trim` | boolean | No | Set to true for a trimmed down version of the response. |
| `cursor` | string | No | Pagination cursor from a previous response to get the next page. |

### Notes

- Use `cursor` to request subsequent pages of pins.
- Set `trim` to true to retrieve a reduced response payload.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/pinterest/board.json`](../../../catalog/models/pinterest/board.json) · Store page: https://www.sandbase.ai/model/pinterest/board
