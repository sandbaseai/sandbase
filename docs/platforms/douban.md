# Douban API: 6 endpoints with pricing and code examples

Call 6 Douban endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`douban/movie-comments`](../models/douban/movie-comments.md) | Short comments (one-line reviews) on a Douban movie or TV subject with rating, user and location, sorted by time or score. | $0.014286 per call (free daily quota) |
| [`douban/movie-review-detail`](../models/douban/movie-review-detail.md) | Get a single Douban long-form review by its review ID. Use it to inspect a known review after discovering it in a subject's review list. | $0.014286 per call (free daily quota) |
| [`douban/movie-reviews`](../models/douban/movie-reviews.md) | Get paginated Douban long-form reviews for a movie or TV subject, ordered by time or popularity. Use it to browse in-depth audience… | $0.014286 per call (free daily quota) |
| [`douban/recent-hot-movie`](../models/douban/recent-hot-movie.md) | Get a paginated list of movies currently featured in Douban's recent-hot collection. Use it to discover popular movie titles and continue… | $0.014286 per call (free daily quota) |
| [`douban/recent-hot-tv`](../models/douban/recent-hot-tv.md) | Get a paginated list of TV titles currently featured in Douban's recent-hot collection. Use it to discover popular series and continue… | $0.014286 per call (free daily quota) |
| [`douban/subject-detail`](../models/douban/subject-detail.md) | Get the public detail page data for a Douban movie or TV subject by subject ID. Use it to inspect a known title before requesting its… | $0.014286 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douban/movie-comments", "subjectId": "1292052"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
