# Kuaishou Hot Board Categories API: pricing, parameters and code examples

`kuaishou/app/hot-board-categories` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the active list of hot board categories available in the Kuaishou app. Use this endpoint to inspect category identifiers and names for trending content rankings.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/hot-board-categories"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/hot-board-categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/hot-board-categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/hot-board-categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/hot-board-categories` with the body above minus `model`.

## Details

Returns the list of hot board categories in the Kuaishou app. It needs no input. Each entry has a board ID, a board name, and a board type.

### Use cases

- Read the `boardId` and `type` values to build a request to the hot board detail API.
- Build a category menu from the `boardName` values in a trend tracking tool.
- Check which boards, such as the main hot list, the local board, or the entertainment board, are currently active.
- Collect the share titles and icons to reuse in a report or a link preview.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/hot-board-categories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "boards": [
    {
      "backgroundUrl": "",
      "bannerIconUrl": "https://tx2.a.kwimgs.com/udata/pkg/se-cdn/top_rd/top/rb_banner.jpg",
      "bannerLinkUrl": "",
      "boardId": 1,
      "boardName": "热榜",
      "darkBackgroundUrl": "",
      "entrySource": "search_entrance_consume_hotlist",
      "fromPage": 14,
      "shareIconUrl": "https://static.yximgs.com/udata/pkg/webserver/feed/share/hotBoard.png",
      "shareTitle": "快手热榜：看人生百态，览人间真实",
      "showType": 1,
      "subShareTitle": "全网热门现场，尽在快手热榜"
    }
  ],
  "host-name": "public-bjx-c34-kce-node3020.idchb1az1.hb1.kwaidc.com",
  "location": "{\"province\":\"福建\",\"cityName\":\"漳州\"}",
  "result": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `boards[]` | List of hot board categories. Each item is one board. |
| `boards[].boardId` | Numeric ID of the board, for example `1` for the main hot list and `9` for the local board. |
| `boards[].boardName` | Display name of the board in Chinese, for example `热榜`, `本地榜`, `文娱榜`. |
| `boards[].type` | Numeric board type. It differs from `boardId`, for example `boardId` `9` has `type` `7`. |
| `boards[].entrySource` | Entry source label for the board, for example `search_entrance_consume_hotlist`. |
| `boards[].shareTitle / boards[].subShareTitle` | Title and subtitle text the app uses when a user shares the board. |
| `boards[].bannerIconUrl / boards[].shareIconUrl` | Image URLs for the board banner and the share icon. |
| `boards[].showType / boards[].fromPage` | Numeric display settings returned for each board. |
| `result` | Status code of the call. The value `1` appears in this response. |
| `location` | JSON string with the `province` and `cityName` the response was resolved for. |

### Notes

- The request body is an empty object `{}`. The API has no parameters.
- Pass `boardId` and `type` from this response to [Kuaishou Hot Board Detail](/apis/kuaishou/app/hot-board-detail) to read the items on a board.
- The `location` field is a JSON string. Parse it before you read `province` or `cityName`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Detail](/apis/kuaishou/app/hot-board-detail): Returns trending topics and search keywords from Kuaishou hot boards based on the specified board identifier and board type.

---
Machine-readable: [`catalog/models/kuaishou/app/hot-board-categories.json`](../../../../catalog/models/kuaishou/app/hot-board-categories.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/hot-board-categories
