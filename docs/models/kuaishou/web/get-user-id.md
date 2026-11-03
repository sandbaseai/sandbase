# Kuaishou User ID Lookup API: pricing, parameters and code examples

`kuaishou/web/get-user-id` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Resolves a Kuaishou user ID from a provided user share link. Useful for extracting internal profile identifiers from public sharing URLs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/get-user-id", "share_link": "https://c.kuaishou.com/fw/user/3xcuu5habgc8z29"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/get-user-id', {'share_link': 'https://c.kuaishou.com/fw/user/3xcuu5habgc8z29'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/get-user-id", {
  "share_link": "https://c.kuaishou.com/fw/user/3xcuu5habgc8z29"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/get-user-id", sandbase.Params{
	"share_link": "https://c.kuaishou.com/fw/user/3xcuu5habgc8z29",
})
```

Same call via the path form: `POST /v1/api/kuaishou/web/get-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `share_link` | string | yes | 用户分享链接/User Share Link  |

## Details

Returns the Kuaishou user ID found in a user share link. It needs one input, `share_link`, which is a Kuaishou user share URL such as `https://c.kuaishou.com/fw/user/3xcuu5habgc8z29`.

### Use cases

- Turn a copied Kuaishou profile share link into a user ID you can store.
- Normalize a list of user share URLs into IDs before you run profile lookups.
- Match a creator's shared link to the same creator in your own database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/get-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"share_link": "https://c.kuaishou.com/fw/user/3xcuu5habgc8z29"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `share_link` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "user_id": "3xcuu5habgc8z29"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_id` | The Kuaishou user ID, returned as a string. |
| `user_id` | In the sample, the value equals the last segment of the share link path (`/fw/user/3xcuu5habgc8z29`). |
| `user_id` | The only field in the response. Pass it to other Kuaishou APIs that take a user identifier. |

### Notes

- Pass the full user share URL in `share_link`. The sample uses the form `https://c.kuaishou.com/fw/user/<id>`.
- The response holds only `user_id`. Use it as input to a profile API such as [Kuaishou Web User Info](/apis/kuaishou/web/user-info) or [Kuaishou Single User Data (V2)](/apis/kuaishou/app/one-user-v2).
- To list a creator's posts after the lookup, try [Kuaishou User Video List (V2)](/apis/kuaishou/app/user-post-v2).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.
- [Kuaishou Web Hot List (V2)](/apis/kuaishou/web/hot-list-v2): Returns current trending search rankings and hot topics on Kuaishou web.

---
Machine-readable: [`catalog/models/kuaishou/web/get-user-id.json`](../../../../catalog/models/kuaishou/web/get-user-id.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/get-user-id
