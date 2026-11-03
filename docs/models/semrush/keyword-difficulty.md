# Semrush Keyword Difficulty API: pricing, parameters and code examples

`semrush/keyword-difficulty` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.005 per call · **Modes:** sync

Keyword difficulty score (0-100) for a phrase in a regional Semrush database.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.005**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/keyword-difficulty", "phrase": "running shoes", "database": "us"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/keyword-difficulty', {'phrase': 'running shoes', 'database': 'us'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/keyword-difficulty", {
  "phrase": "running shoes",
  "database": "us"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/keyword-difficulty", sandbase.Params{
	"phrase": "running shoes",
	"database": "us",
})
```

Same call via the path form: `POST /v1/api/semrush/keyword-difficulty` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `phrase` | string | yes | Keyword to analyze, e.g. "running shoes".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Returns the Semrush keyword difficulty score for one phrase in one regional Semrush database. You send a `phrase` and a `database` code such as `us`. The response is a semicolon-separated text table with a header line and one data line.

### Use cases

- Check how hard it is to rank for a target keyword before you commission an article.
- Compare the difficulty of the same phrase in the `us`, `uk` and `de` databases to pick a market.
- Filter a keyword list by difficulty score to find lower-competition phrases.
- Add a difficulty column to a content planning sheet.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/keyword-difficulty" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"phrase": "running shoes", "database": "us"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | Yes | Regional Semrush database, e.g. "us", "uk", "de". |
| `phrase` | string | Yes | Keyword to analyze, e.g. "running shoes". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
"Keyword;Keyword Difficulty Index\r\nrunning shoes;76"
```

### Response fields

| Field | Meaning |
|---|---|
| `[0][0]` | Header of the first column. It labels the column that holds the phrase. |
| `[0][1]` | Header of the second column. It labels the column that holds the difficulty score. |
| `[1][0]` | The phrase you sent in the request, repeated in the data line. |
| `[1][1]` | The keyword difficulty score for the phrase. The API description gives the range as 0 to 100. The example response returns `76`. |

### Notes

- The response is plain text, not a JSON object, so it has no field names. The paths above use positions: the first index is the line (`0` is the header, `1` is the data) and the second index is the column.
- Lines are separated by `\r\n` and columns by `;`. To read the score, split the text on `\r\n`, take the second line, split it on `;`, and take the second value.
- Both `phrase` and `database` are required in the request schema, although the current README marks `database` as optional.
- For more keyword data such as related phrases, call [Semrush Keyword Overview](/apis/semrush/keyword-overview) or [Semrush Broad Match Keywords](/apis/semrush/broad-match-keywords).

### Pricing

Billed at the actual cost of each call, about $0.005 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/keyword-difficulty.json`](../../../catalog/models/semrush/keyword-difficulty.json) · Store page: https://www.sandbase.ai/model/semrush/keyword-difficulty
