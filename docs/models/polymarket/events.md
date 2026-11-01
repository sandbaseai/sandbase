# Polymarket List events

`polymarket/events` · api · Polymarket

List events with offset based pagination and filter parameters.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/events"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/events', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/events", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/events", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/events` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | array |  | id  |
| `cyom` | boolean |  | cyom  |
| `slug` | array |  | slug  |
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `active` | boolean |  | active  |
| `closed` | boolean |  | Filter by closed state. Omitted includes open and closed events. Use true for closed events, false for open events, or any (case-insensitive) for both states. Unlike markets, any does not require an identifier filter.… one of: `any` |
| `offset` | integer |  | offset range 0– |
| `tag_id` | integer |  | tag_id  |
| `archived` | boolean |  | archived  |
| `featured` | boolean |  | featured  |
| `tag_slug` | string |  | tag_slug  |
| `ascending` | boolean |  | ascending  |
| `recurrence` | string |  | recurrence  |
| `volume_max` | number |  | volume_max  |
| `volume_min` | number |  | volume_min  |
| `end_date_max` | string |  | end_date_max  |
| `end_date_min` | string |  | end_date_min  |
| `include_chat` | boolean |  | include_chat  |
| `related_tags` | boolean |  | related_tags  |
| `liquidity_max` | number |  | liquidity_max  |
| `liquidity_min` | number |  | liquidity_min  |
| `exclude_tag_id` | array |  | exclude_tag_id  |
| `start_date_max` | string |  | start_date_max  |
| `start_date_min` | string |  | start_date_min  |
| `include_template` | boolean |  | include_template  |

## Details

List events with offset based pagination and filter parameters.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/events" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 1, "active": true}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `active` | boolean | No | active |
| `archived` | boolean | No | archived |
| `ascending` | boolean | No | ascending |
| `closed` | boolean | No | Filter by closed state. Omitted includes open and closed events. Use true for closed events, false for open events, or any (case-insensitive) for both states. U |
| `cyom` | boolean | No | cyom |
| `end_date_max` | string | No | end_date_max |
| `end_date_min` | string | No | end_date_min |
| `exclude_tag_id` | array | No | exclude_tag_id |
| `featured` | boolean | No | featured |
| `id` | array | No | id |
| `include_chat` | boolean | No | include_chat |
| `include_template` | boolean | No | include_template |
| `limit` | integer | No | limit |
| `liquidity_max` | number | No | liquidity_max |
| `liquidity_min` | number | No | liquidity_min |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |
| `recurrence` | string | No | recurrence |
| `related_tags` | boolean | No | related_tags |
| `slug` | array | No | slug |
| `start_date_max` | string | No | start_date_max |
| `start_date_min` | string | No | start_date_min |
| `tag_id` | integer | No | tag_id |
| `tag_slug` | string | No | tag_slug |
| `volume_max` | number | No | volume_max |
| `volume_min` | number | No | volume_min |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/events.json`](../../../catalog/models/polymarket/events.json) · Store page: https://www.sandbase.ai/model/polymarket/events
