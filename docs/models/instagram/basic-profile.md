# Instagram Basic Profile

`instagram/basic-profile` · api · Instagram

Fetch an Instagram account's core public profile fields (followers, posts, bio, verification) by user id.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/basic-profile", "userId": "314216"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/basic-profile', {'userId': '314216'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/basic-profile", {
  "userId": "314216"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/basic-profile", sandbase.Params{
	"userId": "314216",
})
```

Same call via the path form: `POST /v1/api/instagram/basic-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | Instagram numeric user id (the account's internal all-digits id, e.g. 314216), NOT the @handle or profile URL. Passing a handle here returns no profile.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `posts`, and it is served only by a source that returns every one of…  |

## Details

Fetch an Instagram account's core public profile fields (followers, posts, bio, verification) by user id.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/basic-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "314216"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | Instagram numeric user id (the account's internal all-digits id, e.g. 314216), NOT the @handle or profile URL. Passing a handle here returns no profile. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `posts`, and it is served only by a source that returns every one of t |

### Pricing

Billed at the actual cost of each call, usually $0.001 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/basic-profile.json`](../../../catalog/models/instagram/basic-profile.json) · Store page: https://www.sandbase.ai/model/instagram/basic-profile
