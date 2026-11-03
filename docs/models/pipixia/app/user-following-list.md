# Pipixia User Following List API: pricing, parameters and code examples

`pipixia/app/user-following-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves the list of accounts followed by a specified Pipixia user. Returns profile summaries and engagement statistics with cursor pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/user-following-list", "user_id": "3602444694069495"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/user-following-list', {'user_id': '3602444694069495'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/user-following-list", {
  "user_id": "3602444694069495"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/user-following-list", sandbase.Params{
	"user_id": "3602444694069495",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/user-following-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page.  |
| `user_id` | string | yes | AKA user id, can be obtained from the share link.  |

## Details

Fetch the following list for any target Pipixia account by providing `user_id`. Supports paginating through results using the `cursor` parameter.

### Use cases

- Analyze the network of accounts a specific user follows.
- Track creator connections and interest graphs on Pipixia.
- Audit following lists for audience and competitor research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/user-following-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3602444694069495"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | AKA user id, can be obtained from the share link. |
| `cursor` | string | No | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "users": [
      {
        "followers_count": 5,
        "followings_count": 33,
        "god_comment_count": 0,
        "id": 102889515304,
        "like_count": 1,
        "name": "皮皮侠35016970",
        "status": 0,
        "vote_count": 0
      }
    ]
  }
}
```

### Notes

- `user_id` can be obtained from the profile share link.
- For pagination, pass the previous page loadmore_cursor value into `cursor` (default is 0).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/user-following-list.json`](../../../../catalog/models/pipixia/app/user-following-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/user-following-list
