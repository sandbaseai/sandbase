# Weibo User Followers API: pricing, parameters and code examples

`weibo/followers` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a page of accounts followed by a Weibo user identified by UID. Use it to examine the account's outgoing follow network or continue through its following list.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/followers", "uid": "2803301701"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/followers', {'uid': '2803301701'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/followers", {
  "uid": "2803301701"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/followers", sandbase.Params{
	"uid": "2803301701",
})
```

Same call via the path form: `POST /v1/api/weibo/followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Weibo User ID (UID).  |
| `page` | integer |  | Page number, starting with 1. default `1` |

## Details

Returns one page of the accounts that a Weibo user follows. It needs the user's numeric `uid` and takes an optional `page` number.

### Use cases

- List the accounts a media outlet or public figure follows to map its outgoing network.
- Collect `followers_count` and `description` for each followed account to find large or relevant accounts.
- Page through a full following list and store it to compare snapshots over time.
- Check which followed accounts follow the user back with `follow_me` and `bi_followers_count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "2803301701"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | Weibo User ID (UID). |
| `page` | integer | No | Page number, starting with 1. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "fill_material": 0,
  "has_filtered_attentions": false,
  "has_filtered_fans": false,
  "next_cursor": 20,
  "ok": 1,
  "previous_cursor": 0,
  "screenName": "人民日报",
  "show_related_topic": false,
  "show_unread": false,
  "sort_type": 0,
  "total_number": 419,
  "type": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `screenName` | Display name of the user whose following list you requested. |
| `total_number` | Total number of accounts in the following list. The sample shows `419`. |
| `next_cursor / previous_cursor` | Position markers for the next and previous page. The sample shows `20` for `next_cursor` and `0` for `previous_cursor`. |
| `users[]` | The followed accounts on this page. Each item is one account profile. |
| `users[].created_at` | Date and time the followed account was created, as text such as `Wed Jan 23 12:51:13 +0800 2013`. |
| `users[].description` | Bio text of the followed account. It can be an empty string. |
| `users[].followers_count / users[].followers_count_str` | Number of followers of the followed account. The `_str` field is the shortened display text, for example `519万`. |
| `users[].friends_count` | Number of accounts the followed account itself follows. |
| `users[].bi_followers_count` | Count of mutual follow relationships for the followed account. |
| `users[].domain / users[].gender` | Custom URL domain name and gender code of the followed account. These fields are missing or empty on some accounts. |
| `users[].avatar_hd / users[].avatar_large / users[].cover_image` | Image URLs for the avatar and the profile cover. The avatar URLs carry an `Expires` parameter. |

### Notes

- Send `page` starting at `1` to move through the list. Check `next_cursor` and `total_number` to see how much is left.
- Some user fields, such as `gender` and `cover_image`, are not present on every account. Handle missing keys.
- To list the accounts that follow this user instead, call [Weibo User Fans](/apis/weibo/fans).
- For profile details of one followed account, call [Weibo User Profile](/apis/weibo/user-detail) with its UID.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/followers.json`](../../../catalog/models/weibo/followers.json) · Store page: https://www.sandbase.ai/model/weibo/followers
