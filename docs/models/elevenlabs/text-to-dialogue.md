# Text To Dialogue

`elevenlabs/text-to-dialogue` · audio · ElevenLabs

ElevenLabs Text to Dialogue uses Eleven v3 to turn a list of lines into a multi-speaker conversation, with a separate voice for each line and inline audio tags for delivery.

## Pricing

- Depends on parameters (`params.inputs`).

Formula: `Math.max(1.0, Math.ceil(sum(map(params.inputs ?? [], len(#.text ?? ""))) / 1000.0)) * 0.2`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "elevenlabs/text-to-dialogue"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('elevenlabs/text-to-dialogue', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("elevenlabs/text-to-dialogue", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "elevenlabs/text-to-dialogue", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `inputs` | array |  | A list of dialogue inputs, each containing text and a voice ID which will be converted into speech.  |
| `stability` | number |  | Determines how stable the voice is and the randomness between each generation. Lower values introduce broader emotional range for the voice. Higher values can result in a monotonous voice with limited emotion. Must be… range 0–1 |
| `language_code` | string |  | Language code (ISO 639-3) used to enforce a language for the model. one of: ``, `afr`, `ara`, `hye`, `asm`, `aze`, `bel`, `ben`, `bos`, `bul`, `cat`, `ceb` … |

## Details

ElevenLabs text-to-dialogue (Eleven v3): a multi-speaker conversation from a list of lines, each with its own voice and inline audio tags.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `inputs` | item[] | — | List of `{text, voice}` lines in speaking order. |
| `language_code` | `` / `afr` / `ara` / `hye` / `asm` / `aze` / `bel` / `ben` / `bos` / `bul` / `cat` / `ceb` / `nya` / `hrv` / `ces` / `dan` / `nld` / `eng` / `est` / `fil` / `fin` / `fra` / `glg` / `kat` / `deu` / `ell` / `guj` / `hau` / `heb` / `hin` / `hun` / `isl` / `ind` / `gle` / `ita` / `jpn` / `jav` / `kan` / `kaz` / `kir` / `kor` / `lav` / `lin` / `lit` / `ltz` / `mkd` / `msa` / `mal` / `cmn` / `mar` / `nep` / `nor` / `pus` / `fas` / `pol` / `por` / `pan` / `ron` / `rus` / `srp` / `snd` / `slk` / `slv` / `som` / `spa` / `swa` / `swe` / `tam` / `tel` / `tha` / `tur` / `ukr` / `urd` / `vie` / `cym` | — | Force a language. |
| `stability` | number 0–1 | — | Lower is more expressive. |

### Billing

$0.20 per started 1,000 characters across all lines, with a one-unit minimum.

| Dialogue | Price |
|---|---|
| 500 characters | $0.20 |
| 1,000 characters | $0.20 |
| 3,000 characters | $0.60 |

Failed runs are not charged.

### Prompting

- Use audio tags like `[laughs]` inside lines for delivery.

### Also on SandBase

Related: `elevenlabs/v3`.

---
Machine-readable: [`catalog/models/elevenlabs/text-to-dialogue.json`](../../../catalog/models/elevenlabs/text-to-dialogue.json) · Store page: https://www.sandbase.ai/model/elevenlabs/text-to-dialogue
