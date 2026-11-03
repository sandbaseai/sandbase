# Reddit Subreddit Details API: pricing, parameters and code examples

`reddit/subreddit-details` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00038 per call · **Modes:** sync

Fetch a subreddit's metadata (weekly active users, description, and category).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00038**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/subreddit-details", "subreddit": "programming"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/subreddit-details', {'subreddit': 'programming'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/subreddit-details", {
  "subreddit": "programming"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/subreddit-details", sandbase.Params{
	"subreddit": "programming",
})
```

Same call via the path form: `POST /v1/api/reddit/subreddit-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `subreddit` | string | yes | Subreddit name without the r/ prefix. Case-sensitive (e.g. "AskReddit", not "askreddit").  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `weeklyActiveUsers` or `advertiserCategory`, and it is served only…  |

## Details

This API returns metadata for one subreddit, such as its ID, description, creation time, and icon. It needs the subreddit name without the `r/` prefix. The name is case-sensitive.

### Use cases

- Check that a subreddit exists before you fetch its posts.
- Store a subreddit's ID, name, and icon in a directory of communities.
- Compare the creation dates of several subreddits to see which communities are oldest.
- Read the weekly active user count and advertiser category for ad planning when the subreddit has them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/subreddit-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"subreddit": "programming"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit` | string | Yes | Subreddit name without the r/ prefix. Case-sensitive (e.g. "AskReddit", not "askreddit"). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `weeklyActiveUsers` or `advertiserCategory`, and it is served only by  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "advertiserCategory": null,
    "createdUtc": 1141150769,
    "description": "Computer Programming",
    "iconUrl": "https://styles.redditmedia.com/t5_2fwo/styles/communityIcon_1bqa1ibfp8q11.png?wi…",
    "id": "t5_2fwo",
    "name": "programming",
    "weeklyActiveUsers": null
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the subreddit exists. A lookup that finds nothing returns `false`. |
| `data.name` | The subreddit name without the `r/` prefix, such as `programming`. |
| `data.id` | The subreddit ID. It starts with `t5_`, for example `t5_2fwo`. |
| `data.description` | A short text description of the subreddit, such as `Computer Programming`. |
| `data.createdUtc` | The creation time of the subreddit as a Unix timestamp in seconds. |
| `data.iconUrl` | The URL of the subreddit's community icon image. |
| `data.weeklyActiveUsers` | The number of weekly active users. It is `null` when the serving source has no value for this subreddit. |
| `data.advertiserCategory` | The advertiser category of the subreddit. It is `null` when the serving source has no value for this subreddit. |

### Notes

- Pass the name exactly as it appears on Reddit. `AskReddit` works and `askreddit` does not.
- `weeklyActiveUsers` and `advertiserCategory` can come back as `null`. Add them to `requireFields` to route the call to a source that can return them. This can raise the price.
- For more detail on a community, try [Reddit App Subreddit Info](/apis/reddit/app/subreddit-info). For its posts, use [Reddit Subreddit Posts](/apis/reddit/subreddit-posts).

### Pricing

Billed at the actual cost of each call, about $0.00038 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/subreddit-details.json`](../../../catalog/models/reddit/subreddit-details.json) · Store page: https://www.sandbase.ai/model/reddit/subreddit-details
