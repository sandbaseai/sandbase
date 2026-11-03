# DataForSEO Bing Audience Estimation API: pricing, parameters and code examples

`dataforseo/v3/keywords_data/bing/audience_estimation/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.09 per call · **Modes:** sync

Estimate Microsoft Ads audience size for targeting criteria. Bing Ads audience estimate for a location plus optional age, gender, industry, and job_function targeting, bid, and daily budget.

## Pricing

- **$0.09 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/bing/audience_estimation/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/bing/audience_estimation/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/bing/audience_estimation/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/bing/audience_estimation/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/bing/audience_estimation/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `age` | array |  | Audience age groups.  |
| `bid` | integer |  | Bid in USD.  |
| `daily_budget` | integer |  | Daily budget in USD.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Returns estimated Microsoft Ads audience size, impressions, clicks and click-through rate for a set of targeting criteria. You send a `location_code` and `language_code`, plus optional targeting such as `age`, and a `bid` and `daily_budget` in USD.

### Use cases

- Check how large a 25 to 34 age group is in the United States before you build a Microsoft Ads campaign.
- Compare expected clicks and impressions at different `bid` and `daily_budget` values to plan a test budget.
- Compare audience sizes across locations or age groups to pick the market to launch in first.
- Add estimated reach numbers to a media plan or client pitch for Bing advertising.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/bing/audience_estimation/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"location_code": 2840, "language_code": "en", "age": ["twenty_five_to_thirty_four"], "bid": 1, "daily_budget": 100}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `age` | array | No | Audience age groups. |
| `bid` | integer | No | Bid in USD. |
| `daily_budget` | integer | No | Daily budget in USD. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "age": [
          "twenty_five_to_thirty_four"
        ],
        "api": "keywords_data",
        "bid": 1,
        "daily_budget": 100,
        "function": "audience_estimation",
        "language_code": "en",
        "location_code": 2840,
        "se": "bing"
      },
      "id": "11030829-1614-0593-0000-3f2f80dfb5a8",
      "path": [
        "v3"
      ],
      "result": [
        {
          "currency": "USDollar",
          "est_audience_size": {
            "high": 49570,
            "low": 15970
          },
          "est_clicks": {
            "high": 6190,
            "low": 1550
          },
          "est_cost_per_event": {
            "high": null,
            "low": null
          },
          "est_ctr": {
            "high": 0.02158363893284101,
            "low": 0
          },
          "est_impressions": {
            "high": 573950,
            "low": 143490
          },
          "est_reach_audience_size": 7420000,
          "est_reach_impressions": 2130000000
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.7798 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.7951 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].est_audience_size.low / est_audience_size.high` | Lower and upper estimate of the audience size for the targeting and budget you sent. |
| `tasks[].result[].est_impressions.low / est_impressions.high` | Lower and upper estimate of ad impressions. |
| `tasks[].result[].est_clicks.low / est_clicks.high` | Lower and upper estimate of clicks. |
| `tasks[].result[].est_ctr.low / est_ctr.high` | Lower and upper estimate of click-through rate, given as a fraction. A value of `0.0216` means about 2.16%. |
| `tasks[].result[].est_cost_per_event.low / est_cost_per_event.high` | Lower and upper estimate of cost per event. Both values are `null` in this response. |
| `tasks[].result[].est_reach_audience_size` | Estimated total reach audience size for the location and language, shown as a single number. |
| `tasks[].result[].est_reach_impressions` | Estimated total reach impressions, shown as a single number. |
| `tasks[].result[].currency` | Currency name for the cost values. This response shows `USDollar`. |
| `tasks[].data` | Echo of the parameters the task ran with, such as `location_code`, `age`, `bid` and `daily_budget`. |
| `tasks[].id` | Unique ID of the task. |

### Notes

- Use `location_code` `2840` for the United States. Pass age groups as an array of strings, for example `["twenty_five_to_thirty_four"]`.
- The description also lists `gender`, `industry` and `job_function` as optional targeting parameters. This example request does not use them.
- Check `tasks[].status_code` and `tasks_error` to confirm the task succeeded. A successful task returns `20000`.

### Pricing

$0.09 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/bing/audience_estimation/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/bing/audience_estimation/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/bing/audience_estimation/live
