# X (Twitter) Community Moderators API: pricing, parameters and code examples

`twitter/community-moderators` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0036 per call · **Modes:** sync

Moderators of an X Community by community ID, with profile details and cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0036**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/community-moderators", "community_id": "1493446837214187523"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/community-moderators', {'community_id': '1493446837214187523'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/community-moderators", {
  "community_id": "1493446837214187523"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/community-moderators", sandbase.Params{
	"community_id": "1493446837214187523",
})
```

Same call via the path form: `POST /v1/api/twitter/community-moderators` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor for pagination  |
| `community_id` | string | yes | ID of the community  |

## Details

Moderators of an X Community by community ID, with profile details and cursor pagination.

The result is returned in `outputs[0].data` as the official X (Twitter) API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/community-moderators" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"community_id": "1493446837214187523"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `community_id` | string | Yes | ID of the community |
| `cursor` | string | No | Cursor for pagination |

### Pricing

Billed at the actual cost of each call, about $0.0036 for a typical request; the cost grows with the number of rows returned. Searches with no results are billed at their actual cost. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/community-moderators.json`](../../../catalog/models/twitter/community-moderators.json) · Store page: https://www.sandbase.ai/model/twitter/community-moderators
