#!/usr/bin/env python3
"""
Search X/Twitter using XAI's Grok API with Agent Tools (x_search).
Returns recent posts, engagement metrics, and key accounts for a given topic.
"""

import os
import sys
import json
from datetime import datetime, timedelta

try:
    from xai_sdk import Client
    from xai_sdk.chat import user
    from xai_sdk.tools import x_search
except ImportError:
    print(json.dumps({
        "error": "xai-sdk package not installed",
        "fix": "pip install xai-sdk>=1.3.1"
    }))
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional if env vars are set directly


def search_x(topic: str) -> dict:
    """
    Search X/Twitter for recent content on a topic using XAI's Grok API.

    Args:
        topic: The topic to search for

    Returns:
        Dictionary containing search results with posts, accounts, and insights
    """
    api_key = os.getenv("XAI_API_KEY")

    if not api_key:
        return {
            "error": "XAI_API_KEY not set",
            "fix": "Set XAI_API_KEY environment variable or add to .env file"
        }

    # Calculate date range (last 30 days)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    date_range = f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"

    client = Client(api_key=api_key)

    search_prompt = f"""Search X/Twitter for the most relevant and engaging content about: {topic}

Focus on posts from the last 30 days ({date_range}).

Please provide:
1. **Top Posts**: The most engaged-with posts (likes, retweets, replies) about this topic. Include the @handle and post URL for each.
2. **Key Accounts**: Influential voices discussing this topic with their @handles.
3. **Trending Angles**: What specific aspects or subtopics are getting the most attention.
4. **Sentiment**: Overall community sentiment (positive, negative, mixed).
5. **Actionable Insights**: Key takeaways, frameworks, or strategies being discussed.

Format the response as structured data that can be easily parsed. Include direct links to posts where possible."""

    try:
        chat = client.chat.create(
            model="grok-4-1-fast",
            tools=[
                x_search(
                    from_date=start_date,
                    to_date=end_date
                )
            ]
        )

        chat.append(user(search_prompt))
        response = chat.sample()

        result = {
            "source": "X/Twitter via XAI Grok",
            "topic": topic,
            "date_range": date_range,
            "content": response.content,
            "model": "grok-4-1-fast"
        }

        # Include citations if available
        if hasattr(response, 'inline_citations') and response.inline_citations:
            citations = []
            for citation in response.inline_citations:
                if hasattr(citation, 'x_citation'):
                    citations.append({
                        "id": citation.id,
                        "url": citation.x_citation.url if hasattr(citation.x_citation, 'url') else None,
                        "handle": citation.x_citation.handle if hasattr(citation.x_citation, 'handle') else None
                    })
            result["citations"] = citations

        return result

    except Exception as e:
        return {
            "error": str(e),
            "topic": topic,
            "source": "X/Twitter via XAI Grok"
        }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "No topic provided",
            "usage": "python search_x.py <topic>"
        }))
        sys.exit(1)

    # Join all arguments as the topic (handles multi-word topics)
    topic = " ".join(sys.argv[1:])

    result = search_x(topic)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
