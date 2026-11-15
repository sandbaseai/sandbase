# Baidu API: 11 endpoints with pricing and code examples

Call 11 Baidu endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`baidu/board-by-tab`](../models/baidu/board-by-tab.md) | General-purpose endpoint to retrieve any board tab (realtime, novel, movie, teleplay) with optional tag filtering. Returns ranked items… | $0.03 per call |
| [`baidu/homepage-summary`](../models/baidu/homepage-summary.md) | Fetch the main home/board overview page summary with cloud trending topics and top items for all categories (realtime, novel, movie,… | $0.03 per call |
| [`baidu/maps`](../models/baidu/maps.md) | Search places on Baidu Maps by keyword in a city or around coordinates, with name, address, category, rating, phone and coordinates. | $0.01 per call |
| [`baidu/movie-rankings`](../models/baidu/movie-rankings.md) | Fetch the hot movie rankings from the Baidu Top board. Returns ranked movies with scores and available filter tags for genre and region. | $0.03 per call |
| [`baidu/news`](../models/baidu/news.md) | Baidu News results for a keyword: headline, source, date, snippet and link. | $0.015 per call |
| [`baidu/novel-rankings`](../models/baidu/novel-rankings.md) | Fetch the hot novel rankings from the Baidu Top board. Returns all novels currently ranked with their scores, along with available genre… | $0.03 per call |
| [`baidu/novel-rankings-by-genre`](../models/baidu/novel-rankings-by-genre.md) | Fetch novel rankings filtered by genre type. Returns novels matching the specified genre along with available tags. Equivalent to… | $0.03 per call |
| [`baidu/realtime-hot-search`](../models/baidu/realtime-hot-search.md) | Fetch the real-time hot search rankings from the Baidu Top board. Returns the current top trending search terms with scores and metadata.… | $0.03 per call |
| [`baidu/search`](../models/baidu/search.md) | Get Baidu web results for a query with organic results, answer boxes, related searches and pagination. | $0.01 per call |
| [`baidu/search-results-for-keyword`](../models/baidu/search-results-for-keyword.md) | Construct a Baidu search URL for a specific hot search keyword to view related news and discussions. Does not fetch search results; only… | $0.03 per call |
| [`baidu/tv-drama-rankings`](../models/baidu/tv-drama-rankings.md) | Fetch the hot TV drama rankings from the Baidu Top board. Returns ranked TV dramas with scores and available filter tags for genre and… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "baidu/board-by-tab", "tab": "realtime"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
