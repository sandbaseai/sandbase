# Instagram User Reposts API: pricing, parameters and code examples

`instagram/user-reposts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

List the posts a public Instagram account has reposted to its feed, with cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/user-reposts", "userId": "787132"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/user-reposts', {'userId': '787132'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/user-reposts", {
  "userId": "787132"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/user-reposts", sandbase.Params{
	"userId": "787132",
})
```

Same call via the path form: `POST /v1/api/instagram/user-reposts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor from a previous response's nextCursor.  |
| `userId` | string | yes | Instagram's numeric account id, as returned by instagram.profile.  |

## Details

This API lists the posts a public Instagram account has reposted to its feed. It needs the account's numeric `userId` and returns one page of posts with the original author, caption, counts and media links.

### Use cases

- Track which creators and brands an account amplifies by reading the `author` and `authorId` of each reposted post.
- Measure the reach of reposted content using `likes`, `comments`, `views` and `reshares`.
- Collect the hashtags, mentions and coauthors in reposted posts to map partnerships around an account.
- Download the `videoUrl` or `image` of reposted reels and photos for review or archiving.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/user-reposts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "787132"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | Instagram's numeric account id, as returned by instagram.profile. |
| `cursor` | string | No | Pagination cursor from a previous response's nextCursor. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_iDvx70kyFbcBgthA-w9g_A",
    "posts": [
      {
        "audioId": "29204579829182362",
        "author": "natgeotravel",
        "authorId": "23947096",
        "authorName": "National Geographic Travel",
        "authorPrivate": false,
        "authorVerified": true,
        "avatarUrl": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/685024507_18593567491011…",
        "caption": "Lose yourself in the green heart of northern Peru, where ancient civilizations, …",
        "captionEdited": true,
        "coauthors": [],
        "comments": 70,
        "countsHidden": false
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.posts[]` | The reposted posts. Each item is one post from the original author's feed. |
| `data.posts[].author / authorId / authorName` | Username, numeric id and display name of the account that published the original post. |
| `data.posts[].authorVerified / authorPrivate` | Whether the original author is verified and whether the author account is private. |
| `data.posts[].id / shortcode / url` | The post's numeric id, its shortcode and the full Instagram link to the post. |
| `data.posts[].mediaType / productType` | The post format, such as `video` or `carousel`, and the Instagram product type, such as `clips` or `carousel_container`. |
| `data.posts[].caption` | The post caption text. `captionEdited` shows whether the caption was edited. |
| `data.posts[].likes / comments / views / reshares` | Engagement counts for the post. `views` and `reshares` appear on video posts only. |
| `data.posts[].createdUtc` | When the post was created, as a Unix timestamp in seconds. |
| `data.posts[].coauthors[] / taggedUsers[]` | Accounts credited as coauthors or tagged in the post, with `username`, `userId` and `displayName`. |
| `data.posts[].videoUrl / image / videoDurationSeconds` | Links to the video file and the preview image, and the video length in seconds. `videoUrl` appears on videos only. |
| `data.nextCursor` | Cursor for the next page of reposts. |

### Notes

- Get `userId` from [Instagram Profile](/apis/instagram/profile). The `userId` is a numeric string such as `787132`.
- To get the next page, pass `data.nextCursor` as `cursor` in the next request with the same `userId`.
- Some fields appear only on some posts. For example, `carouselCount` appears on carousels, and `audioId` and `soundTitle` appear on videos with audio.
- An older variant is also listed as [Instagram User Reposts](/apis/instagram/v1/user-reposts).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/user-reposts.json`](../../../catalog/models/instagram/user-reposts.json) · Store page: https://www.sandbase.ai/model/instagram/user-reposts
