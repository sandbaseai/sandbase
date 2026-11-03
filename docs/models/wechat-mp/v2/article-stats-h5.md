# WeChat MP Article Stats (H5) API: pricing, parameters and code examples

`wechat-mp/v2/article-stats-h5` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get WeChat MP Article Stats (H5) on WeChat MP. Returns the platform data as structured JSON.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/article-stats-h5", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/article-stats-h5', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/article-stats-h5", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/article-stats-h5", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/article-stats-h5` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | True=raw response; False=simplified parsed structure default `true` |
| `url` | string | yes | /mp.weixin.qq.com/s/WeChat MP article URL (https://mp.weixin.qq.com/s/… or long URL with __biz)  |
| `comment_id` | string |  | Article comment id (optional, performance shortcut): when omitted, the API must fetch and parse the whole article HTML to obtain it, which accounts for about half of this endpoint's latency  |

## Details

Returns comment counts and engagement stats for one WeChat official account article. It needs the article `url`, either the short `https://mp.weixin.qq.com/s/…` form or the long form with `__biz`.

### Use cases

- Track how many comments a WeChat article has gathered, and how many were selected for display.
- Get the `comment_id` of an article so you can pass it to a comments API.
- Check which engagement counts WeChat exposes for an article before building a report on it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/article-stats-h5" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw", "raw": true}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | /mp.weixin.qq.com/s/WeChat MP article URL (https://mp.weixin.qq.com/s/… or long URL with __biz) |
| `comment_id` | string | No | Article comment id (optional, performance shortcut): when omitted, the API must fetch and parse the whole article HTML to obtain it, which accounts for about half of this endpoint's latency |
| `raw` | boolean | No | True=raw response; False=simplified parsed structure |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_via": "h5",
  "collect_count": null,
  "comment_count": 26,
  "comment_raw": {
    "appmsgid": "2247780992",
    "comment_id": "3884868893382230017",
    "elected_total": 21,
    "total_count": 26
  },
  "debug_id": "d81634db",
  "debug_info": "gAAAAABq6ZFAaqjYyv3jGWwq26w9Lb0pPyWUxjSpT707gLkGDCq1qMDl2WvffZiKB-HLCwI2aawhofkY…",
  "elected_comment_count": 21,
  "like_count": null,
  "old_like_count": null,
  "read_num": null,
  "share_count": null,
  "star_num": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comment_count` | Total number of comments on the article. It matches `comment_raw.total_count`. |
| `elected_comment_count / comment_raw.elected_total` | Number of comments that were selected for display on the article. |
| `comment_raw.comment_id` | ID of the article's comment thread. Pass it as `comment_id` on later calls. |
| `comment_raw.appmsgid` | ID of the article message, returned as a string. |
| `read_num / like_count / old_like_count` | Read and like counts. In this response they are `null` and listed in `unavailable`. |
| `collect_count / share_count / star_num` | Other engagement counts. In this response they are `null`, so no value was returned for them. |
| `unavailable` | List of stat fields that could not be filled for this article. |
| `_via` | Shows which route returned the data. Here it is `h5`. |

### Notes

- Pass `comment_id` from `comment_raw.comment_id` on later calls for the same article. This skips fetching the article page and shortens the response time.
- Set `raw` to `false` to get a simplified parsed structure instead of the raw response.
- Check `unavailable` before using a count. Fields listed there are `null`.
- To read the comments themselves, call [WeChat MP Article Comments](/apis/wechat-mp/v2/article-comments).

### Pricing

$0.01 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/wechat-mp/v2/article-stats-h5.json`](../../../../catalog/models/wechat-mp/v2/article-stats-h5.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/article-stats-h5
