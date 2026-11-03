# Pipixia User Information API: pricing, parameters and code examples

`pipixia/app/user-info` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves public profile details for a Pipixia user, including avatar image URLs. Takes a user identifier obtained from a share link.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/user-info", "user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/user-info', {'user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/user-info", {
  "user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/user-info", sandbase.Params{
	"user_id": "example",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | AKA user id, can be obtained from the share link.  |

## Details

This API returns the public profile of a Pipixia user, including name-related text, location, follower counts and avatar image URLs. It needs one input: the `user_id`, which you can take from a Pipixia share link.

### Use cases

- Show a Pipixia creator's avatar, bio and city on a community dashboard.
- Track a creator's `followers_count` and `like_count` over time to compare accounts.
- Check whether an account exists and whether `profile_ban` is set before you show its content.
- Fill a third-party user record with the public Pipixia profile text and account creation date.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "3602444694069495"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | AKA user id, can be obtained from the share link. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "profile_ban": true,
    "user_info": {
      "achievements": [],
      "age": "36岁",
      "article_count": 0,
      "authentication": null,
      "author_ecom_info": null,
      "author_info": {
        "AuthorStatus": 1,
        "author_item_type": 1,
        "author_type": 104007473,
        "level": 0,
        "origin_status": 0,
        "owner": "script",
        "recommend_tag": "",
        "tags": []
      },
      "avatar": {
        "download_list": [
          {
            "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/ba804bc702db4d568d93d2ef2a8f…"
          }
        ],
        "height": 200,
        "is_gif": false,
        "uri": "tos-cn-i-8gu37r9deh/ba804bc702db4d568d93d2ef2a8f3c51",
        "url_list": [
          {
            "url": "https://p9-ppx-sign.byteimg.com/tos-cn-i-8gu37r9deh/ba804bc702db4d568d93d2ef2a8f…"
          }
        ],
        "width": 200
      },
      "background": {
        "download_list": [],
        "height": 0,
        "is_gif": false,
        "uri": "",
        "url_list": [],
        "width": 0
      },
      "birthday": null,
      "broadcast_info": null,
      "certify_info": null,
      "city": "武汉"
    }
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691716469
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user_info.id_str` | The user ID as a string. It matches the `user_id` you sent. Use this form instead of the numeric `data.user_info.id` to avoid precision loss. |
| `data.user_info.description` | The bio text the user wrote on their profile. |
| `data.user_info.followers_count / followings_count` | How many accounts follow this user, and how many accounts this user follows. |
| `data.user_info.like_count` | Total likes shown on the profile. |
| `data.user_info.city / city_name / age / horoscope` | Location, age and star sign text shown on the profile. In the sample these are Chinese strings, such as `36岁` for age. |
| `data.user_info.create_time` | Account creation time as a Unix timestamp in seconds. |
| `data.user_info.avatar.url_list[].url` | Signed URL of the 200 by 200 avatar image. The `width` and `height` fields sit next to it. |
| `data.user_info.large_avatar.url_list[].url` | Signed URL of the 600 by 600 avatar image. |
| `data.user_info.is_default_avatar / is_default_name` | Show whether the user still has the default avatar or the default name. |
| `data.profile_ban` | Boolean flag about the profile ban state. It is `true` in the sample response. |

### Notes

- Send `user_id` as a string. Take it from the user's Pipixia share link. If you only have a short link, try [Pipixia Short URL Conversion](/apis/pipixia/app/short-url) first.
- Many fields can be `null` or empty, such as `authentication`, `birthday` and `background`. Handle these cases in your code.
- Avatar URLs carry an `x-expires` query value and a signature. Save the image soon after you fetch it.
- To see what the user posted, call [Pipixia User Post List](/apis/pipixia/app/user-post-list). For their audience, call [Pipixia User Follower List](/apis/pipixia/app/user-follower-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/user-info.json`](../../../../catalog/models/pipixia/app/user-info.json) · Store page: https://www.sandbase.ai/model/pipixia/app/user-info
