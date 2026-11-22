# sandbase (TypeScript / JavaScript)

No runtime dependencies. Node.js 18+ (use a currently supported LTS release), Deno or Bun. Keep your API key in server-side code, never in a public browser bundle.

## Install from source

`@sandbaseai/sdk` is not published to npm yet. Clone and build the client:

```bash
git clone https://github.com/sandbaseai/sandbase.git
cd sandbase/sdk/typescript
npm ci
npm run build
```

Save the following example as `example.mjs` in that directory, then run `node example.mjs`. In an existing TypeScript project, you can instead copy [`src/index.ts`](src/index.ts) to `sandbase.ts` and import `./sandbase.js` using your project's TypeScript build.

For production, pin the repository to a reviewed commit. For other ways to use SandBase, see [Quick Start](https://www.sandbase.ai/docs/getting-started/quickstart) or [CLI / MCP](https://github.com/sandbaseai/cli).

```bash
export SANDBASE_API_KEY=sk-...
```

```js
import { SandBase } from "./dist/index.js";

const sb = new SandBase();

// Any capability, sync or async: run() resolves with the finished result
const r = await sb.run("exa/search", { query: "AI agents", numResults: 3 });
console.log(r.output ?? r.outputs);

// Async without blocking
const job = await sb.submit("bytedance/seedance/2.5/text-to-video", { prompt: "a cat surfing", duration: 4 });
const video = await sb.wait(job.id, { timeoutMs: 900_000 });
console.log(video.outputs?.[0]?.url, await sb.cost(job.id));
```

Calls execute real work and may use your balance. Inspect the model's current schema and price before running examples.

## Timeouts and errors

`new SandBase({ requestTimeoutMs: 60_000 })` limits each HTTP request, including reading the response. The default is 300 seconds. `wait(id, { timeoutMs: 900_000 })` separately limits polling between requests; an in-flight request is bounded by `requestTimeoutMs`.

HTTP failures and request timeouts throw `SandBaseError`. A timeout does not cancel server-side work: check your run history, then resume with `get(id)` or `wait(id)` instead of blindly submitting again. The client does not automatically retry billable submissions.

For LLM streaming, use an OpenAI-compatible client with base URL `https://api.sandbase.ai/v1`. This SDK's `baseUrl` uses the API origin `https://api.sandbase.ai` because its methods already add `/v1`.

## Agents

```ts
const agent = await sb.createAgent({ model: "deepseek/deepseek-v4-flash", instructions: "Answer briefly." });
const r = await sb.runAgent(agent.id, "What is 2+2?");   // { sessionId, status, output, turn }
const r2 = await sb.send(r.sessionId, "And times 10?");
const run = await sb.invokeService("svc_...", "What is 7+7?");   // run.output is the final answer
```

## Sandboxes

Use the official E2B SDK (`npm install e2b`) with `E2B_API_URL=https://sandbox.sandbase.ai`, `E2B_DOMAIN=sandbox.sandbase.ai` and your SandBase key as `E2B_API_KEY`. See [`examples/sandbox/typescript`](../../examples/sandbox/typescript/hello-sandbox.mjs).
