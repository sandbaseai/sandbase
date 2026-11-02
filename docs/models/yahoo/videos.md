# Yahoo Videos Search API: pricing, parameters and code examples

`yahoo/videos` · data API · Yahoo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Yahoo Videos results for a keyword: titles, thumbnails, durations and source sites.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo/videos", "p": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo/videos', {'p': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo/videos", {
  "p": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo/videos", sandbase.Params{
	"p": "coffee",
})
```

Same call via the path form: `POST /v1/api/yahoo/videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `p` | string | yes | p  |

## Details

Yahoo Videos results for a keyword: titles, thumbnails, durations and source sites.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo/videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"p": "coffee"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `p` | string | Yes | p |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo/videos.json`](../../../catalog/models/yahoo/videos.json) · Store page: https://www.sandbase.ai/model/yahoo/videos
