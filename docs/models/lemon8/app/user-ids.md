# Lemon8 User IDs by Share Links API: pricing, parameters and code examples

`lemon8/app/user-ids` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves Lemon8 user identifiers in batch from shared profile links. Accepts an array of up to 10 share links per request and returns the corresponding user IDs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/user-ids", "body": ["<body>"]}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/user-ids', {'body': ['<body>']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/user-ids", {
  "body": [
    "<body>"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/user-ids", sandbase.Params{
	"body": []any{"<body>"},
})
```

Same call via the path form: `POST /v1/api/lemon8/app/user-ids` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `body` | array | yes | Share links list  |

## Details

This endpoint resolves user IDs from an array of Lemon8 share links provided in `body`. It allows looking up up to 10 profile links in a single request.

### Use cases

- Resolve account IDs from copied Lemon8 profile URLs.
- Batch process multiple Lemon8 share links in a single query.
- Map external share links to internal user identifiers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/user-ids" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"body": "<body>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `body` | array | Yes | Share links list |

### Notes

- Accepts up to 10 share links at a time in the `body` parameter array.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/model/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/model/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/model/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/user-ids.json`](../../../../catalog/models/lemon8/app/user-ids.json) · Store page: https://www.sandbase.ai/model/lemon8/app/user-ids
