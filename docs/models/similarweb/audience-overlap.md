# Similarweb Audience Overlap API: pricing, parameters and code examples

`similarweb/audience-overlap` · data API · Similarweb · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.15 per call · **Modes:** sync

Compare the audiences of up to 5 websites: unique visitors per site, overlapping visitors and the combined audience.

## Pricing

- Depends on parameters (`params.limit`).

Formula: `0.15 * Math.max(1.0, Math.min(5.0, (output.data?.data != nil ? len(output.data.data) : (params.limit ?? 20)) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "similarweb/audience-overlap", "domains": "cnn.com,bbc.com", "end_date": "2026-09", "start_date": "2026-09"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('similarweb/audience-overlap', {'domains': 'cnn.com,bbc.com', 'end_date': '2026-09', 'start_date': '2026-09'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("similarweb/audience-overlap", {
  "domains": "cnn.com,bbc.com",
  "end_date": "2026-09",
  "start_date": "2026-09"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "similarweb/audience-overlap", sandbase.Params{
	"domains": "cnn.com,bbc.com",
	"end_date": "2026-09",
	"start_date": "2026-09",
})
```

Same call via the path form: `POST /v1/api/similarweb/audience-overlap` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `country` | string |  | Worldwide data only; values are case-insensitive. one of: `ww`; default `"ww"` |
| `domains` | string | yes | domains  |
| `end_date` | string | yes | end_date  |
| `start_date` | string | yes | start_date  |
| `granularity` | string |  | granularity one of: `monthly`; default `"monthly"` |

## Details

Returns audience overlap numbers for up to 5 websites over a month range. You send a comma-separated list of `domains`, a `start_date` and an `end_date`. The response has one row per single site and one row per combination of sites.

### Use cases

- Measure how many visitors `cnn.com` and `bbc.com` share in a given month.
- Estimate the combined audience a media buyer reaches by advertising on two news sites.
- Find out how much of a competitor's audience is not reached by your own site.
- Check whether a partnership between two sites adds new readers or mostly repeats the same people.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/similarweb/audience-overlap" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_date": "2026-09", "end_date": "2026-09", "country": "ww", "domains": "cnn.com,bbc.com", "granularity": "monthly"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domains` | string | Yes | domains |
| `end_date` | string | Yes | end_date |
| `start_date` | string | Yes | start_date |
| `country` | string | No | Worldwide data only; values are case-insensitive. |
| `granularity` | string | No | granularity |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "domains": "cnn.com",
      "overlap_unique_visitors": 68245446.10000001,
      "union_unique_users": 68245446.10000001
    }
  ],
  "meta": {
    "last_updated": "2026-09-30",
    "request": {
      "country": "ww",
      "domains": "cnn.com,bbc.com",
      "end_date": "2026-09-30",
      "format": "json",
      "granularity": "monthly",
      "metrics": [
        "overlap"
      ],
      "start_date": "2026-09-01",
      "web_source": "total"
    },
    "status": "success"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].domains` | The site or sites the row describes. A single domain such as `cnn.com` is one site. A value like `bbc.com,cnn.com` is a combination of sites. |
| `data[].overlap_unique_visitors` | Unique visitors that fall in the overlap for this row. For a single-domain row it equals the union value. For a combination row it is the number of visitors shared by the sites. |
| `data[].union_unique_users` | Unique users in the combined audience for the row. For a combination row it is the total across the listed sites with shared visitors counted once. |
| `meta.last_updated` | Date the data was last updated, for example `2026-09-30`. |
| `meta.request.start_date / meta.request.end_date` | The full date range used for the query. Month inputs such as `2026-09` become the first and last day of the month. |
| `meta.request.metrics` | The metrics computed for the call. The values are `overlap` and `union`. |
| `meta.request.web_source` | The traffic source filter applied. The value is `total` in this response. |
| `meta.status` | Shows `success` when the call worked. |

### Notes

- Pass `domains` as one comma-separated string, for example `cnn.com,bbc.com`. The API accepts up to 5 domains.
- Use the `YYYY-MM` format for `start_date` and `end_date`. `country` accepts only `ww` and `granularity` accepts only `monthly`.
- Match rows by the `data[].domains` value. Combination rows list the domains in alphabetical order, as in `bbc.com,cnn.com`.
- To see who the visitors are, call [Similarweb Demographics](/apis/similarweb/demographics) or [Similarweb Audience Interest](/apis/similarweb/audience-interest).

### Pricing

Billed at the actual cost of each call, about $0.15 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/similarweb/audience-overlap.json`](../../../catalog/models/similarweb/audience-overlap.json) · Store page: https://www.sandbase.ai/model/similarweb/audience-overlap
