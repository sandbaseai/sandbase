# Lemon8 Topic Post List API: pricing, parameters and code examples

`lemon8/app/topic-post-list` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts under a specific topic or hashtag on Lemon8. Requires the topic category ID, category parameter, and hashtag name.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/topic-post-list", "category": "590", "category_parameter": "7174447913778593798", "hashtag_name": "lemon8christmas"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/topic-post-list', {'category': '590', 'category_parameter': '7174447913778593798', 'hashtag_name': 'lemon8christmas'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/topic-post-list", {
  "category": "590",
  "category_parameter": "7174447913778593798",
  "hashtag_name": "lemon8christmas"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/topic-post-list", sandbase.Params{
	"category": "590",
	"category_parameter": "7174447913778593798",
	"hashtag_name": "lemon8christmas",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/topic-post-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `category` | string | yes | Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`  |
| `sort_type` | string |  | Sort type, 0 for default sort, currently only support default sort, please do not pass other values.  |
| `hashtag_name` | string | yes | Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info`  |
| `max_behot_time` | string |  | Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the max_behot_time returned by the last request is used for subsequent requests.  |
| `category_parameter` | string | yes | Category parameter ID, can be obtained from the interface `/lemon8/app/fetch_topic_info`  |

## Details

Retrieve a list of posts under a Lemon8 topic using `category`, `hashtag_name`, and `category_parameter`. Supports cursor pagination via `max_behot_time`.

### Use cases

- Monitor community posts associated with a specific Lemon8 hashtag.
- Extract topically relevant posts for content discovery and trend tracking.
- Gather user posts across designated Lemon8 categories for analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/topic-post-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category": "590", "category_parameter": "7174447913778593798", "hashtag_name": "lemon8christmas"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | Topic category ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` |
| `hashtag_name` | string | Yes | Hashtag name, can be obtained from the interface `/lemon8/app/fetch_topic_info` |
| `category_parameter` | string | Yes | Category parameter ID, can be obtained from the interface `/lemon8/app/fetch_topic_info` |
| `sort_type` | string | No | Sort type, 0 for default sort, currently only support default sort, please do not pass other values. |
| `max_behot_time` | string | No | Pagination parameter, can be obtained from the return result of the last request. |

### Notes

- Obtain `category`, `category_parameter`, and `hashtag_name` from the `/lemon8/app/fetch_topic_info` endpoint.
- Pagination uses `max_behot_time` returned from the previous request; leave it empty on the first call.
- Set `sort_type` to 0 for default sorting, as other values are currently unsupported.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Lemon8 Discover Page Banners](/apis/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/apis/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/topic-post-list.json`](../../../../catalog/models/lemon8/app/topic-post-list.json) · Store page: https://www.sandbase.ai/model/lemon8/app/topic-post-list
