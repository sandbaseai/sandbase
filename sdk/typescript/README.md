# sandbase (TypeScript / JavaScript)

No dependencies. Node 18+, Deno, Bun, browsers (anything with `fetch`).

The client is a single file, [`src/index.ts`](src/index.ts). Until the npm package is published, copy it into your project, or build it with `npm install && npm run build` and import `dist/index.js`.

```bash
export SANDBASE_API_KEY=sk-...
```

```ts
import { SandBase } from "@sandbaseai/sdk";

const sb = new SandBase();

// Any capability, sync or async: run() resolves with the finished result
const r = await sb.run("exa/search", { query: "AI agents", numResults: 3 });

// Async without blocking
const job = await sb.submit("bytedance/seedance/2.5/text-to-video", { prompt: "a cat surfing", duration: 4 });
const video = await sb.wait(job.id, { timeoutMs: 900_000 });
console.log(video.outputs?.[0]?.url, await sb.cost(job.id));

// LLM: the OpenAI SDK works as-is
import OpenAI from "openai";
const openai = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
```

## Agents

```ts
const agent = await sb.createAgent({ model: "deepseek/deepseek-v4-flash", instructions: "Answer briefly." });
const r = await sb.runAgent(agent.id, "What is 2+2?");   // { sessionId, status, output, turn }
const r2 = await sb.send(r.sessionId, "And times 10?");
const run = await sb.invokeService("svc_...", "What is 7+7?");   // run.output is the final answer
```

## Sandboxes

Use the official E2B SDK (`npm install e2b`) with `E2B_API_URL=https://sandbox.sandbase.ai`, `E2B_DOMAIN=sandbox.sandbase.ai` and your SandBase key as `E2B_API_KEY`. See [`examples/sandbox/typescript`](../../examples/sandbox/typescript/hello-sandbox.mjs).
