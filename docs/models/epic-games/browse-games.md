# Epic Games Store Browse Games API: pricing, parameters and code examples

`epic-games/browse-games` · data API · Epic Games Store · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Browses the Epic Games Store catalog with optional filtering and sorting. Returns paginated results with total count. Uses offset-based pagination via start parameter.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "epic-games/browse-games"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('epic-games/browse-games', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("epic-games/browse-games", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "epic-games/browse-games", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/epic-games/browse-games` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag` | string |  | Genre or tag filter identifier used by the Epic Games Store API. Omitting returns all games.  |
| `count` | integer |  | Number of items to return per page. default `40` |
| `start` | integer |  | Pagination offset (0-based). default `0` |
| `sort_by` | string |  | Sort field. default `"releaseDate"` |
| `category` | string |  | Category filter path. Common values: 'games/edition/base', 'Game', 'Apps'. one of: `games/edition/base`, `Game`, `Apps`; default `"games/edition/base"` |
| `sort_dir` | string |  | Sort direction. default `"DESC"` |

## Details

Browses the Epic Games Store catalog with optional filtering and sorting. Returns paginated results with total count. Uses offset-based pagination via start parameter.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "epic-games/browse-games", "tag": "", "count": 5, "start": 0, "sort_by": "releaseDate", "category": "games/edition/base", "sort_dir": "ASC"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Category filter path. Common values: 'games/edition/base', 'Game', 'Apps'. One of: `games/edition/base`, `Game`, `Apps`. |
| `count` | integer | No | Number of items to return per page. |
| `sort_by` | string | No | Sort field. |
| `sort_dir` | string | No | Sort direction. |
| `start` | integer | No | Pagination offset (0-based). |
| `tag` | string | No | Genre or tag filter identifier used by the Epic Games Store API. Omitting returns all games. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/epic-games/browse-games.json`](../../../catalog/models/epic-games/browse-games.json) · Store page: https://www.sandbase.ai/model/epic-games/browse-games
