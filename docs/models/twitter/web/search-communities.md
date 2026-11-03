# Twitter Search communities API: pricing, parameters and code examples

`twitter/web/search-communities` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search communities on Twitter. Returns the platform data as structured JSON.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/search-communities", "keyword": "superman"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/search-communities', {'keyword': 'superman'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/search-communities", {
  "keyword": "superman"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/search-communities", sandbase.Params{
	"keyword": "superman",
})
```

Same call via the path form: `POST /v1/api/twitter/web/search-communities` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor  |
| `keyword` | string | yes | Search Keyword  |

## Details

Returns a list of Twitter communities that match a search keyword. Each result includes the community name, ID, primary topic, member count and banner images. The only required input is `keyword`.

### Use cases

- Find communities about a topic or franchise, such as `superman`, to join or study.
- Rank communities on a topic by `member_count` to see which ones are largest.
- Collect community IDs to feed into community info, member or timeline lookups.
- Filter out adult communities with the `is_nsfw` flag before showing results in an app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/search-communities" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "superman"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keyword |
| `cursor` | string | No | Cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "communities": [
    {
      "community_id": "1589365710655979520",
      "custom_banner": "https://pbs.twimg.com/community_banner_img/2107751704808579073/T11UFoyj?format=j…",
      "default_banner": "https://pbs.twimg.com/media/FECQfL3UcAc3IfU.jpg",
      "is_nsfw": false,
      "member_count": 111548,
      "name": "DC",
      "primary_topic": "Comics",
      "user_id": ""
    }
  ],
  "next_cursor": "WzgwLjQwNzEzLDE5NDM5Mjk1MzU4ODU3MjIwMTBd"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `communities[]` | List of communities that match the keyword. |
| `communities[].community_id` | ID of the community as a numeric string. Use it to look up the community in other APIs. |
| `communities[].name` | Display name of the community. |
| `communities[].member_count` | Number of members in the community. |
| `communities[].primary_topic` | Main topic label of the community, such as `Comics` or `Movies`. |
| `communities[].is_nsfw` | `true` if the community is marked as adult content, `false` otherwise. |
| `communities[].custom_banner / communities[].default_banner` | Banner image URLs. `custom_banner` is the image the community set, and `default_banner` is a stock image. |
| `communities[].user_id` | User ID field. It was an empty string in the sample response. |
| `next_cursor` | Cursor string for the next page of results. |

### Notes

- Pass `next_cursor` from the response as `cursor` in the next request to get more results.
- `community_id` is a numeric string. Pass it to [Twitter Community info](/apis/twitter/web/community-info) for details about one community.
- Use [Twitter Community timeline](/apis/twitter/web/community-timeline) to read the posts of a community you found.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/web/search-communities.json`](../../../../catalog/models/twitter/web/search-communities.json) · Store page: https://www.sandbase.ai/model/twitter/web/search-communities
