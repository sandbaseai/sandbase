# Ximalaya API: 7 endpoints with pricing and code examples

Call 7 Ximalaya endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`ximalaya/album-comments`](../models/ximalaya/album-comments.md) | Retrieve comments for an album with pagination. Returns comment content, author nickname, likes, reply count, region, creation timestamp,… | $0.03 per call |
| [`ximalaya/album-info`](../models/ximalaya/album-info.md) | Retrieve detailed metadata for a single album by its numeric ID. Returns title, cover, play count, subscription count, pricing, intro… | $0.03 per call |
| [`ximalaya/album-tracks`](../models/ximalaya/album-tracks.md) | List tracks within an album with pagination. Returns track title, duration (seconds), play count, likes, comments count, pricing info, and… | $0.03 per call |
| [`ximalaya/categories`](../models/ximalaya/categories.md) | Retrieve all top-level content categories on Ximalaya. Each category has a pinyin name usable as a key in get_category_albums. Returns the… | $0.03 per call |
| [`ximalaya/category-albums`](../models/ximalaya/category-albums.md) | List albums within a category, sorted by popularity. Category is identified by its pinyin name (from get_categories). Paginates via page… | $0.03 per call |
| [`ximalaya/search-albums`](../models/ximalaya/search-albums.md) | Full-text search for albums by keyword. Supports Chinese and English queries. Returns paginated results with album summaries including… | $0.03 per call |
| [`ximalaya/user-info`](../models/ximalaya/user-info.md) | Retrieve public profile information for a user or anchor by numeric UID. Returns nickname, avatar, fan count, following count, track/album… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ximalaya/album-comments", "album_id": "81519744"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
