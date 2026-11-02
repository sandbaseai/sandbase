# Polymarket API: 59 endpoints with pricing and code examples

Call 59 Polymarket endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`polymarket/activity`](../models/polymarket/activity.md) | Get user activity from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |
| [`polymarket/book`](../models/polymarket/book.md) | Retrieves the order book summary for a specific token ID. Includes bids, asks, market details, and last trade price. | $0.012 per call (free daily quota) |
| [`polymarket/builders-leaderboard`](../models/polymarket/builders-leaderboard.md) | Get aggregated builder leaderboard from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |
| [`polymarket/builders-volume`](../models/polymarket/builders-volume.md) | Get daily builder volume time-series from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |
| [`polymarket/clob-markets`](../models/polymarket/clob-markets.md) | Returns all CLOB-level parameters for a market in a single call — tokens, tick size, base fees, rewards, RFQ status, and fee details. | $0.012 per call (free daily quota) |
| [`polymarket/closed-positions`](../models/polymarket/closed-positions.md) | Get closed positions for a user from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |
| [`polymarket/comments`](../models/polymarket/comments.md) | List comments from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/comments-by-id`](../models/polymarket/comments-by-id.md) | Get comments by comment id from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/comments-user-address`](../models/polymarket/comments-user-address.md) | Get comments by user address from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/events`](../models/polymarket/events.md) | List events with offset based pagination and filter parameters. | $0.00044 per call (free daily quota) |
| [`polymarket/events-by-id`](../models/polymarket/events-by-id.md) | Get event by id from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/events-keyset`](../models/polymarket/events-keyset.md) | List events with cursor based keyset pagination. Use next_cursor as after_cursor to fetch the next page. The offset parameter is rejected. | $0.00044 per call (free daily quota) |
| [`polymarket/events-slug`](../models/polymarket/events-slug.md) | Get event by slug from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/events-tags`](../models/polymarket/events-tags.md) | Get event tags from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/fee-rate`](../models/polymarket/fee-rate.md) | Retrieves the base fee rate for a specific token ID. The fee rate can be provided either as a query parameter or as a path parameter. | $0.012 per call (free daily quota) |
| [`polymarket/fee-rate-by-token-id`](../models/polymarket/fee-rate-by-token-id.md) | Retrieves the base fee rate for a specific token ID using the token ID as a path parameter. | $0.012 per call (free daily quota) |
| [`polymarket/holders`](../models/polymarket/holders.md) | Get top holders for markets from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/last-trade-price`](../models/polymarket/last-trade-price.md) | Retrieves the last trade price and side for a specific token ID. Returns default values of 0.5 for price and empty string for side if no… | $0.012 per call (free daily quota) |
| [`polymarket/leaderboard`](../models/polymarket/leaderboard.md) | Returns trader leaderboard rankings for a selected category and time period. | $0.012 per call (free daily quota) |
| [`polymarket/live-volume`](../models/polymarket/live-volume.md) | Get live volume for an event from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/market-positions`](../models/polymarket/market-positions.md) | Returns positions for a market, optionally filtered to a single user. | $0.012 per call (free daily quota) |
| [`polymarket/markets`](../models/polymarket/markets.md) | List markets from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/markets-by-id`](../models/polymarket/markets-by-id.md) | Get market by id from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/markets-by-token`](../models/polymarket/markets-by-token.md) | Get market by token from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/markets-keyset`](../models/polymarket/markets-keyset.md) | List markets (keyset pagination) from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/markets-slug`](../models/polymarket/markets-slug.md) | Get market by slug from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/markets-tags`](../models/polymarket/markets-tags.md) | Get market tags by id from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/midpoint`](../models/polymarket/midpoint.md) | Retrieves the midpoint price for a specific token ID. The midpoint is calculated as the average of the best bid and best ask prices. | $0.012 per call (free daily quota) |
| [`polymarket/oi`](../models/polymarket/oi.md) | Get open interest from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/positions`](../models/polymarket/positions.md) | Get current positions for a user from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |
| [`polymarket/price`](../models/polymarket/price.md) | Retrieves the best market price for a specific token ID and side (bid or ask). Returns the best bid price for BUY side or best ask price… | $0.012 per call (free daily quota) |
| [`polymarket/prices-history`](../models/polymarket/prices-history.md) | Get prices history from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |
| [`polymarket/public-profile`](../models/polymarket/public-profile.md) | Get public profile by wallet address from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/public-search`](../models/polymarket/public-search.md) | Search markets, events, and profiles from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |
| [`polymarket/rewards-markets`](../models/polymarket/rewards-markets.md) | Get raw rewards for a specific market from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |
| [`polymarket/rewards-markets-current`](../models/polymarket/rewards-markets-current.md) | Returns the current active rewards configurations for markets. | $0.012 per call (free daily quota) |
| [`polymarket/rewards-markets-multi`](../models/polymarket/rewards-markets-multi.md) | Returns multiple markets with rewards and supports filtering and sorting. | $0.012 per call (free daily quota) |
| [`polymarket/sampling-markets`](../models/polymarket/sampling-markets.md) | Returns sampling markets with richer descriptive metadata, token summaries, and tags. | $0.012 per call (free daily quota) |
| [`polymarket/sampling-simplified-markets`](../models/polymarket/sampling-simplified-markets.md) | Returns sampling simplified markets with reward and token summaries. | $0.012 per call (free daily quota) |
| [`polymarket/series`](../models/polymarket/series.md) | List series from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/series-by-id`](../models/polymarket/series-by-id.md) | Get series by id from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/simplified-markets`](../models/polymarket/simplified-markets.md) | Returns simplified CLOB markets with token and reward summaries. | $0.012 per call (free daily quota) |
| [`polymarket/sports`](../models/polymarket/sports.md) | Get sports metadata information from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/sports-market-types`](../models/polymarket/sports-market-types.md) | Get valid sports market types from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/spread`](../models/polymarket/spread.md) | Retrieves the spread for a specific token ID. The spread is the difference between the best ask and best bid prices. | $0.012 per call (free daily quota) |
| [`polymarket/supported-assets`](../models/polymarket/supported-assets.md) | Get supported assets for deposits and withdrawals on the bridge. | $0.012 per call (free daily quota) |
| [`polymarket/tags`](../models/polymarket/tags.md) | List tags from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/tags-by-id`](../models/polymarket/tags-by-id.md) | Get tag by id from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/tags-related-tags`](../models/polymarket/tags-related-tags.md) | Get related tags (relationships) by tag id from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/tags-related-tags-tags`](../models/polymarket/tags-related-tags-tags.md) | Get tags related to a tag id from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/tags-slug`](../models/polymarket/tags-slug.md) | Get tag by slug from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/tags-slug-related-tags`](../models/polymarket/tags-slug-related-tags.md) | Get related tags (relationships) by tag slug from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/tags-slug-related-tags-tags`](../models/polymarket/tags-slug-related-tags-tags.md) | Get tags related to a tag slug from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/teams`](../models/polymarket/teams.md) | List teams from Polymarket. Returns the official Polymarket API response unchanged. | $0.00044 per call (free daily quota) |
| [`polymarket/tick-size`](../models/polymarket/tick-size.md) | Retrieves the minimum tick size (price increment) for a specific token ID. The tick size can be provided either as a query parameter or as… | $0.012 per call (free daily quota) |
| [`polymarket/tick-size-by-token-id`](../models/polymarket/tick-size-by-token-id.md) | Retrieves the minimum tick size (price increment) for a specific token ID using the token ID as a path parameter. | $0.012 per call (free daily quota) |
| [`polymarket/time`](../models/polymarket/time.md) | Returns the current Unix timestamp of the server. This can be used to synchronize client time with server time. | $0.012 per call (free daily quota) |
| [`polymarket/traded`](../models/polymarket/traded.md) | Get total markets a user has traded from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |
| [`polymarket/value`](../models/polymarket/value.md) | Get total value of a user's positions from Polymarket. Returns the official Polymarket API response unchanged. | $0.012 per call (free daily quota) |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/activity", "user": "0x56687bf447db6ffa42ffe2204a05edaa20f55839"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
