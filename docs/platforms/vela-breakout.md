# Vela Breakout API: 5 endpoints with pricing and code examples

Call 5 Vela Breakout endpoints through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`velabreakout/breakouts`](../models/velabreakout/breakouts.md) | Rank the fastest-growing AI apps, models, dev tools, software or companies in one group. | $0.02 per call |
| [`velabreakout/company`](../models/velabreakout/company.md) | Get every measured growth signal for one company by name or web domain. | $0.01 per call |
| [`velabreakout/groups`](../models/velabreakout/groups.md) | List the groups growth can be ranked in, with each one's measure, unit and caveat. | from $0 per run, depending on parameters |
| [`velabreakout/ideas`](../models/velabreakout/ideas.md) | List AI research ideas gaining or losing share of new papers, with who publishes on each. | $0.02 per call |
| [`velabreakout/rising-companies`](../models/velabreakout/rising-companies.md) | List companies growing faster than 90% of peers on two or more measures at once. | $0.02 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "velabreakout/breakouts", "group": "ai_apps"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
