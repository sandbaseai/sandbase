# Pinterest API: 4 endpoints with pricing and code examples

Call 4 Pinterest endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`pinterest/board`](../models/pinterest/board.md) | Returns a paginated list of pins from a specified Pinterest board URL, including pin metadata, images, and aggregated pin metrics. | $0.018 per call |
| [`pinterest/pin`](../models/pinterest/pin.md) | Returns detailed information for a single Pinterest pin using its page URL. Supports an optional setting to return a trimmed response… | $0.018 per call |
| [`pinterest/search`](../models/pinterest/search.md) | Search Pinterest pins by keyword and get pin IDs, URLs, titles, descriptions and images, with cursor pagination. | $0.018 per call |
| [`pinterest/user-boards`](../models/pinterest/user-boards.md) | Get a Pinterest user's boards by username: board name, URL, description, pin and follower counts, cover images and creation date. | $0.018 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pinterest/board", "url": "<url>"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
