# HeyGen Avatar 5 Digital Twin

`heygen/avatar5/digital-twin` · video · HeyGen

Avatar5 Digital Twin by HeyGen - generate cinematic videos from text descriptions with AI. Create high-quality video content with natural motion, camera control, and optional audio generation.

## Pricing

- Depends on parameters (`params.audio`, `usage.duration`).

Formula: `(usage.duration ?? ((params.audio ?? "") != "" ? media_duration(params.audio) : nil) ?? 5.0) * 0.12`

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "heygen/avatar5/digital-twin", "prompt": "Hello and welcome to this demonstration of HeyGen Avatar V."}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('heygen/avatar5/digital-twin', {'prompt': 'Hello and welcome to this demonstration of HeyGen Avatar V.'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("heygen/avatar5/digital-twin", {
  "prompt": "Hello and welcome to this demonstration of HeyGen Avatar V."
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "heygen/avatar5/digital-twin", sandbase.Params{
	"prompt": "Hello and welcome to this demonstration of HeyGen Avatar V.",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

## Parameters

| name | type | required | description |
|---|---|---|---|
| `fit` | string |  | How the avatar fits within the output frame. 'contain' keeps the full avatar in view (may letterbox); 'cover' fills the frame (may crop). one of: `contain`, `cover`; default `"cover"` |
| `audio` | string |  | HTTP(S) URL of an audio file for the avatar to lip-sync to. When provided, the avatar uses this audio instead of text-to-speech and ``prompt``/``voice`` are ignored.  |
| `voice` | string |  | Name of the text-to-speech voice to use for the avatar when ``audio_url`` is not provided. one of: `Warm Pro Narrator`, `Chill Brian`, `Ivy`, `John Doe`, `Monika Sogam`, `Hope `, `Archer `, `Brittney`, `Patrick`, `David Castlemore`, `Michael C`, `Adam Stone ` …; default `"Warm Pro Narrator"` |
| `avatar` | string |  | Name of the Avatar V-eligible avatar to use. default `"Abigail Sofa Front"` |
| `prompt` | string | yes | Text the avatar will speak. Required when ``audio_url`` is not provided.  |
| `caption` | boolean |  | Generate a sidecar SRT caption file alongside the video. default `false` |
| `watermark` | string |  | Optional watermark image URL to overlay on the output video.  |
| `resolution` | string |  | Output resolution preset. one of: `720p`, `1080p`, `4k`; default `"720p"` |
| `aspect_ratio` | string |  | Output aspect ratio. Omit to keep the source aspect ratio (falls back to 16:9 when it cannot be read). one of: `16:9`, `9:16`, `5:4`, `4:5`, `1:1` |
| `output_format` | string |  | Output container format. 'webm' produces a transparent video (automatically removes the background) and ignores the ``background`` field. one of: `mp4`, `webm`; default `"mp4"` |
| `remove_background` | boolean |  | Remove the avatar's background. Requires a matting-enabled avatar. default `false` |

## Details

HeyGen Avatar 5 Digital Twin: a presenter video from a script or audio track, using a stock or custom avatar, up to 4K, with optional captions and background removal.

### Fields

| Field | Type | Default | Notes |
|---|---|---|---|
| `prompt` | string, required | — | Script to speak, or direction when `audio` is supplied. |
| `aspect_ratio` | `16:9` / `9:16` / `5:4` / `4:5` / `1:1` | — | Output frame shape. |
| `audio` | audio URL | — | Optional voice track; otherwise the script is voiced with `voice`. |
| `resolution` | `720p` / `1080p` / `4k` | `720p` | Output resolution. |
| `output_format` | `mp4` / `webm` | `mp4` | Output file format. |
| `remove_background` | boolean | false | Transparent background (WebM). |
| `avatar` | string | `Abigail Sofa Front` | Avatar to use. |
| `voice` | `Warm Pro Narrator` / `Chill Brian` / `Ivy` / `John Doe` / `Monika Sogam` / `Hope ` / `Archer ` / `Brittney` / `Patrick` / `David Castlemore` / `Michael C` / `Adam Stone ` / `Juniper` / `Cassidy ` / `Jessica Anne Bogart` / `Arabella` / `Andrew` / `Spuds Oxley ` / `Grace Elder` / `Helen` / `Canyon Rivers` / `Derya - Lifelike - Excited 🤩` / `Mellow Marcus` / `Jack Sterling - Broadcaster 🎙️` / `Brenda - UGC - 1.mp4` / `Reid` / `Reagan` / `Terry` / `Jenny` / `Radio Rick` / `Denise` / `Tim in car - Excited 🤩` / `Iskander` / `Thompson` / `Delicate Daisy - Excited 🤩` / `Kingston` / `George UGC 1` / `Bold Blake` / `Jane` / `Expressive Evan` / `Marianne - IA` / `Aaron` / `Modern Recipe Host - Voice 1` / `Willow` / `Cute Chloe - Friendly 😊` / `Rafael` / `June - Lifelike` / `Crisp Chloe` / `Slick Simon` / `Nassim - Informative` / `Baritone Ben` / `Maxwell` / `Ellie Faye - Excited 🤩` / `Milani` / `Feisty Fiona - Excited 🤩` / `Professor Dean` / `Rose - UGC - 1.mp4` / `Shona` / `Hudson Wilder` / `Ann - IA` / `Alastair Kensington` / `Oxley` / `Christina` / `Andrew Rizz ` / `Peyton` / `Gerardo - Outdoor` / `Chloe - Lifelike` / `Stephanie` / `Anthony - IA` / `Signal - Voice 1` / `Luca` / `Lisa - Voice 1` / `T.W.Tucker` / `Jack Sullivan - Serious 😐` / `Winter` / `Mireia - Lifelike` / `Georgia` / `Stella` / `Masha - Lifelike` / `Charming Charles - Friendly 😊` / `Serenity` / `Annie - Excited` / `Ralph` / `Bethany` / `Dominic` / `Mason Finn` / `Leena` / `Veteran Victor` / `Tamara` / `Nik Public` / `Calm Chloe` / `Sevik` / `Reilly` / `Raul` / `Imposing Ian` / `Relaxed Ray` / `Dexter - Professional` / `Relaxed Rick` / `Edwin` / `Rupert Blackwood` / `Ginny` / `Hope` | `Warm Pro Narrator` | Voice for the script. |
| `caption` | boolean | false | Burn in captions. |
| `watermark` | string | — | Optional watermark image URL to overlay on the output video. |
| `fit` | `contain` / `cover` | `cover` | How the avatar fills the frame. |

### Billing

$0.12 per output second; length follows the audio or the spoken script. The quote before submission assumes 5 seconds.

| Output | Price |
|---|---|
| 5s | $0.60 |
| 30s | $3.60 |
| 60s | $7.20 |

Failed runs are not charged.

### Also on SandBase

Related: `heygen/heygen-avatar4/image-to-video` (from your own photo).

---
Machine-readable: [`catalog/models/heygen/avatar5/digital-twin.json`](../../../../catalog/models/heygen/avatar5/digital-twin.json) · Store page: https://www.sandbase.ai/model/heygen/avatar5/digital-twin
