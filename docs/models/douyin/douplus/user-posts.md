# Douyin Douplus User Posts

`douyin/douplus/user-posts` · api · Douyin

Returns a concise list of homepage video posts for a specified Douyin user. Supports cursor-based pagination and custom result counts.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/douplus/user-posts", "sec_uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/douplus/user-posts', {'sec_uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/douplus/user-posts", {
  "sec_uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/douplus/user-posts", sandbase.Params{
	"sec_uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/douplus/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` |  |  | Page size, default 10  |
| `cursor` |  |  | Pagination cursor (string), "0" for first page, then pass the cursor from the previous response  |
| `sec_uid` | string | yes | User sec_uid (required)  |

## Details

Query a creator's public profile videos by providing their `sec_uid`. The endpoint returns compact post details with support for cursor pagination.

### Use cases

- Retrieve video listings from a target Douyin creator's profile.
- Monitor new video uploads and tags for competitive profile tracking.
- Feed Douplus post metadata into content performance dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/douplus/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_uid (required) |
| `count` | string | No | Page size, default 10 |
| `cursor` | string | No | Pagination cursor (string), "0" for first page, then pass the cursor from the previous response |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "itemInfoList": [
      {
        "CanMountEnterpriseShopCartType": 2,
        "DouplusUserPostTag": "爆款预定",
        "PlayletType": 0,
        "AwemeInfo": {
          "CreateTime": "1790758823000",
          "Desc": ". #海俪恩蛋尾巴摇摇#海俪恩美瞳#海俪恩小狗#美瞳推荐"
        },
        "ItemSource": {
          "SourceType": 1
        }
      }
    ]
  }
}
```

### Notes

- `sec_uid` is required to identify the target user.
- Use "0" for `cursor` on the first page, then pass the cursor returned in subsequent calls.
- `count` defaults to 10 items per page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin DOU+ Promotable Items](/model/douyin/douplus/promotable-item-list): Returns the promotable video item list for a Douyin account on the DOU+ promotion page.
- [Douyin DOU+ User Search](/model/douyin/douplus/search-user): Searches for Douyin users in the DOU+ delivery context using a Douyin ID or nickname.
- [Douyin DOU+ Talent Categories](/model/douyin/douplus/talent-categories): Returns the Douyin DOU+ talent category directory.

---
Machine-readable: [`catalog/models/douyin/douplus/user-posts.json`](../../../../catalog/models/douyin/douplus/user-posts.json) · Store page: https://www.sandbase.ai/model/douyin/douplus/user-posts
