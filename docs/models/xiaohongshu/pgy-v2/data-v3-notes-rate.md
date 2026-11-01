# Xiaohongshu Pugongying Note Performance Metrics

`xiaohongshu/pgy-v2/data-v3-notes-rate` · api · Xiaohongshu

Get Xiaohongshu Pugongying aggregate note performance metrics for a creator with business, note-type, date-range, and advertisement filters. Use it to compare content performance across selected scopes.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-v3-notes-rate", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-v3-notes-rate', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-v3-notes-rate", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-v3-notes-rate", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-v3-notes-rate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |
| `business` | string |  | Business type. one of: `DAILY_NOTE`, `COOPERATE_NOTE`; default `"DAILY_NOTE"` |
| `dateType` | string |  | Time range for data. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `noteType` | string |  | Type of note. one of: `PHOTO_TEXT_AND_VIDEO`, `PHOTO_TEXT`, `VIDEO`; default `"PHOTO_TEXT_AND_VIDEO"` |
| `advertiseSwitch` | string |  | Advertisement filter. one of: `ALL`, `ORGANIC_ONLY`; default `"ALL"` |

## Details

Get Xiaohongshu Pugongying aggregate note performance metrics for a creator with business, note-type, date-range, and advertisement filters. Use it to compare content performance across selected scopes.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-v3-notes-rate" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |
| `business` | string | No | Business type. |
| `noteType` | string | No | Type of note. |
| `dateType` | string | No | Time range for data. |
| `advertiseSwitch` | string | No | Advertisement filter. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-v3-notes-rate.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-v3-notes-rate.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-v3-notes-rate
