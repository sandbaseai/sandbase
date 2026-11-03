# Xiaohongshu (RED) User Profile Information API: pricing, parameters and code examples

`xiaohongshu/web-v3/user-info` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns public profile details and interaction metrics for a specific Xiaohongshu account based on the provided user ID.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/web-v3/user-info", "user_id": "5e3a8ee700000000010070c6"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/web-v3/user-info', {'user_id': '5e3a8ee700000000010070c6'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/web-v3/user-info", {
  "user_id": "5e3a8ee700000000010070c6"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/web-v3/user-info", sandbase.Params{
	"user_id": "5e3a8ee700000000010070c6",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/web-v3/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID  |

## Details

Returns the public profile of a Xiaohongshu account: nickname, bio, avatar URLs, RED ID, profile tags and interaction counts. It needs one input, the account's `user_id`.

### Use cases

- Show a creator's nickname, bio and avatar in an internal dashboard.
- Compare the follower, following and likes-and-saves counts of several creators before outreach.
- Check a creator's profession tag, such as a fashion blogger label, to sort accounts into categories.
- Look up the public `red_id` for an account when you only hold its internal `user_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/web-v3/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "5e3a8ee700000000010070c6"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "basic_info": {
      "desc": "💒𝐼𝑠𝑙𝑎𝑛𝑑 𝑑𝑖𝑎𝑟𝑦𓇼 ꙳🐰˳ ˖ ˚✩🫧\n         \n   »»  分享生活日常💗🤍",
      "gender": 1,
      "imageb": "https://sns-avatar-qc.rednotecdn.com/avatar/1040g2jo31npcail65m905p38itkaasfspa9…",
      "images": "https://sns-avatar-qc.rednotecdn.com/avatar/1040g2jo31npcail65m905p38itkaasfspa9…",
      "ip_location": "",
      "nickname": "Rose",
      "red_id": "792402293"
    },
    "collected": 29581,
    "extra_info": {
      "blockType": "DEFAULT",
      "fstatus": "none"
    },
    "interactions": [
      {
        "count": "10+",
        "i18n_count": "10+",
        "name": "关注",
        "show": false,
        "type": "follows"
      }
    ],
    "liked": 92964,
    "posted": 2,
    "result": {
      "code": 0,
      "message": "success",
      "success": true
    },
    "tab_public": {
      "collection": false,
      "collectionBoard": {
        "count": 0,
        "display": false,
        "lock": false
      },
      "collectionFile": {
        "count": 0,
        "display": false,
        "lock": false
      },
      "collectionNote": {
        "count": 0,
        "display": false,
        "lock": false
      }
    },
    "tags": [
      {
        "icon": "http://sns-i11.rednotecdn.com/icons/user/gender-female-v1.png",
        "tagType": "info"
      }
    ]
  },
  "msg": "成功",
  "ok": true,
  "status": 200,
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.basic_info.nickname` | Display name of the account. |
| `data.basic_info.red_id` | The account's public RED ID, shown as a string. |
| `data.basic_info.desc` | Profile bio text. It can contain emoji and line breaks. |
| `data.basic_info.images / data.basic_info.imageb` | Avatar image URLs. The `images` URL has a width of 360 in its query string and the `imageb` URL has a width of 540. |
| `data.basic_info.gender` | Numeric gender code. The sample value `1` matches the female icon in `data.tags`. |
| `data.interactions[].type` | Counter type: `follows`, `fans` or `interaction`. |
| `data.interactions[].count / data.interactions[].i18n_count` | Counter value as a rounded display string. `count` uses Chinese units such as `1万+`, and `i18n_count` uses `10K+` style. |
| `data.interactions[].name` | Chinese label for the counter, such as `关注` (following), `粉丝` (followers) or `获赞与收藏` (likes and saves). |
| `data.liked / data.collected / data.posted` | Numeric counts. `liked` and `collected` are exact numbers, and `posted` is the count of posted notes. |
| `data.tags[]` | Profile tags. Items have a `tagType` of `info` (with an `icon`) or `profession` (with a `name`). |

### Notes

- The `user_id` is a 24-character hex string such as `5e3a8ee700000000010070c6`. Find it with [Xiaohongshu (RED) User Search](/apis/xiaohongshu/app-v2/search-users).
- The `count` values in `data.interactions` are rounded strings, not exact numbers. Some entries have `show` set to `false`.
- To list this account's notes, call [Xiaohongshu (RED) User Posted Notes](/apis/xiaohongshu/app-v2/user-posted-notes).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Homepage Feed](/apis/xiaohongshu/web-v3/homefeed): Retrieves recommended notes from the Xiaohongshu homepage feed.
- [Xiaohongshu (RED) Homepage Categories](/apis/xiaohongshu/web-v3/homefeed-categories): Returns a list of available homefeed category channels on Xiaohongshu (RED).
- [Xiaohongshu (RED) Web Note Details](/apis/xiaohongshu/web-v3/note-detail): Returns detailed information for a specific Xiaohongshu note using its identifier and security token obtained from a web share link.

---
Machine-readable: [`catalog/models/xiaohongshu/web-v3/user-info.json`](../../../../catalog/models/xiaohongshu/web-v3/user-info.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/web-v3/user-info
