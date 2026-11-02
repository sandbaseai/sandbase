# TikTok Livestream Room Product List API: pricing, parameters and code examples

`tiktok/app-v3/live-room-product-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the list of showcase products featured in a broadcast session based on the specified room and author identifiers, with support for region filtering and pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/live-room-product-list", "author_id": "7408859677050274859", "room_id": "7420741353250507562"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/live-room-product-list', {'author_id': '7408859677050274859', 'room_id': '7420741353250507562'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/live-room-product-list", {
  "author_id": "7408859677050274859",
  "room_id": "7420741353250507562"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/live-room-product-list", sandbase.Params{
	"author_id": "7408859677050274859",
	"room_id": "7420741353250507562",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/live-room-product-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Page turning cursor, optional parameter, default is 0, increasing by 15 each time.  |
| `region` | string |  | Region, optional parameter, default is `US`. Other regions (for example `VN`) may return no data.  |
| `room_id` | string | yes | Live room id, required parameter.  |
| `author_id` | string | yes | Anchor id, required parameter.  |
| `page_size` | integer |  | Number per page, optional parameter, default is 15.  |

## Details

Retrieve products featured during a broadcast room session by providing `room_id` and `author_id`. You can also configure pagination parameters and specify a `region`.

### Use cases

- Track showcase items featured during broadcast room sessions.
- Catalog merchandise promoted by specific broadcast hosts.
- Inspect regional product selections tied to broadcast rooms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/live-room-product-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"author_id": "<author_id>", "room_id": "<room_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room id, required parameter. |
| `author_id` | string | Yes | Anchor id, required parameter. |
| `offset` | integer | No | Page turning cursor, optional parameter, default is 0, increasing by 15 each time. |
| `region` | string | No | Region, optional parameter, default is `US`. |
| `page_size` | integer | No | Number per page, optional parameter, default is 15. |

### Notes

- `room_id` and `author_id` are required to query the product list.
- The `region` parameter defaults to `US`, and other regions like `VN` may return no data.
- Pagination is controlled with `offset` (default 0, incrementing by 15) and `page_size` (default 15).

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/live-room-product-list.json`](../../../../catalog/models/tiktok/app-v3/live-room-product-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/live-room-product-list
