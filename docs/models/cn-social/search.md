# China Social Media Search API: pricing, parameters and code examples

`cn-social/search` · data API · China Social Media · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Search recent posts and articles across Chinese news sites, Weibo, WeChat, Zhihu, Douyin, Xiaohongshu, Bilibili and Kuaishou by keyword, with source and time-range filters. Results come from a cached index, so rare keywords can return few items.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "cn-social/search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('cn-social/search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("cn-social/search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "cn-social/search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/cn-social/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end` | string |  | End time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request.  |
| `start` | string |  | Start time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request.  |
| `source` | string |  | Target social media platform for search filtering. one of: `ALL`, `NEWS`, `WEIBO`, `WEIXIN`, `ZHIHU`, `DOUYIN`, `XIAOHONGSHU`, `BILIBILI`, `KUAISHOU`; default `"ALL"` |
| `keyword` | string |  | Search query string. Supports these five syntax forms: - AND (&&): A && B matches content containing both A and B. - OR (\|\|): A \|\| B matches content containing A or B. - Exclusion (-): -A matches content that does not…  |
| `nextCursor` | string |  | Pagination cursor provided by the 'nextCursor' field in the previous response.  |

## Details

Search recent posts and articles across Chinese news sites, Weibo, WeChat, Zhihu, Douyin, Xiaohongshu, Bilibili and Kuaishou by keyword, with source and time-range filters. Results come from a cached index, so rare keywords can return few items.

The result is returned in `outputs[0].data` in the platform's original structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/cn-social/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能", "source": "ALL", "start": "2026-10-19 00:00:00", "end": "2026-11-02 00:00:00"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query string. Supports these five syntax forms: - AND (&&): A && B matches content containing both A and B. - OR (||): A || B matches content containing A or B. - Exclusion (-): -A matches content that does not contain A. - Parentheses (): (A && B) || C matches content containing C, or both A and B. - English double quotes (""): "A" disables tokenization and requires an exact match for A. |
| `source` | string | No | Target social media platform for search filtering. |
| `start` | string | No | Start time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request. |
| `end` | string | No | End time of the search period (yyyy-MM-dd HH:mm:ss). Required for initial request. |
| `nextCursor` | string | No | Pagination cursor provided by the 'nextCursor' field in the previous response. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/cn-social/search.json`](../../../catalog/models/cn-social/search.json) · Store page: https://www.sandbase.ai/model/cn-social/search
