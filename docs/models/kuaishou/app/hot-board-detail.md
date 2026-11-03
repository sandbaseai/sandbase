# Kuaishou Hot Board Detail API: pricing, parameters and code examples

`kuaishou/app/hot-board-detail` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending topics and search keywords from Kuaishou hot boards based on the specified board identifier and board type.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/hot-board-detail"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/hot-board-detail', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/hot-board-detail", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/hot-board-detail", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/app/hot-board-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `boardId` | integer |  | 榜单ID/Board ID  |
| `boardType` | integer |  | 榜单类型/Board type default `1` |

## Details

Returns the trending keywords on a Kuaishou hot board, with a heat value and view count for each keyword. The request takes a `boardId` and a `boardType` (default `1`). The response also lists pinned keywords in a separate `topHots` array.

### Use cases

- Track which keywords rank highest on a Kuaishou hot board and how their `hotValue` changes between checks.
- Compare `viewCount` across ranked keywords to see which topics draw the most views.
- Collect pinned keywords from `topHots` to see which topics Kuaishou promotes at the top of a board.
- Feed ranked keywords into a search or video lookup to study content around a trending topic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/hot-board-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `boardId` | integer | No |  |
| `boardType` | integer | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "host-name": "public-bjzey-c37-kce-node10.idchb1az3.hb1.kwaidc.com",
  "hots": [
    {
      "hotValue": 10868868,
      "hotWordType": 0,
      "id": "6489869",
      "keyword": "多海域连发航行警告",
      "ksOrderId": "",
      "newHotTypes": [
        18
      ],
      "normalIndex": 1,
      "pvSoarSignal": 0,
      "viewCount": 11365489,
      "wordId": "6489869"
    }
  ],
  "llsid": "2010304412958466273",
  "result": 1,
  "topHots": [
    {
      "hotValue": 0,
      "hotWordType": 2,
      "id": "6493160",
      "keyword": "让互联网更好造福人民造福世界",
      "ksOrderId": "",
      "newHotTypes": [
        18
      ],
      "pvSoarSignal": 0,
      "viewCount": 11536,
      "wordId": "6493160"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hots[]` | Ranked list of trending keywords on the board. |
| `hots[].keyword` | Text of the trending topic or search keyword. |
| `hots[].normalIndex` | Rank position of the keyword in the list. The value `1` is the top entry. |
| `hots[].hotValue` | Heat score of the keyword. Higher values rank higher. |
| `hots[].viewCount` | View count tied to the keyword. |
| `hots[].id / hots[].wordId` | String ID of the keyword. Both fields hold the same value in the sample. |
| `hots[].newHotTypes` | List of numeric tag codes attached to the keyword. The response does not explain what each code means. |
| `topHots[]` | Pinned keywords shown above the ranked list. Entries have `hotValue` set to `0` and no `normalIndex`. |
| `topHots[].keyword` | Text of the pinned topic. |
| `result` | Status code of the call. The value `1` appears in the sample response. |

### Notes

- Both parameters are optional in the schema. `boardType` defaults to `1`.
- Get valid `boardId` values from [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories).
- Keyword IDs are strings, while `hotValue`, `viewCount` and `normalIndex` are numbers.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Brand Top List](/apis/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/apis/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/apis/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/hot-board-detail.json`](../../../../catalog/models/kuaishou/app/hot-board-detail.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/hot-board-detail
