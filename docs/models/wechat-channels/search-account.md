# WeChat Channels Account Search API: pricing, parameters and code examples

`wechat-channels/search-account` · data API · WeChat Channels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.071429 per call · **Modes:** sync

Looks up a specific WeChat Channels account identity by keyword. Use it to resolve a creator name or account term to the identifier required by account-video queries.

## Pricing

- **$0.071429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/search-account", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/search-account', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/search-account", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/search-account", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/search-account` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword used to resolve a WeChat Channels account id.  |

## Details

Returns one WeChat Channels account that matches a search keyword. The response has the account nickname, signature, avatar images, verification info and the account `username` identifier. It needs one input, `keyword`.

### Use cases

- Resolve a creator name to the `username` value needed by account-video queries.
- Check the nickname and signature of a matched account before you pull its videos.
- Collect avatar and cover image URLs for a creator directory or dashboard.
- Check whether an account shows a verified profession label.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/search-account" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword used to resolve a WeChat Channels account id. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "auth_info": {
      "auth_icon_url": "",
      "auth_profession": ""
    },
    "cover_url": "https://wx.qlogo.cn/finderhead/aXUpZVUYfjyhnicpkp3l5MvI4epIAk9NjzFnjia07kUZT1H2u…",
    "head_url": "https://wx.qlogo.cn/finderhead/aXUpZVUYfjyhnicpkp3l5MvI4epIAk9NjzFnjia07kUZT1H2u…",
    "nickname": "人工智能",
    "signature": "❤️  聚集人工…",
    "username": "v2_060000231003b20faec8c7e48d1dc6d5c802e83db0770775bb566d2b495e6aae711d6d56bd04@…"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.username` | Account identifier string that ends in `@finder`. Pass it to account-video queries as the account id. |
| `data.nickname` | Display name of the matched account. |
| `data.signature` | Profile bio text of the account. It can contain line breaks (`\n`) and emoji. |
| `data.head_url / data.cover_url` | Image URLs for the account avatar and cover. In this response both point to the same image. |
| `data.auth_info.auth_profession` | Verified profession label of the account. It is an empty string when the account has none. |
| `data.auth_info.auth_icon_url` | URL of the verification badge icon. It is an empty string when the account has no badge. |

### Notes

- The response holds a single account object under `data`, not a list, so there is no pagination.
- Copy the full `data.username` value, including the `@finder` suffix, into the next call.
- Call [WeChat Channels Account Videos](/apis/wechat-channels/account-videos) with the returned `username` to list the account's videos.
- Use [WeChat Channels Account Info](/apis/wechat-channels/v2/channel-info) for more detail on an account.

### Pricing

$0.071429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/search-account.json`](../../../catalog/models/wechat-channels/search-account.json) · Store page: https://www.sandbase.ai/model/wechat-channels/search-account
