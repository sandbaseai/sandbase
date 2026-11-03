# Similarweb Website Ranking API: pricing, parameters and code examples

`similarweb/ranking` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.15 per call · **Modes:** sync

Get a website's global, country and category traffic rank month by month.

## Pricing

- Depends on parameters (`params.end_date`, `params.start_date`).

Formula: `0.15 * Math.max(1.0, (params.start_date != nil && params.end_date != nil ? ((int(split(params.end_date, "-")[0]) - int(split(params.start_date, "-")[0])) * 12 + int(split(params.end_date, "-")[1]) - int(split(params.start_date, "-")[1]) + 1) * 1.0 : 12.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/ranking", "domain": "cnn.com", "end_date": "2026-09", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/ranking', {'domain': 'cnn.com', 'end_date': '2026-09', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/ranking", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/ranking", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/ranking` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | domain  |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `desktop`, `mobile_web`, `total` |
| `granularity` | string |  | granularity one of: `monthly`; default `"monthly"` |
| `main_domain_only` | boolean |  | main_domain_only default `true` |

## Details

Returns a website's traffic rank by month, including its country rank, its category rank and its category name. It needs a `domain` plus `start_date` and `end_date` in `YYYY-MM` format.

### Use cases

- Track how a news site's category rank moves from month to month.
- Compare the worldwide rank of a competitor domain against your own domain.
- Find which Similarweb category a domain belongs to before you benchmark it.
- Add monthly rank history to a market research report on a set of domains.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/ranking" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domain": "cnn.com", "granularity": "monthly"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | domain |
| `end_date` | string | Yes | end_date |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `granularity` | string | No | granularity |
| `main_domain_only` | boolean | No | main_domain_only |
| `web_source` | string | No | web_source |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "category": "News_and_Media",
      "category_rank": 16,
      "country_rank": 178,
      "date": "2026-09-01"
    }
  ],
  "meta": {
    "last_updated": "2026-09-30",
    "request": {
      "country": "ww",
      "domain": "cnn.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "metrics": [
        "country_rank"
      ],
      "start_date": "2026-09-01",
      "web_source": "total"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].date` | First day of the month the row covers, for example `2026-09-01`. |
| `data[].country_rank` | The domain's traffic rank for the requested country. With `country` set to `ww`, this is the worldwide rank. A lower number means a higher rank. |
| `data[].category_rank` | The domain's traffic rank inside its category. |
| `data[].category` | The category the domain is ranked in, for example `News_and_Media`. |
| `meta.status` | Shows `success` when the call worked. |
| `meta.last_updated` | Date of the latest data update for this response, for example `2026-09-30`. |
| `meta.request.web_source` | The traffic source the response used. The request here returned `total`. |
| `meta.request.start_date / meta.request.end_date` | The full date range the request used. The short `YYYY-MM` inputs appear as first and last day of the month. |

### Notes

- Send dates as `YYYY-MM`. The response expands them to full dates such as `2026-09-01` and `2026-09-30`.
- The `data` list has one row per month in the range.
- `country` accepts only `ww`, which means worldwide. `granularity` accepts only `monthly`.
- For traffic volume and engagement of the same domain, call [Similarweb Traffic & Engagement](/apis/similarweb/traffic-engagement). To see ranked lists of sites, use [Similarweb Top Sites Ranking](/apis/similarweb/top-sites-ranking).

### Pricing

Billed at the actual cost of each call, about $0.15 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/ranking.json`](../../../catalog/models/similarweb/ranking.json) · Store page: https://www.sandbase.ai/model/similarweb/ranking
