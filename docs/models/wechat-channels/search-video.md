# WeChat Channels Video Search

`wechat-channels/search-video` · api · WeChat Channels

Search WeChat Channels videos by keyword with publish-time, sort, page, offset, and continuation-state controls. Use it to find recent or ordered video results and continue web-search pages.

## Pricing

- **$0.111111 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "wechat-channels/search-video", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('wechat-channels/search-video', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("wechat-channels/search-video", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "wechat-channels/search-video", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/wechat-channels/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Search result offset returned by the previous WeChat Channels search response. Use 0 for the first page. default `0` |
| `keyword` | string | yes | Search keyword for WeChat Channels video results.  |
| `sortType` | string |  | Sort order for WeChat Channels video search results. one of: `COMPREHENSIVE`, `LATEST`, `HOT`; default `"COMPREHENSIVE"` |
| `currentPage` | integer |  | Current page number starting from 1 for WeChat Channels web search pagination. default `1` |
| `publishTimeType` | string |  | Publish time filter for WeChat Channels video web search. one of: `ALL`, `ONE_DAY`, `SEVEN_DAYS`, `HALF_YEAR`; default `"ALL"` |

## Details

Search WeChat Channels videos by keyword with publish-time, sort, page, offset, and continuation-state controls. Use it to find recent or ordered video results and continue web-search pages.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/wechat-channels/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword for WeChat Channels video results. |
| `publishTimeType` | string | No | Publish time filter for WeChat Channels video web search. |
| `sortType` | string | No | Sort order for WeChat Channels video search results. |
| `currentPage` | integer | No | Current page number starting from 1 for WeChat Channels web search pagination. |
| `offset` | integer | No | Search result offset returned by the previous WeChat Channels search response. Use 0 for the first page. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/wechat-channels/search-video.json`](../../../catalog/models/wechat-channels/search-video.json) · Store page: https://www.sandbase.ai/model/wechat-channels/search-video
