# Polymarket List markets

`polymarket/markets` · api · Polymarket

List markets from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/markets"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/markets', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/markets", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/markets", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/markets` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | array |  | id  |
| `cyom` | boolean |  | cyom  |
| `slug` | array |  | slug  |
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `closed` | boolean |  | Filter by closed state. Omitted or false returns open markets; true returns closed markets. Use any (case-insensitive) to include both states in an identifier lookup. Requires at least one of id, slug, clob_token_ids,… one of: `any` |
| `offset` | integer |  | offset range 0– |
| `tag_id` | integer |  | tag_id  |
| `game_id` | string |  | game_id  |
| `ascending` | boolean |  | ascending  |
| `include_tag` | boolean |  | include_tag  |
| `end_date_max` | string |  | end_date_max  |
| `end_date_min` | string |  | end_date_min  |
| `question_ids` | array |  | question_ids  |
| `related_tags` | boolean |  | related_tags  |
| `condition_ids` | array |  | condition_ids  |
| `clob_token_ids` | array |  | clob_token_ids  |
| `start_date_max` | string |  | start_date_max  |
| `start_date_min` | string |  | start_date_min  |
| `volume_num_max` | number |  | volume_num_max  |
| `volume_num_min` | number |  | volume_num_min  |
| `rewards_min_size` | number |  | rewards_min_size  |
| `liquidity_num_max` | number |  | liquidity_num_max  |
| `liquidity_num_min` | number |  | liquidity_num_min  |
| `sports_market_types` | array |  | sports_market_types  |
| `uma_resolution_status` | string |  | uma_resolution_status  |

## Details

List markets from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/markets" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 1, "active": true}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ascending` | boolean | No | ascending |
| `clob_token_ids` | array | No | clob_token_ids |
| `closed` | boolean | No | Filter by closed state. Omitted or false returns open markets; true returns closed markets. Use any (case-insensitive) to include both states in an identifier l |
| `condition_ids` | array | No | condition_ids |
| `cyom` | boolean | No | cyom |
| `end_date_max` | string | No | end_date_max |
| `end_date_min` | string | No | end_date_min |
| `game_id` | string | No | game_id |
| `id` | array | No | id |
| `include_tag` | boolean | No | include_tag |
| `limit` | integer | No | limit |
| `liquidity_num_max` | number | No | liquidity_num_max |
| `liquidity_num_min` | number | No | liquidity_num_min |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |
| `question_ids` | array | No | question_ids |
| `related_tags` | boolean | No | related_tags |
| `rewards_min_size` | number | No | rewards_min_size |
| `slug` | array | No | slug |
| `sports_market_types` | array | No | sports_market_types |
| `start_date_max` | string | No | start_date_max |
| `start_date_min` | string | No | start_date_min |
| `tag_id` | integer | No | tag_id |
| `uma_resolution_status` | string | No | uma_resolution_status |
| `volume_num_max` | number | No | volume_num_max |
| `volume_num_min` | number | No | volume_num_min |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/markets.json`](../../../catalog/models/polymarket/markets.json) · Store page: https://www.sandbase.ai/model/polymarket/markets
