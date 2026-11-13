# Glassdoor Reviews API: pricing, parameters and code examples

`glassdoor/reviews` · data API · Glassdoor · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get employee reviews for a company on Glassdoor by company ID, with rating, pros, cons, job title, date and sub-ratings.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "glassdoor/reviews", "employer_id": "7633"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('glassdoor/reviews', {'employer_id': '7633'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("glassdoor/reviews", {
  "employer_id": "7633"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "glassdoor/reviews", sandbase.Params{
	"employer_id": "7633",
})
```

Same call via the path form: `POST /v1/api/glassdoor/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Parameter defines the text to search for in the reviews, like the review search box of Glassdoor (e.g., `work life balance` or `remote`).  |
| `num` | string |  | Parameter defines the number of reviews per page, from `1` to `100`. It defaults to `10`, like on Glassdoor.  |
| `page` | string |  | Parameter defines the page number of the reviews (e.g., `1` (default) is the first page of reviews, `2` is the 2nd page of reviews, etc.).  |
| `rating` | string |  | Parameter defines the overall rating of the reviews, from `1` to `5` stars. Searches with `q` return the reviews rated `rating` or higher (e.g., `4` for 4 and 5 stars).  |
| `sort_by` | string |  | Parameter defines the sorting order of the reviews. It defaults to `most_relevant`. Available options: `most_relevant` - Most relevant `newest` - Newest `oldest` - Oldest `highest_rating` - Highest rating…  |
| `language` | string |  | Parameter defines the language of the reviews. It defaults to `en` (English). Glassdoor's search of `q` only covers English reviews, so the language doesn't apply to searches with `q`. Available options: `en` - English…  |
| `location` | string |  | Parameter defines the location of the reviewers' jobs: a city, state or country (e.g., `New York, NY`, `California`, or `India`). We use the first location Glassdoor suggests with that name, or else its first suggestion.  |
| `job_title` | string |  | Parameter defines the job title of the reviewers (e.g., `Software Engineer`).  |
| `employer_id` | string | yes | Parameter defines the Glassdoor ID of the company (e.g., `9079` for Google). It is the number after `E` in Glassdoor company URLs (e.g., https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm), and the…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `current_employees` | string |  | Parameter defines whether to only show the reviews of current employees. It can be set to `true` or `false` (default).  |
| `employment_status` | string |  | Parameter defines the employment status of the reviewers. Separate several statuses with a comma (e.g., `intern,contract`). It defaults to `full_time,part_time`. Available options: `full_time` - Full-time `part_time` -…  |

## Details

Get employee reviews for a company on Glassdoor by company ID, with rating, pros, cons, job title, date and sub-ratings.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/glassdoor/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"employer_id": "7633"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `employer_id` | string | Yes | Parameter defines the Glassdoor ID of the company (e.g., `9079` for Google). It is the number after `E` in Glassdoor company URLs (e.g., https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm), and the `employer_id` of our Glassdoor Com |
| `location` | string | No | Parameter defines the location of the reviewers' jobs: a city, state or country (e.g., `New York, NY`, `California`, or `India`). We use the first location Glassdoor suggests with that name, or else its first suggestion. |
| `language` | string | No | Parameter defines the language of the reviews. It defaults to `en` (English). Glassdoor's search of `q` only covers English reviews, so the language doesn't apply to searches with `q`. Available options: `en` - English `fr` - French `de` -  |
| `q` | string | No | Parameter defines the text to search for in the reviews, like the review search box of Glassdoor (e.g., `work life balance` or `remote`). |
| `sort_by` | string | No | Parameter defines the sorting order of the reviews. It defaults to `most_relevant`. Available options: `most_relevant` - Most relevant `newest` - Newest `oldest` - Oldest `highest_rating` - Highest rating `lowest_rating` - Lowest rating |
| `rating` | string | No | Parameter defines the overall rating of the reviews, from `1` to `5` stars. Searches with `q` return the reviews rated `rating` or higher (e.g., `4` for 4 and 5 stars). |
| `employment_status` | string | No | Parameter defines the employment status of the reviewers. Separate several statuses with a comma (e.g., `intern,contract`). It defaults to `full_time,part_time`. Available options: `full_time` - Full-time `part_time` - Part-time `contract`  |
| `current_employees` | string | No | Parameter defines whether to only show the reviews of current employees. It can be set to `true` or `false` (default). |
| `job_title` | string | No | Parameter defines the job title of the reviewers (e.g., `Software Engineer`). |
| `page` | string | No | Parameter defines the page number of the reviews (e.g., `1` (default) is the first page of reviews, `2` is the 2nd page of reviews, etc.). |
| `num` | string | No | Parameter defines the number of reviews per page, from `1` to `100`. It defaults to `10`, like on Glassdoor. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/glassdoor/reviews.json`](../../../catalog/models/glassdoor/reviews.json) · Store page: https://www.sandbase.ai/model/glassdoor/reviews
