# WeChat MP Related Articles API: pricing, parameters and code examples

`wechat-mp/v2/related-articles` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Retrieves the list of related articles displayed at the bottom of a WeChat MP post using its link. Supports choosing between raw and simplified response formats.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/v2/related-articles", "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/v2/related-articles', {'url': 'https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/v2/related-articles", {
  "url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/v2/related-articles", sandbase.Params{
	"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/v2/related-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `raw` | boolean |  | Optional, default True. True=full raw response; False=simplified projection. default `true` |
| `url` | string | yes | WeChat MP article URL (long or short form). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw` (this article has related articles disabled, returns empty)  |

## Details

This API returns the list of related articles shown at the bottom of a WeChat MP post. It needs the article link in `url`. You can set `raw` to `false` to get a simplified response instead of the full raw one.

### Use cases

- Collect the related article links of a given WeChat MP post to map how content links together.
- Check whether a post has related articles enabled by testing if `list` is empty.
- Compare the recommendations shown under different posts from the same official account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/v2/related-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | WeChat MP article URL (long or short form). E.g. `https://mp.weixin.qq.com/s/TSNQKkRpN1qbKsT7BvzqIw` (this article has related articles disabled, returns empty) |
| `raw` | boolean | No | Optional, default True. True=full raw response; False=simplified projection. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "article_size": 0,
  "base_resp": {
    "exportkey_token": "",
    "ret": 0
  },
  "debug_id": "c8654bd8",
  "debug_info": "gAAAAABq6ZE_RcOuigyjp77fpRWqW98EwuA1qKR3MgBMlFp6rtnMIC_7FSFL5Iyfq00msdIWVO3nW6Bo…",
  "empty_scene": 8,
  "list": [],
  "report_info": "{}",
  "show_rec_reason": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `list` | The related articles shown under the post. It is an empty array when the post shows none, as in this example. |
| `article_size` | Number of related articles returned. It is `0` when `list` is empty. |
| `empty_scene` | A numeric code that comes with an empty result. The example shows `8`. The response does not explain what each value means. |
| `show_rec_reason` | A flag that shows whether recommendation reasons are displayed. The example value is `1`. |
| `base_resp.ret` | Status code of the call inside the response. `0` in the example. |
| `base_resp.exportkey_token` | Token string in the response. It is empty in the example. |
| `debug_id / debug_info` | Identifiers for debugging. They do not describe the article content. |
| `report_info` | A JSON string with reporting data. It is `{}` in the example. |

### Notes

- Use a link on `mp.weixin.qq.com/s`, in long or short form. The link must start with `http://` or `https://`.
- `raw` defaults to `true`. Set it to `false` for a simplified projection.
- The example article has related articles disabled, so `list` is empty and `article_size` is `0`.
- To get the article body for a link, call [WeChat MP Article Detail](/apis/wechat-mp/v2/article-detail).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [WeChat MP Account Articles](/apis/wechat-mp/v2/account-articles): Get the published articles of a WeChat official account by its gh_ username: titles, links, covers and post dates, one page at a time, including video and audi…
- [WeChat MP Account Profile](/apis/wechat-mp/v2/account-profile): Retrieves the profile details of an official WeChat account, including name, avatar, signature, and verification entity type using its official account ID.
- [WeChat MP Article Ads](/apis/wechat-mp/v2/article-ad): Returns embedded ad slot information for a specified WeChat MP article URL.

---
Machine-readable: [`catalog/models/wechat-mp/v2/related-articles.json`](../../../../catalog/models/wechat-mp/v2/related-articles.json) · Store page: https://www.sandbase.ai/model/wechat-mp/v2/related-articles
