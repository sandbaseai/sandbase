# Kuaishou User Search API: pricing, parameters and code examples

`kuaishou/search-user` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search public Kuaishou user accounts by keyword with page-number pagination. Use it to discover relevant creators or accounts before requesting profile and published-video data.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/search-user", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/search-user', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/search-user", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/search-user", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/kuaishou/search-user` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for results, starting from 1. default `1` |
| `keyword` | string | yes | The search keyword to find users.  |

## Details

Returns a list of public Kuaishou user accounts that match a search keyword. Each account includes its ID, display name, bio, follower count, avatar and verification status. The only required input is `keyword`.

### Use cases

- Find creators in a niche, such as food accounts for the keyword `美食`, and rank them by `fansCount`.
- Build a list of `user_id` values to feed into profile and video list requests.
- Check which accounts in a topic carry the platform verification badge.
- Collect `kwaiId` handles and bios to screen accounts for outreach.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/search-user" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | The search keyword to find users. |
| `page` | integer | No | Page number for results, starting from 1. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extParams": {
    "disablePhotoInsert": false,
    "dynamicShard": false,
    "isShowPymkUserPhotos": true,
    "isShowScrollTopButton": false,
    "rsRecoAfterPlayInterval": 2,
    "searchTaskParam": {},
    "sessionParams": "",
    "streamExtParams": "{\"single\":false,\"predict\":false,\"searchDetailCost\":{\"filterItem\":0,\"getView\":14}…",
    "subtagWithPic": false
  },
  "host-name": "public-bjmt-c26-kce-node826.idchb1az4.hb1.kwaidc.com",
  "llsid": "2006455000852273746",
  "pcursor": "1",
  "portalFlag": true,
  "recoPcursor": "no_more",
  "recoPymkFlag": false,
  "responseCode": 0,
  "result": 1,
  "userFoldIndex": -1,
  "users": [
    {
      "extra": {
        "userInfoExposed": {
          "lineSecond": "2"
        }
      },
      "fans": false,
      "fansCount": 1229553,
      "feedLogCtx": {
        "stidContainer": "In8xfDIwMDY0NTUwMDA4NTIyNzM3NDZ8QkFTRTo0MDMwMDA1OHx7InBnIjoic3VmIn18eyJiaXoiOiJz…"
      },
      "following": false,
      "headurl": "http://p4.a.yximgs.com/uhead/AB/2021/02/18/12/BMjAyMTAyMTgxMjA0MTRfNDAzMDAwNThfM…",
      "headurls": [
        {
          "cdn": "p4.a.yximgs.com",
          "url": "http://p4.a.yximgs.com/uhead/AB/2021/02/18/12/BMjAyMTAyMTgxMjA0MTRfNDAzMDAwNThfM…"
        }
      ],
      "isBanned": false,
      "isFavorited": false,
      "is_followed": 0,
      "kwaiId": "kuaishoumeishi",
      "messageLink": "kwai://message/40300058"
    }
  ],
  "ussid": "MV81NzQ1MDc3MzkyXzE3OTM2OTEzNzUxNjBfXzQ0NzU"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[]` | List of matching user accounts for the requested page, in search rank order. |
| `users[].user_id` | Numeric ID of the account. Use it to request profile or video data. |
| `users[].user_name` | Display name of the account. |
| `users[].kwaiId` | Public Kuaishou handle of the account. |
| `users[].user_text` | Bio text written by the account owner. |
| `users[].fansCount` | Number of followers the account has. |
| `users[].user_sex` | Gender code of the account. The response shows `F` and `U`. |
| `users[].verified` | `true` if the account is verified. When verified, `verifiedDetail.description` holds the badge text. |
| `users[].headurl / users[].headurls[].url` | Avatar image URL. `headurls` lists the same image on different CDN hosts. |
| `pcursor` | Cursor value returned with the page. It was `1` for the first page. |

### Notes

- Use `page` to get more results. It starts at 1 and defaults to 1.
- `user_id` is a number. Pass it to [Kuaishou User Profile](/apis/kuaishou/user-detail) or [Kuaishou User Published Videos](/apis/kuaishou/user-video-list) to get more about an account.
- [Kuaishou User Search (V2)](/apis/kuaishou/app/search-user-v2) is another user search endpoint if you need a different response.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/kuaishou/search-user.json`](../../../catalog/models/kuaishou/search-user.json) · Store page: https://www.sandbase.ai/model/kuaishou/search-user
