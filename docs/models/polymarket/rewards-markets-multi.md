# Polymarket Get multiple markets with rewards

`polymarket/rewards-markets-multi` · api · Polymarket

Returns multiple markets with rewards and supports filtering and sorting.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/rewards-markets-multi"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/rewards-markets-multi', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/rewards-markets-multi", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/rewards-markets-multi", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/rewards-markets-multi` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Text search on market question/description  |
| `event_id` | string |  | Filter by event ID. Can be repeated for multiple events (e.g., ?event_id=100&event_id=200)  |
| `order_by` | string |  | Field to sort results by one of: `market_id`, `created_at`, `volume_24hr`, `spread`, `competitiveness`, `max_spread`, `min_size`, `question`, `one_day_price_change`, `rate_per_day`, `price`, `end_date` … |
| `position` | string |  | Sort direction one of: `ASC`, `DESC` |
| `tag_slug` | string |  | Filter by tag slug. Can be repeated for OR logic (e.g., ?tag_slug=sports&tag_slug=politics)  |
| `max_price` | number |  | Maximum first token price filter  |
| `min_price` | number |  | Minimum first token price filter  |
| `page_size` | integer |  | Number of items per page (max 500, values above are capped) default `100`; range –500 |
| `max_spread` | number |  | Maximum spread filter  |
| `min_spread` | number |  | Minimum spread filter  |
| `event_title` | string |  | Search event titles using case-insensitive pattern matching  |
| `next_cursor` | string |  | Pagination cursor from previous response  |
| `max_volume_24hr` | number |  | Maximum 24-hour volume filter  |
| `min_volume_24hr` | number |  | Minimum 24-hour volume filter  |

## Details

Returns multiple markets with rewards and supports filtering and sorting.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/rewards-markets-multi" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `event_id` | string | No | Filter by event ID. Can be repeated for multiple events (e.g., ?event_id=100&event_id=200) |
| `event_title` | string | No | Search event titles using case-insensitive pattern matching |
| `max_price` | number | No | Maximum first token price filter |
| `max_spread` | number | No | Maximum spread filter |
| `max_volume_24hr` | number | No | Maximum 24-hour volume filter |
| `min_price` | number | No | Minimum first token price filter |
| `min_spread` | number | No | Minimum spread filter |
| `min_volume_24hr` | number | No | Minimum 24-hour volume filter |
| `next_cursor` | string | No | Pagination cursor from previous response |
| `order_by` | string | No | Field to sort results by |
| `page_size` | integer | No | Number of items per page (max 500, values above are capped) |
| `position` | string | No | Sort direction |
| `q` | string | No | Text search on market question/description |
| `tag_slug` | string | No | Filter by tag slug. Can be repeated for OR logic (e.g., ?tag_slug=sports&tag_slug=politics) |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/rewards-markets-multi.json`](../../../catalog/models/polymarket/rewards-markets-multi.json) · Store page: https://www.sandbase.ai/model/polymarket/rewards-markets-multi
