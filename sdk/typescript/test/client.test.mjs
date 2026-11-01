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
