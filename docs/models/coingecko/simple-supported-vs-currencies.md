# CoinGecko Supported Currencies List API: pricing, parameters and code examples

`coingecko/simple-supported-vs-currencies` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Supported Currencies List from CoinGecko. Returns the official CoinGecko API response unchanged.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/simple-supported-vs-currencies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/simple-supported-vs-currencies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/simple-supported-vs-currencies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/simple-supported-vs-currencies", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/simple-supported-vs-currencies` with the body above minus `model`.

## Details

Returns the list of currency codes that CoinGecko supports, as a flat JSON array of lowercase strings. The request takes no input.

### Use cases

- Fill a currency dropdown with only the codes CoinGecko supports.
- Check that a code such as `eth` or `btc` is on the supported list before you send it in another CoinGecko request.
- Compare the list with your own stored list to spot codes that were added or removed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/simple-supported-vs-currencies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  "btc"
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[]` | The full response is an array. Each item is one supported currency code as a lowercase string. |
| `[0]` | The first code in the array. In the sample response it is `btc`. |
| `[1] / [2]` | Further codes in the array. In the sample response they are `eth` and `ltc`. |

### Notes

- The response is a JSON array of strings, not an object, so there are no named keys.
- To look up coin IDs, call [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list).
- To get market data for coins, call [CoinGecko Coins List with Market Data](/apis/coingecko/coins-markets).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/simple-supported-vs-currencies.json`](../../../catalog/models/coingecko/simple-supported-vs-currencies.json) · Store page: https://www.sandbase.ai/model/coingecko/simple-supported-vs-currencies
