# Pipixia Search API: pricing, parameters and code examples

`pipixia/app/search` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Pipixia (ByteDance humor community) by keyword across posts, videos, images, users and hashtags.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/search", "keyword": "OpenAI", "offset": "0", "search_type": "1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/search', {'keyword': 'OpenAI', 'offset': '0', 'search_type': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/search", {
  "keyword": "OpenAI",
  "offset": "0",
  "search_type": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/search", sandbase.Params{
	"keyword": "OpenAI",
	"offset": "0",
	"search_type": "1",
})
```

Same call via the path form: `POST /v1/api/pipixia/app/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | string |  | Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. default `"0"` |
| `keyword` | string | yes | Search keyword.  |
| `search_type` | string |  | Search type, available values are as follows: 1: Comprehensive; 8: Hot; 9: Fresh; 2: Video; 3: Photo; 4: User; 5: Hashtag default `"1"` |

## Details

Search Pipixia for a keyword. Choose the result type with `search_type` and paginate with `offset`.

### Use cases

- Research trending humor and meme content.
- Find creators in the Pipixia community.
- Monitor brand mentions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "猫"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `offset` | string | No | Page cursor, default is 0, get the corresponding value from the `offset` Key in the previous page. |
| `search_type` | string | No | Search type, available values are as follows: 1: Comprehensive; 8: Hot; 9: Fresh; 2: Video; 3: Photo; 4: User; 5: Hasht… |

### Notes

- `search_type`: 1 comprehensive, 8 hot, 9 fresh, 2 video, 3 photo, 4 user.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Pipixia Hot Search](/model/pipixia/app/hot-search-board-list): Get the Pipixia hot search boards: trending posts with daily likes and top comments.
- [Get hashtag detail](/model/pipixia/app/hashtag-detail): Get hashtag detail data.
- [Get hashtag post list](/model/pipixia/app/hashtag-post-list): Get hashtag post list data.

---
Machine-readable: [`catalog/models/pipixia/app/search.json`](../../../../catalog/models/pipixia/app/search.json) · Store page: https://www.sandbase.ai/model/pipixia/app/search
