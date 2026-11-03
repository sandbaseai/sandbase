# Douyin DOU+ User Search API: pricing, parameters and code examples

`douyin/douplus/search-user` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname. Returns matching user profiles with support for cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/search-user", "count": 20, "cursor": 0, "keyword": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/search-user', {'count': 20, 'cursor': 0, 'keyword': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/search-user", {
  "count": 20,
  "cursor": 0,
  "keyword": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/search-user", sandbase.Params{
	"count": 20,
	"cursor": 0,
	"keyword": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/douplus/search-user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` |  |  | Number of results per page, default 20  |
| `cursor` |  |  | Pagination cursor, 0 for first page, then pass the cursor from the previous response  |
| `keyword` | string | yes | Search keyword (Douyin ID / nickname) (required)  |

## Details

Searches Douyin users in the DOU+ delivery context and returns matching user profiles. It needs a `keyword`, which can be a Douyin ID or a nickname.

### Use cases

- Find Douyin accounts by nickname before you set up DOU+ promotion for them.
- Check a Douyin ID against the returned `unique_id` to confirm which account it belongs to.
- Collect the `sec_uid` of matching accounts to use in other Douyin lookups.
- Page through all accounts that match a topic keyword such as `人工智能`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/search-user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (Douyin ID / nickname) (required) |
| `count` | string | No | Number of results per page, default 20 |
| `cursor` | string | No | Pagination cursor, 0 for first page, then pass the cursor from the previous response |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "cursor": 20,
  "has_more": true,
  "status_code": 0,
  "status_msg": "",
  "user_list": [
    {
      "user_info": {
        "avatar_thumb": {
          "uri": "100x100/aweme-avatar/tos-cn-i-0813c000-ce_oIAh9sA9EEVfEjAEKroAoD2EKIktetAfwAHFA9",
          "url_list": [
            "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c000-ce_oIAh9s…"
          ]
        },
        "nickname": "JYF人工智能",
        "sec_uid": "MS4wLjABAAAAAwIshD25hrP7M8fkn0f3PU79tUhK_bOj0y2bhYjxIqFbwxUCY4DFbL7YZTrYknBu",
        "short_id": "",
        "uid": "4327328752346861",
        "unique_id": "54166183587"
      }
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_list[].user_info.nickname` | Display name of the matching account. |
| `user_list[].user_info.unique_id` | Douyin ID of the account, the public ID that users can search by. |
| `user_list[].user_info.uid` | Numeric user ID of the account, returned as a string. |
| `user_list[].user_info.sec_uid` | Encoded user ID of the account. Other Douyin APIs use this form of ID to identify a user. |
| `user_list[].user_info.short_id` | Short ID of the account. It can be an empty string. |
| `user_list[].user_info.avatar_thumb.url_list` | Image URLs for the account avatar. The path shows a 100x100 size. |
| `user_list[].user_info.avatar_thumb.uri` | Path of the avatar image without the host name. |
| `cursor` | Cursor value to pass in the next request to get the following page. |
| `has_more` | `true` when more results are available after this page. |
| `status_code / status_msg` | Status of the call. `status_code` is `0` in the sample response and `status_msg` is empty. |

### Notes

- Send `cursor` as `0` for the first page. For the next page, pass the `cursor` value from the previous response (the sample returned `20`).
- Keep requesting pages while `has_more` is `true`.
- Use `count` to set the page size. The documented default is 20.
- To see which videos an account can promote, call [Douyin DOU+ Promotable Items](/apis/douyin/douplus/promotable-item-list) next.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin DOU+ Promotable Items](/apis/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ Talent Categories](/apis/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.
- [Douyin DOU+ Talents by Category](/apis/douyin/douplus/talents-by-category): Returns a list of DOU+ talents filtered by category name or keyword.

---
Machine-readable: [`catalog/models/douyin/douplus/search-user.json`](../../../../catalog/models/douyin/douplus/search-user.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/search-user
