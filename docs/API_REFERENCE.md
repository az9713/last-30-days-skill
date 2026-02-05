# API Reference

Detailed technical reference for the Last 30 Days Research Skill.

## Table of Contents

1. [Script Reference](#script-reference)
2. [Input/Output Formats](#inputoutput-formats)
3. [Error Codes](#error-codes)
4. [External APIs](#external-apis)
5. [Environment Variables](#environment-variables)

---

## Script Reference

### search_x.py

**Location:** `.claude/skills/last-30-days/scripts/search_x.py`

**Purpose:** Search X/Twitter for recent posts about a topic using xAI's Grok API.

#### Command Line Usage

```bash
python search_x.py <topic>
```

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| topic | string | Yes | The topic to search for (can be multiple words) |

**Examples:**

```bash
# Single word
python search_x.py Python

# Multiple words
python search_x.py "AI coding assistants"

# Without quotes (also works)
python search_x.py AI coding assistants
```

#### Function Reference

##### `search_x(topic: str) -> dict`

Search X/Twitter for recent content on a topic.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| topic | str | The topic to search for |

**Returns:** `dict` with the following structure:

```python
{
    "source": "X/Twitter via XAI Grok",
    "topic": str,           # The searched topic
    "date_range": str,      # "YYYY-MM-DD to YYYY-MM-DD"
    "content": str,         # Structured findings
    "model": str,           # "grok-4-1-fast"
    "citations": [          # Optional, if available
        {
            "id": str,
            "url": str,     # Post URL
            "handle": str   # @username
        }
    ]
}
```

**Error Return:**

```python
{
    "error": str,           # Error message
    "topic": str,           # The searched topic
    "source": "X/Twitter via XAI Grok"
}
```

---

### search_reddit.py

**Location:** `.claude/skills/last-30-days/scripts/search_reddit.py`

**Purpose:** Analyze Reddit discussions about a topic using OpenAI's GPT-4.

#### Command Line Usage

```bash
python search_reddit.py <topic>
```

**Arguments:**

| Argument | Type | Required | Description |
|----------|------|----------|-------------|
| topic | string | Yes | The topic to analyze |

#### Function Reference

##### `search_reddit(topic: str) -> dict`

Analyze Reddit discussions for a topic.

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| topic | str | The topic to analyze |

**Returns:** `dict` with the following structure:

```python
{
    "source": "Reddit via OpenAI",
    "topic": str,           # The analyzed topic
    "date_range": str,      # "YYYY-MM-DD to YYYY-MM-DD"
    "content": str,         # Structured analysis
    "model": str,           # "gpt-4o-2024-08-06"
    "usage": {
        "prompt_tokens": int,
        "completion_tokens": int
    }
}
```

**Error Return:**

```python
{
    "error": str,           # Error message
    "topic": str,           # The analyzed topic
    "source": "Reddit via OpenAI"
}
```

---

## Input/Output Formats

### Script Input

All scripts accept a topic string as command line arguments:

```
python script.py word1 word2 word3
```

Arguments are joined with spaces to form the topic.

### Script Output

All scripts output JSON to stdout:

```json
{
  "source": "string",
  "topic": "string",
  "date_range": "string",
  "content": "string",
  ...
}
```

### Skill Output Format

The skill produces markdown with this structure:

```markdown
# Research Summary: [Topic]

*Research Date: YYYY-MM-DD*

## Key Discoveries
- [Finding] `[source: X|Reddit|Web]`

## From X/Twitter
**Top Voices**: @user1, @user2
**Key Posts**: [table]
**Trending Angles**: [list]
**Sentiment**: Positive|Negative|Mixed

## From Reddit
**Active Communities**: r/sub1, r/sub2
**Top Discussions**: [list]
**Community Consensus**: [list]
**Contrarian Views**: [list]

## From Web
**Recent Articles**: [list]
**Expert Opinions**: [list]
**Emerging Trends**: [list]

## Actionable Takeaways
1. [Recommendation]

## Audit Trail

### X/Twitter Sources
| Insight | Author | Post URL | Engagement |
|---------|--------|----------|------------|

### Reddit Sources
| Insight | Subreddit | Thread | URL | Upvotes |
|---------|-----------|--------|-----|---------|

### Web Sources
| Insight | Publication | Article | URL | Date |
|---------|-------------|---------|-----|------|
```

---

## Error Codes

### Script Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `XAI_API_KEY not set` | Missing environment variable | Set XAI_API_KEY in .env |
| `OPENAI_API_KEY not set` | Missing environment variable | Set OPENAI_API_KEY in .env |
| `No topic provided` | Script called without arguments | Provide a topic |
| `xai-sdk package not installed` | Missing dependency | pip install xai-sdk |
| `openai package not installed` | Missing dependency | pip install openai |

### API Errors

#### xAI API Errors

| Error | Code | Cause | Solution |
|-------|------|-------|----------|
| `PERMISSION_DENIED: no credits` | 403 | No xAI credits | Add credits at console.x.ai |
| `Rate limit exceeded` | 429 | Too many requests | Wait and retry |
| `Invalid API key` | 401 | Bad API key | Check/regenerate key |
| `Live search is deprecated` | 410 | Old API format | Update to latest code |

#### OpenAI API Errors

| Error | Code | Cause | Solution |
|-------|------|-------|----------|
| `Incorrect API key` | 401 | Bad API key | Check/regenerate key |
| `Rate limit reached` | 429 | Too many requests | Wait and retry |
| `Insufficient quota` | 402 | No credits | Add credits at platform.openai.com |

---

## External APIs

### xAI API (Grok)

**Base URL:** `https://api.x.ai` (via xai-sdk)

**Authentication:** Bearer token via `XAI_API_KEY`

**Endpoint Used:** Responses API

**Tool:** `x_search`

**Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| from_date | datetime | Start of search range |
| to_date | datetime | End of search range |

**Response Includes:**
- Generated content
- Inline citations with URLs

**Documentation:** https://docs.x.ai

**Rate Limits:** See https://console.x.ai/team/[your-team-id]

**Pricing:** Pay-as-you-go, see https://x.ai/api#pricing

### OpenAI API

**Base URL:** `https://api.openai.com/v1`

**Authentication:** Bearer token via `OPENAI_API_KEY`

**Endpoint Used:** `POST /chat/completions`

**Model:** `gpt-4o-2024-08-06`

**Request Format:**

```json
{
  "model": "gpt-4o-2024-08-06",
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
  ]
}
```

**Response Includes:**
- Generated content
- Usage statistics (tokens)

**Documentation:** https://platform.openai.com/docs/api-reference

**Rate Limits:** Varies by tier, see https://platform.openai.com/account/limits

**Pricing:** https://openai.com/pricing

---

## Environment Variables

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `XAI_API_KEY` | xAI API key for X/Twitter search | `xai-abc123...` |
| `OPENAI_API_KEY` | OpenAI API key for Reddit analysis | `sk-abc123...` |

### Setting Variables

#### Using .env file (Recommended)

Create `.env` in project root:

```
XAI_API_KEY=your_xai_key_here
OPENAI_API_KEY=your_openai_key_here
```

The scripts load this file using `python-dotenv`.

#### Using System Environment

**Mac/Linux (temporary):**
```bash
export XAI_API_KEY=your_key_here
export OPENAI_API_KEY=your_key_here
```

**Mac/Linux (permanent):**
Add to `~/.bashrc` or `~/.zshrc`:
```bash
export XAI_API_KEY=your_key_here
export OPENAI_API_KEY=your_key_here
```

**Windows (temporary, PowerShell):**
```powershell
$env:XAI_API_KEY="your_key_here"
$env:OPENAI_API_KEY="your_key_here"
```

**Windows (permanent):**
1. Search for "Environment Variables" in Start menu
2. Click "Environment Variables"
3. Add new user variables

### Variable Validation

Scripts validate variables at startup:

```python
api_key = os.getenv("XAI_API_KEY")
if not api_key:
    return {
        "error": "XAI_API_KEY not set",
        "fix": "Set XAI_API_KEY environment variable or add to .env file"
    }
```

---

## Skill Definition Reference

### Frontmatter

```yaml
---
name: last-30-days
description: Research any topic from the last 30 days...
allowed-tools:
  - Bash
  - WebSearch
  - Read
  - Write
---
```

| Field | Type | Description |
|-------|------|-------------|
| name | string | Skill identifier (used in /command) |
| description | string | Human-readable description |
| allowed-tools | list | Tools the skill can use |

### Variable Substitution

| Variable | Description | Example |
|----------|-------------|---------|
| `$ARGUMENTS` | User's input after skill name | `/last-30-days AI` → `$ARGUMENTS = "AI"` |

### Workflow Phases

| Phase | Purpose | Tools Used |
|-------|---------|------------|
| Phase 1 | Parallel data collection | Bash (scripts), WebSearch |
| Phase 2 | Synthesis and analysis | (Claude's reasoning) |
| Phase 3 | Format presentation | (Template application) |
| Phase 4 | Save to file | Write |

---

## Version Information

| Component | Version | Notes |
|-----------|---------|-------|
| Python | 3.10+ | Required |
| xai-sdk | ≥1.3.1 | For Agent Tools API |
| openai | ≥1.0.0 | For Chat Completions |
| python-dotenv | ≥1.0.0 | For .env loading |
| xAI Model | grok-4-1-fast | Recommended for agent tools |
| OpenAI Model | gpt-4o-2024-08-06 | Current GPT-4 variant |
