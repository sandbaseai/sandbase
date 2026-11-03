# Polymarket Get sports metadata information API: pricing, parameters and code examples

`polymarket/sports` · data API · Polymarket · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00044 per call (free daily quota) · **Modes:** sync

Get sports metadata information from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/sports"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/sports', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/sports", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/sports", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/polymarket/sports` with the body above minus `model`.

## Details

Returns a list of sports and leagues that Polymarket supports, with one object per league. It needs no input. Each object holds the league name, a short sport code, an icon URL, and the tag and series IDs linked to that league.

### Use cases

- Build a league picker for a sports betting dashboard from the `name` and `image` fields.
- Map each `sport` code to its `primaryTagId` so you can filter Polymarket events by league.
- Find the `series` ID of a league to look up its recurring games.
- Track newly added leagues by sorting on `createdAt`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/sports" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
[
  {
    "createdAt": "2026-08-07T21:41:19.879539Z",
    "id": 630,
    "image": "https://polymarket-upload.s3.us-east-2.amazonaws.com/league-icons/ufl.png",
    "name": "UFL",
    "ordering": "away",
    "primaryTagId": 105925,
    "resolution": "https://www.theufl.com/",
    "series": "12553",
    "sport": "ufl",
    "tags": "1,100639,1186,105925"
  }
]
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Numeric ID of the sports metadata entry. |
| `name` | Display name of the league, such as `UFL` or `Abu Dhabi T10 League`. |
| `sport` | Short lowercase code for the league, such as `ufl` or `lmp`. It also appears in the icon file name. |
| `image` | URL of the league icon image. |
| `primaryTagId` | Numeric ID of the main tag for this league. |
| `tags` | Comma-separated string of tag IDs linked to this league. The first values `1` and `100639` appear in all three sample entries. |
| `series` | ID of the series for this league. It is returned as a string. |
| `ordering` | Value `home` or `away` in the sample. The response does not explain what it controls. |
| `resolution` | URL of a web page for the league. The sample entries point to the league's own site. |
| `createdAt` | ISO 8601 UTC timestamp for when the entry was created. |

### Notes

- This API takes no parameters and returns the full list in one response, with no pagination.
- `tags` is one string, not a list. Split it on commas to get the individual tag IDs.
- Use a `primaryTagId` or `tags` value with [Polymarket List events](/apis/polymarket/events) to find events for a league.
- Use [Polymarket Get valid sports market types](/apis/polymarket/sports-market-types) to see which sports market types exist, and [Polymarket Get series by id](/apis/polymarket/series-by-id) to look up a `series` value.

### Pricing

$0.00044 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/polymarket/sports.json`](../../../catalog/models/polymarket/sports.json) · Store page: https://www.sandbase.ai/model/polymarket/sports
