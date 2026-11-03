# CoinGecko Coins Categories List (ID Map) API: pricing, parameters and code examples

`coingecko/coins-categories-list` · data API · CoinGecko · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Coins Categories List (ID Map) from CoinGecko. Returns the official CoinGecko API response unchanged.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "coingecko/coins-categories-list"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('coingecko/coins-categories-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("coingecko/coins-categories-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "coingecko/coins-categories-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/coingecko/coins-categories-list` with the body above minus `model`.

## Details

Returns the list of all coin categories on CoinGecko as an ID map. Each item has a `category_id` and a display `name`. The API takes no input parameters.

### Use cases

- Build a category picker in an app using the `name` field as the label and `category_id` as the value.
- Validate a category ID before you pass it to another CoinGecko call.
- Sync a local table of CoinGecko categories, for example to find new ecosystem or theme groups.
- Map a stored `category_id` to a readable name in reports.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/coingecko/coins-categories-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "category_id": "0g-ecosystem",
    "name": "0g Ecosystem"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `[].category_id` | Unique ID of the category on CoinGecko. It is a lowercase, hyphenated string such as `0g-ecosystem`. |
| `[].name` | Display name of the category, such as `4chan-Themed`. |

### Notes

- The response is a top-level array. It has no wrapper object.
- The request needs no parameters. Send an empty JSON object `{}`.
- This list has no market data. Call [CoinGecko Coins Categories List with Market Data](/apis/coingecko/coins-categories) for market data per category.
- To find coins themselves, call [CoinGecko Coins List (ID Map)](/apis/coingecko/coins-list).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/coingecko/coins-categories-list.json`](../../../catalog/models/coingecko/coins-categories-list.json) · Store page: https://www.sandbase.ai/model/coingecko/coins-categories-list
