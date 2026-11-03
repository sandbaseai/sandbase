# Douyin sec_user_id from URL API: pricing, parameters and code examples

`douyin/web/sec-user-id` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Extracts the Douyin sec_user_id identifier from a provided web link or profile URL. Input the target link in the query parameter to resolve the user identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/sec-user-id", "url": "https://www.douyin.com/video/7691553968815623478"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/sec-user-id', {'url': 'https://www.douyin.com/video/7691553968815623478'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/sec-user-id", {
  "url": "https://www.douyin.com/video/7691553968815623478"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/sec-user-id", sandbase.Params{
	"url": "https://www.douyin.com/video/7691553968815623478",
})
```

Same call via the path form: `POST /v1/api/douyin/web/sec-user-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Url  |

## Details

This API takes a Douyin web link in the `url` parameter and returns a single JSON string. It is meant to extract the `sec_user_id` from a user profile link. In the sample call, a video link came back as the same URL text.

### Use cases

- Turn a shared Douyin profile link into a `sec_user_id` before you request that user's data.
- Prepare user identifiers for [Douyin User Profile (Web)](/apis/douyin/web/user-profile) from profile links you collected.
- Check whether a pasted Douyin link resolves to an identifier or comes back unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/sec-user-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.douyin.com/video/7691553968815623478"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes |  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
"https://www.douyin.com/video/7691553968815623478"
```

### Response fields

| Field | Meaning |
|---|---|
| `$` | The whole response is one plain JSON string, not an object, so it has no named fields. |
| `$` | For a user profile link, this string is the resolved `sec_user_id`, according to the API description. |
| `$` | In the sample call with a video link, the string was the same URL that was sent in `url`. |

### Notes

- Send a user profile or homepage URL in `url` if you want a `sec_user_id`. The sample video URL `https://www.douyin.com/video/7691553968815623478` returned the input unchanged.
- For a video link, call [Douyin Video ID Extractor](/apis/douyin/web/aweme-id) to get the video ID.
- To process many profile links in one call, use [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/sec-user-id.json`](../../../../catalog/models/douyin/web/sec-user-id.json) · Store page: https://www.sandbase.ai/model/douyin/web/sec-user-id
