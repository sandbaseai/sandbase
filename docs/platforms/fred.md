# FRED API: 35 endpoints with pricing and code examples

Call 35 FRED endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`fred/category`](../models/fred/category.md) | category from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/category-children`](../models/fred/category-children.md) | Get Category Children from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/category-related`](../models/fred/category-related.md) | Get Category Related from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/category-related-tags`](../models/fred/category-related-tags.md) | Get Category Related Tags from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/category-series`](../models/fred/category-series.md) | Get Category Series from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/category-tags`](../models/fred/category-tags.md) | Get Category Tags from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/geo-regional-data`](../models/fred/geo-regional-data.md) | GeoFRED Regional Data from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/geo-series-data`](../models/fred/geo-series-data.md) | GeoFRED Series Data from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/geo-series-group`](../models/fred/geo-series-group.md) | GeoFRED Series Group from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/geo-shapes-file`](../models/fred/geo-shapes-file.md) | GeoFRED Shape Files from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/related-tags`](../models/fred/related-tags.md) | Get Related Tags from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/release`](../models/fred/release.md) | Get Release from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/release-dates`](../models/fred/release-dates.md) | Get Release Dates from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/release-related-tags`](../models/fred/release-related-tags.md) | Get Release Related Tags from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/release-series`](../models/fred/release-series.md) | Get Release Series from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/release-sources`](../models/fred/release-sources.md) | Get Release Sources from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/release-tables`](../models/fred/release-tables.md) | Get Release Tables from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/release-tags`](../models/fred/release-tags.md) | Get Release Tags from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/releases`](../models/fred/releases.md) | Get Releases from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/releases-dates`](../models/fred/releases-dates.md) | Get Releases Dates from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series`](../models/fred/series.md) | Get Series from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series-categories`](../models/fred/series-categories.md) | Get Series Categories from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series-observations`](../models/fred/series-observations.md) | Get Series Observations from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series-release`](../models/fred/series-release.md) | Get Series Release from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series-search`](../models/fred/series-search.md) | Search Series from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series-search-related-tags`](../models/fred/series-search-related-tags.md) | Search Series Related Tags from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series-search-tags`](../models/fred/series-search-tags.md) | Search Series Tags from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series-tags`](../models/fred/series-tags.md) | Get Series Tags from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series-updates`](../models/fred/series-updates.md) | Get Series Updates from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/series-vintagedates`](../models/fred/series-vintagedates.md) | Get Series Vintage Dates from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/source`](../models/fred/source.md) | Get Source from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/source-releases`](../models/fred/source-releases.md) | Get Source Releases from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/sources`](../models/fred/sources.md) | Get Sources from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/tags`](../models/fred/tags.md) | Get Tags from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |
| [`fred/tags-series`](../models/fred/tags-series.md) | Get Tags Series from FRED. Returns the official FRED API response unchanged. | $1e-05 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/category"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
