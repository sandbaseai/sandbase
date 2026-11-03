# Kuaishou Web Hot List (V2) API: pricing, parameters and code examples

`kuaishou/web/hot-list-v2` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns current trending search rankings and hot topics on Kuaishou web. Supports selecting different ranking boards using the board type parameter.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/web/hot-list-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/web/hot-list-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/web/hot-list-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/web/hot-list-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/kuaishou/web/hot-list-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `board_type` | string |  | 榜单类型 (board_type)/Board Type default `"1"` |

## Details

Returns the current trending search list on Kuaishou web, with each keyword, its heat value and a ranking entry ID. It takes an optional `board_type` string to pick a ranking board, and the default is `"1"`.

### Use cases

- Track which topics rank highest on Kuaishou web at the moment you call.
- Compare `hotValue` across keywords to see how far the top entries lead the rest of the board.
- Log the board on a schedule to build a history of which keywords entered the ranking and when.
- Spot pinned entries by reading the separate `topHots` list next to the main `hots` list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/web/hot-list-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `board_type` | string | No |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "host-name": "public-bjmt-c58-kce-node10.idchb1az4.hb1.kwaidc.com",
  "hots": [
    {
      "hotValue": 12950162,
      "hotWordType": 0,
      "id": "6489869",
      "keyword": "多海域连发航行警告",
      "ksOrderId": "",
      "pvSoarSignal": 0,
      "viewCount": 0
    }
  ],
  "llsid": "2006450543472340162",
  "result": 1,
  "topHots": [
    {
      "hotValue": 12979279,
      "hotWordType": 2,
      "id": "6493160",
      "keyword": "让互联网更好造福人民造福世界",
      "ksOrderId": "",
      "pvSoarSignal": 0,
      "viewCount": 0
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hots[]` | The main ranked list of trending keywords. Entries appear in descending order of `hotValue` in the sample. |
| `hots[].keyword` | The trending search phrase as shown on the board. |
| `hots[].hotValue` | Numeric heat score for the keyword. A higher number means a hotter entry. |
| `hots[].id` | String ID of the hot entry. |
| `hots[].hotWordType / topHots[].hotWordType` | Integer type code for the entry. Regular entries show `0` and the pinned entry shows `2` in the sample. The response does not explain what each code means. |
| `hots[].iconInfo.iconUrl[].url` | Image URL of a badge shown beside some keywords. Each item has a `cdn` host name and a `url`. `iconWidth` and `iconHeight` give the icon size. |
| `hots[].viewCount / hots[].pvSoarSignal` | Extra counters on each entry. Both are `0` in the sample, so they may be empty for many keywords. |
| `topHots[]` | A separate list of top entries, with the same fields as `hots[]`. The sample holds one item. |
| `result` | Status number for the call. The sample shows `1`. |
| `llsid` | String ID that identifies this response. |

### Notes

- `board_type` is a string. Leave it out to use the default `"1"`.
- Both `hots` and `topHots` use the same entry shape, so one parser can handle both.
- `iconInfo` appears only on some entries, so check that it exists before reading it.
- For the older version of this board, call [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Kuaishou Web Share Short URL](/apis/kuaishou/web/generate-share-short-url): Returns a shareable short URL for a specified Kuaishou video or photo post.
- [Kuaishou User ID Lookup](/apis/kuaishou/web/get-user-id): Resolves a Kuaishou user ID from a provided user share link.
- [Kuaishou Web Hot List](/apis/kuaishou/web/hot-list-v1): Returns the current trending hot list from Kuaishou Web.

---
Machine-readable: [`catalog/models/kuaishou/web/hot-list-v2.json`](../../../../catalog/models/kuaishou/web/hot-list-v2.json) · Store page: https://www.sandbase.ai/model/kuaishou/web/hot-list-v2
