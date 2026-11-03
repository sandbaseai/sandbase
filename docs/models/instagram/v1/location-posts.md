# Instagram Location Posts (V1) API: pricing, parameters and code examples

`instagram/v1/location-posts` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts tagged at a designated location. Supports sorting by top or latest posts alongside cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v1/location-posts", "location_id": "703457703"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v1/location-posts', {'location_id': '703457703'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v1/location-posts", {
  "location_id": "703457703"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v1/location-posts", sandbase.Params{
	"location_id": "703457703",
})
```

Same call via the path form: `POST /v1/api/instagram/v1/location-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tab` | string |  | Sorting method, ranked(top)/recent(latest) default `"ranked"` |
| `end_cursor` | string |  | Pagination cursor, omit for first request  |
| `location_id` | string | yes | Location ID  |

## Details

Returns a page of Instagram posts tagged at one location. It needs a `location_id`, and you can choose top or latest posts with `tab`.

### Use cases

- Pull the posts tagged at a venue or landmark to see what visitors share there.
- Collect the latest posts at a store location with `tab` set to `recent`.
- Page through a location feed with `end_cursor` to build a dataset of location-tagged media.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v1/location-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_id": "703457703"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location_id` | string | Yes | Location ID |
| `end_cursor` | string | No | Pagination cursor, omit for first request |
| `tab` | string | No | Sorting method, ranked(top)/recent(latest) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "attempts": "14",
  "edges": [
    {
      "cursor": null,
      "node": {
        "__typename": "XDTMediaDict",
        "accessibility_caption": null,
        "ad_id": null,
        "affiliate_info": null,
        "audience": null,
        "boost_unavailable_identifier": null,
        "boost_unavailable_reason": null,
        "boosted_status": null
      }
    }
  ],
  "page_info": {
    "end_cursor": "a1214191bfcb4d848b21401eac8045a9",
    "has_next_page": true
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `edges[]` | One post tagged at the location. The list holds a page of results. |
| `edges[].node` | The media object for the post. |
| `edges[].node.__typename` | The type of the media object. The sample shows `XDTMediaDict`. |
| `edges[].cursor` | Per-item cursor. It is `null` in the sample, so use `page_info.end_cursor` to page. |
| `edges[].node.accessibility_caption` | Accessibility caption for the media. It is `null` in the sample. |
| `edges[].node.ad_id / edges[].node.boosted_status` | Ad and boost details for the post. They are `null` in the sample, so the posts shown are not marked as ads. |
| `page_info.end_cursor` | Cursor for the next page. Send it as `end_cursor` in the next request. |
| `page_info.has_next_page` | `true` when more posts are available after this page. |
| `attempts` | Number of attempts made to build this response. The sample value is `14`. |

### Notes

- Send only `location_id` on the first request. Then pass `page_info.end_cursor` as `end_cursor` to get the next page.
- `tab` accepts `ranked` for top posts (the default) and `recent` for latest posts.
- Many `node` fields come back as `null` in the sample, so check each field before you use it.
- Use [Instagram Location Details (V1)](/apis/instagram/v1/location-info) to look up details for the same `location_id`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Cities by Country](/apis/instagram/v1/cities): Returns a list of Instagram cities and regions for a specified country code.
- [Instagram Hashtag Posts (V1)](/apis/instagram/v1/hashtag-posts): Returns public Instagram posts associated with a specific hashtag.
- [Instagram Location Details (V1)](/apis/instagram/v1/location-info): Returns detailed metadata and profile information for a specified Instagram location using its unique identifier.

---
Machine-readable: [`catalog/models/instagram/v1/location-posts.json`](../../../../catalog/models/instagram/v1/location-posts.json) · Store page: https://www.sandbase.ai/model/instagram/v1/location-posts
