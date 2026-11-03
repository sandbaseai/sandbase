# Similarweb Demographics API: pricing, parameters and code examples

`similarweb/demographics` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.6 per call · **Modes:** sync

Get the age and gender breakdown of a website's visitors for the selected period.

## Pricing

- **$0.6 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/demographics", "domain": "cnn.com", "end_date": "2026-09", "granularity": "monthly", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/demographics', {'domain': 'cnn.com', 'end_date': '2026-09', 'granularity': 'monthly', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/demographics", {
  "domain": "cnn.com",
  "end_date": "2026-09",
  "granularity": "monthly",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/demographics", sandbase.Params{
	"domain": "cnn.com",
	"end_date": "2026-09",
	"granularity": "monthly",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/demographics` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | domain  |
| `format` | string |  | format one of: `json` |
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `web_source` | string |  | web_source one of: `total` |
| `granularity` | string | yes | granularity one of: `monthly` |
| `main_domain_only` | boolean |  | main_domain_only  |

## Details

Returns the age and gender split of a website's visitors for a chosen period. You send a `domain`, a `start_date`, an `end_date` and `granularity`, and get back shares between 0 and 1.

### Use cases

- Compare the age mix of a news site with a competitor's to see which one reaches older readers.
- Check the male and female split of a domain before planning an ad buy.
- Build audience profiles for a list of publishers in a media planning sheet.
- Track how a site's age mix changes by running the same domain over different months.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/demographics" \
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
| `granularity` | string | Yes | granularity |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `format` | string | No | format |
| `main_domain_only` | boolean | No | main_domain_only |
| `web_source` | string | No | web_source |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "age_18_to_24_share": 0.08070495283947984,
      "age_25_to_34_share": 0.18467731979384402,
      "age_35_to_44_share": 0.2067059697120009,
      "age_45_to_54_share": 0.20790595096812176,
      "age_55_to_64_share": 0.19314205276691135,
      "age_65_plus_share": 0.12686375391964214,
      "female_share": 0.4365859576418669,
      "male_share": 0.5634140423581331
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
        "age_18_to_24_share"
      ],
      "start_date": "2026-09-01"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].age_18_to_24_share` | Share of the site's visitors aged 18 to 24, as a fraction of 1. |
| `data[].age_25_to_34_share / age_35_to_44_share / age_45_to_54_share / age_55_to_64_share` | Share of visitors in each of these age brackets, as a fraction of 1. |
| `data[].age_65_plus_share` | Share of visitors aged 65 and older. |
| `data[].female_share / male_share` | Share of visitors who are female and male. The two values add up to 1. |
| `meta.last_updated` | Date the data was last updated, in `YYYY-MM-DD` format. |
| `meta.request.start_date / meta.request.end_date` | Period the data covers. A monthly request is expanded to the first and last day of the month. |
| `meta.request.metrics` | Metric names tied to the request. |
| `meta.status` | Shows `success` when the call worked. |

### Notes

- Dates in the request use the `YYYY-MM` format, for example `2026-09`.
- `country` accepts only `ww`, which means worldwide data. `granularity` accepts only `monthly`.
- For age and gender data on specific groups, call [Similarweb Demographics - Specific Groups](/apis/similarweb/traffic-by-demographics-aggregated).
- To see which topics the audience cares about, call [Similarweb Audience Interest](/apis/similarweb/audience-interest).

### Pricing

$0.6 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/demographics.json`](../../../catalog/models/similarweb/demographics.json) · Store page: https://www.sandbase.ai/model/similarweb/demographics
