# Semrush Question Keywords API: pricing, parameters and code examples

`semrush/question-keywords` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.08 per call · **Modes:** sync

Question-form keyword ideas for a seed phrase, with search volume, CPC and competition.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.08**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/question-keywords", "phrase": "running shoes", "database": "us"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/question-keywords', {'phrase': 'running shoes', 'database': 'us'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/question-keywords", {
  "phrase": "running shoes",
  "database": "us"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/question-keywords", sandbase.Params{
	"phrase": "running shoes",
	"database": "us",
})
```

Same call via the path form: `POST /v1/api/semrush/question-keywords` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `phrase` | string | yes | Keyword to analyze, e.g. "running shoes".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Returns question-form keyword ideas for a seed phrase, such as `how to choose running shoes`. Each row has the search volume and the CPC. You send a `phrase` and a regional `database`.

### Use cases

- Find the questions people ask about a topic to plan FAQ sections and blog posts.
- Sort the rows by search volume to pick the best article titles for a topic.
- Compare CPC across questions to spot ones that advertisers value.
- Run the same `phrase` against `us`, `uk` and `de` to compare question demand by country.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/question-keywords" \
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
"Keyword;Search Volume;CPC\r\nhow to choose running shoes;110000;0.43\r\nhow long do …"
```

### Response fields

| Field | Meaning |
|---|---|
| `[0]` | Column 1 of each row, with the header `Keyword`. It holds the question-form keyword, for example `how long do running shoes last`. |
| `[1]` | Column 2 of each row, with the header `Search Volume`. It holds the search volume for the keyword in the chosen database. For example, `how to choose running shoes` shows `110000`. |
| `[2]` | Column 3 of each row, with the header `CPC`. It holds the cost per click as a decimal number such as `0.43`. The response does not show the currency. |

### Notes

- The response is one text table, not JSON objects. The first line is the header `Keyword;Search Volume;CPC`, and lines are separated by `\r\n`.
- Split each line on `;` to get the columns. In the field list, `[0]`, `[1]` and `[2]` mean the first, second and third column of a line.
- The description mentions competition, but the sample response only shows the `Keyword`, `Search Volume` and `CPC` columns.
- To check how hard a question is to rank for, pass it to [Semrush Keyword Difficulty](/apis/semrush/keyword-difficulty). For more detail on one keyword, use [Semrush Keyword Overview](/apis/semrush/keyword-overview).

### Pricing

Billed at the actual cost of each call, about $0.08 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/question-keywords.json`](../../../catalog/models/semrush/question-keywords.json) · Store page: https://www.sandbase.ai/model/semrush/question-keywords
