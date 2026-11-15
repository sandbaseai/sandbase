# Temu Continue Batch Store Session API: pricing, parameters and code examples

`temu/continue-batch-store-session` · data API · Temu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Continue paginated store sessions started by batch_get_stores. Accepts an array of opaque session tokens (from previous next_session_token fields), fetches the next page for each store, and returns updated tokens. Handles list_id expiration with automatic recovery.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/continue-batch-store-session", "session_tokens": "[\"eyJ2IjoxLCJ0Ijoic3RvcmUiLCJtaWQiOiIyNjEwMTI3IiwibCI6ImVuIiwibGlkIjoiYWJjMTIzIiwibyI6MTAsImxpbSI6MTB9.placeholder_sig\"]"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('temu/continue-batch-store-session', {'session_tokens': '["eyJ2IjoxLCJ0Ijoic3RvcmUiLCJtaWQiOiIyNjEwMTI3IiwibCI6ImVuIiwibGlkIjoiYWJjMTIzIiwibyI6MTAsImxpbSI6MTB9.placeholder_sig"]'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("temu/continue-batch-store-session", {
  "session_tokens": "[\"eyJ2IjoxLCJ0Ijoic3RvcmUiLCJtaWQiOiIyNjEwMTI3IiwibCI6ImVuIiwibGlkIjoiYWJjMTIzIiwibyI6MTAsImxpbSI6MTB9.placeholder_sig\"]"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "temu/continue-batch-store-session", sandbase.Params{
	"session_tokens": "[\"eyJ2IjoxLCJ0Ijoic3RvcmUiLCJtaWQiOiIyNjEwMTI3IiwibCI6ImVuIiwibGlkIjoiYWJjMTIzIiwibyI6MTAsImxpbSI6MTB9.placeholder_sig\"]",
})
```

Same call via the path form: `POST /v1/api/temu/continue-batch-store-session` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Override the page size stored in the token (max 999).  |
| `include_dto` | boolean |  | If true, include the flat normalized DTO per store. default `true` |
| `include_raw` | boolean |  | If true, include the raw API response data per store. default `true` |
| `session_tokens` | string | yes | JSON array of opaque session token strings from batch_get_stores or a previous continue_batch_store_session response (up to 20).  |

## Details

Continue paginated store sessions started by batch_get_stores. Accepts an array of opaque session tokens (from previous next_session_token fields), fetches the next page for each store, and returns updated tokens. Handles list_id expiration with automatic recovery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "temu/continue-batch-store-session", "limit": 40, "include_dto": true, "include_raw": true, "session_tokens": "[\"eyJ2IjoxLCJ0Ijoic3RvcmUiLCJtaWQiOiIyNjEwMTI3IiwibCI6ImVuIiwibGlkIjoiYWJjMTIzIiwibyI6MTAsImxpbSI6MTB9.placeholder_sig\"]"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `session_tokens` | string | Yes | JSON array of opaque session token strings from batch_get_stores or a previous continue_batch_store_session response (up to 20). |
| `include_dto` | boolean | No | If true, include the flat normalized DTO per store. |
| `include_raw` | boolean | No | If true, include the raw API response data per store. |
| `limit` | integer | No | Override the page size stored in the token (max 999). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/temu/continue-batch-store-session.json`](../../../catalog/models/temu/continue-batch-store-session.json) · Store page: https://www.sandbase.ai/model/temu/continue-batch-store-session
