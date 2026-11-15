# Temu Continue Search Session API: pricing, parameters and code examples

`temu/continue-search-session` · data API · Temu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Continue a paginated search session started by start_search_session.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/continue-search-session", "pagination_token": "<pagination_token>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('temu/continue-search-session', {'pagination_token': '<pagination_token>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("temu/continue-search-session", {
  "pagination_token": "<pagination_token>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "temu/continue-search-session", sandbase.Params{
	"pagination_token": "<pagination_token>",
})
```

Same call via the path form: `POST /v1/api/temu/continue-search-session` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results to return per page (max 40). default `40` |
| `pagination_token` | string | yes | Opaque signed token from start_search_session or a previous continue_search_session response (the session_id field).  |

## Details

Continue a paginated search session started by start_search_session.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "temu/continue-search-session", "limit": 40}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pagination_token` | string | Yes | Opaque signed token from start_search_session or a previous continue_search_session response (the session_id field). |
| `limit` | integer | No | Number of results to return per page (max 40). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/temu/continue-search-session.json`](../../../catalog/models/temu/continue-search-session.json) · Store page: https://www.sandbase.ai/model/temu/continue-search-session
