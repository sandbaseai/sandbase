# Douyin URL Shortener API: pricing, parameters and code examples

`douyin/web/shorten-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Shortens a target web address for Douyin web workflows. Accepts a full destination link and returns a compact shortened URL.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/shorten-url", "target_url": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/shorten-url', {'target_url': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/shorten-url", {
  "target_url": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/shorten-url", sandbase.Params{
	"target_url": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/web/shorten-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `target_url` | string | yes | Target URL to be converted  |

## Details

Takes one full Douyin web address in `target_url` and returns a short `https://v.douyin.com/` link for it. The response holds the short link as a single string in `data`.

### Use cases

- Turn a long Douyin video page link into a short link for chat messages or posts.
- Store short links in a database or spreadsheet instead of long video URLs.
- Build share links for Douyin videos inside an app with limited screen space.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/shorten-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"target_url": "https://www.douyin.com/video/7575136499386720761"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `target_url` | string | Yes | Target URL to be converted |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": "https://v.douyin.com/nzl1K-jOpdo/",
  "message": "success",
  "now": 1793691150
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data` | The shortened URL for the submitted `target_url`. In this example it is `https://v.douyin.com/nzl1K-jOpdo/`. |
| `code` | Status code of the call. `0` appears with a successful result. |
| `message` | Short status text. It reads `success` when the call works. |
| `now` | Number in the response, `1793691150` in this example. It looks like a Unix timestamp in seconds. |

### Notes

- Send the full link in `target_url`, including `https://`, for example a video page like `https://www.douyin.com/video/7575136499386720761`.
- The short link is a plain string in `data`, not an object.
- To get IDs out of Douyin links, use [Douyin Video ID Extractor](/apis/douyin/web/aweme-id) or [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/shorten-url.json`](../../../../catalog/models/douyin/web/shorten-url.json) · Store page: https://www.sandbase.ai/model/douyin/web/shorten-url
