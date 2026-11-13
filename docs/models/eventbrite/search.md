# Eventbrite Search API: pricing, parameters and code examples

`eventbrite/search` · data API · Eventbrite · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Eventbrite events by keyword and location, with title, date, venue, price, organizer and event link.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eventbrite/search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('eventbrite/search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("eventbrite/search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "eventbrite/search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/eventbrite/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string |  | Parameter defines the query you want to search (e.g., `jazz`, `yoga`, or `tech meetup`). It works like Eventbrite's search box: some queries, like `comedy`, return only the matching events, while others, like `jazz`,…  |
| `date` | string |  | Parameter defines the dates of the events. It defaults to all current and future events. Available options: `today` - Today `tomorrow` - Tomorrow `this_weekend` - This weekend `this_week` - This week `next_week` - Next…  |
| `page` | string |  | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Eventbrite returns up to 20 events per page,…  |
| `price` | string |  | Parameter defines the price of the events. It takes a single value, and defaults to both free and paid events. Available options: `free` - Free `paid` - Paid  |
| `online` | string |  | Parameter defines whether to search for Eventbrite's online events instead of the events in a location. It can be set to `true` or `false` (default). `online` and `location` parameters can't be used together.  |
| `sort_by` | string |  | Parameter defines the sorting of the events. It defaults to Eventbrite's relevance ranking. Available options: `date` - Date (soonest first)  |
| `category` | string |  | Parameter defines the category of the events (e.g., `music`). It takes a single category. Available options: `business_and_professional` - Business & professional `science_and_technology` - Science & technology `music`…  |
| `end_date` | string |  | Parameter defines the last day of the date range to search for events in. The format is **YYYY-MM-DD** (e.g., `2026-12-14`). It can't be earlier than `start_date`, and can be the same day to search for the events of a…  |
| `location` | string |  | Parameter defines the location to search for events in (e.g., `Austin, Texas, United States`). It's required unless `online` is set to `true`. If several locations match the location requested, we'll pick the most…  |
| `event_type` | string |  | Parameter defines the type of the events (e.g., `concert`). It takes a single type. Used together with `category`, only the events matching both are returned (e.g., `music` concerts). Available options: `conference` -…  |
| `start_date` | string |  | Parameter defines the first day of the date range to search for events in. The format is **YYYY-MM-DD** (e.g., `2026-12-12`). It can't be in the past. It must be used together with `end_date`, and can't be used with…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Eventbrite events by keyword and location, with title, date, venue, price, organizer and event link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/eventbrite/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "tech meetup", "location": "austin"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | No | Parameter defines the query you want to search (e.g., `jazz`, `yoga`, or `tech meetup`). It works like Eventbrite's search box: some queries, like `comedy`, return only the matching events, while others, like `jazz`, return all the events o |
| `location` | string | No | Parameter defines the location to search for events in (e.g., `Austin, Texas, United States`). It's required unless `online` is set to `true`. If several locations match the location requested, we'll pick the most popular one. Head to the / |
| `online` | string | No | Parameter defines whether to search for Eventbrite's online events instead of the events in a location. It can be set to `true` or `false` (default). `online` and `location` parameters can't be used together. |
| `date` | string | No | Parameter defines the dates of the events. It defaults to all current and future events. Available options: `today` - Today `tomorrow` - Tomorrow `this_weekend` - This weekend `this_week` - This week `next_week` - Next week `this_month` - T |
| `start_date` | string | No | Parameter defines the first day of the date range to search for events in. The format is **YYYY-MM-DD** (e.g., `2026-12-12`). It can't be in the past. It must be used together with `end_date`, and can't be used with `date`. |
| `end_date` | string | No | Parameter defines the last day of the date range to search for events in. The format is **YYYY-MM-DD** (e.g., `2026-12-14`). It can't be earlier than `start_date`, and can be the same day to search for the events of a single day. It must be |
| `category` | string | No | Parameter defines the category of the events (e.g., `music`). It takes a single category. Available options: `business_and_professional` - Business & professional `science_and_technology` - Science & technology `music` - Music `film_media_a |
| `event_type` | string | No | Parameter defines the type of the events (e.g., `concert`). It takes a single type. Used together with `category`, only the events matching both are returned (e.g., `music` concerts). Available options: `conference` - Conference `seminar` - |
| `price` | string | No | Parameter defines the price of the events. It takes a single value, and defaults to both free and paid events. Available options: `free` - Free `paid` - Paid |
| `sort_by` | string | No | Parameter defines the sorting of the events. It defaults to Eventbrite's relevance ranking. Available options: `date` - Date (soonest first) |
| `page` | string | No | Value is used to get results on a specific page. (e.g., `1` (default) is the first page of results, `2` is the 2nd page of results, `3` is the 3rd page of results, etc.). Eventbrite returns up to 20 events per page, and up to 50 pages (abou |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/eventbrite/search.json`](../../../catalog/models/eventbrite/search.json) · Store page: https://www.sandbase.ai/model/eventbrite/search
