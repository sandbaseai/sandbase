# Polymarket Get current active rewards configurations API: pricing, parameters and code examples

`polymarket/rewards-markets-current` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns the current active rewards configurations for markets.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/rewards-markets-current"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/rewards-markets-current', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/rewards-markets-current", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/rewards-markets-current", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/rewards-markets-current` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sponsored` | boolean |  | If true, returns sponsored reward configurations instead of standard ones default `false` |
| `next_cursor` | string |  | Pagination cursor from previous response  |

## Details

Returns the current active liquidity rewards configurations for Polymarket markets. Each row has a market `condition_id`, the daily reward rate, and the quoting rules for earning rewards. No input is required, and you can pass `sponsored` to switch to sponsored configurations.

### Use cases

- List every market that currently pays liquidity rewards, so a market maker can pick where to quote.
- Rank markets by `total_daily_rate` to find the largest daily reward pools.
- Check `rewards_max_spread` and `rewards_min_size` to set quote width and order size for a reward-earning strategy.
- Compare standard and sponsored reward configurations by calling with `sponsored` set to `true` and `false`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/rewards-markets-current" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `next_cursor` | string | No | Pagination cursor from previous response |
| `sponsored` | boolean | No | If true, returns sponsored reward configurations instead of standard ones |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 500,
  "data": [
    {
      "condition_id": "0x0000c7fe300953933808d82cd4aa35dbc9f291f0b78ca9da43b0604883906c6c",
      "native_daily_rate": 1,
      "rewards_config": [
        {
          "asset_address": "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB",
          "end_date": "2500-12-31",
          "id": 0,
          "rate_per_day": 1,
          "start_date": "2026-11-03",
          "total_rewards": 0
        }
      ],
      "rewards_max_spread": 5.5,
      "rewards_min_size": 20,
      "total_daily_rate": 1
    }
  ],
  "limit": 500,
  "next_cursor": "NTAw"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].condition_id` | Identifier of the market the reward applies to. It starts with `0x`. |
| `data[].total_daily_rate` | Total daily reward rate for the market. |
| `data[].native_daily_rate` | Daily reward rate from the native reward configuration. In the sample rows it equals `total_daily_rate`. |
| `data[].rewards_max_spread` | Maximum spread setting for the market's rewards. |
| `data[].rewards_min_size` | Minimum size setting for the market's rewards. |
| `data[].rewards_config[].asset_address` | Address of the asset used for the reward, starting with `0x`. |
| `data[].rewards_config[].rate_per_day` | Reward rate per day for this configuration entry. |
| `data[].rewards_config[].start_date / data[].rewards_config[].end_date` | Dates in `YYYY-MM-DD` format that bound the reward configuration. |
| `data[].rewards_config[].total_rewards` | Total rewards value for this configuration entry. |
| `next_cursor` | Cursor string to pass as `next_cursor` to get the next page. |

### Notes

- Pass the `next_cursor` value from one response as the `next_cursor` parameter to fetch the next page. `count` and `limit` were both `500` in the sample.
- `sponsored` defaults to `false`, which returns standard configurations.
- Use `condition_id` to look up a single market with [Polymarket Get raw rewards for a specific market](/apis/polymarket/rewards-markets) or market details with [Polymarket Get CLOB market info](/apis/polymarket/clob-markets).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/rewards-markets-current.json`](../../../catalog/models/polymarket/rewards-markets-current.json) · Store page: https://www.sandbase.ai/model/polymarket/rewards-markets-current
