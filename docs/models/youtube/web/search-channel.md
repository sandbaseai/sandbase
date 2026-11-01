# YouTube Channel Video Search

`youtube/web/search-channel` · api · YouTube

Searches videos within a specific YouTube channel using a keyword query. Returns matching video details including title, view count, post date, and video ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web/search-channel", "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw", "country_code": "us", "language_code": "en", "search_query": "AMD"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web/search-channel', {'channel_id': 'UCXuqSBlHAE6Xw-yeJA0Tunw', 'country_code': 'us', 'language_code': 'en', 'search_query': 'AMD'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web/search-channel", {
  "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
  "country_code": "us",
  "language_code": "en",
  "search_query": "AMD"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web/search-channel", sandbase.Params{
	"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
	"country_code": "us",
	"language_code": "en",
	"search_query": "AMD",
})
```

Same call via the path form: `POST /v1/api/youtube/web/search-channel` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `channel_id` | string | yes | Channel ID  |
| `country_code` | string |  | Country code, default is us. default `"us"` |
| `search_query` | string | yes | Search keyword.  |
| `language_code` | string |  | Language code, default is en. default `"en"` |
| `continuation_token` | string |  | Token to continue fetching search results. Default is None.  |

## Details

Search for videos uploaded by a specific channel using `channel_id` and `search_query`. Supports optional localization via `country_code` and `language_code`.

### Use cases

- Find relevant videos uploaded by a specific creator.
- Audit channel coverage on particular topics or brand keywords.
- Retrieve video identifiers and view metrics for targeted channel searches.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web/search-channel" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw", "search_query": "AMD"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `channel_id` | string | Yes | Channel ID |
| `search_query` | string | Yes | Search keyword. |
| `country_code` | string | No | Country code, default is us. |
| `language_code` | string | No | Language code, default is en. |
| `continuation_token` | string | No | Token to continue fetching search results. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "videos": [
    {
      "author": "Linus Tech Tips",
      "channel_id": "UCXuqSBlHAE6Xw-yeJA0Tunw",
      "description": "Thanks to AMD for sponsoring this series and sending us a couple of ROG Allys to give awa…",
      "number_of_views": 3963165,
      "published_time": "2 years ago",
      "title": "Don't Get in Trouble with HR Challenge (HARD) - AMD $5,000 Ultimate Tech Upgrade",
      "type": "NORMAL",
      "video_id": "oTYwd9OjFRk"
    }
  ]
}
```

### Notes

- Use `continuation_token` to paginate through subsequent search results.
- `country_code` defaults to us and `language_code` defaults to en.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel ID Lookup](/model/youtube/web/channel-id): Retrieves the unique YouTube channel ID associated with a specific channel name.
- [YouTube Channel ID from URL (V2)](/model/youtube/web/channel-id-v2): Resolves a YouTube channel URL into its unique channel ID and standardized channel URL.
- [YouTube Channel Information](/model/youtube/web/channel-info): Returns profile details and external links for a specified YouTube channel.

---
Machine-readable: [`catalog/models/youtube/web/search-channel.json`](../../../../catalog/models/youtube/web/search-channel.json) · Store page: https://www.sandbase.ai/model/youtube/web/search-channel
