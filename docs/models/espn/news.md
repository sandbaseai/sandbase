# ESPN News API: pricing, parameters and code examples

`espn/news` · data API · ESPN · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get latest news articles and headlines for a specific league. Returns articles with full metadata including categories, images, and links.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "espn/news", "league": "nba"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('espn/news', {'league': 'nba'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("espn/news", {
  "league": "nba"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "espn/news", sandbase.Params{
	"league": "nba",
})
```

Same call via the path form: `POST /v1/api/espn/news` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of articles to return. default `25` |
| `league` | string | yes | League identifier. one of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1` … |

## Details

Get latest news articles and headlines for a specific league. Returns articles with full metadata including categories, images, and links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "espn/news", "limit": 5, "league": "nba"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `league` | string | Yes | League identifier. One of: `nba`, `nfl`, `mlb`, `nhl`, `wnba`, `college-football`, `mens-college-basketball`, `womens-college-basketball`, `college-baseball`, `college-softball`, `eng.1`, `esp.1`. |
| `limit` | integer | No | Number of articles to return. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/espn/news.json`](../../../catalog/models/espn/news.json) · Store page: https://www.sandbase.ai/model/espn/news
