# Vela Breakout Breakouts API: pricing, parameters and code examples

`velabreakout/breakouts` · data API · Vela Breakout · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** async

Rank the fastest-growing AI apps, models, dev tools, software or companies in one group.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "velabreakout/breakouts", "group": "ai_apps"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('velabreakout/breakouts', {'group': 'ai_apps'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("velabreakout/breakouts", {
  "group": "ai_apps"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "velabreakout/breakouts", sandbase.Params{
	"group": "ai_apps",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/velabreakout/breakouts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `group` | string | yes | Which group to rank (ids from /groups): ai_apps (AI tokens an app uses), ai_models (tokens a model serves a week), ai_labs (each lab's share of all AI tokens), ai_work (open jobs paying experts to train and test AI… one of: `ai_apps`, `ai_models`, `ai_labs`, `ai_work`, `open_models`, `editor_extensions`, `open_editor_extensions`, `workplace_add_ons`, `browser_extensions`, `agent_skills`, `agent_tools`, `company_packages` … |
| `limit` | integer |  | How many rows to return, 1-25. The price is the same for any limit. range 1–25 |
| `steady` | boolean |  | When true, keep only items that are also up over a longer window — use it for 'steadily', 'sustained' or 'starting to' questions, to drop one-off spikes. A group with no longer window answers an empty ranking.  |
| `min_size` | string |  | Size floor: only items at least as big as the group's median (the default), its 75th percentile, or none. A floor keeps tiny starts from dominating the ranking. one of: `median`, `p75`, `none` |
| `window_days` | number |  | Growth window in days: 7, 30, 90 or 365. Omit to use the group's default (usually `usual_window_days` from /groups); the answer's `window` states the one used. one of: `7`, `30`, `90`, `365` |

## Details

Rank the fastest-growing AI apps, models, dev tools, software or companies in one group.

---
Machine-readable: [`catalog/models/velabreakout/breakouts.json`](../../../catalog/models/velabreakout/breakouts.json) · Store page: https://www.sandbase.ai/model/velabreakout/breakouts
