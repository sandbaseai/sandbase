# Google Maps Contributor Reviews API: pricing, parameters and code examples

`google-maps/contributor-reviews` · data API · Google Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get up to 200 reviews written by one Google Maps contributor.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/contributor-reviews", "contributor_id": "<contributor_id>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-maps/contributor-reviews', {'contributor_id': '<contributor_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-maps/contributor-reviews", {
  "contributor_id": "<contributor_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-maps/contributor-reviews", sandbase.Params{
	"contributor_id": "<contributor_id>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/google-maps/contributor-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code. Default 'us'.  |
| `hl` | string |  | Review and interface language, such as 'en', 'en-US', or 'fr'. Default 'en'.  |
| `limit` | integer |  | Number of reviews to return, 1-200. Default 200. range 1–200 |
| `contributor_id` | string | yes | 10 to 32 digit ID from a Google Maps contributor URL.  |

## Details

Get up to 200 reviews written by one Google Maps contributor.

---
Machine-readable: [`catalog/models/google-maps/contributor-reviews.json`](../../../catalog/models/google-maps/contributor-reviews.json) · Store page: https://www.sandbase.ai/model/google-maps/contributor-reviews
