# WeChat Account Search API: pricing, parameters and code examples

`wechat-search/search-account` · data API · WeChat Search · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.057143 per call · **Modes:** sync

Search WeChat Official Accounts by keyword with page-number pagination and one result per page. Use it to find an account by name or related term before profile or article lookup.

## Pricing

- **$0.057143 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-search/search-account", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-search/search-account', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-search/search-account", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-search/search-account", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-search/search-account` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number starting from 1 for WeChat Official Account profile search. default `1` |
| `keyword` | string | yes | Search keyword for WeChat Official Account profiles.  |

## Details

This API searches WeChat Official Accounts by keyword and returns matching account profiles. It needs a `keyword` and takes an optional `page` number. Each page holds one result.

### Use cases

- Find the Official Account for a brand or topic name and get its `biz` and `wxid` identifiers.
- Compare follower counts and average read counts across accounts that match a topic keyword.
- Check which company owns an Official Account by reading `owner_name` and `customer_type`.
- Build a list of accounts in a niche by stepping through `page` values for one keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-search/search-account" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword for WeChat Official Account profiles. |
| `page` | integer | No | Page number starting from 1 for WeChat Official Account profile search. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "avatar": "https://wx.qlogo.cn/mmhead/Q3auHgzwzM6B7P7K0g311MAbOHz2d3DqwiaZRPyWlSNK1HU7iaB6F…",
      "avg_top_read": 151,
      "avg_top_zan": 0,
      "biz": "MzAwNzIyMTQ2MA==",
      "customer_type": "企业",
      "fans": 36143,
      "ghid": "gh_143f18f53985",
      "lastest_publish": 1693393200,
      "name": "人工智能",
      "owner_name": "郑州夺蓝网络技术有限公司",
      "qrcode": "https://open.weixin.qq.com/qr/code?username=worldofai",
      "week_articles": 0
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].name` | Display name of the Official Account. |
| `data[].wxid` | Account username. The `qrcode` link also contains this value. |
| `data[].ghid` | Account ID that starts with `gh_`. |
| `data[].biz` | Account identifier in base64-style text, such as `MzAwNzIyMTQ2MA==`. |
| `data[].fans` | Follower count for the account. |
| `data[].avg_top_read / avg_top_zan` | Average reads and average likes (`zan`) for the account's top article. The sample shows `151` reads and `0` likes. |
| `data[].week_articles` | Number of articles the account published in the week. The sample value is `0`. |
| `data[].lastest_publish` | Time of the latest publication as a Unix timestamp in seconds. The key is spelled `lastest_publish`. |
| `data[].owner_name / customer_type` | Name of the entity that registered the account and its type, such as `企业` (enterprise). |
| `data[].avatar / qrcode` | URL of the account's avatar image and URL of its QR code link. |

### Notes

- `page` starts at 1 and each page returns one account, so increase `page` to see more matches.
- Use the returned `name` or `biz` value as the input for profile or article lookups.
- To search articles by keyword instead, call [WeChat Article Search](/apis/wechat-search/search-article).

### Pricing

$0.057143 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-search/search-account.json`](../../../catalog/models/wechat-search/search-account.json) · Store page: https://www.sandbase.ai/model/wechat-search/search-account
