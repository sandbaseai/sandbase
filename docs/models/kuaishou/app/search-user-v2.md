# Kuaishou User Search (V2) API: pricing, parameters and code examples

`kuaishou/app/search-user-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches for Kuaishou accounts matching a query term. Results can be filtered by gender and account relationship status, as well as sorted by follower count.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/search-user-v2", "keyword": "test"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/search-user-v2', {'keyword': 'test'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/search-user-v2", {
  "keyword": "test"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/search-user-v2", sandbase.Params{
	"keyword": "test",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/search-user-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | 搜索关键词/Search keyword  |
| `pcursor` | string |  | Pagination cursor, empty for first page, pass pcursor from previous response  |
| `fans_sort` | string |  | default / most_to_least / least_to_most one of: `default`, `most_to_least`, `least_to_most` |
| `user_gender` | string |  | all / male / female one of: `all`, `male`, `female` |
| `user_relation` | string |  | all / same_city / verified / live / following one of: `all`, `same_city`, `verified`, `live`, `following` |

## Details

Returns a page of Kuaishou accounts that match a search term. It needs a `keyword`, and you can add filters for gender, relationship status and follower sorting.

### Use cases

- Build a list of Kuaishou creators who work on a topic such as artificial intelligence.
- Rank accounts for a keyword by follower count to find the largest ones.
- Limit a creator search to verified accounts or to accounts that are live now.
- Collect account avatars and follower counts for a keyword to compare creators.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/search-user-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes |  |
| `fans_sort` | string | No | default / most_to_least / least_to_most |
| `pcursor` | string | No | Pagination cursor, empty for first page, pass pcursor from previous response |
| `user_gender` | string | No | all / male / female |
| `user_relation` | string | No | all / same_city / verified / live / following |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "debug_id": "7fbac2b2",
  "debug_info": "gAAAAABq6Y7kO_4aeUqh7f6fgim7-5UXv1o1FrponeDxd468LhTh3DFWhujIQSLOOxcuXOslnnb_nc-Y…",
  "extParams": {
    "disablePhotoInsert": false,
    "dynamicShard": false,
    "isCreativeMode": false,
    "isShowPymkUserPhotos": true,
    "isShowScrollTopButton": false,
    "livePendantResource": "https://static.yximgs.com/udata/pkg/ks-nearby/nearby_living_tag/origin_196uxh2cv…",
    "multiFilterModels": [
      {
        "filterModels": [
          {
            "filterType": "100",
            "multiSelect": false,
            "name": "All users"
          }
        ],
        "title": "relation"
      }
    ],
    "outerStreamFetch": 6,
    "pageSingleDoubleStyle": 0,
    "rsRecoAfterPlayInterval": 2,
    "searchTaskParam": {},
    "sessionParams": ""
  },
  "host-name": "public-bjzey-c34-kce-node353.idchb1az3.hb1.kwaidc.com",
  "llsid": "2006449996850283570",
  "mixFeeds": [
    {
      "atmosphereType": 0,
      "extInfo": {},
      "feedLogCtx": {
        "stidContainer": "InUxfDIwMDY0NDk5OTY4NTAyODM1NzB8VVNFUjoyODgwMjIyNjkwfHsicGciOiJzdWYifXx7ImJpeiI6…"
      },
      "isSingleColumnMode": false,
      "itemTransferInfo": "{\"refer_single_double_type\":0}",
      "itemType": 4,
      "rank": 0,
      "user": {
        "extra": {
          "userInfoExposed": {
            "lineSecond": "2"
          }
        },
        "fans": false,
        "fansCount": 112583,
        "feedLogCtx": {
          "stidContainer": "InUxfDIwMDY0NDk5OTY4NTAyODM1NzB8QkFTRToyODgwMjIyNjkwfHsicGciOiJzdWYifXx7ImJpeiI6…"
        },
        "following": false,
        "headurl": "http://p22.a.yximgs.com/uhead/AB/2026/08/27/16/BMjAyNjA4MjcxNjI1MTNfMjg4MDIyMjY5…",
        "headurls": [
          {
            "cdn": "p22.a.yximgs.com",
            "url": "http://p22.a.yximgs.com/uhead/AB/2026/08/27/16/BMjAyNjA4MjcxNjI1MTNfMjg4MDIyMjY5…"
          }
        ],
        "isBanned": false
      }
    }
  ],
  "pcursor": "1",
  "portalFlag": true,
  "recoInterestFlag": false,
  "recoPcursor": "no_more",
  "recoPymkFlag": false,
  "responseCode": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `mixFeeds[]` | List of search result entries. Each entry holds one account under `user`. |
| `mixFeeds[].rank` | Position of the result in the list, starting at 0. |
| `mixFeeds[].user.fansCount` | Number of followers the account has. |
| `mixFeeds[].user.following / mixFeeds[].user.fans` | Boolean flags for the relationship between the account and the viewer. |
| `mixFeeds[].user.headurl` | URL of the account avatar image. |
| `mixFeeds[].user.headurls[].url / mixFeeds[].user.headurls[].cdn` | Alternative avatar URLs and the CDN host that serves each one. |
| `mixFeeds[].user.isBanned` | Boolean flag that shows whether the account is banned. |
| `mixFeeds[].feedLogCtx.stidContainer` | Encoded tracking string for the result. It ends with the user ID encoded inside it. |
| `pcursor` | Cursor for the next page of results. |
| `extParams.multiFilterModels[]` | Filter options the search screen offers, grouped by `relation`, `gender` and `Fans count`. |

### Notes

- Leave `pcursor` empty for the first page. Pass the `pcursor` value from the previous response to get the next page.
- The response also has `recoPcursor`, which was `no_more` in this example.
- Use `fans_sort` with `most_to_least` or `least_to_most` to order results by followers.
- To read a full profile for an account, call [Kuaishou Single User Data (V2)](/apis/kuaishou/app/one-user-v2).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/search-user-v2.json`](../../../../catalog/models/kuaishou/app/search-user-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/search-user-v2
