# Twitter Search communities API: pricing, parameters and code examples

`twitter/web/search-communities` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search communities on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/search-communities", "keyword": "superman"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/search-communities', {'keyword': 'superman'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/search-communities", {
  "keyword": "superman"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/search-communities", sandbase.Params{
	"keyword": "superman",
})
```

Same call via the path form: `POST /v1/api/twitter/web/search-communities` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor  |
| `keyword` | string | yes | Search Keyword  |

## Details

Search communities on Twitter. Returns the platform data as structured JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/search-communities" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "superman"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keyword |
| `cursor` | string | No | Cursor |

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

---
Machine-readable: [`catalog/models/twitter/web/search-communities.json`](../../../../catalog/models/twitter/web/search-communities.json) · Store page: https://www.sandbase.ai/model/twitter/web/search-communities
