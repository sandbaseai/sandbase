# Sync Labs models API: 2 endpoints with pricing and code examples

Call 2 Sync Labs models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`sync/lipsync/3.0/image-to-video`](../models/sync/lipsync/3.0/image-to-video.md) | Sync 3 animates the face in a still image so it speaks the provided audio; the output matches the audio length. | about $0.675 per call |
| [`sync/lipsync/3.0/video-to-video`](../models/sync/lipsync/3.0/video-to-video.md) | Sync 3 by sync. re-animates the speaker's lips in an existing video to match new audio, with studio-grade identity preservation. | about $0.675 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sync/lipsync/3.0/image-to-video", "audio": "https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/b3a8612b-d1e8-4efb-97c0-34d3cd05a581.wav", "image": "https://static.sandbase.ai/examples/561589e7-7f64-4b10-8636-6a598fd9b9b8/input/0b00a2c7-affa-4bef-9e70-4f1526d9579a.png"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
