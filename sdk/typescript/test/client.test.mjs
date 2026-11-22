import { test } from "node:test";
import assert from "node:assert/strict";
import { SandBase, SandBaseError } from "../dist/index.js";

function fakeFetch(routes) {
  return async (url, init) => {
    const path = new URL(url).pathname;
    const handler = routes[`${init.method} ${path}`];
    if (!handler) return new Response("not found", { status: 404 });
    const { status = 200, body } = handler(init.body ? JSON.parse(init.body) : undefined);
    return new Response(JSON.stringify(body), { status });
  };
}

test("run waits for async capability", async () => {
  let polls = 0;
  const sb = new SandBase({
    apiKey: "sk-test",
    baseUrl: "https://x.test",
    fetch: fakeFetch({
      "POST /v1/run": (b) => {
        assert.equal(b.model, "app-store/search");
        assert.equal(b.term, "notes");
        return { body: { id: "r1", status: "pending" } };
      },
      "GET /v1/run/r1": () => ({ body: ++polls < 2 ? { id: "r1", status: "processing" } : { id: "r1", status: "completed", outputs: [{ data: 1 }] } }),
    }),
  });
  const run = await sb.run("app-store/search", { term: "notes" }, { intervalMs: 10 });
  assert.equal(run.status, "completed");
  assert.deepEqual(run.outputs, [{ data: 1 }]);
});

test("failed runs and HTTP errors reject", async () => {
  const sb = new SandBase({
    apiKey: "k",
    baseUrl: "https://x.test",
    fetch: fakeFetch({
      "POST /v1/run": (b) => (b.model === "bad" ? { status: 400, body: { error: "validation" } } : { body: { id: "r2", status: "failed" } }),
    }),
  });
  await assert.rejects(sb.run("m"), SandBaseError);
  await assert.rejects(sb.run("bad"), (e) => e instanceof SandBaseError && e.status === 400);
});

test("agent output preserves content order within each message and excludes previous turns", async () => {
  const message = (...texts) => ({ type: "message", role: "assistant", content: texts.map(text => ({ type: "output_text", text })) });
  const sb = new SandBase({ apiKey: "test-key", fetch: fakeFetch({
    "POST /v1/agents/sessions": () => ({ body: { id: "s1" } }),
    "GET /v1/agents/sessions/s1/turns": () => ({ body: { data: [{ id: "t1", status: "completed" }] } }),
    "GET /v1/agents/sessions/s1/items": () => ({ body: { data: [
      message("third", "fourth"), message("first", "second"),
      { type: "message", role: "user", content: [] }, message("old"),
    ] } }),
  }) });
  assert.equal((await sb.runAgent("a1", "hello")).output, "first\nsecond\nthird\nfourth");
});

test("request timeout aborts a stalled fetch without retrying the submission", async () => {
  let calls = 0;
  const sb = new SandBase({ apiKey: "test-key", requestTimeoutMs: 20, fetch: async (_url, init) => {
    calls++;
    return new Promise((_resolve, reject) => init.signal.addEventListener("abort", () => reject(new Error("aborted")), { once: true }));
  } });
  await assert.rejects(sb.submit("example"), error => error instanceof SandBaseError && /timed out.*check run history/.test(error.message));
  assert.equal(calls, 1);
});

test("request timeout also covers a stalled response body", async () => {
  const sb = new SandBase({ apiKey: "test-key", requestTimeoutMs: 20, fetch: async (_url, init) => ({
    ok: true, status: 200,
    text: () => new Promise((_resolve, reject) => init.signal.addEventListener("abort", () => reject(new Error("aborted")), { once: true })),
  }) });
  await assert.rejects(sb.get("r1"), /timed out/);
});

test("successful requests clear their abort timer", async () => {
  let signal;
  const sb = new SandBase({ apiKey: "test-key", requestTimeoutMs: 10, fetch: async (_url, init) => {
    signal = init.signal;
    return new Response(JSON.stringify({ id: "r1", status: "completed" }));
  } });
  await sb.get("r1");
  await new Promise(resolve => setTimeout(resolve, 30));
  assert.equal(signal.aborted, false);
});

test("rejects invalid request timeouts", () => {
  for (const requestTimeoutMs of [0, -1, NaN, Infinity, 2_147_483_648]) {
    assert.throws(() => new SandBase({ apiKey: "test-key", requestTimeoutMs }), /requestTimeoutMs/);
  }
});
