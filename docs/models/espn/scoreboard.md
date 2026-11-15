# ESPN Scoreboard API: pricing, parameters and code examples

`espn/scoreboard` · data API · ESPN · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get live scores, final results, and upcoming fixtures for any supported league.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "espn/scoreboard", "league": "nba"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('espn/scoreboard', {'league': 'nba'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("espn/scoreboard", {
  "league": "nba"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "espn/scoreboard", sandbase.Params{
	"league": "nba",
})
```

Same call via the path form: `POST /v1/api/espn/scoreboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `dates` | string |  | Date filter in YYYYMMDD format (e.g., 20260424). When omitted, returns current day's events.  |
| `limit` | integer |  | Maximum number of events to return.  |
| `league` | string | yes | League identifier. one of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1` … |
| `matchday` | integer |  | Matchday/round number (e.g., 1, 2, 38). Filters events to a specific matchday. Primarily useful for soccer leagues that organize fixtures by round. When omitted, no matchday filter is applied.  |

## Details

Get live scores, final results, and upcoming fixtures for any supported league.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "espn/scoreboard", "dates": "20261115", "limit": 10, "league": "nba"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `league` | string | Yes | League identifier. One of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1`. |
| `dates` | string | No | Date filter in YYYYMMDD format (e.g., 20260424). When omitted, returns current day's events. |
| `limit` | integer | No | Maximum number of events to return. |
| `matchday` | integer | No | Matchday/round number (e.g., 1, 2, 38). Filters events to a specific matchday. Primarily useful for soccer leagues that organize fixtures by round. When omitted, no matchday filter is applied. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/espn/scoreboard.json`](../../../catalog/models/espn/scoreboard.json) · Store page: https://www.sandbase.ai/model/espn/scoreboard
