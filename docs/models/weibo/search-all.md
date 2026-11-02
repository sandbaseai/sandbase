# Weibo Keyword Search API: pricing, parameters and code examples

`weibo/search-all` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Search Weibo posts by keyword within a required day-and-hour time range, with page-based pagination, hot or time sorting, and filters for pictures, video, music, or links.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/search-all", "q": "新闻", "startDay": "2026-10-22", "startHour": 0, "endDay": "2026-10-29", "endHour": 23}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/search-all', {'q': '新闻', 'startDay': '2026-10-22', 'startHour': 0, 'endDay': '2026-10-29', 'endHour': 23})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/search-all", {
  "q": "新闻",
  "startDay": "2026-10-22",
  "startHour": 0,
  "endDay": "2026-10-29",
  "endHour": 23
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/search-all", sandbase.Params{
	"q": "新闻",
	"startDay": "2026-10-22",
	"startHour": 0,
	"endDay": "2026-10-29",
	"endHour": 23,
})
```

Same call via the path form: `POST /v1/api/weibo/search-all` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Search Keywords.  |
| `page` | integer |  | Page number, starting with 1. default `1` |
| `endDay` | string | yes | End Day (yyyy-MM-dd).  |
| `endHour` | integer | yes | End Hour (0-23).  |
| `hotSort` | boolean |  | Hot sort, true for hot sort, false for time sort. Default is false. default `false` |
| `contains` | string |  | Contains filter for the result set. one of: `ALL`, `PICTURE`, `VIDEO`, `MUSIC`, `LINK`; default `"ALL"` |
| `startDay` | string | yes | Start Day (yyyy-MM-dd).  |
| `startHour` | integer | yes | Start Hour (0-23).  |

## Details

Search Weibo posts by keyword within a required day-and-hour time range, with page-based pagination, hot or time sorting, and filters for pictures, video, music, or links.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/search-all" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "新闻", "startDay": "2026-10-22", "startHour": 0, "endDay": "2026-10-29", "endHour": 23}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Search Keywords. |
| `startDay` | string | Yes | Start Day (yyyy-MM-dd). |
| `startHour` | integer | Yes | Start Hour (0-23). |
| `endDay` | string | Yes | End Day (yyyy-MM-dd). |
| `endHour` | integer | Yes | End Hour (0-23). |
| `hotSort` | boolean | No | Hot sort, true for hot sort, false for time sort. Default is false. |
| `contains` | string | No | Contains filter for the result set. |
| `page` | integer | No | Page number, starting with 1. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/weibo/search-all.json`](../../../catalog/models/weibo/search-all.json) · Store page: https://www.sandbase.ai/model/weibo/search-all
