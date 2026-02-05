# Last 30 Days Research Scripts

Python scripts for gathering research data from various sources.

## Scripts

### search_x.py

Searches X/Twitter for recent posts and discussions using xAI's Grok API.

**Requirements:**
- `xai-sdk>=1.3.1`
- `XAI_API_KEY` environment variable

**Usage:**
```bash
python search_x.py "your search topic"
```

**Output:** JSON with posts, accounts, sentiment, and citations.

**API Notes:**
- Uses the xAI Responses API with `x_search()` agent tool
- Model: `grok-4-1-fast` (recommended for agent tools)
- Searches posts from the last 30 days by default

### search_reddit.py

Searches Reddit for discussions and community sentiment using OpenAI API.

**Requirements:**
- `openai>=1.0.0`
- `OPENAI_API_KEY` environment variable

**Usage:**
```bash
python search_reddit.py "your search topic"
```

**Output:** JSON with subreddits, discussions, consensus, and sentiment analysis.

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
XAI_API_KEY=your_xai_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## Changelog

### 2026-02-04

- **search_x.py**: Migrated from deprecated Live Search API to Agent Tools API
  - Switched from `openai` client to native `xai-sdk`
  - Uses `x_search()` tool with date range filtering
  - Updated model to `grok-4-1-fast`
  - Added citation extraction for audit trail
