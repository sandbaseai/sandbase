# Xiaohongshu PGY related keywords API: pricing, parameters and code examples

`xiaohongshu/pgy/keyword-related` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

PGY related keywords on Xiaohongshu. Returns the platform data as structured JSON.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/keyword-related", "search_word": "面膜"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/keyword-related', {'search_word': '面膜'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/keyword-related", {
  "search_word": "面膜"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/keyword-related", sandbase.Params{
	"search_word": "面膜",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/keyword-related` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `search_word` | string | yes | Keyword  |

## Details

Returns related search keywords for a Xiaohongshu keyword, taken from the PGY (Pugongying) creator marketplace. It needs one input, `search_word`, and returns two lists: terms that lead into the keyword and terms that follow it.

### Use cases

- Find long-tail search terms around a product keyword such as `面膜` to plan note titles and tags.
- Compare note volume and total reads across related terms to see which topics have the most content.
- Spot brand-related terms by checking `brandTag` on each related keyword.
- Build a keyword expansion list before pulling trend data for each term.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/keyword-related" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_word": "面膜"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_word` | string | Yes | Keyword |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "downSearchWords": [
      {
        "brandTag": 0,
        "noteNum": 93424,
        "readTotalCount": 534895518,
        "relevanceRank": 1,
        "searchScore": 2434694.0,
        "searchWord": "面膜推荐"
      }
    ],
    "upSearchWords": [
      {
        "brandTag": 0,
        "noteNum": 118837,
        "readTotalCount": 389528705,
        "relevanceRank": 1,
        "searchScore": 2537304.0,
        "searchWord": "洗面奶"
      }
    ]
  },
  "guid": null,
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.downSearchWords[].searchWord` | A related keyword in the `downSearchWords` list. In the example these are longer terms that extend `面膜`, such as `面膜推荐` and `面膜补水`. |
| `data.upSearchWords[].searchWord` | A related keyword in the `upSearchWords` list. In the example these are broader or neighboring terms such as `洗面奶`, `护肤` and `身体乳`. |
| `data.downSearchWords[].relevanceRank / data.upSearchWords[].relevanceRank` | Rank of the related keyword within its list. `1` is the first item. |
| `data.downSearchWords[].noteNum / data.upSearchWords[].noteNum` | Number of notes tied to the related keyword. |
| `data.downSearchWords[].readTotalCount / data.upSearchWords[].readTotalCount` | Total read count for the related keyword. |
| `data.downSearchWords[].searchScore / data.upSearchWords[].searchScore` | Search score for the related keyword. Higher values mean a higher score. The scale is not documented. |
| `data.downSearchWords[].brandTag / data.upSearchWords[].brandTag` | Brand flag for the keyword. All sample rows show `0`. The meaning of other values is not shown. |
| `success / msg / code` | Call status. The sample shows `success` as `true`, `code` as `0` and `msg` as `成功`. |

### Notes

- Pass the keyword in `search_word`. The API takes no pagination parameters.
- The result is returned in `outputs[0].data`, and the fields above sit under its `data` object.
- To see how a related term performs over time, send it to [Xiaohongshu PGY keyword daily trend](/apis/xiaohongshu/pgy/keyword-daily).
- For a summary of one keyword, call [Xiaohongshu PGY keyword overview](/apis/xiaohongshu/pgy/keyword-stat).

### Pricing

$0.02 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/keyword-related.json`](../../../../catalog/models/xiaohongshu/pgy/keyword-related.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/keyword-related
