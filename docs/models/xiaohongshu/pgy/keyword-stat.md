# Xiaohongshu PGY keyword overview API: pricing, parameters and code examples

`xiaohongshu/pgy/keyword-stat` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

PGY keyword overview on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/keyword-stat", "search_word": "面膜"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/keyword-stat', {'search_word': '面膜'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/keyword-stat", {
  "search_word": "面膜"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/keyword-stat", sandbase.Params{
	"search_word": "面膜",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/keyword-stat` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `search_word` | string | yes | Keyword  |

## Details

Returns an overview of one keyword on Xiaohongshu's PGY (Pugongying) creator platform. It includes engagement and exposure totals for the keyword, plus a profile of the creators who post about it. The only input is the `search_word` keyword.

### Use cases

- Compare how much search interest and note volume two product keywords such as `面膜` have before picking a campaign topic.
- Check which creator follower tiers and price tiers dominate a keyword to set a realistic influencer budget.
- Find the content tags and feature tags tied to a keyword to shape a brief for creators.
- Track the 30-day change figures of a keyword to see if interest is rising or falling.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/keyword-stat" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_word": "面膜"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_word` | string | Yes | Keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "searchWordData": {
      "brandTag": 0,
      "cmtNum": 1560934,
      "dateKey": null,
      "engageNum": 27873561,
      "engageNum30bm": "24.9",
      "favNum": 6604839,
      "followCnt": 1175571,
      "impNum": 4300308291,
      "impNum30bm": "52.4",
      "likeNum": 19707788,
      "noteNum": 175570,
      "noteNum30bm": "13.9"
    },
    "wordKolProfile": {
      "contentTagStat": [
        {
          "name": "护肤",
          "percent": 92.2
        }
      ],
      "fansStat": [
        {
          "end": 5000,
          "percent": 70.1,
          "start": 1000
        }
      ],
      "featureTagStat": [
        {
          "name": "保湿补水",
          "percent": 52.5
        }
      ],
      "personalTagStat": [
        {
          "name": "妈妈",
          "percent": 22.9
        }
      ],
      "picPriceStat": [
        {
          "end": 1000,
          "percent": 88.2,
          "start": 0
        }
      ],
      "videoPriceStat": [
        {
          "end": 1000,
          "percent": 88.3,
          "start": 0
        }
      ]
    }
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.searchWordData.noteNum / userNum` | Number of notes and number of creators tied to the keyword. |
| `data.searchWordData.impNum / readNum` | Total impressions and total reads for the keyword's notes. |
| `data.searchWordData.likeNum / favNum / cmtNum / shareNum` | Counts of likes, favorites, comments and shares. |
| `data.searchWordData.engageNum` | Total engagement count for the keyword. |
| `data.searchWordData.searchScore` | Search score of the keyword, returned as a string. |
| `data.searchWordData.noteNum30bm / userNum30bm / impNum30bm / readNum30bm / engageNum30bm / searchScore30bm` | Values returned as strings that pair with the matching metric above, such as `24.9`. The `30bm` suffix suggests a 30-day comparison, but the response does not state the unit. |
| `data.wordKolProfile.contentTagStat[]` | Content categories of creators for this keyword. Each row has the tag `name` and its `percent` share. |
| `data.wordKolProfile.featureTagStat[] / personalTagStat[]` | Product feature tags (such as `保湿补水`) and creator persona tags (such as `妈妈`), each with a `percent` share. |
| `data.wordKolProfile.fansStat[]` | Creator share by follower range. `start` and `end` set the range and `percent` gives the share. |
| `data.wordKolProfile.picPriceStat[] / videoPriceStat[]` | Creator share by price range for image notes and video notes. `start` and `end` set the range and `percent` gives the share. |

### Notes

- Send the keyword in `search_word`. Chinese keywords such as `面膜` are used in the example.
- Read the result from `outputs[0].data`. A successful call has `code` set to `0` and `success` set to `true`.
- For related terms, call [Xiaohongshu PGY related keywords](/apis/xiaohongshu/pgy/keyword-related). For a day-by-day trend, call [Xiaohongshu PGY keyword daily trend](/apis/xiaohongshu/pgy/keyword-daily).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/keyword-stat.json`](../../../../catalog/models/xiaohongshu/pgy/keyword-stat.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/keyword-stat
