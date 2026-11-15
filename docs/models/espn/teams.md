# ESPN Teams API: pricing, parameters and code examples

`espn/teams` · data API · ESPN · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get all teams for a given league with IDs, names, logos, and links. Returns a complete roster of teams participating in the specified league.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "espn/teams", "league": "nba"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('espn/teams', {'league': 'nba'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("espn/teams", {
  "league": "nba"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "espn/teams", sandbase.Params{
	"league": "nba",
})
```

Same call via the path form: `POST /v1/api/espn/teams` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `league` | string | yes | League identifier. one of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1` … |

## Details

Get all teams for a given league with IDs, names, logos, and links. Returns a complete roster of teams participating in the specified league.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "espn/teams", "league": "nba"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `league` | string | Yes | League identifier. One of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1`. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/espn/teams.json`](../../../catalog/models/espn/teams.json) · Store page: https://www.sandbase.ai/model/espn/teams
