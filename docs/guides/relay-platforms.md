# Use SandBase from a gateway or relay platform

SandBase works as an upstream for gateways and relay platforms: new-api, one-api, LiteLLM, and any client that supports a custom OpenAI base URL. You need one SandBase key. The price files in [`exports/`](../../exports/) are regenerated daily from the catalog, so your configured prices stay in sync with SandBase list prices.

| Upstream setting | Value |
|---|---|
| Protocol | OpenAI-compatible (Chat Completions, Responses, Embeddings). Anthropic `/v1/messages` and Gemini `/v1beta/models/...` also work |
| Base URL | `https://api.sandbase.ai` (add `/v1` if your tool expects the full path) |
| Key | Your SandBase API key |
| Model list | `GET /v1/models`, or [`exports/openai-models.json`](../../exports/openai-models.json) |

## new-api / one-api

Tested with new-api on 2026-11-02. We added a channel, synced the ratios, and called streaming and non-streaming chat through it. The billed quota matched SandBase's per-token price.

1. **Add a channel.** Under **Channels → Add**, set:
   - **Type:** OpenAI
   - **Base URL:** `https://api.sandbase.ai`
   - **Key:** your SandBase key
   - **Models:** click *Fetch models*, or paste [`exports/new-api/models.txt`](../../exports/new-api/models.txt)
2. **Set prices.** Under **Settings → Ratio settings**, paste:
   - [`model_ratio.json`](../../exports/new-api/model_ratio.json) into *Model ratio*
   - [`completion_ratio.json`](../../exports/new-api/completion_ratio.json) into *Completion ratio*
   - [`cache_ratio.json`](../../exports/new-api/cache_ratio.json) into *Cache ratio*

   These ratios reproduce SandBase's list price. Ratio 1 equals $2 per 1M input tokens. Multiply by your group ratio to add your margin.
3. **Create a token** and call your relay as usual:
   ```bash
   curl https://your-relay.example.com/v1/chat/completions -H "Authorization: Bearer sk-..." \
     -d '{"model": "deepseek/deepseek-v4-flash", "messages": [{"role": "user", "content": "Hi"}]}'
   ```

To keep prices current, re-paste the three files after a SandBase price change. `git log -p exports/new-api/` shows what changed. You can also automate it through new-api's option API:
```bash
for k in ModelRatio:model_ratio CompletionRatio:completion_ratio CacheRatio:cache_ratio; do
  curl -s -X PUT https://your-relay.example.com/api/option/ -H "Authorization: Bearer $ADMIN_TOKEN" -H "New-Api-User: 1" \
    -H 'Content-Type: application/json' \
    -d "$(jq -n --arg k "${k%%:*}" --rawfile v <(curl -s https://raw.githubusercontent.com/sandbaseai/sandbase/main/exports/new-api/${k##*:}.json) '{key:$k,value:$v}')"
done
```

## LiteLLM

[`exports/litellm/config.yaml`](../../exports/litellm/config.yaml) lists every SandBase LLM with its price:

```bash
export SANDBASE_API_KEY=sk-... LITELLM_MASTER_KEY=sk-your-proxy-key
litellm --config exports/litellm/config.yaml
```

To get spend tracking without the proxy, register [`model_prices.json`](../../exports/litellm/model_prices.json) with `litellm.register_model(...)` and use model names prefixed with `sandbase/`.

Both were tested on 2026-11-02. The proxy served a chat completion, and `litellm.completion_cost` returned exactly SandBase's per-token price.

## Chat clients and frameworks

Cherry Studio, LobeChat, Open WebUI, Dify, Cline and other tools that accept an OpenAI-compatible provider need three settings:
- **Base URL:** `https://api.sandbase.ai/v1`
- **Key:** your SandBase key
- **Model name:** any `llm` name from the catalog

Tools that read the OpenRouter model format can use [`exports/openrouter-models.json`](../../exports/openrouter-models.json). It has per-token USD prices and context lengths.

## Image, video, audio and data APIs

Relay platforms usually only proxy the OpenAI chat format. Every other SandBase capability uses one endpoint, `POST /v1/run`, documented per model in [`docs/models/`](../models/). To resell these capabilities, forward `/v1/run` and `/v1/run/{id}` as a generic HTTP passthrough. Use [`exports/pricing.csv`](../../exports/pricing.csv) for prices: it has a per-call price, a token price, or a from–to range for each capability.

## Notes

- Capabilities with `"status": "coming_soon"` in the catalog are listed but not callable yet. They are left out of the export files.
- Prices are SandBase list prices in USD. Your account discounts apply to what SandBase bills you, not to these files.
