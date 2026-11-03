# Xiaohongshu PGY keyword daily trend API: pricing, parameters and code examples

`xiaohongshu/pgy/keyword-daily` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

PGY keyword daily trend on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/keyword-daily", "search_word": "面膜"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/keyword-daily', {'search_word': '面膜'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/keyword-daily", {
  "search_word": "面膜"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/keyword-daily", sandbase.Params{
	"search_word": "面膜",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/keyword-daily` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `search_word` | string | yes | Keyword  |

## Details

Returns a day-by-day trend for one keyword on Xiaohongshu's PGY platform. Each row has the date, note count, user count, reads, impressions, engagement and a search score. It needs one input, `search_word`.

### Use cases

- Plot how interest in a product keyword such as `面膜` rises and falls from day to day.
- Compare `searchScore` with `noteNum` to see whether search demand is growing faster than content supply.
- Track daily `impNum` and `readNum` to pick the best days to launch a campaign around a keyword.
- Check `engageNum` over time to judge how much interaction notes on a topic attract.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/keyword-daily" \
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
    "dailyData": [
      {
        "brandTag": 0,
        "cmtNum": null,
        "dateKey": "2026-08-04",
        "engageNum": 245994,
        "engageNum30bm": null,
        "favNum": null,
        "followCnt": null,
        "impNum": 36445871,
        "impNum30bm": null,
        "likeNum": null,
        "noteNum": 26704,
        "noteNum30bm": null
      }
    ]
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.dailyData[].dateKey` | Date of the data point, in `YYYY-MM-DD` format. |
| `data.dailyData[].searchScore` | Search score for the keyword on that day. It is returned as a string. |
| `data.dailyData[].noteNum` | Number of notes for the keyword on that day. |
| `data.dailyData[].userNum` | Number of users tied to the keyword on that day. |
| `data.dailyData[].impNum / readNum` | Impressions and reads for the keyword on that day. |
| `data.dailyData[].engageNum` | Engagement count for the keyword on that day. |
| `data.dailyData[].cmtNum / favNum / likeNum / shareNum / followCnt` | Comment, favorite, like, share and follow counts. These were `null` in this response. |
| `data.dailyData[].impNum30bm / readNum30bm / noteNum30bm / engageNum30bm / userNum30bm / searchScore30bm` | Companion fields for each main metric. These were `null` in this response. |
| `success / msg` | `success` is `true` and `msg` is `成功` when the call works. |

### Notes

- Pass the keyword in `search_word`. Chinese keywords such as `面膜` work.
- The data sits in `data.dailyData`, one object per day, in ascending date order.
- Several fields can be `null`, so check for `null` before you calculate with them.
- Call [Xiaohongshu PGY related keywords](/apis/xiaohongshu/pgy/keyword-related) to find more keywords, or [Xiaohongshu PGY keyword overview](/apis/xiaohongshu/pgy/keyword-stat) for a summary of one keyword.

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/keyword-daily.json`](../../../../catalog/models/xiaohongshu/pgy/keyword-daily.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/keyword-daily
