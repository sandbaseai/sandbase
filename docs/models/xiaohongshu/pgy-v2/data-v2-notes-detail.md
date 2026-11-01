# Xiaohongshu Pugongying Creator Note List

`xiaohongshu/pgy-v2/data-v2-notes-detail` · api · Xiaohongshu

Get a paginated Xiaohongshu Pugongying creator note list with advertisement, sort-order, note-type, and third-platform filters. Use it to browse selected content from a known creator.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-v2-notes-detail", "userId": "64b898310000000014037b21"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-v2-notes-detail', {'userId': '64b898310000000014037b21'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-v2-notes-detail", {
  "userId": "64b898310000000014037b21"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-v2-notes-detail", sandbase.Params{
	"userId": "64b898310000000014037b21",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-v2-notes-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |
| `noteType` | string |  | Type of note. one of: `ALL`, `COOPERATION`, `PHOTO_TEXT`, `VIDEO`; default `"ALL"` |
| `orderType` | string |  | Sorting order. one of: `LATEST`, `MOST_READ`, `MOST_INTERACT`; default `"LATEST"` |
| `pageNumber` | integer |  | Page number. default `1` |
| `advertiseSwitch` | string |  | Advertisement filter. one of: `ALL`, `ORGANIC_ONLY`; default `"ALL"` |
| `isThirdPlatform` | string |  | Whether from third-party platform. one of: `NO`, `YES`; default `"NO"` |

## Details

Get a paginated Xiaohongshu Pugongying creator note list with advertisement, sort-order, note-type, and third-platform filters. Use it to browse selected content from a known creator.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-v2-notes-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "64b898310000000014037b21"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |
| `advertiseSwitch` | string | No | Advertisement filter. |
| `orderType` | string | No | Sorting order. |
| `noteType` | string | No | Type of note. |
| `isThirdPlatform` | string | No | Whether from third-party platform. |
| `pageNumber` | integer | No | Page number. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-v2-notes-detail.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-v2-notes-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-v2-notes-detail
