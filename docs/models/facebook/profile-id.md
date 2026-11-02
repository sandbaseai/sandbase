# Facebook Profile ID API: pricing, parameters and code examples

`facebook/profile-id` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Resolve the numeric Facebook profile ID behind a profile path such as "zuck", for use with endpoints that need a profile ID.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/profile-id", "url": "zuck"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/profile-id', {'url': 'zuck'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/profile-id", {
  "url": "zuck"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/profile-id", sandbase.Params{
	"url": "zuck",
})
```

Same call via the path form: `POST /v1/api/facebook/profile-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The path portion of the Facebook profile URL, such as /<profile-path>. Do not include the scheme or host.  |

## Details

Resolve the numeric Facebook profile ID behind a profile path such as "zuck", for use with endpoints that need a profile ID.

The result is returned in `outputs[0].data` in the platform's original structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/profile-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "zuck"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The path portion of the Facebook profile URL, such as /<profile-path>. Do not include the scheme or host. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/facebook/profile-id.json`](../../../catalog/models/facebook/profile-id.json) · Store page: https://www.sandbase.ai/model/facebook/profile-id
