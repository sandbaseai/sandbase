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
  -d '{"model": "pinterest/pin", "url": "<url>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pinterest/pin', {'url': '<url>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pinterest/pin", {
  "url": "<url>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pinterest/pin", sandbase.Params{
	"url": "<url>",
})
```

Same call via the path form: `POST /v1/api/pinterest/pin` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The Pinterest pin URL to fetch details for.  |
| `trim` | boolean |  | Set to true for a trimmed down version of the response.  |

## Details

Retrieve detailed metadata for a specific Pinterest pin by supplying its link via `url`. Set `trim` to true to receive a compact version of the data.

### Use cases

- Inspect metadata and media details from a Pinterest pin URL.
- Display pin information within external social media monitoring tools.
- Retrieve compact pin details by enabling the trimmed response option.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pinterest/pin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "<url>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The Pinterest pin URL to fetch details for. |
| `trim` | boolean | No | Set to true for a trimmed down version of the response. |

### Notes

- Set `trim` to true to obtain a trimmed-down version of the response.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/pinterest/pin.json`](../../../catalog/models/pinterest/pin.json) · Store page: https://www.sandbase.ai/model/pinterest/pin
