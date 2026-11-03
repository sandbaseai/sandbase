# App Store Search API: pricing, parameters and code examples

`app-store/search` · data API · App Store · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Search iPhone, iPad, and Mac apps or developers on the Apple App Store by storefront.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "app-store/search", "term": "software"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('app-store/search', {'term': 'software'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("app-store/search", {
  "term": "software"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "app-store/search", sandbase.Params{
	"term": "software",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/app-store/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `num` | integer |  | Maximum results after filtering, 1-200. Default 10. range 1–200 |
| `lang` | string |  | Language-region code, such as 'en-us' or 'fr-fr'. Default 'en-us'.  |
| `term` | string | yes | Search term, 1-2,048 UTF-8 bytes (at most 4,096 bytes URL-encoded).  |
| `device` | string |  | 'mobile' for iPhone apps, 'tablet' for iPad apps, 'desktop' for Mac apps. Default 'mobile'. one of: `mobile`, `tablet`, `desktop` |
| `country` | string |  | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'.  |
| `property` | string |  | 'developer' matches developer names instead of app names, ignoring case. one of: `developer` |
| `category_id` | integer |  | Filter results by a native genre identifier. range 1–2147483647 |
| `disallow_explicit` | boolean |  | Exclude explicit results.  |

## Details

Returns a ranked list of Apple App Store apps that match a search term. Each result includes the title, developer, genres, rating, version and store links. The only required input is `term`.

### Use cases

- Track which apps rank for a keyword in a given country storefront.
- Find every app from one publisher by searching with `property` set to `developer`.
- Compare ratings, rating counts and release dates of competing apps in one category.
- Build a list of iPad or Mac apps in a genre by combining `device` and `category_id`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/app-store/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"term": "software"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `term` | string | Yes | Search term, 1-2,048 UTF-8 bytes (at most 4,096 bytes URL-encoded). |
| `category_id` | integer | No | Filter results by a native genre identifier. |
| `country` | string | No | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'. |
| `device` | string | No | 'mobile' for iPhone apps, 'tablet' for iPad apps, 'desktop' for Mac apps. Default 'mobile'. |
| `disallow_explicit` | boolean | No | Exclude explicit results. |
| `lang` | string | No | Language-region code, such as 'en-us' or 'fr-fr'. Default 'en-us'. |
| `num` | integer | No | Maximum results after filtering, 1-200. Default 10. |
| `property` | string | No | 'developer' matches developer names instead of app names, ignoring case. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "organic_results": [
    {
      "age_rating": "4+",
      "bundle_id": "com.microsoft.Office.Word",
      "developer": {
        "id": 298856275,
        "link": "https://apps.apple.com/us/developer/microsoft-corporation/id298856275?uo=4",
        "name": "Microsoft Corporation"
      },
      "features": [
        "iosUniversal"
      ],
      "game_center_enabled": false,
      "genres": [
        {
          "id": 6007,
          "name": "Productivity",
          "primary": true
        }
      ],
      "id": 586447913,
      "latest_version_release_date": "2026-11-02 05:07:19 UTC",
      "link": "https://apps.apple.com/us/app/microsoft-word/id586447913?uo=4",
      "logos": [
        {
          "link": "https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/c9/0d/34/c90d341a-8dfb-212…",
          "size": "60x60"
        }
      ],
      "minimum_os_version": "26.0",
      "position": 1
    }
  ],
  "search_information": {
    "results_count": 9
  },
  "search_metadata": {
    "created_at": "2026-11-03T07:27:08.338171+00:00",
    "id": "994e99f484266a1b4770aa3a",
    "processed_at": "2026-11-03T07:27:08.853517+00:00",
    "status": "Success",
    "total_time_taken": 0.515
  },
  "search_parameters": {
    "country": "us",
    "device": "mobile",
    "disallow_explicit": false,
    "lang": "en-us",
    "num": 10,
    "term": "software"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `organic_results[].position` | Rank of the app in the results, starting at 1. |
| `organic_results[].title / organic_results[].bundle_id` | App name shown in the store and its bundle identifier, such as `com.microsoft.Office.Word`. |
| `organic_results[].id` | Numeric App Store ID of the app. It is also the number after `id` in `link`. |
| `organic_results[].developer.name / organic_results[].developer.id` | Name and numeric ID of the developer. `developer.link` points to the developer page. |
| `organic_results[].genres[].name` | Genres of the app. The entry with `primary` set to `true` is the main genre. `id` is the genre identifier that `category_id` accepts. |
| `organic_results[].rating[].rating / organic_results[].rating[].count` | Average star rating and number of ratings. Each entry has a `type`, either `All Times` or `Current Version`. |
| `organic_results[].version / organic_results[].latest_version_release_date / organic_results[].release_date` | Current version number, the date of the latest version, and the first release date. Dates look like `2026-11-02 05:07:19 UTC`. |
| `organic_results[].age_rating / organic_results[].advisories` | Age rating such as `4+` or `17+`, and content advisories when the app has any. |
| `organic_results[].size_in_bytes / organic_results[].minimum_os_version` | App download size in bytes and the lowest OS version the app supports. |
| `search_information.results_count` | Number of results returned for this search. |

### Notes

- `num` sets the maximum number of results, from 1 to 200. The default is 10.
- The `country` and `lang` parameters pick the storefront and the language of the text. The response echoes the values used in `search_parameters`.
- Some results omit fields such as `description`, `release_note` and `seller_link`, so check that a key exists before you read it.
- To get more detail on one app, pass its `id` to [App Store Product](/apis/app-store/product). For user reviews, use [App Store Reviews](/apis/app-store/reviews).

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/app-store/search.json`](../../../catalog/models/app-store/search.json) · Store page: https://www.sandbase.ai/model/app-store/search
