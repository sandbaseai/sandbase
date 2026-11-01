// Run code in a SandBase sandbox with the official E2B SDK (npm install e2b).
//
//   export SANDBASE_API_KEY=sk-...
//   node hello-sandbox.mjs
//
// SandBase speaks the E2B protocol: point the SDK at sandbox.sandbase.ai and use your SandBase key.
process.env.E2B_API_KEY ??= process.env.SANDBASE_API_KEY;
process.env.E2B_API_URL ??= "https://sandbox.sandbase.ai";
process.env.E2B_DOMAIN ??= "sandbox.sandbase.ai";
delete process.env.E2B_SANDBOX_URL;

const { Sandbox } = await import("e2b");

async function firstReadyTemplate() {
  const res = await fetch("https://sandbox.sandbase.ai/v2/templates?limit=100", {
    headers: { "X-API-Key": process.env.E2B_API_KEY },
  });
  const ready = (await res.json()).filter((t) => t.buildStatus === "ready");
  if (!ready.length) throw new Error("no ready sandbox template is visible to this key");
  return ready[0].templateID;
}

const template = process.env.SANDBASE_TEMPLATE_ID ?? (await firstReadyTemplate());
const sandbox = await Sandbox.create(template, { timeoutMs: 120_000 });
try {
  console.log("sandbox:", sandbox.sandboxId);
  const r = await sandbox.commands.run("python3 -c 'print(sum(range(10)))'");
  console.log("stdout:", r.stdout.trim(), "exit:", r.exitCode);
  await sandbox.files.write("/tmp/hello.txt", "hello from SandBase");
  console.log("file:", await sandbox.files.read("/tmp/hello.txt"));
} finally {
  await sandbox.kill();
  console.log("deleted");
}
