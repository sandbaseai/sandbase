# Ximalaya Category Albums API: pricing, parameters and code examples

`ximalaya/category-albums` · data API · Ximalaya · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

List albums within a category, sorted by popularity. Category is identified by its pinyin name (from get_categories). Paginates via page number; each page returns up to page_size albums with play counts, track counts, and anchor info.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ximalaya/category-albums"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ximalaya/category-albums', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ximalaya/category-albums", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ximalaya/category-albums", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/ximalaya/category-albums` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `page_size` | integer |  | Number of albums per page. default `30` |
| `category_name` | string |  | Category pinyin name from get_categories (e.g. youshengshu, yinyue, ertong, xiangsheng, comic, finance, culture, kid, entertainment, train). one of: `yinyue`, `youshengshu`, `ertong`, `xiangsheng`, `comic`, `finance`, `culture`; default `"youshengshu"` |

## Details

List albums within a category, sorted by popularity. Category is identified by its pinyin name (from get_categories). Paginates via page number; each page returns up to page_size albums with play counts, track counts, and anchor info.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "ximalaya/category-albums", "page": 1, "page_size": 10, "category_name": "yinyue"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_name` | string | No | Category pinyin name from get_categories (e.g. youshengshu, yinyue, ertong, xiangsheng, comic, finance, culture, kid, entertainment, train). One of: `yinyue`, `youshengshu`, `ertong`, `xiangsheng`, `comic`, `finance`, `c |
| `page` | integer | No | Page number for pagination. |
| `page_size` | integer | No | Number of albums per page. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ximalaya/category-albums.json`](../../../catalog/models/ximalaya/category-albums.json) · Store page: https://www.sandbase.ai/model/ximalaya/category-albums
