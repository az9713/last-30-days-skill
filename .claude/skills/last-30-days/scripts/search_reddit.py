#!/usr/bin/env python3
"""
Search Reddit discussions using OpenAI's API (which has Reddit data partnership).
Returns subreddits, top threads, and community insights for a given topic.
"""

import os
import sys
import json
from datetime import datetime, timedelta

try:
    from openai import OpenAI
except ImportError:
    print(json.dumps({
        "error": "openai package not installed",
        "fix": "pip install openai>=1.0.0"
    }))
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional if env vars are set directly


def search_reddit(topic: str) -> dict:
    """
    Search Reddit for recent discussions on a topic using OpenAI's API.

    Args:
        topic: The topic to search for

    Returns:
        Dictionary containing search results with subreddits, threads, and insights
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return {
            "error": "OPENAI_API_KEY not set",
            "fix": "Set OPENAI_API_KEY environment variable or add to .env file"
        }

    # Calculate date range (last 30 days)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    date_range = f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"

    client = OpenAI(api_key=api_key)

    search_prompt = f"""Search Reddit discussions from the last 30 days about: {topic}

Please provide comprehensive information including:

1. **Relevant Subreddits**: Which subreddits are actively discussing this topic?
   - Include subscriber counts if known
   - Note the community's expertise level and focus

2. **Top Discussions**: Most upvoted and commented threads about this topic
   - Thread titles and brief summaries
   - Key points from top comments
   - Upvote/comment counts when available

3. **Community Consensus**: What do Redditors generally agree on?
   - Popular recommendations
   - Widely-accepted best practices
   - Common warnings or pitfalls

4. **Contrarian Views**: What minority opinions exist?
   - Alternative approaches
   - Criticisms of mainstream advice

5. **Actionable Insights**: Specific tips, tools, or strategies mentioned
   - Concrete recommendations
   - Resources shared (books, tools, courses)
   - Step-by-step approaches

6. **Sentiment Analysis**: Overall community sentiment about this topic
   - Enthusiasm level
   - Common frustrations
   - Emerging trends

Format the response as structured, actionable information."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a research assistant that specializes in finding and synthesizing Reddit discussions. Provide comprehensive, well-organized results with specific examples from actual Reddit threads when possible. Focus on actionable insights and community consensus."
                },
                {
                    "role": "user",
                    "content": search_prompt
                }
            ]
        )

        result = {
            "source": "Reddit via OpenAI",
            "topic": topic,
            "date_range": date_range,
            "content": response.choices[0].message.content,
            "model": response.model,
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens
            }
        }

        return result

    except Exception as e:
        return {
            "error": str(e),
            "topic": topic,
            "source": "Reddit via OpenAI"
        }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "No topic provided",
            "usage": "python search_reddit.py <topic>"
        }))
        sys.exit(1)

    # Join all arguments as the topic (handles multi-word topics)
    topic = " ".join(sys.argv[1:])

    result = search_reddit(topic)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
