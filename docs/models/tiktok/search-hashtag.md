# TikTok Hashtag Search API: pricing, parameters and code examples

`tiktok/search-hashtag` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search TikTok by hashtag and get matching videos (caption, views, likes, comments, shares) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/search-hashtag", "query": "recipe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/search-hashtag', {'query': 'recipe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/search-hashtag", {
  "query": "recipe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/search-hashtag", sandbase.Params{
	"query": "recipe",
})
```

Same call via the path form: `POST /v1/api/tiktok/search-hashtag` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Hashtag or keyword to search for (without the leading #).  |
| `cursor` | string |  | Pagination cursor from a previous response.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle` or `locationName`, and it is served only by a source…  |

## Details

This API returns TikTok videos that match a hashtag or keyword. It needs one input, `query`, which is the hashtag text without the leading #. Each video includes its caption, author, engagement counts, sound details and links.

### Use cases

- Find top-performing videos for a hashtag such as `recipe` to see what content gets the most views.
- Collect creators who post under a niche hashtag and rank them by `views`, `likes` or `saves`.
- Track which sounds are used in videos for a topic by reading `soundTitle` and `soundAuthor`.
- Build a dataset of captions and co-used hashtags to study how a topic is described.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/search-hashtag" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "recipe"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Hashtag or keyword to search for (without the leading #). |
| `cursor` | string | No | Pagination cursor from a previous response. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `soundTitle` or `locationName`, and it is served only by a source that |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "nextCursor": "cur_TBtidisJbVI12bgEDrnxcA",
    "videos": [
      {
        "author": "thehomemaderecipe",
        "authorImage": "https://p16-common-sign.tiktokcdn-eu.com/tos-maliva-avt-0068/b386c207818f2066ea2…",
        "authorName": "The Homemade Recipe",
        "authorUserId": "7504858285972735018",
        "authorVerified": false,
        "caption": "I learned this chicken recipe at a Chinese restaurant. You have to try it! #chic…",
        "comments": 776,
        "createdUtc": 1761662258,
        "durationSeconds": 88.047,
        "hashtags": [
          "chicken"
        ],
        "id": "7566281652981353758",
        "image": "https://p16-common-sign.tiktokcdn-eu.com/tos-useast8-p-0068-tx2/oE6R3AEAFAnSeBVl…"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.videos[].id / data.videos[].url` | The video ID and the public TikTok link to the video. |
| `data.videos[].caption` | The video caption text, including inline hashtags. |
| `data.videos[].hashtags[]` | Hashtags used on the video, listed without the # sign. |
| `data.videos[].views / likes / comments / shares / saves` | Engagement counts for the video as whole numbers. |
| `data.videos[].author / authorName / authorUserId` | The author's handle, display name and numeric user ID. |
| `data.videos[].authorVerified` | Whether the author account is marked as verified. |
| `data.videos[].createdUtc` | Creation time of the video as a Unix timestamp in seconds. |
| `data.videos[].durationSeconds` | Length of the video in seconds. |
| `data.videos[].soundTitle / soundAuthor / soundClipId` | The title, author and ID of the sound used in the video. |
| `data.videos[].locationName` | The location tagged on the video. It is `null` when none is set. |
| `data.nextCursor` | Cursor string to pass as `cursor` to get the next page of results. |

### Notes

- To get the next page, send the same `query` with `cursor` set to the `data.nextCursor` value from the previous response.
- Use `requireFields` with `soundTitle`, `soundAuthor` or `locationName` if your request must be served by a source that returns those fields.
- `videoUrl`, `image` and `authorImage` are direct media links and may be long, so store the video `id` and `url` as your stable reference.
- For details on one video, call [TikTok Video Details](/apis/tiktok/app-v3/one-video). For hashtag-level data, use [TikTok Hashtag Detail](/apis/tiktok/app-v3/hashtag-detail).

### Pricing

Billed at the actual cost of each call, about $0.0012 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/search-hashtag.json`](../../../catalog/models/tiktok/search-hashtag.json) · Store page: https://www.sandbase.ai/model/tiktok/search-hashtag
