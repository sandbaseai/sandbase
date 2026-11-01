# Polymarket List teams

`polymarket/teams` · api · Polymarket

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

List teams from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/teams" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 2}'
```

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

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/teams.json`](../../../catalog/models/polymarket/teams.json) · Store page: https://www.sandbase.ai/model/polymarket/teams
