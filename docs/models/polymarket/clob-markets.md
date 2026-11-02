# Polymarket Get CLOB market info API: pricing, parameters and code examples

`polymarket/clob-markets` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns all CLOB-level parameters for a market in a single call — tokens, tick size, base fees, rewards, RFQ status, and fee details.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/clob-markets", "condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/clob-markets', {'condition_id': '0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/clob-markets", {
  "condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/clob-markets", sandbase.Params{
	"condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
})
```

Same call via the path form: `POST /v1/api/polymarket/clob-markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `condition_id` | string | yes | The condition ID of the market  |

## Details

Returns all CLOB-level parameters for a market in a single call — tokens, tick size, base fees, rewards, RFQ status, and fee details.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/clob-markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition_id": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `condition_id` | string | Yes | The condition ID of the market |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/clob-markets.json`](../../../catalog/models/polymarket/clob-markets.json) · Store page: https://www.sandbase.ai/model/polymarket/clob-markets
