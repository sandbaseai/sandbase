# Polymarket List teams API: pricing, parameters and code examples

`polymarket/teams` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

List teams from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/teams"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/teams', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/teams", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/teams", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/teams` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` | array |  | name  |
| `limit` | integer |  | limit range 0– |
| `order` | string |  | Comma-separated list of fields to order by  |
| `league` | array |  | league  |
| `offset` | integer |  | offset range 0– |
| `ascending` | boolean |  | ascending  |
| `abbreviation` | array |  | abbreviation  |

## Details

Returns a list of sports and esports teams listed on Polymarket. Each team has a name, abbreviation, league, logo URL and record. All inputs are optional filters, so an empty request returns teams without a filter.

### Use cases

- Build a lookup table of team names, abbreviations and logos to label sports markets in your own app.
- List every team in one league, such as `ufc` or `csgo`, by passing the `league` filter.
- Find a team's `id` and `abbreviation` from its name before you match it to a market or event.
- Track when team records change by reading `record` and `updatedAt`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/teams" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `abbreviation` | array | No | abbreviation |
| `ascending` | boolean | No | ascending |
| `league` | array | No | league |
| `limit` | integer | No | limit |
| `name` | array | No | name |
| `offset` | integer | No | offset |
| `order` | string | No | Comma-separated list of fields to order by |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "abbreviation": "axe",
    "color": "#CF9275",
    "createdAt": "2025-11-03T18:43:58.938256Z",
    "id": 216158,
    "league": "ufc",
    "logo": "https://polymarket-upload.s3.us-east-2.amazonaws.com/team_logos/mma/axel_sola.pn…",
    "name": "Axel Sola",
    "providerId": 140005569,
    "record": "13-1-1",
    "updatedAt": "2026-05-15T09:00:01.449694Z"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Numeric ID of the team on Polymarket. |
| `name` | Display name of the team or fighter, for example `Axel Sola`. |
| `abbreviation` | Short code for the team, in lowercase, for example `axe` or `usa`. |
| `league` | League the team belongs to, for example `ufc` or `csgo`. |
| `record` | Win-loss record as a string, for example `13-1-1` or `0-0`. |
| `logo` | URL of the team logo image. |
| `color` | Hex color code for the team, for example `#CF9275`. |
| `providerId` | Numeric ID of the team in an external sports data source. Use it to match this team to outside data. |
| `createdAt / updatedAt` | ISO 8601 UTC timestamps for when the team record was created and last changed. |

### Notes

- Use `limit` and `offset` to page through results. `limit` is the page size and `offset` is the number of teams to skip.
- Use `order` with a comma-separated list of field names, and set `ascending` to control the sort direction.
- `abbreviation`, `league` and `name` each take an array of strings, so you can filter on several values in one call.
- To see which leagues exist, call [Polymarket Get sports metadata information](/apis/polymarket/sports).

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/teams.json`](../../../catalog/models/polymarket/teams.json) · Store page: https://www.sandbase.ai/model/polymarket/teams
