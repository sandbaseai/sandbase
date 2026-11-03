# Weibo Post Likes API: pricing, parameters and code examples

`weibo/app/status-likes` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of likes for a specified Weibo post or video. Supports filtering reactions using an attitude type parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/status-likes", "status_id": "5016922058656962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/status-likes', {'status_id': '5016922058656962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/status-likes", {
  "status_id": "5016922058656962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/status-likes", sandbase.Params{
	"status_id": "5016922058656962",
})
```

Same call via the path form: `POST /v1/api/weibo/app/status-likes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `status_id` | string | yes | Post ID or Video ID (required)  |
| `attitude_type` | string |  | Like type filter  |

## Details

Returns the users who liked a Weibo post or video, plus a summary of like counts by reaction type. It needs one input, the post ID or video ID in `status_id`. You can narrow the results with `attitude_type`.

### Use cases

- Pull the accounts that liked a specific post to review who engages with it.
- Read the per-type like counts for a post to compare reaction types.
- Check the profile data of likers, such as verification status and avatar, to profile an audience.
- Filter likes by reaction type with `attitude_type` to study one kind of reaction.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/status-likes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status_id": "5016922058656962"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `status_id` | string | Yes | Post ID or Video ID (required) |
| `attitude_type` | string | No | Like type filter |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "config": "{}",
  "items": [
    {
      "category": "detail",
      "data": {
        "attitudes_count": [
          {
            "count": 87629,
            "type": 0
          }
        ],
        "cur_sub_tab": 0
      },
      "type": "like_attitude"
    }
  ],
  "loadedInfo": "{}",
  "pageData": "{}"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `items[].type` | Row kind. `like_attitude` is the summary row with counts. `like` is one user who liked the post. |
| `items[].data.attitudes_count[].count` | Number of likes for one reaction type in the summary row. |
| `items[].data.attitudes_count[].type` | Reaction type code for that count. The response shows values `0`, `1` and `6`, and does not name them. |
| `items[].data.attitude` | Reaction type code of the like from this user. The sample rows show `1`. |
| `items[].data.user` | Profile object of the user who liked the post. |
| `items[].data.user.avatar_hd` | URL of the user's high-resolution avatar image. |
| `items[].data.user.auth_status` | Numeric verification status of the user's account. |
| `items[].data.user.allow_all_comment / items[].data.user.allow_all_act_msg` | Boolean flags for the user's settings. They show whether everyone may comment and whether everyone may send action messages. |

### Notes

- Use the `id` of a post as `status_id`. The example value is `5016922058656962`.
- The first item in `items` is the `like_attitude` summary row. User rows with type `like` follow it.
- Several fields in the response, such as `config`, `loadedInfo` and `pageData`, come back as empty JSON strings in this sample.
- To get the post itself, call [Weibo Post Detail (App)](/apis/weibo/app/status-detail). For its comments, call [Weibo Post Comments (App)](/apis/weibo/app/status-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/apis/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/status-likes.json`](../../../../catalog/models/weibo/app/status-likes.json) · Store page: https://www.sandbase.ai/model/weibo/app/status-likes
