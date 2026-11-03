# Polymarket Builders Leaderboard API: pricing, parameters and code examples

`polymarket/builders-leaderboard` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Leaderboard of Polymarket builders (apps routing orders) by volume for a time period.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/builders-leaderboard"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/builders-leaderboard', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/builders-leaderboard", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/builders-leaderboard", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/builders-leaderboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | First-page size. Ignored when `cursor` is supplied. range 0–1000 |
| `cursor` | string |  | Opaque pagination cursor from a prior response's `next_cursor`.  |
| `time_period` | string |  | Window: `day` \| `week` \| `month` \| `all`. Defaults to `day`.  |

## Details

Returns a ranked list of Polymarket builders, which are apps that route orders, ordered by trading volume for a chosen time window. It needs no required input. You can set `time_period` to `day`, `week`, `month` or `all`, and set `limit` for the page size.

### Use cases

- Rank the apps that route the most Polymarket order volume today or over all time.
- Track how many active users each builder has to compare large and small order-routing apps.
- Check which builders are verified before you list or integrate them.
- Pull the `builder_code` of top builders to match them against volume data in another call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/builders-leaderboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Opaque pagination cursor from a prior response's `next_cursor`. |
| `limit` | integer | No | First-page size. Ignored when `cursor` is supplied. |
| `time_period` | string | No | Window: `day` / `week` / `month` / `all`. Defaults to `day`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "active_users": 137,
      "builder_code": "0xceebf77a833b30520287ddd9478ff51abbdffa30aa90a8d655dba0e8a79ce0c1",
      "builder_name": "betmoar",
      "profile_image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/betmoar_2.png",
      "rank": 1,
      "verified": true,
      "volume": 3712124.5321740014
    }
  ],
  "pagination": {
    "has_more": true,
    "limit": 2,
    "next_cursor": "eyJkYXRhIjp7InR5cGUiOiJidWlsZGVyc19sZWFkZXJib2FyZCIsInBhcmFtcyI6eyJsIjoyLCJvIjoy…",
    "offset": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].rank` | Position of the builder on the leaderboard for the chosen time window. `1` is the highest volume. |
| `data[].builder_name` | Display name of the builder app. |
| `data[].builder_code` | Hex identifier of the builder. Use it to match the builder in other data. |
| `data[].volume` | Trading volume routed by the builder in the time window, as a decimal number. |
| `data[].active_users` | Number of active users for the builder in the time window. |
| `data[].verified` | `true` when the builder is marked as verified. |
| `data[].profile_image` | URL of the builder's profile image. |
| `pagination.has_more` | `true` when more rows are available after this page. |
| `pagination.next_cursor` | Opaque cursor for the next page. Pass it back as `cursor`. |
| `pagination.limit` | Page size used for this response. |

### Notes

- Pass `next_cursor` as `cursor` to get the next page. When you send `cursor`, `limit` is ignored, and the window is kept inside the cursor.
- `time_period` defaults to `day` when you leave it out.
- For volume figures per builder over time, see [Polymarket Builders Volume](/apis/polymarket/builders-volume). For ranking individual traders instead of apps, see [Polymarket Trader Leaderboard](/apis/polymarket/leaderboard).

### Pricing

$0.012 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/builders-leaderboard.json`](../../../catalog/models/polymarket/builders-leaderboard.json) · Store page: https://www.sandbase.ai/model/polymarket/builders-leaderboard
