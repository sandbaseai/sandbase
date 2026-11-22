"""Offline client regressions; no credentials or live API calls required."""
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sandbase import SandBase, SandBaseError, _last_assistant_text


class Response(io.BytesIO):
    def __init__(self, value):
        super().__init__(json.dumps(value).encode() if value is not None else b"")


class ClientTests(unittest.TestCase):
    def setUp(self):
        self.client = SandBase(api_key="test-key", base_url="https://example.test/")

    def test_missing_key(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaisesRegex(SandBaseError, "missing API key"):
                SandBase()

    def test_environment_configuration(self):
        with patch.dict("os.environ", {"SANDBASE_API_KEY": "test-key", "SANDBASE_BASE_URL": "https://example.test/"}):
            client = SandBase()
            self.assertEqual(client.api_key, "test-key")
            self.assertEqual(client.base_url, "https://example.test")

    def test_request_serialization_auth_and_timeout(self):
        with patch("urllib.request.urlopen", return_value=Response({"id": "r1", "status": "completed"})) as http:
            self.client.submit("exa/search", query="AI agents")
        request = http.call_args.args[0]
        self.assertEqual(request.full_url, "https://example.test/v1/run")
        self.assertEqual(request.get_method(), "POST")
        self.assertEqual(request.get_header("Authorization"), "Bearer test-key")
        self.assertTrue(request.get_header("User-agent").startswith("sandbase-python/"))
        self.assertEqual(json.loads(request.data), {"model": "exa/search", "query": "AI agents"})
        self.assertEqual(http.call_args.kwargs["timeout"], 300)

    def test_http_errors_preserve_status_and_body(self):
        for raw, expected in [(b'{"error":"invalid input"}', {"error": "invalid input"}), (b"gateway unavailable", "gateway unavailable")]:
            with self.subTest(raw=raw):
                error = HTTPError("https://example.test", 400, "bad request", {}, io.BytesIO(raw))
                with patch("urllib.request.urlopen", side_effect=error), self.assertRaises(SandBaseError) as caught:
                    self.client.get("r1")
                self.assertEqual(caught.exception.status, 400)
                self.assertEqual(caught.exception.body, expected)

    def test_empty_response(self):
        with patch("urllib.request.urlopen", return_value=Response(None)):
            self.assertIsNone(self.client.request("DELETE", "/v1/example"))

    def test_sync_run_does_not_poll(self):
        result = {"id": "r1", "status": "completed", "output": {"results": []}}
        with patch.object(self.client, "submit", return_value=result), patch.object(self.client, "get") as get:
            self.assertEqual(self.client.run("exa/search"), result)
            get.assert_not_called()

    def test_async_run_polls_without_resubmitting(self):
        done = {"id": "r1", "status": "completed", "outputs": [{"url": "https://example.test/result.png"}]}
        with patch.object(self.client, "submit", return_value={"id": "r1", "status": "pending"}) as submit, patch.object(self.client, "get", side_effect=[{"id": "r1", "status": "processing"}, done]) as get, patch("sandbase.time.sleep"):
            self.assertEqual(self.client.run("image-model"), done)
            submit.assert_called_once()
            self.assertEqual(get.call_count, 2)

    def test_failed_run_can_be_inspected(self):
        failed = {"id": "r1", "status": "failed", "error": "provider error"}
        with patch.object(self.client, "submit", return_value=failed):
            with self.assertRaises(SandBaseError) as caught:
                self.client.run("example")
            self.assertEqual(caught.exception.body, failed)
            self.assertEqual(self.client.run("example", raise_on_failure=False), failed)

    def test_wait_timeout_preserves_run(self):
        pending = {"id": "r1", "status": "processing"}
        with patch.object(self.client, "get", return_value=pending), patch("sandbase.time.monotonic", side_effect=[0, 2]):
            with self.assertRaises(SandBaseError) as caught:
                self.client.wait("r1", timeout=1)
            self.assertEqual(caught.exception.body, pending)

    def test_terminal_cancelled_run_stops_polling(self):
        for status in ("cancelled", "canceled", "succeeded"):
            with patch.object(self.client, "get", return_value={"id": "r1", "status": status}) as get:
                self.assertEqual(self.client.wait("r1")["status"], status)
                get.assert_called_once()

    def test_agent_output_preserves_parts_and_discards_previous_turn(self):
        items = [
            {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "old"}]},
            {"type": "message", "role": "user", "content": []},
            {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "first"}, {"type": "output_text", "text": "second"}]},
            {"type": "message", "role": "assistant", "content": [{"type": "output_text", "text": "third"}]},
        ]
        self.assertEqual(_last_assistant_text(items), "first\nsecond\nthird")
        with patch.object(self.client, "request", return_value={"data": list(reversed(items))}):
            self.assertEqual(self.client._latest_output("s1"), "first\nsecond\nthird")


if __name__ == "__main__":
    unittest.main()
