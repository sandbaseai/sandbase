# Instagram User Highlights

`instagram/user-highlights` · api · Instagram

List an Instagram account's story highlight reels by handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/user-highlights", "handle": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/user-highlights', {'handle': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/user-highlights", {
  "handle": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/user-highlights", sandbase.Params{
	"handle": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/user-highlights` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Instagram username without the leading @.  |
| `userId` | string |  | Instagram numeric user id (optional, faster than handle).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `mediaCount`, and it is served only by a source that returns every…  |

## Details

List an Instagram account's story highlight reels by handle.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/user-highlights" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "nasa"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Instagram username without the leading @. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `mediaCount`, and it is served only by a source that returns every one |
| `userId` | string | No | Instagram numeric user id (optional, faster than handle). |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/user-highlights.json`](../../../catalog/models/instagram/user-highlights.json) · Store page: https://www.sandbase.ai/model/instagram/user-highlights
