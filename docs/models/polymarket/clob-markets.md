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

Returns the CLOB trading settings for one Polymarket market. These include its outcome tokens, tick size, base fees, rewards settings and fee details. It needs the market's `condition_id`.

### Use cases

- Look up the `Yes` and `No` token IDs for a market before you query prices or order books.
- Read the tick size before you build limit orders for a market.
- Check whether a market has rewards settings before you plan market making.
- Compare the fee settings of several markets by calling this API once per `condition_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/clob-markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"condition_id": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `condition_id` | string | Yes | The condition ID of the market |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ao": true,
  "aot": "2025-07-03T20:36:33Z",
  "c": "0xa467b14d51f01b957109d9cbb1d6c124fab2a089d52ed8f471d23c2812e743b7",
  "cbos": true,
  "fd": {
    "e": 1,
    "r": 0.04,
    "to": true
  },
  "ibce": true,
  "mbf": 1000,
  "mos": 5,
  "mts": 0.001,
  "r": {
    "e": true,
    "ma": 3.5,
    "mi": 200,
    "moas": 4
  },
  "t": [
    {
      "o": "Yes",
      "t": "32338220190071351435772801779725302244575775216413325951443816017994629993401"
    }
  ],
  "tbf": 1000
}
```

### Response fields

| Field | Meaning |
|---|---|
| `c` | The condition ID of the market. It matches the `condition_id` you sent. |
| `t[].o / t[].t` | One row per outcome. `o` is the outcome label, such as `Yes` or `No`. `t` is the token ID for that outcome, as a long decimal string. |
| `mts` | The tick size setting for the market. The value is `0.001` in this example. |
| `mbf / tbf` | The base fee settings for the market. Both are `1000` in this example. |
| `r.e / r.ma / r.mi / r.moas` | The rewards settings for the market. `e` is `true` when rewards are set up. The response gives these keys in short form only, so check the numbers against Polymarket's rewards docs. |
| `fd.e / fd.r / fd.to` | The fee details for the market. The example returns `e` as `1`, `r` as `0.04` and `to` as `true`. |
| `aot` | A timestamp in ISO 8601 UTC format, such as `2025-07-03T20:36:33Z`. |
| `v` | A version string. The value is `v1` in this example. |

### Notes

- The response uses short keys such as `c`, `t` and `mts`. The response is returned as the official Polymarket API sends it.
- Token IDs in `t[].t` are long decimal strings. Keep them as strings so no digits are lost.
- Use a token ID from `t[].t` with token-based APIs such as [Polymarket Get fee rate by path parameter](/apis/polymarket/fee-rate-by-token-id) or [Polymarket Get market by token](/apis/polymarket/markets-by-token).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/clob-markets.json`](../../../catalog/models/polymarket/clob-markets.json) · Store page: https://www.sandbase.ai/model/polymarket/clob-markets
