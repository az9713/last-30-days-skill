#!/usr/bin/env python3
"""
Search X/Twitter using the Xquik REST API.
Returns recent posts from the last 30 days for a given topic.
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timedelta, timezone
from typing import Any
from urllib.parse import urlencode

import requests

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


DEFAULT_BASE_URL = "https://xquik.com"
DEFAULT_LIMIT = 20
MAX_LIMIT = 200


def _get_limit() -> int:
    raw_limit = os.getenv("XQUIK_SEARCH_LIMIT", str(DEFAULT_LIMIT)).strip()
    try:
        limit = int(raw_limit)
    except ValueError:
        return DEFAULT_LIMIT
    return max(1, min(limit, MAX_LIMIT))


def _tweet_items(payload: Any) -> list[Any]:
    if isinstance(payload, list):
        return payload
    if not isinstance(payload, dict):
        return []
    for key in ("tweets", "data", "items", "results"):
        value = payload.get(key)
        if isinstance(value, list):
            return value
    return []


def search_xquik(topic: str) -> dict[str, Any]:
    api_key = os.getenv("XQUIK_API_KEY", "").strip()
    if not api_key:
        return {
            "error": "XQUIK_API_KEY not set",
            "fix": "Set XQUIK_API_KEY in your environment or .env file",
        }

    end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=30)
    date_range = f"{start_date.date().isoformat()} to {end_date.date().isoformat()}"

    base_url = os.getenv("XQUIK_BASE_URL", DEFAULT_BASE_URL).strip().rstrip("/")
    limit = _get_limit()
    query = urlencode(
        {
            "q": topic,
            "queryType": "Latest",
            "sinceTime": start_date.isoformat(),
            "untilTime": end_date.isoformat(),
            "limit": str(limit),
        }
    )
    url = f"{base_url}/api/v1/x/tweets/search?{query}"

    try:
        response = requests.get(
            url,
            headers={"X-API-Key": api_key, "Accept": "application/json"},
            timeout=60,
        )
        response.raise_for_status()
        payload: Any = response.json()
    except requests.Timeout:
        return {
            "error": "Xquik API timeout",
            "topic": topic,
            "source": "X/Twitter via Xquik",
        }
    except requests.RequestException as exc:
        return {
            "error": str(exc),
            "topic": topic,
            "source": "X/Twitter via Xquik",
        }
    except ValueError:
        return {
            "error": "Xquik API returned non-JSON response",
            "topic": topic,
            "source": "X/Twitter via Xquik",
        }

    tweets = _tweet_items(payload)
    return {
        "source": "X/Twitter via Xquik",
        "topic": topic,
        "date_range": date_range,
        "limit": limit,
        "tweets": tweets,
        "raw": payload,
    }


def main() -> None:
    if len(sys.argv) < 2:
        print(
            json.dumps(
                {
                    "error": "No topic provided",
                    "usage": "python search_xquik.py <topic>",
                }
            )
        )
        sys.exit(1)

    topic = " ".join(sys.argv[1:])
    result = search_xquik(topic)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
