# X (Twitter) Twitter Community

`twitter/community` · api · X (Twitter)

Fetch a Twitter/X community's public details (name, description, member count, join policy) by URL.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/community", "url": "https://x.com/i/communities/1926186499399139650"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/community', {'url': 'https://x.com/i/communities/1926186499399139650'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/community", {
  "url": "https://x.com/i/communities/1926186499399139650"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/community", sandbase.Params{
	"url": "https://x.com/i/communities/1926186499399139650",
})
```

Same call via the path form: `POST /v1/api/twitter/community` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Community URL (e.g. https://x.com/i/communities/1926186499399139650).  |

## Details

Fetch a Twitter/X community's public details (name, description, member count, join policy) by URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/community" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://x.com/i/communities/1926186499399139650"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Community URL (e.g. https://x.com/i/communities/1926186499399139650). |

### Pricing

Billed at the actual cost of each call, usually $0.0001 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/twitter/community.json`](../../../catalog/models/twitter/community.json) · Store page: https://www.sandbase.ai/model/twitter/community
