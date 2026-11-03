# Weibo User Fans API: pricing, parameters and code examples

`weibo/fans` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get a page of fan accounts that follow a Weibo user identified by UID. Use it to browse the account's follower audience or continue through its fan list.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/fans", "uid": "2803301701"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/fans', {'uid': '2803301701'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/fans", {
  "uid": "2803301701"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/fans", sandbase.Params{
	"uid": "2803301701",
})
```

Same call via the path form: `POST /v1/api/weibo/fans` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | Weibo User ID (UID).  |
| `page` | integer |  | Page number, starting with 1. default `1` |

## Details

Returns one page of fan accounts that follow a Weibo user. It needs the user's `uid`, and an optional `page` number. Each page lists fan profiles along with the target account's total fan count.

### Use cases

- Browse the accounts that follow a large Weibo account such as a news outlet.
- Collect fan profiles with follower counts and creation dates to look for new or empty accounts.
- Track the total fan count of an account by calling it on a schedule and comparing `total_number`.
- Page through a fan list to build a sample of an account's audience.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/fans" \
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
  "display_total_number": 158132191,
  "display_total_number_str": "1.58亿",
  "fill_material": 0,
  "has_filtered_attentions": false,
  "has_filtered_fans": false,
  "next_cursor": 20,
  "ok": 1,
  "previous_cursor": 0,
  "screenName": "人民日报",
  "show_related_topic": false,
  "show_unread": false,
  "sort_type": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `screenName` | Display name of the account whose fans are listed. In the example it is `人民日报`. |
| `total_number / display_total_number` | Total fan count for the account as a number. `display_total_number` is a second count, and the example values differ. |
| `display_total_number_str` | Fan count as a short display string, for example `1.58亿`. |
| `next_cursor / previous_cursor` | Cursor values for moving between pages. The example returns `20` for `next_cursor` and `0` for `previous_cursor`. |
| `users[].id` | Not shown in the trimmed sample; use `users[].fansIcon.uid` for the numeric ID of each fan. |
| `users[].fansIcon.uid` | Numeric ID of the fan account. It matches `fansIcon.fans_uid`. |
| `users[].description` | Bio text of the fan account. It can be an empty string. |
| `users[].created_at` | Date and time the fan account was created, for example `Fri Nov 07 14:54:19 +0800 2014`. |
| `users[].followers_count / users[].friends_count / users[].favourites_count` | Number of followers, number of accounts followed, and number of favourites for the fan account. |
| `users[].gender` | Gender code of the fan account. The example shows `f`. |
| `users[].avatar_hd / users[].avatar_large` | Image URLs for the fan's avatar, in high and large sizes. The URLs contain `Expires` and `ssig` query values. |

### Notes

- Get the `uid` for an account with [Weibo User Profile](/apis/weibo/user-detail) or [Weibo User Profile Information](/apis/weibo/app/user-info).
- Send `page` starting at `1`. The sample response also returns `next_cursor` for the next position.
- `created_at` uses the format `Fri Nov 07 14:54:19 +0800 2014`.
- To list the accounts a user follows instead, call [Weibo User following](/apis/weibo/app/user-following).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/fans.json`](../../../catalog/models/weibo/fans.json) · Store page: https://www.sandbase.ai/model/weibo/fans
