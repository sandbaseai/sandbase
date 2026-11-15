# Yahoo! Auctions Japan Completed Listing Evidence API: pricing, parameters and code examples

`yahoo-auctions-jp/completed-listing-evidence` · data API · Yahoo! Auctions Japan · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Read the public Yahoo Auctions item page for one listing and return the price, timing and status facts exactly as the page states them, without inference.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-auctions-jp/completed-listing-evidence", "item_id": "h1246232284"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-auctions-jp/completed-listing-evidence', {'item_id': 'h1246232284'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-auctions-jp/completed-listing-evidence", {
  "item_id": "h1246232284"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-auctions-jp/completed-listing-evidence", sandbase.Params{
	"item_id": "h1246232284",
})
```

Same call via the path form: `POST /v1/api/yahoo-auctions-jp/completed-listing-evidence` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Auction/Listing ID (e.g., 'm1233190744')  |

## Details

Read the public Yahoo Auctions item page for one listing and return the price, timing and status facts exactly as the page states them, without inference.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yahoo-auctions-jp/completed-listing-evidence", "item_id": "h1246232284"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Auction/Listing ID (e.g., 'm1233190744') |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-auctions-jp/completed-listing-evidence.json`](../../../catalog/models/yahoo-auctions-jp/completed-listing-evidence.json) · Store page: https://www.sandbase.ai/model/yahoo-auctions-jp/completed-listing-evidence
