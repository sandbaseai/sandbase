# Twitter User about profile API: pricing, parameters and code examples

`twitter/web/user-about` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get user about profile on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-about", "screen_name": "elonmusk"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-about', {'screen_name': 'elonmusk'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-about", {
  "screen_name": "elonmusk"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-about", sandbase.Params{
	"screen_name": "elonmusk",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-about` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `screen_name` | string | yes | Screen Name  |

## Details

Get user about profile on Twitter. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-about" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "elonmusk"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `screen_name` | string | Yes | Screen Name |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/twitter/web/user-about.json`](../../../../catalog/models/twitter/web/user-about.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-about
