# Facebook Get Profile Posts API: pricing, parameters and code examples

`facebook/profile-posts` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.027778 per call · **Modes:** sync

Get public posts for a Facebook profile ID with cursor pagination. Use it to browse a known profile's public posting history or continue through subsequent post pages.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/profile-posts", "profileId": "4"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/profile-posts', {'profileId': '4'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/profile-posts", {
  "profileId": "4"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/profile-posts", sandbase.Params{
	"profileId": "4",
})
```

Same call via the path form: `POST /v1/api/facebook/profile-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor for fetching the next set of results.  |
| `profileId` | string | yes | The unique Facebook profile ID.  |

## Details

Get public posts for a Facebook profile ID with cursor pagination. Use it to browse a known profile's public posting history or continue through subsequent post pages.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/profile-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"profileId": "4"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `profileId` | string | Yes | The unique Facebook profile ID. |
| `cursor` | string | No | Pagination cursor for fetching the next set of results. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/facebook/profile-posts.json`](../../../catalog/models/facebook/profile-posts.json) · Store page: https://www.sandbase.ai/model/facebook/profile-posts
