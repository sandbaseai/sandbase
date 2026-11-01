# Polymarket Get event by slug

`polymarket/events-slug` · api · Polymarket

Get event by slug from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/events-slug", "slug": "nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/events-slug', {'slug': 'nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/events-slug", {
  "slug": "nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/events-slug", sandbase.Params{
	"slug": "nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup",
})
```

Same call via the path form: `POST /v1/api/polymarket/events-slug` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | slug  |
| `include_chat` | boolean |  | include_chat  |
| `include_template` | boolean |  | include_template  |

## Details

Get event by slug from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/events-slug" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "nba-will-the-mavericks-beat-the-grizzlies-by-more-than-5pt5-points-in-their-december-4-matchup"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | slug |
| `include_chat` | boolean | No | include_chat |
| `include_template` | boolean | No | include_template |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/events-slug.json`](../../../catalog/models/polymarket/events-slug.json) · Store page: https://www.sandbase.ai/model/polymarket/events-slug
