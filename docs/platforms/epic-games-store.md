# Epic Games Store API: 12 endpoints with pricing and code examples

Call 12 Epic Games Store endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`epic-games/browse-discounted-games`](../models/epic-games/browse-discounted-games.md) | Browses the Epic Games Store catalog filtered to discounted games only (priceTier=tierDiscounted). Supports the same filtering, sorting,… | $0.03 per call |
| [`epic-games/browse-games`](../models/epic-games/browse-games.md) | Browses the Epic Games Store catalog with optional filtering and sorting. Returns paginated results with total count. Uses offset-based… | $0.03 per call |
| [`epic-games/discover-something-new`](../models/epic-games/discover-something-new.md) | Returns games from the Discover Something New section on the Epic Games Store homepage. These are recently highlighted or newly released… | $0.03 per call |
| [`epic-games/free-games`](../models/epic-games/free-games.md) | Returns all currently free and upcoming free games from the Epic Games Store free games promotion page. Each game includes its status… | $0.03 per call |
| [`epic-games/free-games-coming-soon`](../models/epic-games/free-games-coming-soon.md) | Returns only games labeled COMING SOON from the Epic Games Store free games section. Filters out currently free games. Subset of… | $0.03 per call |
| [`epic-games/free-games-now`](../models/epic-games/free-games-now.md) | Returns only games currently labeled FREE NOW from the Epic Games Store free games section. Filters out upcoming free games. Subset of… | $0.03 per call |
| [`epic-games/game-details`](../models/epic-games/game-details.md) | Fetches full details for a specific game on the Epic Games Store by its URL slug. Returns description, pricing, genres, features, ratings,… | $0.03 per call |
| [`epic-games/homepage-featured`](../models/epic-games/homepage-featured.md) | Returns the hero/featured carousel items from the Epic Games Store homepage, including featured games, sales, and promotions with taglines… | $0.03 per call |
| [`epic-games/news`](../models/epic-games/news.md) | Returns recent news articles and blog posts from the Epic Games Store news section. Each article includes title, summary, publication… | $0.03 per call |
| [`epic-games/popular-genres`](../models/epic-games/popular-genres.md) | Returns popular game genre categories from the Epic Games Store browse page, including genre names, slugs, and representative images. | $0.03 per call |
| [`epic-games/search-games`](../models/epic-games/search-games.md) | Searches for games by keyword in the Epic Games Store catalog. Returns up to 20 matching results sorted by relevancy. | $0.03 per call |
| [`epic-games/top-new-releases`](../models/epic-games/top-new-releases.md) | Returns games from the Top New Releases section on the Epic Games Store homepage. These are recently released titles curated by Epic. | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "epic-games/browse-discounted-games"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
