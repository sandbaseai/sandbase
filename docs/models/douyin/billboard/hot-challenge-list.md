# Douyin Hot Challenge List API: pricing, parameters and code examples

`douyin/billboard/hot-challenge-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending Douyin challenge leaderboard entries with rank, hot score, and video counts. Supports filtering by keyword and page-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-challenge-list", "page": 1, "page_size": 10}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-challenge-list', {'page': 1, 'page_size': 10})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-challenge-list", {
  "page": 1,
  "page_size": 10
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-challenge-list", sandbase.Params{
	"page": 1,
	"page_size": 10,
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-challenge-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer | yes | Page number  |
| `keyword` | string |  | Hot search term default `""` |
| `page_size` | integer | yes | Number of items per page  |

## Details

Returns the Douyin hot challenge leaderboard as a ranked list. Each entry has a rank, a hot score, a video count, and a short hot score history. The request needs `page` and `page_size`, and accepts an optional `keyword`.

### Use cases

- Track which challenge topics hold the top ranks on Douyin right now.
- Chart the hot score history of a challenge from its `trends` list.
- Filter the leaderboard with `keyword` to find challenges on one theme.
- Collect `sentence_id` values to join challenge entries with data from other Douyin APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-challenge-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page": 1, "page_size": 10}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | Yes | Page number |
| `page_size` | integer | Yes | Number of items per page |
| `keyword` | string | No | Hot search term |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "last_update_time": "20261103152500",
    "objs": [
      {
        "SnapshotID": 20261103152500,
        "SnapshotSubType": "hotspot_challenge",
        "SnapshotType": 2,
        "allow_publish": false,
        "city_code": 0,
        "city_name": "",
        "create_at": 1793592534,
        "first_item_cover_url": "",
        "hot_score": 9088842,
        "index": 1,
        "is_favorite": false,
        "item_list": null
      }
    ],
    "page": {
      "page": 1,
      "page_size": 100,
      "total": 50
    }
  },
  "extra": {
    "now": 1793691107000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.objs[].sentence` | Name of the challenge topic, as Douyin shows it on the leaderboard. |
| `data.objs[].sentence_id` | Numeric ID of the challenge topic. |
| `data.objs[].rank / data.objs[].index` | Position of the entry on the leaderboard, starting at 1. |
| `data.objs[].hot_score` | Current hot score of the challenge. Higher scores rank higher. |
| `data.objs[].video_count` | Video count for the challenge entry, as returned on the leaderboard. |
| `data.objs[].trends[].datetime / data.objs[].trends[].hot_score` | Past hot score samples. `datetime` uses the format `YYYYMMDDHHMMSS`. |
| `data.objs[].create_at` | Unix timestamp in seconds for the entry. |
| `data.objs[].sentence_tag` | Numeric tag code for the challenge. `sentence_tag_name` is empty in this response. |
| `data.last_update_time` | Time of the latest leaderboard snapshot, in the format `YYYYMMDDHHMMSS`. |
| `data.page.page / data.page.page_size / data.page.total` | Pagination info. `total` is the number of entries in the leaderboard. |

### Notes

- `page` and `page_size` are both required. Increase `page` to read further entries.
- The `page.page_size` value in the response can differ from the `page_size` you sent, so check the number of items in `objs`.
- `SnapshotID` has the same format as `last_update_time`, so you can use it to see which snapshot an entry came from.
- For a rising-topic view, try [Douyin Rising Hot Search List](/apis/douyin/billboard/hot-rise-list) or [Douyin Hot Topic Billboard](/apis/douyin/billboard/hot-total-topic-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-challenge-list.json`](../../../../catalog/models/douyin/billboard/hot-challenge-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-challenge-list
