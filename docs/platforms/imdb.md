# IMDb API: 17 endpoints with pricing and code examples

Call 17 IMDb endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`imdb/news-by-category-query`](../models/imdb/news-by-category-query.md) | Get IMDb news for a selected top, movie, TV, or celebrity category using language and country preferences. Use it to monitor entertainment… | $0.007143 per call (free daily quota) |
| [`imdb/streaming-picks-query`](../models/imdb/streaming-picks-query.md) | Get IMDb streaming picks for Prime Video using selected language and country preferences. Use it to explore streaming titles for… | $0.007143 per call (free daily quota) |
| [`imdb/title-awards-summary-query`](../models/imdb/title-awards-summary-query.md) | Get the IMDb awards summary for a title ID using selected language and country preferences. Use it to research a title's awards record or… | $0.007143 per call (free daily quota) |
| [`imdb/title-base-query`](../models/imdb/title-base-query.md) | Get base IMDb information for a title ID using selected language and country preferences. Use it to perform a lightweight title lookup or… | $0.007143 per call (free daily quota) |
| [`imdb/title-box-office-summary`](../models/imdb/title-box-office-summary.md) | Get the IMDb box-office summary for a title ID using selected language and country preferences. Use it to research reported theatrical… | $0.007143 per call (free daily quota) |
| [`imdb/title-chart-rankings`](../models/imdb/title-chart-rankings.md) | Get the IMDb Top 250 movie or TV chart selected by ranking type using language and country preferences. Use it to monitor chart positions… | $0.007143 per call (free daily quota) |
| [`imdb/title-countries-of-origin`](../models/imdb/title-countries-of-origin.md) | Get countries of origin associated with an IMDb title ID using selected language and country preferences. Use it to enrich regional… | $0.007143 per call (free daily quota) |
| [`imdb/title-critics-review-summary-query`](../models/imdb/title-critics-review-summary-query.md) | Get the IMDb critics-review summary for a title ID using selected language and country preferences. Use it to review critical reception or… | $0.007143 per call (free daily quota) |
| [`imdb/title-details-query`](../models/imdb/title-details-query.md) | Get IMDb title details for a title ID using selected language and country preferences. Use it to support detailed title research or enrich… | $0.007143 per call (free daily quota) |
| [`imdb/title-did-you-know-query`](../models/imdb/title-did-you-know-query.md) | Get IMDb 'Did You Know' information for a title ID using selected language and country preferences. Use it to research title trivia and… | $0.007143 per call (free daily quota) |
| [`imdb/title-extended-details-query`](../models/imdb/title-extended-details-query.md) | Get extended IMDb details for a title ID using selected language and country preferences. Use it to enrich a title catalog or perform… | $0.007143 per call (free daily quota) |
| [`imdb/title-more-like-this-query`](../models/imdb/title-more-like-this-query.md) | Get IMDb titles similar to a specified title ID using selected language and country preferences. Use it to support related-title… | $0.007143 per call (free daily quota) |
| [`imdb/title-plot-query`](../models/imdb/title-plot-query.md) | Get IMDb plot information for a title ID using selected language and country preferences. Use it to review a movie or series storyline or… | $0.007143 per call (free daily quota) |
| [`imdb/title-redux-overview-query`](../models/imdb/title-redux-overview-query.md) | Get the IMDb Redux overview for a title ID using selected language and country preferences. Use it to obtain a consolidated title overview… | $0.007143 per call (free daily quota) |
| [`imdb/title-release-expectation-query`](../models/imdb/title-release-expectation-query.md) | Get IMDb release-expectation information for a title ID using selected language and country preferences. Use it to monitor a title's… | $0.007143 per call (free daily quota) |
| [`imdb/title-top-cast-and-crew`](../models/imdb/title-top-cast-and-crew.md) | Get IMDb top cast and crew information for a title ID using selected language and country preferences. Use it to research principal talent… | $0.007143 per call (free daily quota) |
| [`imdb/title-user-reviews-summary-query`](../models/imdb/title-user-reviews-summary-query.md) | Get the IMDb user-reviews summary for a title ID using selected language and country preferences. Use it to review audience reception or… | $0.007143 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "imdb/news-by-category-query", "category": "TOP"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
