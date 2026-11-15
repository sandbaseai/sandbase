# Baidu Novel Rankings By Genre API: pricing, parameters and code examples

`baidu/novel-rankings-by-genre` · data API · Baidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetch novel rankings filtered by genre type. Returns novels matching the specified genre along with available tags. Equivalent to get_board_by_tab with tab=novel and the genre as tag.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/novel-rankings-by-genre", "genre": "xuanhuan"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('baidu/novel-rankings-by-genre', {'genre': 'xuanhuan'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("baidu/novel-rankings-by-genre", {
  "genre": "xuanhuan"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "baidu/novel-rankings-by-genre", sandbase.Params{
	"genre": "xuanhuan",
})
```

Same call via the path form: `POST /v1/api/baidu/novel-rankings-by-genre` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `genre` | string | yes | Novel genre filter. Available genres can be discovered from the tags_available field of get_novel_rankings.  |

## Details

Fetch novel rankings filtered by genre type. Returns novels matching the specified genre along with available tags. Equivalent to get_board_by_tab with tab=novel and the genre as tag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "baidu/novel-rankings-by-genre", "genre": "xuanhuan"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `genre` | string | Yes | Novel genre filter. Available genres can be discovered from the tags_available field of get_novel_rankings. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/baidu/novel-rankings-by-genre.json`](../../../catalog/models/baidu/novel-rankings-by-genre.json) · Store page: https://www.sandbase.ai/model/baidu/novel-rankings-by-genre
