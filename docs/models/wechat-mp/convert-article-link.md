# WeChat MP Article Link Conversion API: pricing, parameters and code examples

`wechat-mp/convert-article-link` · data API · WeChat MP · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Expands a WeChat Official Account article link to its resolved long-form destination. Use it to normalize a short or intermediate link before article lookup or collection.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-mp/convert-article-link", "link": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-mp/convert-article-link', {'link': 'http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-mp/convert-article-link", {
  "link": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-mp/convert-article-link", sandbase.Params{
	"link": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd",
})
```

Same call via the path form: `POST /v1/api/wechat-mp/convert-article-link` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `link` | string | yes | WeChat Official Account article short link or intermediate link to convert.  |

## Details

This API takes a WeChat Official Account article link and returns two normalized URLs for the same article. It needs one input, `link`, which can be a short link or an intermediate link.

### Use cases

- Normalize article links collected from chats or shares into one standard form before storing them.
- Remove duplicate articles by comparing the returned `long_url` values.
- Turn a long article link into a short `mp.weixin.qq.com/s/...` link for sharing or display.
- Prepare a clean link before passing it to an article lookup API.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-mp/convert-article-link" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"link": "http://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f78d7358bc2dfe90cde700e21d55&chksm=bc881cb3f28a27f35e0711803b28d8110305cfc1b8beb651674e1aa7870ddf963c658f4dc19a&scene=7#rd"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `link` | string | Yes | WeChat Official Account article short link or intermediate link to convert. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "long_url": "https://mp.weixin.qq.com/s?__biz=MjM5NzI3NDg4MA==&mid=2659064933&idx=1&sn=c536f7…",
  "short_url": "https://mp.weixin.qq.com/s/THnBSh_vaxhLeYa2lp3d1g"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `long_url` | The article link in long form. It carries the `__biz`, `mid`, `idx` and `sn` query parameters that identify the account and the article. |
| `short_url` | The short form of the article link, in the format `https://mp.weixin.qq.com/s/<code>`. |

### Notes

- Send the link in the `link` field. The example input is an intermediate link that includes extra parameters such as `chksm` and `scene`.
- In the sample response, `long_url` drops the `chksm` and `scene` parameters from the input link and keeps `__biz`, `mid`, `idx` and `sn`.
- To read the article itself, pass the returned link to [WeChat MP Article Detail](/apis/wechat-mp/article-detail) or [WeChat MP Article Detail (H5, Recommended)](/apis/wechat-mp/v2/article-detail-h5).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/wechat-mp/convert-article-link.json`](../../../catalog/models/wechat-mp/convert-article-link.json) · Store page: https://www.sandbase.ai/model/wechat-mp/convert-article-link
