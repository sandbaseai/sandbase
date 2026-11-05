# OpenAI models API: 51 endpoints with pricing and code examples

Call 51 OpenAI models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`openai/gpt-4.1`](../models/openai/gpt-4.1.md) | GPT-4.1 is OpenAI's flagship non-reasoning model in the GPT-4.1 series, released in April 2025 alongside GPT-4.1 mini and nano, with text… | $2 input / $8 output per 1M tokens |
| [`openai/gpt-4.1-mini`](../models/openai/gpt-4.1-mini.md) | GPT-4.1 mini is the smaller, faster tier of OpenAI's GPT-4.1 series, released in April 2025 as a non-reasoning model that accepts text and… | $0.4 input / $1.6 output per 1M tokens |
| [`openai/gpt-4.1-nano`](../models/openai/gpt-4.1-nano.md) | GPT-4.1 nano is the fastest and smallest tier of OpenAI's GPT-4.1 series, released in April 2025 as a non-reasoning model with text and… | $0.1 input / $0.4 output per 1M tokens |
| [`openai/gpt-4o`](../models/openai/gpt-4o.md) | GPT-4o ("o" for "omni") is OpenAI's versatile, high-intelligence GPT model released in May 2024, accepting text and image input and… | $2.5 input / $10 output per 1M tokens |
| [`openai/gpt-4o-2024-05-13`](../models/openai/gpt-4o-2024-05-13.md) | This is the pinned May 13, 2024 snapshot of OpenAI's GPT-4o, the original API release of the model, with text and image input and text… | $5 input / $15 output per 1M tokens |
| [`openai/gpt-4o-2024-08-06`](../models/openai/gpt-4o-2024-08-06.md) | This is the pinned August 6, 2024 snapshot of OpenAI's GPT-4o, accepting text and image input and producing text output. It was the first… | $2.5 input / $10 output per 1M tokens |
| [`openai/gpt-4o-2024-11-20`](../models/openai/gpt-4o-2024-11-20.md) | This is the pinned November 20, 2024 snapshot of OpenAI's GPT-4o, with text and image input and text output, plus Structured Outputs and… | $2.5 input / $10 output per 1M tokens |
| [`openai/gpt-4o-mini`](../models/openai/gpt-4o-mini.md) | GPT-4o mini is OpenAI's small, fast model from the GPT-4o family, released in July 2024 with text and image input and text output,… | $0.15 input / $0.6 output per 1M tokens |
| [`openai/gpt-5`](../models/openai/gpt-5.md) | GPT-5 is OpenAI's reasoning model released in August 2025 for coding, reasoning and agentic tasks across domains, accepting text and image… | $1.25 input / $10 output per 1M tokens |
| [`openai/gpt-5-mini`](../models/openai/gpt-5-mini.md) | GPT-5 mini is the faster, more efficient tier of OpenAI's GPT-5 reasoning family, released in August 2025 with text and image input and… | $0.25 input / $2 output per 1M tokens |
| [`openai/gpt-5.1`](../models/openai/gpt-5.1.md) | GPT-5.1 is OpenAI's GPT-5 series flagship released in November 2025 for coding and agentic tasks, with text and image input and text… | $1.25 input / $10 output per 1M tokens |
| [`openai/gpt-5.1-codex`](../models/openai/gpt-5.1-codex.md) | GPT-5.1-Codex is a version of OpenAI's GPT-5.1 optimized for agentic coding in Codex and similar environments, released in November 2025… | $1.25 input / $10 output per 1M tokens |
| [`openai/gpt-5.2`](../models/openai/gpt-5.2.md) | GPT-5.2 is OpenAI's GPT-5 series flagship released in December 2025, positioned by OpenAI for complex professional work and long-running… | $1.75 input / $14 output per 1M tokens |
| [`openai/gpt-5.3-codex`](../models/openai/gpt-5.3-codex.md) | GPT-5.3-Codex is OpenAI's agentic coding model announced in February 2026, optimized for Codex and similar environments, with text and… | $1.75 input / $14 output per 1M tokens |
| [`openai/gpt-5.4`](../models/openai/gpt-5.4.md) | GPT-5.4 is OpenAI's flagship GPT-5.4 reasoning model for complex professional work, released in March 2026 with text and image input, text… | $2.5 input / $15 output per 1M tokens |
| [`openai/gpt-5.4-mini`](../models/openai/gpt-5.4-mini.md) | GPT-5.4 mini is the smaller, faster tier of OpenAI's GPT-5.4 family, released in March 2026 with text and image input and text output.… | $0.75 input / $4.5 output per 1M tokens |
| [`openai/gpt-5.4-nano`](../models/openai/gpt-5.4-nano.md) | GPT-5.4 nano is the smallest and fastest tier of OpenAI's GPT-5.4 family, released in March 2026 with text and image input and text… | $0.2 input / $1.25 output per 1M tokens |
| [`openai/gpt-5.5`](../models/openai/gpt-5.5.md) | GPT-5.5 is an OpenAI flagship reasoning model with text and image input, made available in the API in April 2026 and described by OpenAI… | $5 input / $30 output per 1M tokens |
| [`openai/gpt-5.5-pro`](../models/openai/gpt-5.5-pro.md) | GPT-5.5 Pro is a separate OpenAI model in the GPT-5.5 family that uses more compute to think harder and give consistently better answers,… | $30 input / $180 output per 1M tokens |
| [`openai/gpt-5.6-luna`](../models/openai/gpt-5.6-luna.md) | GPT-5.6 Luna is the smallest, fastest tier of OpenAI's GPT-5.6 reasoning family, with text and image input; OpenAI says it roughly… | $0.2 input / $1.2 output per 1M tokens |
| [`openai/gpt-5.6-luna-pro`](../models/openai/gpt-5.6-luna-pro.md) | GPT-5.6 Luna Pro is the same GPT-5.6 Luna model, OpenAI's smallest GPT-5.6 tier, served in OpenAI's pro reasoning mode rather than as… | $0.2 input / $1.2 output per 1M tokens |
| [`openai/gpt-5.6-sol`](../models/openai/gpt-5.6-sol.md) | GPT-5.6 Sol is the flagship tier of OpenAI's GPT-5.6 reasoning family, accepting text and image input; OpenAI says it roughly corresponds… | $4 input / $20 output per 1M tokens |
| [`openai/gpt-5.6-sol-pro`](../models/openai/gpt-5.6-sol-pro.md) | GPT-5.6 Sol Pro is the same GPT-5.6 Sol model, the flagship of OpenAI's GPT-5.6 family, served in OpenAI's pro reasoning mode rather than… | $4 input / $20 output per 1M tokens |
| [`openai/gpt-5.6-terra`](../models/openai/gpt-5.6-terra.md) | GPT-5.6 Terra is the middle tier of OpenAI's GPT-5.6 reasoning family, with text and image input, and is described by OpenAI as a balanced… | $2 input / $12 output per 1M tokens |
| [`openai/gpt-5.6-terra-pro`](../models/openai/gpt-5.6-terra-pro.md) | GPT-5.6 Terra Pro is the same GPT-5.6 Terra model, the balanced middle tier of OpenAI's GPT-5.6 family, served in OpenAI's pro reasoning… | $2 input / $12 output per 1M tokens |
| [`openai/gpt-6-astra`](../models/openai/gpt-6-astra.md) | GPT-6 Astra is OpenAI's flagship GPT-6 reasoning model, described by OpenAI as its most capable model for the most demanding work, with… | $10 input / $50 output per 1M tokens |
| [`openai/gpt-6-astra-pro`](../models/openai/gpt-6-astra-pro.md) | GPT-6 Astra Pro is the same GPT-6 Astra model, OpenAI's most capable GPT-6 tier, served in OpenAI's pro reasoning mode rather than as… | $10 input / $50 output per 1M tokens |
| [`openai/gpt-6-luna`](../models/openai/gpt-6-luna.md) | GPT-6 Luna is the smallest, fastest tier of OpenAI's GPT-6 reasoning family, described by OpenAI as its most efficient model for focused,… | $0.1 input / $0.5 output per 1M tokens |
| [`openai/gpt-6-luna-pro`](../models/openai/gpt-6-luna-pro.md) | GPT-6 Luna Pro is the same GPT-6 Luna model, OpenAI's most efficient GPT-6 tier, served in OpenAI's pro reasoning mode instead of standard… | $0.1 input / $0.5 output per 1M tokens |
| [`openai/gpt-6-sol`](../models/openai/gpt-6-sol.md) | GPT-6 Sol is the middle tier of OpenAI's GPT-6 reasoning family, released in September 2026 alongside GPT-6 Luna and built, according to… | $2 input / $10 output per 1M tokens |
| [`openai/gpt-6-sol-pro`](../models/openai/gpt-6-sol-pro.md) | GPT-6 Sol Pro is the same GPT-6 Sol model, the middle tier of OpenAI's GPT-6 family, served in OpenAI's pro reasoning mode rather than as… | $2 input / $10 output per 1M tokens |
| [`openai/gpt-6.1-sol`](../models/openai/gpt-6.1-sol.md) | GPT-6.1 Sol is OpenAI's upgrade to GPT-6 Sol, introduced at DevDay 2026 and positioned between GPT-6 Astra and GPT-6 Luna, with text and… | $2 input / $10 output per 1M tokens |
| [`openai/gpt-6.1-sol-pro`](../models/openai/gpt-6.1-sol-pro.md) | GPT-6.1 Sol Pro is the same GPT-6.1 Sol model, OpenAI's near-Astra GPT-6 tier, served in OpenAI's pro reasoning mode rather than as… | $2 input / $10 output per 1M tokens |
| [`openai/gpt-6.1-terra`](../models/openai/gpt-6.1-terra.md) | GPT-6.1 Terra is the middle tier of OpenAI's GPT-6.1 family and the replacement for GPT-5.6 Terra, with text and image input. OpenAI… | $1 input / $5 output per 1M tokens |
| [`openai/gpt-6.1-terra-pro`](../models/openai/gpt-6.1-terra-pro.md) | GPT-6.1 Terra Pro is the same GPT-6.1 Terra model, the balanced middle tier of OpenAI's GPT-6.1 family, served in OpenAI's pro reasoning… | $1 input / $5 output per 1M tokens |
| [`openai/gpt-image-1-mini/edit`](../models/openai/gpt-image-1-mini/edit.md) | Gpt Image 1 Mini Edit is OpenAI's intelligent image editing model. Transform, retouch, and reimagine existing images using text prompts -… | from $0.007 to $0.054 per run, depending on parameters |
| [`openai/gpt-image-1.5`](../models/openai/gpt-image-1.5.md) | Gpt Image 1.5 is OpenAI's advanced text-to-image AI model. Create photorealistic images, illustrations, and concept art from natural… | from $0.014 to $0.205 per run, depending on parameters |
| [`openai/gpt-image-1.5/edit`](../models/openai/gpt-image-1.5/edit.md) | Gpt Image 1.5 Edit by OpenAI - AI-powered image editing, style transfer, and transformation. Edit photos with natural language… | from $0.009 to $0.2 per run, depending on parameters |
| [`openai/gpt-image-2`](../models/openai/gpt-image-2.md) | GPT Image 2, OpenAI's latest image model, is capable of making fine-grained, detailed edits to images. | from $0.01 to $0.72 per run, depending on parameters |
| [`openai/gpt-image-2.5-flare`](../models/openai/gpt-image-2.5-flare.md) | GPT Image 2.5 Flare is optimized for fast, high-quality image generation for everyday creative workflows. | from $0.01 to $1 per run, depending on parameters |
| [`openai/gpt-image-2.5-flare/edit`](../models/openai/gpt-image-2.5-flare/edit.md) | GPT Image 2.5 Flare Edit is optimized for fast, high-quality image editing and multi-image composition. | from $0.025 to $1.015 per run, depending on parameters |
| [`openai/gpt-image-2.5-sunburst`](../models/openai/gpt-image-2.5-sunburst.md) | GPT Image 2.5 Sunburst prioritizes visual fidelity and precision for complex image generation workflows. | from $0.01 to $1 per run, depending on parameters |
| [`openai/gpt-image-2.5-sunburst/edit`](../models/openai/gpt-image-2.5-sunburst/edit.md) | GPT Image 2.5 Sunburst Edit prioritizes precision and visual fidelity for complex image editing workflows. | from $0.025 to $1.015 per run, depending on parameters |
| [`openai/gpt-image-2.6-flare`](../models/openai/gpt-image-2.6-flare.md) | GPT Image 2.6 Flare is optimized for fast, high-quality image generation, with improved layout quality for posters, product imagery, and… | from $0.01 to $0.27 per run, depending on parameters |
| [`openai/gpt-image-2.6-flare/edit`](../models/openai/gpt-image-2.6-flare/edit.md) | GPT Image 2.6 Flare Edit is optimized for fast, high-quality image editing and multi-image composition. | from $0.025 to $0.285 per run, depending on parameters |
| [`openai/gpt-image-2.6-sunburst`](../models/openai/gpt-image-2.6-sunburst.md) | GPT Image 2.6 Sunburst prioritizes detail and precision for complex image generation workflows. | from $0.01 to $0.27 per run, depending on parameters |
| [`openai/gpt-image-2.6-sunburst/edit`](../models/openai/gpt-image-2.6-sunburst/edit.md) | GPT Image 2.6 Sunburst Edit prioritizes precision and consistency across successive edits for complex image editing workflows. | from $0.025 to $0.285 per run, depending on parameters |
| [`openai/gpt-image-2/edit`](../models/openai/gpt-image-2/edit.md) | GPT Image 2 Editing supports image editing and multi-image synthesis with high-quality results. | from $0.02 to $0.73 per run, depending on parameters |
| [`openai/gpt-oss-120b`](../models/openai/gpt-oss-120b.md) | gpt-oss-120b is OpenAI's largest open-weight reasoning model, released in August 2025 under the Apache 2.0 license: a 117B-parameter… | $0.039 input / $0.18 output per 1M tokens |
| [`openai/text-embedding-3-large`](../models/openai/text-embedding-3-large.md) | OpenAI text-embedding-3-large creates embeddings for semantic search, retrieval, clustering, and classification. | $0.13 input / $0 output per 1M tokens |
| [`openai/wizper`](../models/openai/wizper.md) | Wizper is a fast Whisper v3 speech-to-text model. It transcribes audio or video in about 100 languages, or translates the speech into… | $0.006 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-4.1"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
