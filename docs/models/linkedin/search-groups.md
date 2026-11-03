# LinkedIn Group Search API: pricing, parameters and code examples

`linkedin/search-groups` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0013 per call · **Modes:** sync

Search LinkedIn groups by keyword, 10 per page: group name, URL, member count, summary, and logo.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0013**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-groups", "query": "python"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-groups', {'query': 'python'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-groups", {
  "query": "python"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-groups", sandbase.Params{
	"query": "python",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-groups` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Which page of up to 10 groups to return, starting at 1 (1-100, default 1). Each page is billed as one request. default `1`; range 1–100 |
| `query` | string | yes | Keyword to search LinkedIn groups for (e.g. python or sales).  |

## Details

This API searches LinkedIn groups by keyword and returns up to 10 groups per page. Each result has the group name, URL, a short description, a member count label, and a logo image. It needs a `query` keyword.

### Use cases

- Find large LinkedIn groups about a topic such as Python to decide where to share content.
- Build a list of niche professional communities for outreach or market research.
- Compare the reach of competing groups by reading their member count labels.
- Collect group IDs to pass to a group lookup or group posts call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-groups" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "python"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search LinkedIn groups for (e.g. python or sales). |
| `page` | integer | No | Which page of up to 10 groups to return, starting at 1 (1-100, default 1). Each page is billed as one request. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "description": "Scikit-Learn, Claude AI, Claude Code, Claude Mythos, OpenClaw, Keras, NumPy, Moj…",
        "id": "25827",
        "image": "https://media.licdn.com/dms/image/v2/D4E07AQGgKbsF_8T1UQ/group-logo_image-shrink…",
        "membersText": "3M members",
        "name": "Python Developers Community (moderated)",
        "url": "https://www.linkedin.com/groups/25827"
      }
    ],
    "page": 1,
    "totalPages": 100,
    "totalResults": 4967
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].name` | Name of the LinkedIn group. |
| `data.items[].url` | Link to the group page on LinkedIn. |
| `data.items[].id` | Numeric group ID as a string. It is also the last part of the group URL. |
| `data.items[].membersText` | Member count as display text, for example `3M members`. It is a rounded label, not an exact number. |
| `data.items[].description` | Short summary of the group. Long text is cut off with an ellipsis. |
| `data.items[].image` | URL of the group logo image. |
| `data.page` | Page number of this result set. |
| `data.totalPages` | Number of result pages available for the query. |
| `data.totalResults` | Total number of groups that matched the query. |
| `found` | `true` when the search returned results. |

### Notes

- Use `page` from 1 to 100 to move through results. Each page holds up to 10 groups.
- `membersText` is a string such as `984K members`, so parse it yourself if you need a number.
- Pass a group `id` or `url` to [LinkedIn Group](/apis/linkedin/group) for group details, or to [LinkedIn Group Posts](/apis/linkedin/group-posts) for its posts.

### Pricing

Billed at the actual cost of each call, about $0.0013 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/search-groups.json`](../../../catalog/models/linkedin/search-groups.json) · Store page: https://www.sandbase.ai/model/linkedin/search-groups
