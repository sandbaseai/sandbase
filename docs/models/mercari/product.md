# Mercari Product API: pricing, parameters and code examples

`mercari/product` · data API · Mercari · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Get one Mercari US or Japan listing by item id or URL: title, description, price, original price, status, condition, brand, category, size, photos, shipping terms (who pays, method, ships-from region, handling days), whether offers are accepted, likes, seller name, rating, listing count and join date, when it was listed, and for a sold US item when it sold. For a sold item the price is the final sale price after any accepted offer.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "mercari/product", "itemId": "m73121443159"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('mercari/product', {'itemId': 'm73121443159'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("mercari/product", {
  "itemId": "m73121443159"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "mercari/product", sandbase.Params{
	"itemId": "m73121443159",
})
```

Same call via the path form: `POST /v1/api/mercari/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | Mercari item id or full listing URL (e.g. m73121443159 or https://www.mercari.com/us/item/m73121443159/). A jp.mercari.com URL is looked up in Japan whatever country says. Every mercari.search and mercari.sold_listings…  |
| `country` | string |  | Mercari marketplace of the item id: us (USD) or jp (JPY). Ids are not shared between countries. one of: `us`, `jp`; default `"us"` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `sellerJoinedUtc`, and it is served only by a source that returns…  |

## Details

Get one Mercari US or Japan listing by item id or URL: title, description, price, original price, status, condition, brand, category, size, photos, shipping terms (who pays, method, ships-from region, handling days), whether offers are accepted, likes, seller name, rating, listing count and join date, when it was listed, and for a sold US item when it sold. For a sold item the price is the final sale price after any accepted offer.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "mercari/product", "itemId": "m73121443159"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | Mercari item id or full listing URL (e.g. m73121443159 or https://www.mercari.com/us/item/m73121443159/). A jp.mercari.com URL is looked up in Japan whatever country says. Every mercari.search and mercari.sold_listings r |
| `country` | string | No | Mercari marketplace of the item id: us (USD) or jp (JPY). Ids are not shared between countries. One of: `us`, `jp`. Default `"us"`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `sellerJoinedUtc`, and it is served only by a source that returns ever |

### Pricing

Billed at the actual cost of each call, about $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/mercari/product.json`](../../../catalog/models/mercari/product.json) · Store page: https://www.sandbase.ai/model/mercari/product
