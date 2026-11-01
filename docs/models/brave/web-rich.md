# Brave Rich Search

`brave/web-rich` · api · Brave

Rich Search from Brave. Returns the official Brave API response unchanged.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "brave/web-rich", "callback_key": "9a186935547145e29271648369eeec01"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('brave/web-rich', {'callback_key': '9a186935547145e29271648369eeec01'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("brave/web-rich", {
  "callback_key": "9a186935547145e29271648369eeec01"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "brave/web-rich", sandbase.Params{
	"callback_key": "9a186935547145e29271648369eeec01",
})
```

Same call via the path form: `POST /v1/api/brave/web-rich` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `callback_key` | string | yes | The callback key to use for the rich header  |

## Details

Rich Search from Brave. Returns the official Brave API response unchanged.

The response is the official Brave API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/brave/web-rich" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"callback_key": "9a186935547145e29271648369eeec01"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `callback_key` | string | Yes | The callback key to use for the rich header |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/brave/web-rich.json`](../../../catalog/models/brave/web-rich.json) · Store page: https://www.sandbase.ai/model/brave/web-rich
