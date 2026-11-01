# Xiaohongshu Keyword Note Search

`xiaohongshu/search-note` · api · Xiaohongshu

Search Xiaohongshu (RedNote) notes by keyword with page-based pagination, sorting and note-type filters. The V2 noteTime filter may return notes outside the selected time range.

## Pricing

- **$0.020833 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/search-note", "keyword": "美食"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/search-note', {'keyword': '美食'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/search-note", {
  "keyword": "美食"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/search-note", sandbase.Params{
	"keyword": "美食",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/search-note` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. Start at 1, then increment page while keeping the keyword and filters unchanged. default `1` |
| `sort` | string |  | Sort order for the result set. one of: `general`, `popularity_descending`, `time_descending`, `comment_descending`, `collect_descending`; default `"general"` |
| `keyword` | string | yes | Search keyword.  |
| `noteTime` | string |  | Note publish time filter. Results may include notes published outside the selected time range. one of: `ONE_DAY`, `ONE_WEEK`, `HALF_YEAR` |
| `noteType` | string |  | Note type filter. one of: `_0`, `_1`, `_2`; default `"_0"` |

## Details

Search Xiaohongshu (RedNote) notes by keyword with page-based pagination, sorting and note-type filters. The V2 noteTime filter may return notes outside the selected time range.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/search-note" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "美食"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | integer | No | Page number for pagination. Start at 1, then increment page while keeping the keyword and filters unchanged. |
| `sort` | string | No | Sort order for the result set. |
| `noteType` | string | No | Note type filter. |
| `noteTime` | string | No | Note publish time filter. Results may include notes published outside the selected time range. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/search-note.json`](../../../catalog/models/xiaohongshu/search-note.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/search-note
