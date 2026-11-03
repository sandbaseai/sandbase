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

Returns the list of accounts that a Pipixia user follows. Each entry holds a profile summary with follower counts, like counts and badge details. You send the user's `user_id` and can page through results with `cursor`.

### Use cases

- Map which creators a given Pipixia account follows to study its interests.
- Find large creator accounts in a user's following list by sorting on `followers_count`.
- Check the verification label of followed accounts through `certify_info` for audience research.
- Collect `id_str` values from the list and pass them to other Pipixia user APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/user-following-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3602444694069495"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | AKA user id, can be obtained from the share link. |
| `cursor` | string | No | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "cursor": {
      "feed_len": 0,
      "has_more": false,
      "loadmore_cursor": 1669015588861,
      "previous_cursor": null,
      "refresh_cursor": 1696163675006
    },
    "users": [
      {
        "achievements": null,
        "age": "",
        "author_info": null,
        "avatar": {
          "download_list": [
            {
              "url": "https://p6-ppx-sign.byteimg.com/p1056/ce77ebdc9130471899863567fac9cbb3~tplv-f3gp…"
            }
          ],
          "height": 200,
          "is_gif": false,
          "uri": "p1056/ce77ebdc9130471899863567fac9cbb3",
          "url_list": [
            {
              "url": "https://p9-ppx-sign.byteimg.com/p1056/ce77ebdc9130471899863567fac9cbb3~tplv-f3gp…"
            }
          ],
          "width": 200
        },
        "broadcast_info": null,
        "certify_info": null,
        "commerce_permission_list": null,
        "creative_level_info": null,
        "decoration_list": null,
        "description": "",
        "followers_count": 5,
        "followings_count": 33
      }
    ]
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691714777
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.users[].id_str` | User ID of the followed account as a string. The same value appears as a number in `id`. |
| `data.users[].name / data.users[].description` | Display name and profile bio of the followed account. `description` can be an empty string. |
| `data.users[].followers_count / data.users[].followings_count` | Number of followers the account has and number of accounts it follows. |
| `data.users[].like_count / data.users[].vote_count / data.users[].god_comment_count` | Engagement counters for the account, such as total likes received. |
| `data.users[].certify_info.description` | Verification label text shown on the profile, for example a creator category. `certify_info` is `null` for accounts without one. |
| `data.users[].medal_info.total_medal` | Number of badges the account holds. `wear_medal_info` holds the badge currently worn, including `medal_condition`. |
| `data.users[].avatar.url_list[].url` | Signed link to the profile picture, with `width` and `height` next to it. |
| `data.users[].region / data.users[].language` | Region code and language code of the account, such as `cn` and `zh`. |
| `data.users[].profile_schema` | In-app link to the user's profile page. |
| `data.cursor.loadmore_cursor / data.cursor.has_more` | `loadmore_cursor` is the value for the next page. `has_more` shows whether more results exist. |

### Notes

- Get `user_id` from the user's share link. If you only have a short link, use [Pipixia Short URL Conversion](/apis/pipixia/app/short-url) first.
- For the next page, pass `data.cursor.loadmore_cursor` from the previous response as `cursor`. The default is `0`.
- Stop paging when `data.cursor.has_more` is `false`.
- To see who follows a user instead, call [Pipixia User Follower List](/apis/pipixia/app/user-follower-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/user-following-list.json`](../../../../catalog/models/pipixia/app/user-following-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/user-following-list
