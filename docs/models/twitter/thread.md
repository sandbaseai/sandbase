# X / Twitter Tweet Thread

`twitter/thread` · api · X (Twitter)

Resolve the linear self-thread containing an X (Twitter) post, from its root through the author's linked continuations. This excludes replies from other users.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00269**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/thread", "url": "https://x.com/SpaceX/status/1732824684683784516"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/thread', {'url': 'https://x.com/SpaceX/status/1732824684683784516'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/thread", {
  "url": "https://x.com/SpaceX/status/1732824684683784516"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/thread", sandbase.Params{
	"url": "https://x.com/SpaceX/status/1732824684683784516",
})
```

Same call via the path form: `POST /v1/api/twitter/thread` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Canonical x.com or twitter.com status URL with a numeric tweet ID. Any tweet in the self-thread can be supplied; the provider resolves the thread root.  |

## Details

Resolve the linear self-thread containing an X (Twitter) post, from its root through the author's linked continuations. This excludes replies from other users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/thread" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/SpaceX/status/1732824684683784516"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Canonical x.com or twitter.com status URL with a numeric tweet ID. Any tweet in the self-thread can be supplied; the provider resolves the thread root. |

### Pricing

Billed at the actual cost of each call, usually $0.00269 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/twitter/thread.json`](../../../catalog/models/twitter/thread.json) · Store page: https://www.sandbase.ai/model/twitter/thread
