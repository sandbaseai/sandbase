# X / Twitter Followers

`twitter/followers` · api · X (Twitter)

Fetch the follower list of any public X (Twitter) account by username with cursor pagination. Limit is a per-page maximum and a native page holds up to 200 accounts; follow the response's nextCursor for more.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00045**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/followers", "username": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/followers', {'username': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/followers", {
  "username": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/followers", sandbase.Params{
	"username": "nasa",
})
```

Same call via the path form: `POST /v1/api/twitter/followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Accepted but does not change the page: every call returns one full native page of followers (up to 200, depending on the source), never trimmed, so follow nextCursor to continue exactly where this response ended. default `200`; range 1–100000 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of followers.  |
| `username` | string | yes | The X (Twitter) username to fetch followers for, without the @ prefix (e.g. elonmusk).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `bio`, and it is served only by a source that returns every one of…  |

## Details

Fetch the follower list of any public X (Twitter) account by username with cursor pagination. Limit is a per-page maximum and a native page holds up to 200 accounts; follow the response's nextCursor for more.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 200, "username": "nasa"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | The X (Twitter) username to fetch followers for, without the @ prefix (e.g. elonmusk). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of followers. |
| `limit` | integer | No | Accepted but does not change the page: every call returns one full native page of followers (up to 200, depending on the source), never trimmed, so follow nextCursor to continue exactly where this response ended. Default |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `bio`, and it is served only by a source that returns every one of the |

### Pricing

Billed at the actual cost of each call, usually $0.00045 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/twitter/followers.json`](../../../catalog/models/twitter/followers.json) · Store page: https://www.sandbase.ai/model/twitter/followers
