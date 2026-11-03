# Zhihu User Pins API: pricing, parameters and code examples

`zhihu/web/user-pins` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of pins or moments posted by a specific Zhihu user. Supports pagination controls using offset and limit parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-pins", "user_url_token": "excited-vczh"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-pins', {'user_url_token': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-pins", {
  "user_url_token": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-pins", sandbase.Params{
	"user_url_token": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-pins` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of pins per page  |
| `offset` | string |  | Offset  |
| `user_url_token` | string | yes | User ID  |

## Details

Returns a page of pins (short posts or moments) published by one Zhihu user. The only required input is the user's `user_url_token`, and `limit` and `offset` control paging.

### Use cases

- Build a timeline of short posts from a Zhihu creator's profile.
- Archive a user's pins page by page with `offset`.
- Check whether a Zhihu account has posted any pins before you fetch more data.
- Collect pin IDs to pass to a pin detail or pin comments lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-pins" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_url_token": "excited-vczh"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_url_token` | string | Yes | User ID |
| `limit` | string | No | Number of pins per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [],
  "paging": {
    "is_end": true,
    "is_start": true,
    "next": "https://www.zhihu.com/api/v4/v2/pins/excited-vczh/moments?includes=data%5B%2A%5D…",
    "previous": "https://www.zhihu.com/api/v4/v2/pins/excited-vczh/moments?includes=data%5B%2A%5D…",
    "totals": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data` | List of pins on the current page. It is an empty list when the user has no pins, as in the example response. |
| `paging.totals` | Total number of pins the response reports for this user. It is `0` in the example. |
| `paging.is_end / paging.is_start` | Booleans that show whether this page is the last page or the first page of the list. |
| `paging.next` | URL for the next page. It carries the `limit` and `offset` values for that page. |
| `paging.previous` | URL for the previous page. It carries the `limit` and `offset` values for that page. |

### Notes

- `user_url_token` is the slug in a Zhihu profile URL, for example `excited-vczh` in `zhihu.com/people/excited-vczh`.
- The `next` and `previous` links in `paging` show a default page size of `20` and step the `offset` by that amount.
- Stop paging when `paging.is_end` is `true`.
- To read one pin in full, call [Zhihu Pin Detail](/apis/zhihu/web/pin-detail). For its replies, call [Zhihu Pin Comments](/apis/zhihu/web/pin-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-pins.json`](../../../../catalog/models/zhihu/web/user-pins.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-pins
