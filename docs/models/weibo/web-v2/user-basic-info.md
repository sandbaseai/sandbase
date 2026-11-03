# Weibo User Basic Information API: pricing, parameters and code examples

`weibo/web-v2/user-basic-info` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns lightweight basic profile information for a specified Weibo user. Provide the target account identifier to retrieve user details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-basic-info", "uid": "7648703289"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-basic-info', {'uid': '7648703289'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-basic-info", {
  "uid": "7648703289"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-basic-info", sandbase.Params{
	"uid": "7648703289",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-basic-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |

## Details

Returns a short public profile for one Weibo user, including name, avatar, cover image, bio, gender, follower count and following count. It needs the numeric user ID in the `uid` parameter.

### Use cases

- Show a Weibo user's name, avatar and bio on a dashboard or contact card.
- Check whether an account is verified before adding it to an influencer list.
- Read the displayed follower count of an account to compare creators.
- Confirm that a numeric `uid` maps to the expected `screen_name`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-basic-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "7648703289"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatar": "https://tvax3.sinaimg.cn/crop.0.0.1080.1080.180/008lDb85ly8ha4by3jwh3j30u00u0q47…",
    "block": false,
    "cover": "https://ww1.sinaimg.cn/mw690/9d44112bjw1f1xl1c10tuj20hs0hs0tw.jpg",
    "descText": "恨比爱长久",
    "follow_me": false,
    "followers_count_str": "362.4万",
    "following": false,
    "friends_count_str": 292,
    "gender": "f",
    "genderText": "她",
    "id": 7648703289,
    "idstr": "7648703289"
  },
  "ok": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.screen_name` | Display name of the user. |
| `data.id / data.idstr` | The user ID as a number and as a string. Both match the `uid` you sent. |
| `data.descText` | The bio text on the profile. |
| `data.followers_count_str` | Follower count as a display string, for example `362.4万`. It is not a plain integer, so parse the unit suffix yourself. |
| `data.friends_count_str` | Count of accounts this user follows. It appears as a number in this response. |
| `data.gender / data.genderText` | Gender code (`f` here) and the pronoun label shown on the profile (`她` here). |
| `data.verified / data.verified_type` | Whether the account is verified, and a numeric verification type. The value `-1` appears with `verified` set to `false`. |
| `data.avatar / data.cover` | URLs of the profile picture and the cover image. |
| `data.profile_url` | Relative profile path, in the form `u/<uid>`. |
| `data.follow_me / data.following / data.special_follow / data.block` | Relationship flags between the user and the calling account. All are `false` in this response. |

### Notes

- Pass `uid` as a string of digits, such as `7648703289`.
- The avatar URL contains `Expires` and `ssig` query values, so it may stop working later. Save the image if you need to keep it.
- For more profile data, call [Weibo User Profile Details (Web V2)](/apis/weibo/web-v2/user-info).
- To read the user's content, call [Weibo User Posts](/apis/weibo/web-v2/user-posts) or [Weibo User Follower List](/apis/weibo/web-v2/user-fans).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-basic-info.json`](../../../../catalog/models/weibo/web-v2/user-basic-info.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-basic-info
