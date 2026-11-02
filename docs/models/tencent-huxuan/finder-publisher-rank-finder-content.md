# Tencent Huxuan Hot Content Trends API: pricing, parameters and code examples

`tencent-huxuan/finder-publisher-rank-finder-content` · data API · Tencent Huxuan · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.042857 per call · **Modes:** sync

List QQ Huxuan hot Video Account content by month and creator category, with six descending sort metrics and page-number pagination. Use it to research monthly content trends for Tencent Huxuan campaign planning.

## Pricing

- **$0.042857 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent-huxuan/finder-publisher-rank-finder-content"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tencent-huxuan/finder-publisher-rank-finder-content', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tencent-huxuan/finder-publisher-rank-finder-content", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tencent-huxuan/finder-publisher-rank-finder-content", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tencent-huxuan/finder-publisher-rank-finder-content` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. Each page contains up to 48 items. default `1` |
| `sort` | string |  | Sort metric. Results are sorted in descending order. one of: `INTERACTION`, `PLAY`, `THUMB_LIKE`, `HEART_LIKE`, `COMMENT`, `SHARE`; default `"INTERACTION"` |
| `month` | string |  | Statistics month in yyyy-MM format. Omit to use the latest month available on QQ Huxuan.  |
| `category` | string |  | Creator category. ALL includes every category. one of: `ALL`, `FOOD`, `LIFESTYLE`, `COMEDY`, `EMOTION`, `SOCIETY`, `HUMANITIES_ARTS`, `DRAMA`, `ENTERTAINMENT`, `TECHNOLOGY`, `FINANCE`, `FILM_TV_VARIETY` …; default `"ALL"` |

## Details

List QQ Huxuan hot Video Account content by month and creator category, with six descending sort metrics and page-number pagination. Use it to research monthly content trends for Tencent Huxuan campaign planning.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tencent-huxuan/finder-publisher-rank-finder-content" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Creator category. ALL includes every category. |
| `sort` | string | No | Sort metric. Results are sorted in descending order. |
| `month` | string | No | Statistics month in yyyy-MM format. Omit to use the latest month available on QQ Huxuan. |
| `page` | integer | No | Page number, starting at 1. Each page contains up to 48 items. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/tencent-huxuan/finder-publisher-rank-finder-content.json`](../../../catalog/models/tencent-huxuan/finder-publisher-rank-finder-content.json) · Store page: https://www.sandbase.ai/model/tencent-huxuan/finder-publisher-rank-finder-content
