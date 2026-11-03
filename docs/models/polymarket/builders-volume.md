# Polymarket Builders Volume API: pricing, parameters and code examples

`polymarket/builders-volume` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Daily, weekly or monthly volume of Polymarket builders over time.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/builders-volume"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/builders-volume', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/builders-volume", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/builders-volume", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/builders-volume` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | How many of the most recent buckets to return. Defaults to 30, capped at 90; a lower ceiling than the rest of the surface, because only ~308 daily buckets exist and the family maximum would return the whole series.… range 0–90 |
| `interval` | string |  | Bucket width: `day` \| `week` \| `month` \| `all`. Defaults to `day`. `timePeriod` and `time_period` are accepted aliases.  |

## Details

Returns builder volume on Polymarket, grouped into time buckets. Each row gives one builder's volume, active users and rank for one date. You can set the bucket width with `interval` and the number of recent buckets with `limit`. No input is required.

### Use cases

- Track how a builder's trading volume changes from day to day.
- Rank Polymarket builders by volume for the latest bucket.
- Compare `active_users` against `volume` to see which builders bring in large traders versus many small ones.
- Chart total builder volume over weeks or months by summing rows per `date`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/builders-volume" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `interval` | string | No | Bucket width: `day` / `week` / `month` / `all`. Defaults to `day`. `timePeriod` and `time_period` are accepted aliases. |
| `limit` | integer | No | How many of the most recent buckets to return. Defaults to 30, capped at 90; a lower ceiling than the rest of the surface, because only ~308 daily buckets exist and the family maximum would return the whole series. Bound |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "active_users": 136,
      "builder_code": "0xceebf77a833b30520287ddd9478ff51abbdffa30aa90a8d655dba0e8a79ce0c1",
      "builder_name": "betmoar",
      "date": "2026-11-03",
      "profile_image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/betmoar_2.png",
      "rank": 1,
      "verified": true,
      "volume": 3710921.3821739997
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One row per builder per time bucket. |
| `data[].builder_name` | Display name of the builder. |
| `data[].builder_code` | Hex code that identifies the builder. |
| `data[].date` | Date of the bucket, in `YYYY-MM-DD` format. |
| `data[].volume` | Trading volume the builder produced in that bucket. Values are decimal numbers. |
| `data[].active_users` | Number of active users for the builder in that bucket. |
| `data[].rank` | Position of the builder within its bucket. `1` has the highest volume in the sample. |
| `data[].verified` | Whether the builder is marked as verified. |
| `data[].profile_image` | URL of the builder's profile image. It can be an empty string. |

### Notes

- `limit` counts buckets, not rows. Each bucket holds several builder rows, so a request with `limit` set to `2` can return more than two rows.
- `limit` defaults to 30 and has a maximum of 90. `interval` accepts `day`, `week`, `month` or `all` and defaults to `day`. `timePeriod` and `time_period` work as aliases for `interval`.
- For a ranked list of builders without the time series, call [Polymarket Builders Leaderboard](/apis/polymarket/builders-leaderboard).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/builders-volume.json`](../../../catalog/models/polymarket/builders-volume.json) · Store page: https://www.sandbase.ai/model/polymarket/builders-volume
