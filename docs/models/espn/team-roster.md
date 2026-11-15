# ESPN Team Roster API: pricing, parameters and code examples

`espn/team-roster` · data API · ESPN · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get full roster for a team including player profiles, injuries, and contract details. Each athlete includes biographical info, position, physical attributes, and current status.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "espn/team-roster", "league": "nba", "team_id": "1"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('espn/team-roster', {'league': 'nba', 'team_id': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("espn/team-roster", {
  "league": "nba",
  "team_id": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "espn/team-roster", sandbase.Params{
	"league": "nba",
	"team_id": "1",
})
```

Same call via the path form: `POST /v1/api/espn/team-roster` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `league` | string | yes | League identifier. one of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1` … |
| `team_id` | string | yes | Team ID obtained from get_teams endpoint teams[*].id or search endpoint results[*].id  |

## Details

Get full roster for a team including player profiles, injuries, and contract details. Each athlete includes biographical info, position, physical attributes, and current status.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "espn/team-roster", "team_id": "1", "league": "nba"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `league` | string | Yes | League identifier. One of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1`. |
| `team_id` | string | Yes | Team ID obtained from get_teams endpoint teams[*].id or search endpoint results[*].id |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/espn/team-roster.json`](../../../catalog/models/espn/team-roster.json) · Store page: https://www.sandbase.ai/model/espn/team-roster
