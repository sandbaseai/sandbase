# DataForSEO Google Play App Listings Search API: pricing, parameters and code examples

`dataforseo/v3/app_data/google/app_listings/search/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.11 per call · **Modes:** sync

Search the Google Play catalog by app title or description and get ratings, review counts, installs and prices for each match.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.11**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/app_data/google/app_listings/search/live"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/app_data/google/app_listings/search/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/app_data/google/app_listings/search/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/app_data/google/app_listings/search/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/app_data/google/app_listings/search/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of apps to return.  |
| `title` | string |  | Words to match in app titles.  |
| `filters` | string |  | Optional filter array, e.g. [["rating.value", ">", 4]].  |
| `description` | string |  | Optional words to match in app descriptions.  |

## Details

This API searches the Google Play catalog for apps whose title matches the words in `title`. Each match returns its `app_id`, a Play Store link, and developer details. You can also match on `description` and narrow results with `filters`.

### Use cases

- Find every VPN app on Google Play and list the developers behind them.
- Collect developer emails, websites and addresses for outreach to app publishers in a niche.
- Check how crowded a category is by reading `total_count` for a title keyword.
- Build a list of Play Store URLs to feed into an app tracking or review workflow.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/app_data/google/app_listings/search/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"title": "vpn", "limit": 10}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `description` | string | No | Optional words to match in app descriptions. |
| `filters` | string | No | Optional filter array, e.g. [["rating.value", ">", 4]]. |
| `limit` | integer | No | Maximum number of apps to return. |
| `title` | string | No | Words to match in app titles. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "app_data",
        "function": "search",
        "limit": 10,
        "se": "google",
        "title": "vpn"
      },
      "id": "11030828-2190-0554-0000-9d225ac53baf",
      "path": [
        "v3"
      ],
      "result": [
        {
          "count": 10,
          "items": [
            {
              "app_id": "free.vpn.unblock.proxy.turbovpn",
              "check_url": "https://play.google.com/store/apps/details?id=free.vpn.unblock.proxy.turbovpn&hl…",
              "item": {
                "app_id": "free.vpn.unblock.proxy.turbovpn",
                "description": "Turbo VPN is a free and unlimited VPN proxy, offering you a fast VPN connection …",
                "developer": "Innovative Connecting",
                "developer_address": "8 MARINA VIEW\n#43-052A ASIA SQUARE TOWER 1\nSingapore 018960",
                "developer_email": "developer@inconnecting.com",
                "developer_id": "7006518471988336602",
                "developer_url": "https://play.google.com/store/apps/dev?id=7006518471988336602",
                "developer_website": "https://www.turbovpn.co"
              },
              "language_code": "en",
              "location_code": 2840,
              "se_domain": "play.google.com",
              "time_update": "2026-11-02 22:15:27 +00:00"
            }
          ],
          "offset": 0,
          "offset_token": "eyJDdXJy…",
          "total_count": 4024
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.1872 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.1960 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Number of apps in the catalog that match the search. It can be far larger than the number returned in one call. |
| `tasks[].result[].count` | Number of apps returned in this response. |
| `tasks[].result[].items[].app_id` | Google Play package name of the app, such as `free.vpn.unblock.proxy.turbovpn`. |
| `tasks[].result[].items[].check_url` | Link to the app's page on Google Play, with `hl` and `gl` set in the query string. |
| `tasks[].result[].items[].item.developer` | Name of the app's developer. |
| `tasks[].result[].items[].item.developer_email / tasks[].result[].items[].item.developer_website / tasks[].result[].items[].item.developer_address` | Contact details the developer lists for the app. Some apps leave fields out. |
| `tasks[].result[].items[].item.developer_id / tasks[].result[].items[].item.developer_url` | Developer identifier and the Google Play page for that developer. |
| `tasks[].result[].items[].item.description` | Start of the app description. The text is cut off with an ellipsis. Not every app includes it. |
| `tasks[].result[].items[].item.genres[]` | Genre labels for the app, such as `Tools`. Not every app includes them. |
| `tasks[].result[].items[].time_update` | Timestamp for the listing record, in the form `2026-11-02 22:15:27 +00:00`. |

### Notes

- Pass `title` with the words to match. Add `description` to match words in the app text as well.
- `limit` sets how many apps come back. The response includes `offset` and `offset_token` for fetching further results.
- Use `app_id` as the identifier for the same app in other calls. The response also returns `language_code`, `location_code` and `se_domain`.
- To search Apple's store instead, use [DataForSEO App Store App Listings Search](/apis/dataforseo/v3/app_data/apple/app_listings/search/live).

### Pricing

Billed at the actual cost of each call, about $0.11 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/app_data/google/app_listings/search/live.json`](../../../../../../../../catalog/models/dataforseo/v3/app_data/google/app_listings/search/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/app_data/google/app_listings/search/live
