# Pipixia User Follower List API: pricing, parameters and code examples

`pipixia/app/user-follower-list` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of followers for a specified Pipixia user account. Supports pagination through cursor tokens to navigate subsequent pages.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/user-follower-list", "user_id": "3602444694069495"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/user-follower-list', {'user_id': '3602444694069495'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/user-follower-list", {
  "user_id": "3602444694069495"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/user-follower-list", sandbase.Params{
	"user_id": "3602444694069495",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/user-follower-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Page cursor, default is 0, get the corresponding value from the `loadmore_cursor` Key in the previous page.  |
| `user_id` | string | yes | AKA user id, can be obtained from the share link.  |

## Details

Returns a page of follower accounts for a Pipixia user. It needs the target account's `user_id`, and an optional `cursor` to fetch later pages.

### Use cases

- Pull the follower list of a Pipixia creator to review who follows them.
- Page through all followers of an account and store each follower's `id_str` and `name`.
- Check the `region` and `language` of followers to see where an audience comes from.
- Collect follower profile links to open each account in the app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/user-follower-list" \
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
      "has_more": true,
      "loadmore_cursor": 1793311346712,
      "previous_cursor": null,
      "refresh_cursor": 1793689318517
    },
    "users": [
      {
        "achievements": null,
        "age": "",
        "author_info": null,
        "avatar": {
          "download_list": [
            {
              "url": "https://p3-ppx-sign.byteimg.com/tos-cn-i-0000/d2647397bb814fd0b49ee2d0011206c8~t…"
            }
          ],
          "height": 200,
          "is_gif": false,
          "uri": "tos-cn-i-0000/d2647397bb814fd0b49ee2d0011206c8",
          "url_list": [
            {
              "url": "https://p6-ppx-sign.byteimg.com/tos-cn-i-0000/d2647397bb814fd0b49ee2d0011206c8~t…"
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
        "followers_count": null,
        "followings_count": null
      }
    ]
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691714612
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.users[].id_str / data.users[].id` | The follower's user ID as a string and as a number. Use `id_str` when the number is too large for your tools. |
| `data.users[].name` | Display name of the follower. |
| `data.users[].avatar.url_list[].url` | Link to a 200 by 200 WebP avatar image for the follower. |
| `data.users[].avatar.download_list[].url` | Link to the avatar image in a download format. |
| `data.users[].region / data.users[].language` | Region code and language code on the follower's profile, such as `cn` and `zh`. |
| `data.users[].medal_info.total_medal` | Number of medals the follower holds. `medal_info.wall_schema` is the in-app link to the badge wall. |
| `data.users[].profile_schema` | In-app link to the follower's profile page. |
| `data.cursor.loadmore_cursor` | Cursor value to send as `cursor` to get the next page. |
| `data.cursor.has_more` | `true` when more followers remain after this page. |

### Notes

- Get `user_id` from the account's share link. If you only have a short link, use [Pipixia Short URL Conversion](/apis/pipixia/app/short-url) first.
- For the next page, send `data.cursor.loadmore_cursor` as `cursor`. The first request can omit `cursor`, which defaults to 0.
- Many profile fields in each user, such as `followers_count` and `like_count`, are `null` in this list. Call [Pipixia User Information](/apis/pipixia/app/user-info) for fuller profile data.
- To see the accounts a user follows, call [Pipixia User Following List](/apis/pipixia/app/user-following-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/user-follower-list.json`](../../../../catalog/models/pipixia/app/user-follower-list.json) · Store page: https://www.sandbase.ai/model/pipixia/app/user-follower-list
