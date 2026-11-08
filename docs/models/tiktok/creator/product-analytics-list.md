# TikTok Creator Product Analytics List API: pricing, parameters and code examples

`tiktok/creator/product-analytics-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call · **Modes:** sync

Returns products promoted by a TikTok Shop creator along with sales analytics for a designated date range. Results can be filtered by dates and navigated through page numbers.

## Pricing

- **$0.001 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/creator/product-analytics-list", "cookie": "<cookie>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/creator/product-analytics-list', {'cookie': '<cookie>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/creator/product-analytics-list", {
  "cookie": "<cookie>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/creator/product-analytics-list", sandbase.Params{
	"cookie": "<cookie>",
})
```

Same call via the path form: `POST /v1/api/tiktok/creator/product-analytics-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, default is the first page `0`  |
| `proxy` |  |  | Optional HTTP proxy address, can be omitted if not used  |
| `cookie` | string | yes | Cookie string of your own logged-in TikTok Shop creator account (from your browser session on the TikTok Shop / Seller Center site). Sent to the upstream for this request only and never stored by SandBase.  |
| `end_date` | string |  | End date, formatted as 'YYYY-MM-DD', e.g., '2025-05-01'  |
| `start_date` | string |  | Start date, formatted as 'YYYY-MM-DD', e.g., '2025-04-01'  |

## Details

Query promoted products and their sales metrics for a creator account over a specific timeframe using `start_date` and `end_date`.

### Use cases

- Review sales performance for products promoted by a creator.
- Track product revenue trends across custom date intervals.
- Extract historical affiliate product performance records.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/creator/product-analytics-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cookie": "<YOUR_TIKTOK_SHOP_COOKIE>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cookie` | string | Yes | Cookie string of your own logged-in TikTok Shop creator account. Used for this request only and never stored |
| `page` | integer | No | Page number, default is the first page `0` |
| `proxy` | string | No | Optional HTTP proxy address, can be omitted if not used |
| `end_date` | string | No | End date, formatted as 'YYYY-MM-DD', e.g., '2025-05-01' |
| `start_date` | string | No | Start date, formatted as 'YYYY-MM-DD', e.g., '2025-04-01' |

### Notes

- Requires `cookie` from your own TikTok Shop creator account. The data returned belongs to that account; this API cannot look up other creators. SandBase forwards the cookie for this synchronous request only and does not store it in call history or logs, so async mode and retries are not supported.
- Pagination is controlled via `page`, which defaults to `0` for the first page.
- Dates must follow the 'YYYY-MM-DD' format for `start_date` and `end_date`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/tiktok/creator/product-analytics-list.json`](../../../../catalog/models/tiktok/creator/product-analytics-list.json) · Store page: https://www.sandbase.ai/model/tiktok/creator/product-analytics-list
