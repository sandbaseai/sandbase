# WeChat MP Account Profile API: pricing, parameters and code examples

`wechat-mp/v2/account-profile` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves the profile details of an official WeChat account, including name, avatar, signature, and verification entity type using its official account ID.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/account-profile", "username": "gh_363b924965e9"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/account-profile', {'username': 'gh_363b924965e9'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/account-profile", {
  "username": "gh_363b924965e9"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/account-profile", sandbase.Params{
	"username": "gh_363b924965e9",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/account-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=raw; False=simplified parsing.  |
| `username` | string | yes | Official account `gh_username` (`gh_…`). Sources: `content.user_name` from article detail, or `jumpInfo.userName` from WeChat Search V2 `fetch_search` (business_type=account) results. E.g. `gh_363b924965e9`  |

## Details

Look up official WeChat account profile information by passing the account ID in `username`.

### Use cases

- Verify official WeChat account details such as verification status and entity type.
- Display official account avatar, nickname, and signature in external dashboards.
- Inspect raw or simplified profile data structures for integrated WeChat monitoring tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/account-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "gh_363b924965e9"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Official account `gh_username` (`gh_…`). |
| `raw` | boolean | No | Optional, default True. |

### Notes

- Set `username` using the `gh_` ID obtained from article details or WeChat search results.
- Set `raw` to false for simplified parsing, or keep it true by default for raw profile data.
- Profile fields such as nickname, signature, or avatar URL may return as null.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [WeChat MP Account Articles](/apis/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Article Ads](/apis/wechat-mp/v2/article-ad): Returns embedded ad slot information for a specified WeChat MP article URL.
- [WeChat MP Article Comments](/apis/wechat-mp/v2/article-comments): Get the comments on a WeChat official account article from its URL: comment text, likes, time and commenter region, with cursor pagination.

---
Machine-readable: [`catalog/models/wechat-mp/v2/account-profile.json`](../../../../catalog/models/wechat-mp/v2/account-profile.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/account-profile
