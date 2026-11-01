# YouTube Video Comment Replies

`youtube/web-v2/video-comment-replies` · api · YouTube

Returns second-level replies for a YouTube video comment using a continuation token, with optional filters for region, language, and formatted output.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-comment-replies", "continuation_token": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-comment-replies', {'continuation_token': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-comment-replies", {
  "continuation_token": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-comment-replies", sandbase.Params{
	"continuation_token": "example",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-comment-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `need_format` | boolean |  | **Purpose**: Whether to return cleaned simplified data  |
| `country_code` | string |  | **Purpose**: Region code  |
| `language_code` | string |  | **Purpose**: Language preference for comments  |
| `continuation_token` | string | yes | **Purpose**: Reply continuation token from first-level comment  |

## Details

Retrieve threaded replies to a top-level video comment by supplying `continuation_token`.

### Use cases

- Display conversation threads beneath specific video comments.
- Collect user responses in targeted languages and regions.
- Extract simplified reply data for sentiment analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-comment-replies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"continuation_token": "<continuation_token>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `continuation_token` | string | Yes | Purpose: Reply continuation token from first-level comment |
| `need_format` | boolean | No | Purpose: Whether to return cleaned simplified data |
| `country_code` | string | No | Purpose: Region code |
| `language_code` | string | No | Purpose: Language preference for comments |

### Notes

- Pass `continuation_token` obtained from a first-level comment to access its replies.
- Set `need_format` to true to receive cleaned, simplified response data.
- Filter replies by locale using `country_code` and `language_code`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-comment-replies.json`](../../../../catalog/models/youtube/web-v2/video-comment-replies.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-comment-replies
