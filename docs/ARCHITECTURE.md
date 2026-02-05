# System Architecture

Technical architecture of the Last 30 Days Research Skill.

## Table of Contents

1. [System Overview](#system-overview)
2. [Component Details](#component-details)
3. [Data Flow](#data-flow)
4. [API Integrations](#api-integrations)
5. [File System Structure](#file-system-structure)
6. [Security Considerations](#security-considerations)
7. [Performance Characteristics](#performance-characteristics)
8. [Extensibility](#extensibility)

---

## System Overview

### High-Level Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                              USER                                     │
│                     Types: /last-30-days <topic>                     │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        CLAUDE CODE CLI                                │
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │                      Skill Loader                                │ │
│  │  • Detects /last-30-days command                                │ │
│  │  • Loads .claude/skills/last-30-days/skill.md                   │ │
│  │  • Substitutes $ARGUMENTS with user input                       │ │
│  └─────────────────────────────────────────────────────────────────┘ │
│                                    │                                  │
│                                    ▼                                  │
│  ┌─────────────────────────────────────────────────────────────────┐ │
│  │                    Claude AI (Opus/Sonnet)                       │ │
│  │  • Interprets skill instructions                                │ │
│  │  • Orchestrates tool calls                                      │ │
│  │  • Synthesizes results                                          │ │
│  │  • Generates output                                             │ │
│  └─────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ▼               ▼               ▼
            ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
            │    Bash     │ │  WebSearch  │ │    Write    │
            │    Tool     │ │    Tool     │ │    Tool     │
            └─────────────┘ └─────────────┘ └─────────────┘
                    │               │               │
                    ▼               │               ▼
            ┌─────────────┐         │       ┌─────────────┐
            │   Python    │         │       │  output/    │
            │   Scripts   │         │       │   *.md      │
            └─────────────┘         │       └─────────────┘
                    │               │
        ┌───────────┴───────────┐   │
        ▼                       ▼   ▼
┌─────────────┐         ┌─────────────┐
│   xAI API   │         │   Web APIs  │
│   (Grok)    │         │             │
└─────────────┘         └─────────────┘
        │                       │
        ▼                       ▼
┌─────────────┐         ┌─────────────┐
│  X/Twitter  │         │  Web Pages  │
│    Data     │         │             │
└─────────────┘         └─────────────┘
```

### Design Principles

1. **Parallel Execution**: All three data sources are searched simultaneously
2. **Graceful Degradation**: If one source fails, others continue
3. **Source Attribution**: Every insight is traceable to its origin
4. **Structured Output**: Consistent format for all research reports
5. **Local Storage**: Results saved locally, no cloud dependencies

---

## Component Details

### 1. Skill Definition (skill.md)

**Location:** `.claude/skills/last-30-days/skill.md`

**Responsibility:**
- Define the skill's metadata (name, description, tools)
- Specify the workflow (4 phases)
- Define output format template
- Provide troubleshooting guidance

**Format:** Markdown with YAML frontmatter

```yaml
---
name: last-30-days
description: Research any topic...
allowed-tools:
  - Bash      # Run Python scripts
  - WebSearch # Search the web
  - Read      # Read files
  - Write     # Write output files
---
```

### 2. X/Twitter Search Script (search_x.py)

**Location:** `.claude/skills/last-30-days/scripts/search_x.py`

**Responsibility:**
- Connect to xAI API
- Search X/Twitter for recent posts
- Return structured JSON results

**Technology Stack:**
- Python 3.10+
- xai-sdk (native xAI Python SDK)
- python-dotenv (environment loading)

**API Used:** xAI Responses API with `x_search` agent tool

**Input:** Topic string (command line argument)

**Output:** JSON object with:
```json
{
  "source": "X/Twitter via XAI Grok",
  "topic": "string",
  "date_range": "YYYY-MM-DD to YYYY-MM-DD",
  "content": "string (structured findings)",
  "model": "grok-4-1-fast",
  "citations": [
    {
      "id": "string",
      "url": "string",
      "handle": "string"
    }
  ]
}
```

### 3. Reddit Search Script (search_reddit.py)

**Location:** `.claude/skills/last-30-days/scripts/search_reddit.py`

**Responsibility:**
- Connect to OpenAI API
- Generate Reddit discussion analysis
- Return structured JSON results

**Technology Stack:**
- Python 3.10+
- openai (OpenAI Python SDK)
- python-dotenv

**API Used:** OpenAI Chat Completions API (GPT-4)

**Note:** This script doesn't scrape Reddit directly. It uses GPT-4's knowledge to synthesize typical Reddit discussions about the topic.

**Input:** Topic string (command line argument)

**Output:** JSON object with:
```json
{
  "source": "Reddit via OpenAI",
  "topic": "string",
  "date_range": "YYYY-MM-DD to YYYY-MM-DD",
  "content": "string (structured analysis)",
  "model": "gpt-4o-2024-08-06",
  "usage": {
    "prompt_tokens": 123,
    "completion_tokens": 456
  }
}
```

### 4. Web Search (Built-in Tool)

**Responsibility:**
- Search the web for recent articles
- Retrieve current information
- Support Claude's analysis

**Technology:** Claude Code's built-in WebSearch tool

**No code required** - invoked directly by Claude during skill execution.

### 5. Output Writer (Built-in Tool)

**Responsibility:**
- Save research reports to disk
- Create markdown files in output/

**Technology:** Claude Code's built-in Write tool

---

## Data Flow

### Phase 1: Parallel Search

```
User Input: /last-30-days "AI trends"
                    │
                    ▼
            ┌───────────────┐
            │ Skill Loader  │
            │ $ARGUMENTS =  │
            │ "AI trends"   │
            └───────────────┘
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
┌─────────┐   ┌─────────┐   ┌─────────┐
│ Bash:   │   │ Bash:   │   │WebSearch│
│search_x │   │search_  │   │  tool   │
│  .py    │   │reddit.py│   │         │
└─────────┘   └─────────┘   └─────────┘
    │               │               │
    ▼               ▼               ▼
┌─────────┐   ┌─────────┐   ┌─────────┐
│  JSON   │   │  JSON   │   │ Search  │
│ result  │   │ result  │   │ results │
└─────────┘   └─────────┘   └─────────┘
```

### Phase 2: Synthesis

```
┌─────────────────────────────────────────────────────┐
│                   Claude AI                          │
│                                                      │
│  Inputs:                                             │
│  • X/Twitter JSON                                    │
│  • Reddit JSON                                       │
│  • Web search results                                │
│                                                      │
│  Processing:                                         │
│  • Identify patterns across sources                  │
│  • Extract actionable insights                       │
│  • Track source attribution                          │
│  • Summarize trends                                  │
│                                                      │
│  Output:                                             │
│  • Synthesized findings                              │
│  • Source tags for each insight                      │
└─────────────────────────────────────────────────────┘
```

### Phase 3: Present

```
┌─────────────────────────────────────────────────────┐
│              Structured Report                       │
│                                                      │
│  ## Research Summary: AI trends                      │
│                                                      │
│  ### Key Discoveries                                 │
│  - Finding 1 [source: X]                            │
│  - Finding 2 [source: Reddit]                       │
│                                                      │
│  ### From X/Twitter                                  │
│  ...                                                 │
│                                                      │
│  ### Audit Trail                                     │
│  | Insight | Source | URL |                         │
│  |---------|--------|-----|                         │
└─────────────────────────────────────────────────────┘
```

### Phase 4: Save

```
┌─────────────────────────────────────────────────────┐
│                   Write Tool                         │
│                                                      │
│  Input: Markdown content                             │
│  Output: output/ai-trends-research-2026.md          │
└─────────────────────────────────────────────────────┘
```

---

## API Integrations

### xAI API (Grok)

**Endpoint:** `https://api.x.ai/v1` (via xai-sdk)

**Authentication:** API key in `XAI_API_KEY` environment variable

**API Type:** Responses API with Agent Tools

**Tool Used:** `x_search`

**Capabilities:**
- Search X/Twitter posts by keyword
- Filter by date range
- Get engagement metrics
- Return citations

**Rate Limits:** Check https://console.x.ai for current limits

**Pricing:** Pay-as-you-go, requires credits

### OpenAI API

**Endpoint:** `https://api.openai.com/v1`

**Authentication:** API key in `OPENAI_API_KEY` environment variable

**API Type:** Chat Completions

**Model:** `gpt-4o-2024-08-06`

**Capabilities:**
- Generate structured analysis
- Synthesize typical Reddit discussions
- Return formatted content

**Rate Limits:** Varies by tier (check OpenAI dashboard)

**Pricing:** Pay-per-token

---

## File System Structure

### Input Files

```
.env                    # API keys (required, git-ignored)
.env.example           # Template for .env
```

### Configuration Files

```
.claude/
├── settings.json                      # Claude Code settings
└── skills/
    └── last-30-days/
        ├── skill.md                   # Skill definition
        └── scripts/
            ├── search_x.py            # X search script
            ├── search_reddit.py       # Reddit search script
            ├── requirements.txt       # Python dependencies
            └── README.md              # Script documentation
```

### Output Files

```
output/
├── ai-coding-assistants-research-2026.md
├── generative-ai-infrastructure-research-2026.md
└── [topic]-research-[year].md
```

### Documentation

```
docs/
├── QUICK_START.md
├── USER_GUIDE.md
├── DEVELOPER_GUIDE.md
├── ARCHITECTURE.md        # This file
├── TROUBLESHOOTING.md
└── API_REFERENCE.md
```

---

## Security Considerations

### API Key Protection

1. **Storage:** Keys stored in `.env` file, never committed to git
2. **Git Ignore:** `.env` is in `.gitignore`
3. **Example File:** `.env.example` provides template without real keys

### Data Privacy

1. **Local Processing:** Research results stored locally only
2. **No Telemetry:** Skill doesn't send data to third parties (except API calls)
3. **User Control:** Users control what topics are researched

### API Security

1. **HTTPS:** All API calls use HTTPS
2. **Key Rotation:** Users should rotate API keys periodically
3. **Minimal Permissions:** APIs only have permissions needed for search

---

## Performance Characteristics

### Timing

| Phase | Typical Duration | Notes |
|-------|-----------------|-------|
| X/Twitter Search | 5-15 seconds | Depends on API response |
| Reddit Search | 3-8 seconds | Depends on GPT-4 load |
| Web Search | 2-5 seconds | Depends on result count |
| Synthesis | 5-10 seconds | Depends on data volume |
| **Total** | **30-60 seconds** | Parallel execution helps |

### Resource Usage

| Resource | Usage | Notes |
|----------|-------|-------|
| CPU | Low | Python scripts are I/O bound |
| Memory | ~100MB | Python interpreter + libraries |
| Network | Moderate | API calls + web search |
| Disk | Minimal | Only output files |

### API Costs

| API | Approximate Cost | Notes |
|-----|-----------------|-------|
| xAI | $0.01-0.05/query | Depends on response length |
| OpenAI | $0.02-0.10/query | GPT-4 pricing |
| **Total** | **$0.03-0.15/research** | Varies by topic complexity |

---

## Extensibility

### Adding New Data Sources

See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md#adding-new-data-sources)

1. Create new Python script in `scripts/`
2. Update `requirements.txt`
3. Add to skill.md Phase 1
4. Update output format in Phase 3
5. Add to audit trail template

### Modifying Output Format

Edit `.claude/skills/last-30-days/skill.md` Phase 3 template.

### Changing Date Range

Edit both Python scripts:
```python
start_date = end_date - timedelta(days=NEW_VALUE)
```

### Custom Filters

Modify scripts to add filtering:
- By language
- By region
- By engagement threshold
- By specific accounts/subreddits

---

## Future Considerations

### Potential Enhancements

1. **Real Reddit API:** Use Reddit's official API for actual data
2. **Caching:** Cache results to reduce API costs
3. **Scheduling:** Automated periodic research
4. **Multiple Languages:** Support non-English research
5. **Custom Prompts:** User-configurable analysis prompts

### Known Limitations

1. Reddit search uses GPT synthesis, not actual API
2. Web search limited by Claude's tool capabilities
3. X search requires paid xAI credits
4. 30-day window is hardcoded
