# Semrush Domain vs Domain API: pricing, parameters and code examples

`semrush/domain-vs-domain` · data API · Semrush · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.16 per call · **Modes:** sync

Keyword gap between domains: shared and unique keywords with each domain's ranking position.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.16**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "semrush/domain-vs-domain", "database": "us", "domains": "*|or|nike.com|*|or|adidas.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('semrush/domain-vs-domain', {'database': 'us', 'domains': '*|or|nike.com|*|or|adidas.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("semrush/domain-vs-domain", {
  "database": "us",
  "domains": "*|or|nike.com|*|or|adidas.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "semrush/domain-vs-domain", sandbase.Params{
	"database": "us",
	"domains": "*|or|nike.com|*|or|adidas.com",
})
```

Same call via the path form: `POST /v1/api/semrush/domain-vs-domain` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domains` | string | yes | Domains to compare in Semrush syntax, e.g. "*\|or\|nike.com\|*\|or\|adidas.com".  |
| `database` | string | yes | Regional Semrush database, e.g. "us", "uk", "de".  |

## Details

Returns a keyword gap report for the domains you compare on a Semrush regional database. It needs a `database` code and a `domains` string in Semrush syntax. The response is semicolon-separated text with a header line and one line per keyword.

### Use cases

- Find keywords where a competitor ranks and your domain does not.
- Compare the ranking positions of two brands on the same keyword.
- Build a content plan from keywords that only one domain ranks for.
- Spot shared keywords where a rival ranks higher than you.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/semrush/domain-vs-domain" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"database": "us", "domains": "*|or|nike.com|*|or|adidas.com"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `database` | string | Yes | Regional Semrush database, e.g. "us", "uk", "de". |
| `domains` | string | Yes | Domains to compare in Semrush syntax, e.g. "*/or/nike.com/*/or/adidas.com". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
"Keyword;nike.com\r\nsoccer;31\r\nrunning;7\r\nrunning shoes;1\r\nbasketball shoes;1\r\nsoc…"
```

### Response fields

| Field | Meaning |
|---|---|
| `[0]` | The header line. It names each column, starting with `Keyword`, followed by one column per domain, such as `nike.com`. |
| `[]` | One line per keyword. Split the text on `\r\n` to get the lines. |
| `[][0]` | The search keyword for that line, such as `running shoes`. |
| `[][1]` | The ranking position of the domain named in the second header column. For example, `running shoes;1` means that domain ranks at position 1 for `running shoes`. |

### Notes

- The response is plain text, not JSON objects. Split it on `\r\n` for lines and on `;` for columns. The paths above refer to the lines and columns after that split.
- The `domains` value uses Semrush syntax. Each domain is written as `*|or|domain.com`, and the entries are joined with `|`. For example, `*|or|nike.com|*|or|adidas.com`.
- To see all keywords for one domain, call [Semrush Domain Organic Keywords](/apis/semrush/domain-organic-keywords). To find rival domains first, call [Semrush Organic Competitors](/apis/semrush/domain-organic-competitors).

### Pricing

Billed at the actual cost of each call, about $0.16 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/semrush/domain-vs-domain.json`](../../../catalog/models/semrush/domain-vs-domain.json) · Store page: https://www.sandbase.ai/model/semrush/domain-vs-domain
