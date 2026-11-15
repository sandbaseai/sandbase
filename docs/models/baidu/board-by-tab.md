# Baidu Board By Tab API: pricing, parameters and code examples

`baidu/board-by-tab` · data API · Baidu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

General-purpose endpoint to retrieve any board tab (realtime, novel, movie, teleplay) with optional tag filtering. Returns ranked items and available filter tags.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/board-by-tab", "tab": "realtime"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('baidu/board-by-tab', {'tab': 'realtime'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("baidu/board-by-tab", {
  "tab": "realtime"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "baidu/board-by-tab", sandbase.Params{
	"tab": "realtime",
})
```

Same call via the path form: `POST /v1/api/baidu/board-by-tab` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tab` | string | yes | Board tab name: realtime, novel, movie, teleplay. one of: `realtime`, `novel`, `movie`, `teleplay` |
| `tag` | string |  | Optional category/genre filter tag. Available tags are returned in the tags_available field of any board response.  |

## Details

General-purpose endpoint to retrieve any board tab (realtime, novel, movie, teleplay) with optional tag filtering. Returns ranked items and available filter tags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "baidu/board-by-tab", "tab": "realtime", "tag": "xuanhuan"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tab` | string | Yes | Board tab name: realtime, novel, movie, teleplay. One of: `realtime`, `novel`, `movie`, `teleplay`. |
| `tag` | string | No | Optional category/genre filter tag. Available tags are returned in the tags_available field of any board response. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/baidu/board-by-tab.json`](../../../catalog/models/baidu/board-by-tab.json) · Store page: https://www.sandbase.ai/model/baidu/board-by-tab
