# Polymarket Get raw rewards for a specific market

`polymarket/rewards-markets` · api · Polymarket

Get raw rewards for a specific market from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/rewards-markets", "condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/rewards-markets', {'condition_id': '0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/rewards-markets", {
  "condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/rewards-markets", sandbase.Params{
	"condition_id": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
})
```

Same call via the path form: `POST /v1/api/polymarket/rewards-markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sponsored` | boolean |  | If true, folds sponsored daily rates into each config's rate_per_day default `false` |
| `next_cursor` | string |  | Pagination cursor from previous response  |
| `condition_id` | string | yes | The condition ID of the market  |

## Details

Get raw rewards for a specific market from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/rewards-markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition_id": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `condition_id` | string | Yes | The condition ID of the market |
| `next_cursor` | string | No | Pagination cursor from previous response |
| `sponsored` | boolean | No | If true, folds sponsored daily rates into each config's rate_per_day |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/rewards-markets.json`](../../../catalog/models/polymarket/rewards-markets.json) · Store page: https://www.sandbase.ai/model/polymarket/rewards-markets
