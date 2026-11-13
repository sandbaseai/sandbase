# Glassdoor Jobs API: pricing, parameters and code examples

`glassdoor/jobs` · data API · Glassdoor · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Glassdoor job listings by keyword and location, with title, company, rating, salary estimate, location and posting age.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "glassdoor/jobs"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('glassdoor/jobs', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("glassdoor/jobs", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "glassdoor/jobs", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/glassdoor/jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Parameter defines the job search query, like the job title or keyword search box of Glassdoor (e.g., `software engineer`, `nurse`, or `Python`). `q`, `location`, or `employer_id` is required.  |
| `radius` | string |  | Parameter defines the maximum distance from `location`, in miles in the United States and in kilometers elsewhere, like the Distance filter of Glassdoor. It defaults to `25` for cities. Available options: `0` - Within…  |
| `remote` | string |  | Parameter defines whether to only show remote jobs, like the Remote only filter of Glassdoor. It can be set to `true` or `false` (default).  |
| `job_type` | string |  | Parameter defines the type of the jobs. Available options: `full_time` - Full-time `part_time` - Part-time `contract` - Contract  |
| `location` | string |  | Parameter defines the location of the jobs, like the location search box of Glassdoor: a city, state or country (e.g., `New York, NY`, `Texas`, `London`, or `Germany`). We use the first location Glassdoor suggests with…  |
| `easy_apply` | string |  | Parameter defines whether to only show jobs you can apply to on Glassdoor, like the Easy Apply only filter of Glassdoor. It can be set to `true` or `false` (default).  |
| `max_salary` | string |  | Parameter defines the maximum yearly salary of the jobs, in the currency of `location` (e.g., `150000`).  |
| `min_rating` | string |  | Parameter defines the minimum Glassdoor rating of the companies, from `1` to `4` (e.g., `4` for companies rated 4.0 and up).  |
| `min_salary` | string |  | Parameter defines the minimum yearly salary of the jobs, in the currency of `location` (e.g., `100000`).  |
| `date_posted` | string |  | Parameter defines the maximum number of days since the jobs were posted. Available options: `1` - Last day `3` - Last 3 days `7` - Last week `14` - Last 2 weeks `30` - Last month  |
| `employer_id` | string |  | Parameter defines the Glassdoor ID of the company to show the jobs of (e.g., `9079` for Google). It is the number after `E` in Glassdoor company URLs (e.g., https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm),…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `next_page_token` | string |  | Parameter defines the token of the next page of results. Up to `30` results are returned per page, for up to `30` pages. The token is in the JSON response: `the API_pagination.next_page_token`. Use it with the same…  |
| `seniority_level` | string |  | Parameter defines the seniority level of the jobs. Available options: `internship` - Internship `entry_level` - Entry level `mid_senior_level` - Mid-senior level `director` - Director `executive` - Executive  |

## Details

Search Glassdoor job listings by keyword and location, with title, company, rating, salary estimate, location and posting age.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/glassdoor/jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "data engineer"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | No | Parameter defines the job search query, like the job title or keyword search box of Glassdoor (e.g., `software engineer`, `nurse`, or `Python`). `q`, `location`, or `employer_id` is required. |
| `location` | string | No | Parameter defines the location of the jobs, like the location search box of Glassdoor: a city, state or country (e.g., `New York, NY`, `Texas`, `London`, or `Germany`). We use the first location Glassdoor suggests with that name, or else it |
| `radius` | string | No | Parameter defines the maximum distance from `location`, in miles in the United States and in kilometers elsewhere, like the Distance filter of Glassdoor. It defaults to `25` for cities. Available options: `0` - Within 0 `5` - Within 5 `10`  |
| `date_posted` | string | No | Parameter defines the maximum number of days since the jobs were posted. Available options: `1` - Last day `3` - Last 3 days `7` - Last week `14` - Last 2 weeks `30` - Last month |
| `job_type` | string | No | Parameter defines the type of the jobs. Available options: `full_time` - Full-time `part_time` - Part-time `contract` - Contract |
| `seniority_level` | string | No | Parameter defines the seniority level of the jobs. Available options: `internship` - Internship `entry_level` - Entry level `mid_senior_level` - Mid-senior level `director` - Director `executive` - Executive |
| `remote` | string | No | Parameter defines whether to only show remote jobs, like the Remote only filter of Glassdoor. It can be set to `true` or `false` (default). |
| `easy_apply` | string | No | Parameter defines whether to only show jobs you can apply to on Glassdoor, like the Easy Apply only filter of Glassdoor. It can be set to `true` or `false` (default). |
| `min_rating` | string | No | Parameter defines the minimum Glassdoor rating of the companies, from `1` to `4` (e.g., `4` for companies rated 4.0 and up). |
| `min_salary` | string | No | Parameter defines the minimum yearly salary of the jobs, in the currency of `location` (e.g., `100000`). |
| `max_salary` | string | No | Parameter defines the maximum yearly salary of the jobs, in the currency of `location` (e.g., `150000`). |
| `employer_id` | string | No | Parameter defines the Glassdoor ID of the company to show the jobs of (e.g., `9079` for Google). It is the number after `E` in Glassdoor company URLs (e.g., https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm), and the `company_id` o |
| `next_page_token` | string | No | Parameter defines the token of the next page of results. Up to `30` results are returned per page, for up to `30` pages. The token is in the JSON response: `the API_pagination.next_page_token`. Use it with the same other parameters as the s |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/glassdoor/jobs.json`](../../../catalog/models/glassdoor/jobs.json) · Store page: https://www.sandbase.ai/model/glassdoor/jobs
