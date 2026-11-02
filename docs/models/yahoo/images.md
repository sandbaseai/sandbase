# Yahoo Images Search API: pricing, parameters and code examples

`yahoo/images` · data API · Yahoo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Yahoo Images results for a keyword: image URLs, thumbnails, sizes and source pages.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo/images", "p": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo/images', {'p': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo/images", {
  "p": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo/images", sandbase.Params{
	"p": "coffee",
})
```

Same call via the path form: `POST /v1/api/yahoo/images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `p` | string | yes | p  |

## Details

Yahoo Images results for a keyword: image URLs, thumbnails, sizes and source pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo/images" \
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
Machine-readable: [`catalog/models/yahoo/images.json`](../../../catalog/models/yahoo/images.json) · Store page: https://www.sandbase.ai/model/yahoo/images
