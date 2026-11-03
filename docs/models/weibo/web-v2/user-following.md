# Weibo User Following List API: pricing, parameters and code examples

`weibo/web-v2/user-following` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of accounts that a specified Weibo user follows. Accepts a user identifier and supports page-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-following", "uid": "8431518763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-following', {'uid': '8431518763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-following", {
  "uid": "8431518763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-following", sandbase.Params{
	"uid": "8431518763",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-following` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `page` | integer |  | Page number, starts from 0 (default 0)  |

## Details

Returns the list of accounts that a Weibo user follows, based on the numeric `uid`. You can pass `page` to step through the list. The response also includes paging cursors and a total count.

### Use cases

- Pull the accounts a given Weibo user follows to map who that user pays attention to.
- Build a connection graph between influencers by collecting each account's following list.
- Check whether the following list of an account is empty or hidden before running further analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-following" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `page` | integer | No | Page number, starts from 0 (default 0) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "fill_material": 0,
  "has_filtered_attentions": false,
  "has_filtered_fans": false,
  "next_cursor": 0,
  "ok": 1,
  "previous_cursor": 0,
  "screenName": "用户8431518763",
  "show_related_topic": false,
  "show_unread": false,
  "sort_type": 0,
  "total_number": 0,
  "type": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[]` | List of followed accounts on the requested page. In the sample response this list is empty. |
| `total_number` | Total number of followed accounts reported for the user. The sample response returns `0`. |
| `next_cursor / previous_cursor` | Cursor values for neighbouring pages. Both are `0` in the sample response. |
| `screenName` | Display name of the user whose following list was requested. |
| `ok` | Status flag. The value `1` means the request succeeded. |
| `has_filtered_attentions` | Boolean flag. The sample response returns `false`. |
| `sort_type` | Numeric sort mode of the list. The sample response returns `0`. |

### Notes

- `uid` is a required string, for example `8431518763`.
- `page` starts at `0`, and `0` is the default.
- An empty `users` array with `total_number` of `0` can come back with `ok` set to `1`.
- To see who follows the user instead, call [Weibo User Follower List](/apis/weibo/web-v2/user-fans).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-following.json`](../../../../catalog/models/weibo/web-v2/user-following.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-following
