# Reddit Profile

`reddit/profile` · api · Reddit

Fetch a Reddit user's public profile (karma split, post and comment counts, bio, avatar, account age) by username.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/profile", "username": "spez"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/profile', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/profile", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/profile", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Reddit username, without the u/ prefix. Example: "spez".  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `verified`, and it is served only by a source that returns every one…  |

## Details

Fetch a Reddit user's public profile (karma split, post and comment counts, bio, avatar, account age) by username.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username, without the u/ prefix. Example: "spez". |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `verified`, and it is served only by a source that returns every one o |

### Pricing

Billed at the actual cost of each call, usually $0.0008 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/reddit/profile.json`](../../../catalog/models/reddit/profile.json) · Store page: https://www.sandbase.ai/model/reddit/profile
