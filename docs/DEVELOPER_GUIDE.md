# Developer Guide

Technical documentation for developers who want to understand, modify, or extend the Last 30 Days Research Skill.

## Table of Contents

1. [Development Environment Setup](#development-environment-setup)
2. [Project Architecture](#project-architecture)
3. [Code Walkthrough](#code-walkthrough)
4. [How Claude Code Skills Work](#how-claude-code-skills-work)
5. [Modifying the Skill](#modifying-the-skill)
6. [Adding New Data Sources](#adding-new-data-sources)
7. [Testing](#testing)
8. [Debugging](#debugging)
9. [API Reference](#api-reference)
10. [Contributing Guidelines](#contributing-guidelines)

---

## Development Environment Setup

### Prerequisites

Before you begin development, ensure you have:

| Requirement | Version | Check Command |
|-------------|---------|---------------|
| Python | 3.10+ | `python --version` |
| pip | Latest | `pip --version` |
| Git | Any | `git --version` |
| Claude Code | Latest | `claude --version` |

### Step-by-Step Setup

#### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/last-30-days.git
cd last-30-days
```

#### Step 2: Create a Virtual Environment (Recommended)

A virtual environment keeps project dependencies isolated from your system Python.

**On Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate
```

You'll see `(venv)` in your terminal prompt when activated.

#### Step 3: Install Dependencies

```bash
pip install -r .claude/skills/last-30-days/scripts/requirements.txt
```

**What gets installed:**

| Package | Version | Purpose |
|---------|---------|---------|
| xai-sdk | ≥1.3.1 | X/Twitter search via xAI API |
| openai | ≥1.0.0 | Reddit search via OpenAI API |
| python-dotenv | ≥1.0.0 | Load environment variables from .env |
| requests | ≥2.31.0 | HTTP requests (utility) |

#### Step 4: Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Edit with your keys
nano .env  # or use any text editor
```

Add your API keys:
```
XAI_API_KEY=your_xai_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

#### Step 5: Verify Setup

Test each script individually:

```bash
# Test X/Twitter search
python .claude/skills/last-30-days/scripts/search_x.py "test topic"

# Test Reddit search
python .claude/skills/last-30-days/scripts/search_reddit.py "test topic"
```

Expected output: JSON with search results or a descriptive error message.

---

## Project Architecture

### Directory Structure

```
last-30-days/
│
├── .claude/                          # Claude Code configuration
│   ├── settings.json                 # Claude Code settings
│   └── skills/                       # Skills directory
│       └── last-30-days/             # This skill
│           ├── skill.md              # Skill definition (THE MAIN FILE)
│           └── scripts/              # Python scripts
│               ├── search_x.py       # X/Twitter search
│               ├── search_reddit.py  # Reddit search
│               ├── requirements.txt  # Python dependencies
│               └── README.md         # Scripts documentation
│
├── output/                           # Research output files
│   └── *.md                          # Generated research reports
│
├── docs/                             # Documentation
│   ├── QUICK_START.md
│   ├── USER_GUIDE.md
│   ├── DEVELOPER_GUIDE.md            # This file
│   ├── ARCHITECTURE.md
│   ├── TROUBLESHOOTING.md
│   └── API_REFERENCE.md
│
├── .env                              # API keys (git-ignored)
├── .env.example                      # Example environment file
├── .gitignore                        # Git ignore rules
├── CLAUDE.md                         # Claude Code project context
├── CONTRIBUTING.md                   # Contribution guidelines
└── README.md                         # Project overview
```

### Component Relationships

```
┌─────────────────────────────────────────────────────────────────┐
│                         Claude Code CLI                          │
│                    (Interprets user commands)                    │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                          skill.md                                │
│              (Defines workflow and output format)                │
└─────────────────────────────────────────────────────────────────┘
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
        ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
        │ search_x.py │ │search_reddit│ │ WebSearch   │
        │             │ │    .py      │ │   Tool      │
        │  (xai-sdk)  │ │  (openai)   │ │  (built-in) │
        └─────────────┘ └─────────────┘ └─────────────┘
                │               │               │
                ▼               ▼               ▼
        ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
        │   xAI API   │ │ OpenAI API  │ │  Web APIs   │
        │   (Grok)    │ │   (GPT-4)   │ │             │
        └─────────────┘ └─────────────┘ └─────────────┘
                │               │               │
                └───────────────┼───────────────┘
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                        Claude Code                               │
│              (Synthesizes results, generates report)             │
└─────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────┐
│                      output/*.md                                 │
│                   (Saved research files)                         │
└─────────────────────────────────────────────────────────────────┘
```

---

## Code Walkthrough

### skill.md - The Skill Definition

Location: `.claude/skills/last-30-days/skill.md`

This file defines:
1. **Metadata** (name, description, allowed tools)
2. **Workflow** (phases 1-4)
3. **Output format** (template for reports)
4. **Troubleshooting** (common errors and solutions)

**Key sections:**

```markdown
---
name: last-30-days
description: Research any topic...
allowed-tools:
  - Bash
  - WebSearch
  - Read
  - Write
---

# Workflow sections follow...
```

The `allowed-tools` section specifies which Claude Code tools this skill can use.

### search_x.py - X/Twitter Search

Location: `.claude/skills/last-30-days/scripts/search_x.py`

**Purpose:** Search X/Twitter for recent posts about a topic.

**Key imports:**
```python
from xai_sdk import Client
from xai_sdk.chat import user
from xai_sdk.tools import x_search
```

**Main function:**
```python
def search_x(topic: str) -> dict:
    """
    Search X/Twitter for recent content on a topic.

    Args:
        topic: The topic to search for

    Returns:
        Dictionary with search results or error
    """
```

**How it works:**

1. Load API key from environment
2. Calculate date range (last 30 days)
3. Create xAI client
4. Create chat with x_search tool
5. Send search prompt
6. Return structured results

**Output format:**
```json
{
  "source": "X/Twitter via XAI Grok",
  "topic": "your topic",
  "date_range": "2026-01-05 to 2026-02-04",
  "content": "...",
  "model": "grok-4-1-fast",
  "citations": [...]
}
```

### search_reddit.py - Reddit Search

Location: `.claude/skills/last-30-days/scripts/search_reddit.py`

**Purpose:** Analyze Reddit discussions about a topic.

**Key imports:**
```python
from openai import OpenAI
```

**How it works:**

1. Load API key from environment
2. Create OpenAI client
3. Send prompt asking for Reddit analysis
4. Return structured results

**Note:** This doesn't actually scrape Reddit. It uses GPT-4's knowledge to synthesize what Reddit discussions typically contain about a topic. This is a limitation but provides useful general insights.

**Output format:**
```json
{
  "source": "Reddit via OpenAI",
  "topic": "your topic",
  "date_range": "...",
  "content": "structured analysis...",
  "model": "gpt-4o-2024-08-06",
  "usage": {...}
}
```

---

## How Claude Code Skills Work

### Skill Anatomy

A Claude Code skill is a markdown file with:

1. **Frontmatter** (YAML between `---` markers)
2. **Content** (instructions for Claude)

```markdown
---
name: skill-name
description: What the skill does
allowed-tools:
  - Bash
  - WebSearch
---

# Instructions for Claude

When this skill is invoked, Claude reads these instructions
and follows them step by step.

## Workflow

### Phase 1: Do something
Run this command:
```bash
python script.py "$ARGUMENTS"
```

### Phase 2: Do something else
...
```

### Variable Substitution

`$ARGUMENTS` is replaced with whatever the user types after the skill name:

```
/last-30-days AI trends
```
→ `$ARGUMENTS` becomes `"AI trends"`

### Skill Invocation

When a user types `/skill-name arguments`:

1. Claude Code finds the skill in `.claude/skills/`
2. Loads the skill.md file
3. Substitutes variables
4. Claude follows the instructions
5. Uses allowed tools to complete the task

---

## Modifying the Skill

### Changing the Output Format

Edit `.claude/skills/last-30-days/skill.md`, Phase 3:

```markdown
### Phase 3: Present Findings

Structure the output as:

```
## Research Summary: [Topic]

### Key Discoveries
- [Finding] `[source: X|Reddit|Web]`
...
```
```

### Adding New Sections

Add to the template in skill.md:

```markdown
### New Section Name
- [New data point]
- [Another data point]
```

### Changing the Date Range

Edit `search_x.py` and `search_reddit.py`:

```python
# Current: 30 days
start_date = end_date - timedelta(days=30)

# Change to 7 days:
start_date = end_date - timedelta(days=7)
```

---

## Adding New Data Sources

### Step 1: Create a New Script

Create `.claude/skills/last-30-days/scripts/search_newsource.py`:

```python
#!/usr/bin/env python3
"""
Search [New Source] for topic information.
"""

import os
import sys
import json

def search_newsource(topic: str) -> dict:
    """Search the new source for topic."""

    api_key = os.getenv("NEWSOURCE_API_KEY")

    if not api_key:
        return {"error": "NEWSOURCE_API_KEY not set"}

    # Your search logic here

    return {
        "source": "New Source",
        "topic": topic,
        "content": "..."
    }

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No topic provided"}))
        sys.exit(1)

    topic = " ".join(sys.argv[1:])
    result = search_newsource(topic)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
```

### Step 2: Update requirements.txt

Add any new dependencies:

```
existing-package>=1.0.0
new-package>=2.0.0
```

### Step 3: Update skill.md

Add to Phase 1:

```markdown
4. **New Source Search**:
   ```bash
   python .claude/skills/last-30-days/scripts/search_newsource.py "$ARGUMENTS"
   ```
```

Add to Phase 3 output template:

```markdown
### From New Source
- [Data points from new source]
```

Add to Audit Trail:

```markdown
### New Source
| Insight | Source | URL | Date |
|---------|--------|-----|------|
```

### Step 4: Update Environment

Add to `.env.example`:

```
NEWSOURCE_API_KEY=your_key_here
```

---

## Testing

### Manual Testing

Test each script individually:

```bash
# Activate virtual environment first
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Test X search
python .claude/skills/last-30-days/scripts/search_x.py "test topic"

# Test Reddit search
python .claude/skills/last-30-days/scripts/search_reddit.py "test topic"
```

### Expected Outputs

**Successful X search:**
```json
{
  "source": "X/Twitter via XAI Grok",
  "topic": "test topic",
  "content": "...",
  "model": "grok-4-1-fast"
}
```

**Missing API key:**
```json
{
  "error": "XAI_API_KEY not set",
  "fix": "Set XAI_API_KEY environment variable"
}
```

### Integration Testing

Test the full skill in Claude Code:

```bash
claude
```

Then:
```
/last-30-days test topic
```

Verify:
1. All three sources are searched
2. Output follows expected format
3. File is saved to `output/`
4. Audit trail includes sources

---

## Debugging

### Common Issues

#### 1. Script Not Found

**Error:**
```
python: can't open file 'search_x.py': [Errno 2] No such file or directory
```

**Solution:** Ensure you're in the project root directory:
```bash
cd /path/to/last-30-days
```

#### 2. Module Not Found

**Error:**
```
ModuleNotFoundError: No module named 'xai_sdk'
```

**Solution:** Install dependencies:
```bash
pip install -r .claude/skills/last-30-days/scripts/requirements.txt
```

#### 3. API Key Not Found

**Error:**
```json
{"error": "XAI_API_KEY not set"}
```

**Solution:**
1. Check `.env` file exists
2. Check key is correct (no quotes)
3. Restart terminal to reload environment

#### 4. API Errors

**Error:**
```
PERMISSION_DENIED: Your team doesn't have any credits
```

**Solution:** Add credits at https://console.x.ai

### Debug Mode

Add debug output to scripts:

```python
import sys

# Add at the start of your function
print(f"DEBUG: topic = {topic}", file=sys.stderr)
print(f"DEBUG: api_key exists = {bool(api_key)}", file=sys.stderr)
```

Stderr output won't affect the JSON output parsed by Claude.

### Logging

For more extensive debugging, add logging:

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='debug.log'
)

logging.debug(f"Searching for topic: {topic}")
```

---

## API Reference

See [API_REFERENCE.md](API_REFERENCE.md) for detailed documentation of:
- Script functions
- Input/output formats
- Error codes
- API rate limits

---

## Contributing Guidelines

### Code Style

- Use Python type hints
- Follow PEP 8 style guide
- Add docstrings to all functions
- Handle errors gracefully with structured JSON

### Git Workflow

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-feature`
3. Make changes
4. Test thoroughly
5. Commit with clear messages
6. Push and create pull request

### Commit Message Format

```
type: short description

Longer description if needed.

- Bullet points for multiple changes
- Another change
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`

### Pull Request Checklist

- [ ] Code follows style guide
- [ ] All tests pass
- [ ] Documentation updated
- [ ] No sensitive data in commits
- [ ] Changelog updated if applicable

---

## Next Steps

- **Architecture details**: See [ARCHITECTURE.md](ARCHITECTURE.md)
- **Troubleshooting**: See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **API details**: See [API_REFERENCE.md](API_REFERENCE.md)
