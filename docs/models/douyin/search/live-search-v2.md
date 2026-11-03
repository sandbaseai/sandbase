# Douyin Live search V2 API: pricing, parameters and code examples

`douyin/search/live-search-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Fetch live search V2 on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/live-search-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/live-search-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/live-search-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/live-search-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/live-search-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor, 0 for the first request, then the cursor from the last response default `0` |
| `keyword` | string |  | Douyin ID or nickname default `"小耳朵"` |

## Details

Searches Douyin for accounts that match a Douyin ID or nickname. Returns a page of matching users with follower counts, profile IDs and live room status. It needs a `keyword` and an optional `cursor`.

### Use cases

- Find a creator's Douyin account from a nickname and read their follower count.
- Resolve a Douyin ID to the `secUid` that other Douyin user APIs need.
- Check whether a matching account is live right now before you pull live room data.
- Build a list of accounts with similar names by paging through results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/live-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "小耳朵", "cursor": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor, 0 for the first request, then the cursor from the last response |
| `keyword` | string | No | Douyin ID or nickname |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "cursor": 10,
    "hasMore": true,
    "userList": [
      {
        "avatar": "https://p3.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-avt-0015_69061032f579…",
        "followerCount": 5205393,
        "followerCountStr": "",
        "liveRoomInfo": {
          "LiveRoomInfoDetail": {
            "AnchorNickname": "一只小耳朵",
            "LiveRoomCoverUri": "aweme-avatar/tos-cn-avt-0015_69061032f579b15d5d2d7e067d1c3471",
            "RoomId": "0",
            "Title": ""
          },
          "LiveRoomInfoExtra": {
            "HasBisinessComponent": false,
            "HasClosedShoppingCart": false,
            "HasWindmill": false,
            "IsForO2ORoom": false
          },
          "LiveRoomLiveStatus": 0
        },
        "nickname": "一只小耳朵",
        "secUid": "MS4wLjABAAAAkOvK-iD0N7wlM8V4Q9otZfPAJp6GKYPgPWlZOzobwR8",
        "shortId": "4768507",
        "uniqueId": "xed1216"
      }
    ]
  },
  "msg": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.userList[]` | One matching Douyin account per item. |
| `data.userList[].nickname` | Display name of the account. |
| `data.userList[].uniqueId / shortId` | Public Douyin ID values for the account. `uniqueId` is the custom ID, and `shortId` is a numeric short ID. |
| `data.userList[].secUid` | Encoded user ID string. Use it to look up the same user in other Douyin user APIs. |
| `data.userList[].followerCount` | Number of followers as an integer. `followerCountStr` was an empty string in this response. |
| `data.userList[].avatar` | URL of the account's avatar image. |
| `data.userList[].liveRoomInfo.LiveRoomLiveStatus` | Live status code for the account. All users in this response returned `0`, and their `RoomId` was `"0"`. |
| `data.userList[].liveRoomInfo.LiveRoomInfoDetail.AnchorNickname / Title` | Nickname of the live anchor and the live room title. `Title` is empty when no live room is active. |
| `data.cursor` | Cursor value to send as `cursor` in the next request to get the next page. |
| `data.hasMore` | Shows `true` when more results are available. |

### Notes

- Send `cursor` as `0` for the first request. For the next page, send the `data.cursor` value from the last response, and stop when `data.hasMore` is `false`.
- `keyword` accepts a Douyin ID or a nickname.
- To look up a full profile, pass the returned `secUid` to [Douyin User Profile (App V3)](/apis/douyin/app-v3/user-profile).
- To list an account's videos, use [Douyin User Videos](/apis/douyin/app-v3/user-post-videos) with the `secUid`.

### Pricing

$0.01 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/search/live-search-v2.json`](../../../../catalog/models/douyin/search/live-search-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/live-search-v2
