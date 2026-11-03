# Douyin Item Report Interaction Analysis API: pricing, parameters and code examples

`douyin/xingtu-v2/item-report-th-analysis` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call · **Modes:** sync

Get Item Report Interaction Analysis on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.003 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/item-report-th-analysis", "item_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/item-report-th-analysis', {'item_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/item-report-th-analysis", {
  "item_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/item-report-th-analysis", sandbase.Params{
	"item_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/item-report-th-analysis` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video (item) ID  |

## Details

This API returns interaction analysis for one Douyin video as two maps of numbered buckets: `like_info` and `play_lose_info`. It needs the video ID in `item_id`.

### Use cases

- Compare the `like_info` buckets to see at which stage of a video's playback most likes happen.
- Check `play_lose_info` to see where viewers stop watching a creator's sponsored video.
- Compare bucket shapes across several videos to find which content holds viewers longer.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/item-report-th-analysis" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video (item) ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "like_info": {
    "1": "17512",
    "2": "75181",
    "3": "32052",
    "4": "17422",
    "5": "11156",
    "6": "8685",
    "7": "7102",
    "8": "5085",
    "9": "0"
  },
  "play_lose_info": {
    "1": "501853",
    "2": "741827",
    "3": "375488",
    "4": "226554",
    "5": "146815",
    "6": "104903",
    "7": "79733",
    "8": "61463",
    "9": "360036"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `base_resp.status_code / base_resp.status_message` | Call status. A `status_code` of `0` with an empty `status_message` means the request worked. |
| `like_info.1 ... like_info.9` | Like counts as strings, one per numbered bucket from `1` to `9`. The response does not say what each bucket covers, so treat the numbers as ordered labels. In the sample, bucket `2` has the highest value and bucket `9` is `0`. |
| `play_lose_info.1 ... play_lose_info.9` | Drop-off counts as strings, one per numbered bucket from `1` to `9`. In the sample, the values fall from bucket `1` to bucket `8`, then rise again in bucket `9`. |

### Notes

- Send the video ID as `item_id`. It is a numeric string such as `7372484719365098803`.
- All counts come back as strings, so convert them to numbers before you sum or compare them.
- For other views of the same video, call [Douyin Item Report Detail](/apis/douyin/xingtu-v2/item-report-detail), [Douyin Item Report Trend](/apis/douyin/xingtu-v2/item-report-trend) or [Douyin Item Report Comments](/apis/douyin/xingtu-v2/item-report-comments).

### Pricing

$0.003 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/item-report-th-analysis.json`](../../../../catalog/models/douyin/xingtu-v2/item-report-th-analysis.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/item-report-th-analysis
