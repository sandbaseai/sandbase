# ESPN Athlete Gamelog API: pricing, parameters and code examples

`espn/athlete-gamelog` · data API · ESPN · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.06 per call · **Modes:** sync

Get game-by-game stats for an athlete with monthly breakdowns, totals, and averages. Stats labels are sport-specific. Each game includes opponent, result, score, and full stat line.

## Pricing

- **$0.06 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "espn/athlete-gamelog", "league": "nba", "athlete_id": "1966"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('espn/athlete-gamelog', {'league': 'nba', 'athlete_id': '1966'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("espn/athlete-gamelog", {
  "league": "nba",
  "athlete_id": "1966"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "espn/athlete-gamelog", sandbase.Params{
	"league": "nba",
	"athlete_id": "1966",
})
```

Same call via the path form: `POST /v1/api/espn/athlete-gamelog` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `league` | string | yes | League identifier. one of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1` … |
| `season` | string |  | Season year (e.g., 2026). When omitted, returns current season gamelog.  |
| `athlete_id` | string | yes | Athlete ID obtained from search endpoint results[*].id or get_team_roster endpoint athletes[*].id  |

## Details

Get game-by-game stats for an athlete with monthly breakdowns, totals, and averages. Stats labels are sport-specific. Each game includes opponent, result, score, and full stat line.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "espn/athlete-gamelog", "athlete_id": "1966", "league": "nba"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `athlete_id` | string | Yes | Athlete ID obtained from search endpoint results[*].id or get_team_roster endpoint athletes[*].id |
| `league` | string | Yes | League identifier. One of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1`. |
| `season` | string | No | Season year (e.g., 2026). When omitted, returns current season gamelog. |

### Pricing

Flat $0.06 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/espn/athlete-gamelog.json`](../../../catalog/models/espn/athlete-gamelog.json) · Store page: https://www.sandbase.ai/model/espn/athlete-gamelog
