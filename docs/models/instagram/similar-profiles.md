# Instagram Similar Profiles

`instagram/similar-profiles` · api · Instagram

List the accounts Instagram recommends as similar to a public profile, with each account's handle, display name, verified flag and avatar.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00175**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/similar-profiles", "handle": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/similar-profiles', {'handle': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/similar-profiles", {
  "handle": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/similar-profiles", sandbase.Params{
	"handle": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/similar-profiles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Instagram username without the leading @.  |

## Details

List the accounts Instagram recommends as similar to a public profile, with each account's handle, display name, verified flag and avatar.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/similar-profiles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "nasa"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Instagram username without the leading @. |

### Pricing

Billed at the actual cost of each call, usually $0.00175 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/similar-profiles.json`](../../../catalog/models/instagram/similar-profiles.json) · Store page: https://www.sandbase.ai/model/instagram/similar-profiles
