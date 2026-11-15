# ESPN API: 10 endpoints with pricing and code examples

Call 10 ESPN endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`espn/athlete-gamelog`](../models/espn/athlete-gamelog.md) | Get game-by-game stats for an athlete with monthly breakdowns, totals, and averages. Stats labels are sport-specific. Each game includes… | $0.06 per call |
| [`espn/athlete-overview`](../models/espn/athlete-overview.md) | Get comprehensive athlete data including season/career stats, fantasy projections, recent news, awards, and expert analysis. Stats labels… | $0.03 per call |
| [`espn/athlete-profile`](../models/espn/athlete-profile.md) | Get detailed athlete profile including biographical info, team, injuries, contracts, and status. Returns physical attributes, career… | $0.03 per call |
| [`espn/news`](../models/espn/news.md) | Get latest news articles and headlines for a specific league. Returns articles with full metadata including categories, images, and links. | $0.03 per call |
| [`espn/scoreboard`](../models/espn/scoreboard.md) | Get live scores, final results, and upcoming fixtures for any supported league. | $0.03 per call |
| [`espn/search`](../models/espn/search.md) | Search for athletes and teams across all sports. Returns matching results with IDs for use in other endpoints. When type filter is… | $0.06 per call |
| [`espn/search-news`](../models/espn/search-news.md) | Search ESPN news articles about a topic within a league using the site's article search. | $0.03 per call |
| [`espn/standings`](../models/espn/standings.md) | Get current standings/rankings for a league, organized by conference/division with full statistics. Season type '2' returns regular season… | $0.03 per call |
| [`espn/team-roster`](../models/espn/team-roster.md) | Get full roster for a team including player profiles, injuries, and contract details. Each athlete includes biographical info, position,… | $0.03 per call |
| [`espn/teams`](../models/espn/teams.md) | Get all teams for a given league with IDs, names, logos, and links. Returns a complete roster of teams participating in the specified… | $0.03 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "espn/athlete-gamelog", "league": "nba", "athlete_id": "1966"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
