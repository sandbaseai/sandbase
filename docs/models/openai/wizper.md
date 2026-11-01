# Wizper (Whisper v3)

`openai/wizper` · audio · OpenAI

Wizper is a fast Whisper v3 speech-to-text model. It transcribes audio or video in about 100 languages, or translates the speech into English, with segment-level timestamps.

## Pricing

- **$0.006 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/wizper"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('openai/wizper', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("openai/wizper", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "openai/wizper", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `task` | string |  | Task to perform on the audio file. Either transcribe or translate. one of: `transcribe`, `translate`; default `"transcribe"` |
| `audio` | string |  | URL of the audio file to transcribe. Supported formats: mp3, mp4, mpeg, mpga, m4a, wav or webm.  |
| `version` | string |  | Version of the model to use. All of the models are the Whisper large variant. default `"3"` |
| `language` | string |  | Language of the audio file. If translate is selected as the task, the audio will be translated to English, regardless of the language selected. If `None` is passed, the language will be automatically detected. This… one of: `af`, `am`, `ar`, `as`, `az`, `ba`, `be`, `bg`, `bn`, `bo`, `br`, `bs` …; default `"en"` |
| `chunk_level` | string |  | Level of the chunks to return. default `"segment"` |
| `merge_chunks` | boolean |  | Whether to merge consecutive chunks. When enabled, chunks are merged if their combined duration does not exceed max_segment_len. default `true` |
| `max_segment_len` | integer |  | Maximum speech segment duration in seconds before splitting. default `29`; range 10–29 |

## Details

Wizper is a fast Whisper v3 speech-to-text model: transcribe audio in about 100 languages, or translate it to English.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `audio` | audio URL | — | Audio or video URL to transcribe. |
| `task` | `transcribe` / `translate` | `transcribe` | `transcribe` keeps the source language; `translate` outputs English. |
| `chunk_level` | string | `segment` | Timestamp granularity. |
| `max_segment_len` | integer 10–29 | 29 | Maximum segment length in seconds. |
| `language` | `af` / `am` / `ar` / `as` / `az` / `ba` / `be` / `bg` / `bn` / `bo` / `br` / `bs` / `ca` / `cs` / `cy` / `da` / `de` / `el` / `en` / `es` / `et` / `eu` / `fa` / `fi` / `fo` / `fr` / `gl` / `gu` / `ha` / `haw` / `he` / `hi` / `hr` / `ht` / `hu` / `hy` / `id` / `is` / `it` / `ja` / `jw` / `ka` / `kk` / `km` / `kn` / `ko` / `la` / `lb` / `ln` / `lo` / `lt` / `lv` / `mg` / `mi` / `mk` / `ml` / `mn` / `mr` / `ms` / `mt` / `my` / `ne` / `nl` / `nn` / `no` / `oc` / `pa` / `pl` / `ps` / `pt` / `ro` / `ru` / `sa` / `sd` / `si` / `sk` / `sl` / `sn` / `so` / `sq` / `sr` / `su` / `sv` / `sw` / `ta` / `te` / `tg` / `th` / `tk` / `tl` / `tr` / `tt` / `uk` / `ur` / `uz` / `vi` / `yi` / `yo` / `zh` | `en` | Source language code. |
| `version` | string | `3` | Version of the model to use. |
| `merge_chunks` | boolean | true | Merge short segments. |

### Billing

$0.006 per request, whatever the audio length.

| Request | Price |
|---|---|
| One file | $0.006 |

Failed runs are not charged.

### Limits

- One audio file per request.

---
Machine-readable: [`catalog/models/openai/wizper.json`](../../../catalog/models/openai/wizper.json) · Store page: https://www.sandbase.ai/model/openai/wizper
