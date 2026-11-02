# Xiaohongshu Pugongying Content Square Notes API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/content-square-search-note-v2` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020833 per call · **Modes:** sync

Search Xiaohongshu Pugongying Content Square notes by keyword or browse all notes, with business-category, ranking, time-window, and page controls. Use it to discover high-performing campaign content.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/content-square-search-note-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/content-square-search-note-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/content-square-search-note-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/content-square-search-note-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/content-square-search-note-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `nd` | string |  | Time range in days. one of: `DAY_3`, `DAY_7`, `DAY_14`, `DAY_30`; default `"DAY_7"` |
| `bizType` | string |  | Business category. one of: `XIAOHONGSHU_HOT`, `PRODUCT_SEEDING`, `ECOMMERCE_PROMOTION`, `PUGONGYING_COOPERATION`, `LEAD_COLLECTION`, `ECOMMERCE_HOT`, `SEEDING_DIRECT`, `APP_PROMOTION`; default `"XIAOHONGSHU_HOT"` |
| `orderBy` | string |  | Ranking metric. one of: `premium_imp_num`, `premium_good_read_rate`, `premium_read_num`, `premium_engage_num`, `premium_engage_rate`, `premium_like_num`, `premium_fav_num`, `premium_cmt_num`; default `"premium_imp_num"` |
| `pageNum` | integer |  | Page number for results. default `1` |
| `searchWord` | string |  | Keyword for note search. Empty string searches all notes.  |

## Details

Search Xiaohongshu Pugongying Content Square notes by keyword or browse all notes, with business-category, ranking, time-window, and page controls. Use it to discover high-performing campaign content.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/content-square-search-note-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `searchWord` | string | No | Keyword for note search. Empty string searches all notes. |
| `pageNum` | integer | No | Page number for results. |
| `bizType` | string | No | Business category. |
| `orderBy` | string | No | Ranking metric. |
| `nd` | string | No | Time range in days. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/content-square-search-note-v2.json`](../../../../catalog/models/xiaohongshu/pgy-v2/content-square-search-note-v2.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/content-square-search-note-v2
