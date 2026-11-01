# Twitter User Published Posts

`twitter/user-posts` · api · Twitter

Get posts published by an X (Twitter) user identified by Rest ID, with cursor pagination. Use it to browse a known account's timeline or continue through its public post history.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/user-posts", "restId": "44196397"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/user-posts', {'restId': '44196397'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/user-posts", {
  "restId": "44196397"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/user-posts", sandbase.Params{
	"restId": "44196397",
})
```

Same call via the path form: `POST /v1/api/twitter/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor for navigating through long timelines.  |
| `restId` | string | yes | The unique numeric identifier (Rest ID) for the X user.  |

## Details

Get posts published by an X (Twitter) user identified by Rest ID, with cursor pagination. Use it to browse a known account's timeline or continue through its public post history.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"restId": "44196397"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `restId` | string | Yes | The unique numeric identifier (Rest ID) for the X user. |
| `cursor` | string | No | Pagination cursor for navigating through long timelines. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/twitter/user-posts.json`](../../../catalog/models/twitter/user-posts.json) · Store page: https://www.sandbase.ai/model/twitter/user-posts
