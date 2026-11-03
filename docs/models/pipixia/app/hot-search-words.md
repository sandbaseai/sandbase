# Pipixia Hot Search Words API: pricing, parameters and code examples

`pipixia/app/hot-search-words` · data API · Pipixia · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the current list of trending search keywords from Pipixia. Helps track popular search topics and user query trends across the platform without requiring input parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "pipixia/app/hot-search-words"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('pipixia/app/hot-search-words', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("pipixia/app/hot-search-words", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "pipixia/app/hot-search-words", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/pipixia/app/hot-search-words` with the body above minus `model`.

## Details

Returns the current list of suggested hot search keywords from the Pipixia app. It needs no input: send an empty JSON object `{}`.

### Use cases

- Show the current Pipixia hot search terms on a trend dashboard.
- Log the keyword list over time to see which topics enter and leave the list.
- Seed a content search with the current hot keywords using the Pipixia search API.
- Pre-fill a search box with keywords that Pipixia itself suggests.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/pipixia/app/hot-search-words" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "hot_keywords": [
      "搞笑视频"
    ],
    "tip": "",
    "words": [
      {
        "hot_logo_image": null,
        "hot_type": 0,
        "schema": "",
        "tip": "搞笑视频",
        "write_history": true
      }
    ]
  },
  "message": "success",
  "prompt": "",
  "status_code": 0,
  "time": 1793691709812
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.hot_keywords[]` | Plain list of the hot search keywords as strings, in the order returned. |
| `data.words[]` | One object per hot keyword, with extra display and behavior settings for that keyword. |
| `data.words[].tip` | The keyword text. It matches the entry in `data.hot_keywords[]`. |
| `data.words[].hot_type` | Numeric type code for the keyword. All items in this sample have the value `0`. |
| `data.words[].hot_logo_image` | Logo image attached to the keyword. It is `null` in this sample, so no logo is set. |
| `data.words[].schema` | Link or schema string for the keyword. It is an empty string in this sample. |
| `data.words[].write_history` | Boolean flag. It is `true` in this sample. The key name suggests it controls whether the term is saved to the user's search history. |
| `data.tip` | Top-level tip text. It is an empty string in this sample. |
| `status_code / message` | `status_code` is `0` and `message` is `success` when the call works. |
| `time` | Timestamp of the response, shown as a 13-digit number (milliseconds). |

### Notes

- The request schema has no parameters, so always send `{}`.
- Keyword text is in Chinese in the sample response.
- To search posts for a keyword, pass it to [Pipixia Search](/apis/pipixia/app/search).
- For ranked hot topic boards, see [Pipixia Hot Search](/apis/pipixia/app/hot-search-board-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Pipixia Hashtag Details](/apis/pipixia/app/hashtag-detail): Retrieves metadata and profile assets for a specific Pipixia hashtag by its unique identifier.
- [Pipixia Hashtag Post List](/apis/pipixia/app/hashtag-post-list): Returns a list of posts associated with a specific hashtag on Pipixia.
- [Pipixia App Home Feed](/apis/pipixia/app/home-feed): Returns recommended posts from the Pipixia home feed.

---
Machine-readable: [`catalog/models/pipixia/app/hot-search-words.json`](../../../../catalog/models/pipixia/app/hot-search-words.json) · Store page: https://www.sandbase.ai/model/pipixia/app/hot-search-words
