# X (Twitter) Verified Followers API: pricing, parameters and code examples

`twitter/verified-followers` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.006 per call · **Modes:** sync

Verified (blue check) followers of a user by numeric user ID, with profile details and cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/verified-followers", "user_id": "11348282"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/verified-followers', {'user_id': '11348282'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/verified-followers", {
  "user_id": "11348282"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/verified-followers", sandbase.Params{
	"user_id": "11348282",
})
```

Same call via the path form: `POST /v1/api/twitter/verified-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | The cursor to paginate through the results. First page is empty.  |
| `user_id` | string | yes | User ID of the user.  |

## Details

Verified (blue check) followers of a user by numeric user ID, with profile details and cursor pagination.

The result is returned in `outputs[0].data` as the official X (Twitter) API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/verified-followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "11348282"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | The cursor to paginate through the results. First page is empty. |
| `user_id` | string | Yes | User ID of the user. |

### Pricing

Billed at the actual cost of each call, about $0.006 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/verified-followers.json`](../../../catalog/models/twitter/verified-followers.json) · Store page: https://www.sandbase.ai/model/twitter/verified-followers
