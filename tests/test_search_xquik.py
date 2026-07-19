from __future__ import annotations

import importlib.util
import os
import unittest
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit


SCRIPT_PATH = (
    Path(__file__).parents[1]
    / ".claude"
    / "skills"
    / "last-30-days"
    / "scripts"
    / "search_xquik.py"
)
SPEC = importlib.util.spec_from_file_location("search_xquik", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load search_xquik.py")
SEARCH_XQUIK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SEARCH_XQUIK)


class FixedDateTime(datetime):
    @classmethod
    def now(cls, tz: Any = None) -> datetime:
        return cls(2026, 7, 17, 12, 34, 56, tzinfo=timezone.utc)


class FakeResponse:
    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict[str, list[dict[str, str]]]:
        return {"tweets": [{"id": "tweet-1"}]}


class SearchXquikTests(unittest.TestCase):
    def test_search_sends_iso_8601_time_bounds(self) -> None:
        request: dict[str, Any] = {}

        def fake_get(
            url: str,
            *,
            headers: dict[str, str],
            timeout: int,
        ) -> FakeResponse:
            request.update(url=url, headers=headers, timeout=timeout)
            return FakeResponse()

        environment = {
            "XQUIK_API_KEY": "test-key",
            "XQUIK_BASE_URL": "https://example.test",
            "XQUIK_SEARCH_LIMIT": "25",
        }
        with (
            patch.dict(os.environ, environment, clear=True),
            patch.object(SEARCH_XQUIK, "datetime", FixedDateTime),
            patch.object(SEARCH_XQUIK.requests, "get", side_effect=fake_get),
        ):
            result = SEARCH_XQUIK.search_xquik("AI agents")

        query = parse_qs(urlsplit(request["url"]).query)
        self.assertEqual(query["q"], ["AI agents"])
        self.assertEqual(query["queryType"], ["Latest"])
        self.assertEqual(query["sinceTime"], ["2026-06-17T12:34:56+00:00"])
        self.assertEqual(query["untilTime"], ["2026-07-17T12:34:56+00:00"])
        self.assertEqual(query["limit"], ["25"])
        self.assertEqual(request["headers"]["X-API-Key"], "test-key")
        self.assertEqual(request["timeout"], 60)
        self.assertEqual(result["tweets"], [{"id": "tweet-1"}])


if __name__ == "__main__":
    unittest.main()
