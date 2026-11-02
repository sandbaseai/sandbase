# Instagram Post Likers API: pricing, parameters and code examples

`instagram/post-likers` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0024 per call · **Modes:** sync

List the accounts that liked a public Instagram post, one page of likers per call, with each liker's handle, display name, verified flag and avatar.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0024**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/post-likers", "url": "https://www.instagram.com/reel/DWzrfE2kaY8/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/post-likers', {'url': 'https://www.instagram.com/reel/DWzrfE2kaY8/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/post-likers", {
  "url": "https://www.instagram.com/reel/DWzrfE2kaY8/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/post-likers", sandbase.Params{
	"url": "https://www.instagram.com/reel/DWzrfE2kaY8/",
})
```

Same call via the path form: `POST /v1/api/instagram/post-likers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Canonical URL of a public Instagram post or reel.  |

## Details

List the accounts that liked a public Instagram post, one page of likers per call, with each liker's handle, display name, verified flag and avatar.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/post-likers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/reel/DWzrfE2kaY8/"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Canonical URL of a public Instagram post or reel. |

### Pricing

Billed at the actual cost of each call, usually $0.0024 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/post-likers.json`](../../../catalog/models/instagram/post-likers.json) · Store page: https://www.sandbase.ai/model/instagram/post-likers
