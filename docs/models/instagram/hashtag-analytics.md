# Instagram Hashtag Analytics API: pricing, parameters and code examples

`instagram/hashtag-analytics` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Get the total post count for any Instagram hashtag.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/hashtag-analytics", "hashtag": "travel"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/hashtag-analytics', {'hashtag': 'travel'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/hashtag-analytics", {
  "hashtag": "travel"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/hashtag-analytics", sandbase.Params{
	"hashtag": "travel",
})
```

Same call via the path form: `POST /v1/api/instagram/hashtag-analytics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Deprecated. Has no effect. range 1–20 |
| `hashtag` | string | yes | The Instagram hashtag to analyze, with or without the # symbol (e.g. streetphotography).  |

## Details

This API returns the total post count for one Instagram hashtag. It needs a `hashtag` value, with or without the # symbol.

### Use cases

- Compare the size of several hashtags before you pick tags for a campaign.
- Track how the post count of a niche hashtag changes by calling it on a schedule.
- Show a short post count such as `798M` next to a hashtag in a dashboard.
- Check that a hashtag exists before you request its posts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/hashtag-analytics" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 5, "hashtag": "travel"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hashtag` | string | Yes | The Instagram hashtag to analyze, with or without the # symbol (e.g. streetphotography). |
| `limit` | integer | No | Deprecated. Has no effect. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "id": "17843819167049166",
        "name": "travel",
        "postsCount": 798659650,
        "postsFormatted": "798M",
        "url": "https://www.instagram.com/explore/tags/travel"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the hashtag was found. A lookup that finds nothing returns `found: false`. |
| `data.items[].name` | The hashtag name, without the # symbol. |
| `data.items[].id` | The Instagram ID of the hashtag, as a string. |
| `data.items[].postsCount` | The total number of posts that use the hashtag, as a full number. |
| `data.items[].postsFormatted` | The same post count in short form, for example `798M`. |
| `data.items[].url` | Link to the hashtag page on Instagram. |

### Notes

- The `limit` parameter is deprecated and has no effect. You can leave it out.
- The response holds one entry in `data.items[]`. Read `postsCount` for exact math and `postsFormatted` for display.
- To see posts under a hashtag, call [Instagram Hashtag Top Posts](/apis/instagram/hashtag-top-posts) or [Instagram Hashtag Recent Posts](/apis/instagram/hashtag-recent-posts).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/hashtag-analytics.json`](../../../catalog/models/instagram/hashtag-analytics.json) · Store page: https://www.sandbase.ai/model/instagram/hashtag-analytics
