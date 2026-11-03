# DataForSEO App Store App Listings Search API: pricing, parameters and code examples

`dataforseo/v3/app_data/apple/app_listings/search/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.11 per call · **Modes:** sync

Search the Apple App Store catalog by app title or description and get ratings, review counts and prices for each match.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.11**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/app_data/apple/app_listings/search/live"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/app_data/apple/app_listings/search/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/app_data/apple/app_listings/search/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/app_data/apple/app_listings/search/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/app_data/apple/app_listings/search/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of apps to return.  |
| `title` | string |  | Words to match in app titles.  |
| `filters` | string |  | Optional filter array, e.g. [["rating.value", ">", 4]].  |
| `description` | string |  | Optional words to match in app descriptions.  |

## Details

This API searches the Apple App Store catalog for apps whose title (and optionally description) match the words you send. It needs a `title` value and returns a list of matching apps with their IDs, developer details, store URLs and icons.

### Use cases

- Find competing VPN apps by searching a keyword like `vpn` in app titles.
- Build a list of apps from one developer by collecting `developer_id` and `developer_url` values.
- Check how many App Store apps match a keyword with `total_count` to gauge how crowded a niche is.
- Collect `app_id` values to feed into other app lookups or to track specific apps.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/app_data/apple/app_listings/search/live" \
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
        "se": "apple",
        "title": "vpn"
      },
      "id": "11030828-2190-0556-0000-555cc30267bd",
      "path": [
        "v3"
      ],
      "result": [
        {
          "count": 10,
          "items": [
            {
              "app_id": "1370293473",
              "check_url": "https://apps.apple.com/us/app/id1370293473?l=en-US",
              "item": {
                "advisories": [
                  "4+"
                ],
                "app_id": "1370293473",
                "categories": null,
                "description": "■ Free VPN for iPhone - access global content\n■ Unlimited time, bandwidth, and s…",
                "developer": "Mobile Jump Pte Ltd",
                "developer_id": "1484585154",
                "developer_url": "https://apps.apple.com/us/developer/mobile-jump-pte-ltd/id1484585154?platform=ip…",
                "icon": "https://is1-ssl.mzstatic.com/image/thumb/PurpleSource211/v4/3e/b9/ad/3eb9ad77-10…"
              },
              "language_code": "en",
              "location_code": 2840,
              "se_domain": "itunes.apple.com",
              "time_update": "2026-10-02 05:33:49 +00:00"
            }
          ],
          "offset": 0,
          "offset_token": "eyJDdXJy…",
          "total_count": 1873
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "0.2280 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "0.2401 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].total_count` | Total number of apps that match the search. It can be larger than the number returned in this call. |
| `tasks[].result[].count` | Number of apps returned in this response. |
| `tasks[].result[].items[].app_id` | App Store ID of the app, as a string. It is the number in the `check_url` after `id`. |
| `tasks[].result[].items[].check_url` | Link to the app's page on the App Store. |
| `tasks[].result[].items[].item.developer / tasks[].result[].items[].item.developer_id` | Name and numeric ID of the developer that publishes the app. |
| `tasks[].result[].items[].item.developer_url` | Link to the developer's page on the App Store. |
| `tasks[].result[].items[].item.description` | Start of the app description text. Some items do not include it, and long text is cut. |
| `tasks[].result[].items[].item.advisories` | Age rating labels for the app, such as `4+`. |
| `tasks[].result[].items[].item.icon / tasks[].result[].items[].item.images[]` | URLs of the app icon and of its listing screenshots. `images` appears only on some items. |
| `tasks[].result[].items[].time_update` | Date and time the listing was last updated, in the format `2026-10-02 05:33:49 +00:00`. |

### Notes

- Use `offset_token` from `tasks[].result[]` to continue past the first page. `offset` shows where the current page starts.
- `limit` sets the maximum number of apps returned. The example request uses `10`.
- `location_code` is `2840` and `language_code` is `en` in this response. `se_domain` is `itunes.apple.com`.
- To search Android apps instead, use [DataForSEO Google Play App Listings Search](/apis/dataforseo/v3/app_data/google/app_listings/search/live).

### Pricing

Billed at the actual cost of each call, about $0.11 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/dataforseo/v3/app_data/apple/app_listings/search/live.json`](../../../../../../../../catalog/models/dataforseo/v3/app_data/apple/app_listings/search/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/app_data/apple/app_listings/search/live
