# VEED models API: 1 endpoints with pricing and code examples

Call 1 VEED models through SandBase with one API key: no separate account, one balance, the same request format for every endpoint. Each page has the input schema, the price and curl / Python / TypeScript / Go examples.

| Endpoint | What it does | Price |
|---|---|---|
| [`veed/lipsync/2.0`](../models/veed/lipsync/2.0.md) | VEED Lipsync 2.0 makes the person in a video articulate a new audio track. | about $0.375 per call |

## Quick start

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "veed/lipsync/2.0", "audio": "https://static.sandbase.ai/examples/1e3c1d50-3506-4215-ab86-d63bdf2b277a/input/adb496f2-9bfc-4bd0-bdb6-becfd4c320d5.mp3", "video": "https://static.sandbase.ai/examples/1e3c1d50-3506-4215-ab86-d63bdf2b277a/input/2d3f9e09-37e3-4878-b5f2-5e21ec7f494b.mp4"}'
```

Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).
