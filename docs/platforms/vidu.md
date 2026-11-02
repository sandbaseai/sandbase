# Vidu models API: 7 endpoints with pricing and code examples

Call 7 Vidu models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`vidu/q3/image-to-video`](../models/vidu/q3/image-to-video.md) | Vidu Q3 by Shengshu - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion, camera… | from $0.07 to $2.56 per run, depending on parameters |
| [`vidu/q3/image-to-video/turbo`](../models/vidu/q3/image-to-video/turbo.md) | Vidu Q3 Turbo by Shengshu - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion,… | from $0.04 to $1.28 per run, depending on parameters |
| [`vidu/q3/reference-to-video/mix`](../models/vidu/q3/reference-to-video/mix.md) | Vidu Q3 Mix by Shengshu - animate still images into dynamic videos with AI. Transform photos into cinematic clips with natural motion,… | from $0.07 to $2.464 per run, depending on parameters |
| [`vidu/q3/text-to-video`](../models/vidu/q3/text-to-video.md) | Vidu Q3 is Shengshu's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic… | from $0.07 to $2.56 per run, depending on parameters |
| [`vidu/q3/text-to-video/turbo`](../models/vidu/q3/text-to-video/turbo.md) | Vidu Q3 Turbo is Shengshu's text-to-video AI model. Turn written scripts and prompts into professional-quality video clips with realistic… | from $0.04 to $1.28 per run, depending on parameters |
| [`vidu/q4/image-to-video`](../models/vidu/q4/image-to-video.md) | Vidu Q4 Preview by Shengshu animates a first-frame image into a 3 to 16 second video at up to 4K. Prompts can direct motion, camera cuts,… | from $0.135 to $6.24 per run, depending on parameters |
| [`vidu/q4/reference-to-video`](../models/vidu/q4/reference-to-video.md) | Vidu Q4 Preview by Shengshu builds a 3 to 16 second video at up to 4K from up to 12 reference images and 3 voice clips, keeping… | from $0.135 to $6.24 per run, depending on parameters |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vidu/q3/image-to-video", "image": "https://static.sandbase.ai/examples/c5e6585e-7e89-4c14-a4e1-6fb94916f126/input/066353de-0ec8-4d21-bf03-46efafa9db7b.png", "prompt": "The astronaut waved and the camera moved up."}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
