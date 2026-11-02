# Stepfun models API: 1 endpoints with pricing and code examples

Call 1 Stepfun models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`stepfun/step-5-preview`](../models/stepfun/step-5-preview.md) | Step 5 Preview is StepFun's flagship model for agentic work, built on a sparse Mixture-of-Experts architecture with 27B active and 600B… | $1 input / $2.7 output per 1M tokens |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stepfun/step-5-preview"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
