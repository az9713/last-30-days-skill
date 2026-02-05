# User Guide

Complete guide to using the Last 30 Days Research Skill.

## Table of Contents

1. [Overview](#overview)
2. [How It Works](#how-it-works)
3. [Using the Skill](#using-the-skill)
4. [Understanding Results](#understanding-results)
5. [Working with Output Files](#working-with-output-files)
6. [Tips for Better Research](#tips-for-better-research)
7. [Limitations](#limitations)
8. [Frequently Asked Questions](#frequently-asked-questions)

---

## Overview

### What is This Skill?

The Last 30 Days Research Skill is a tool that helps you research any topic by gathering current information from three sources:

1. **X/Twitter**: Real-time posts, trending discussions, influential voices
2. **Reddit**: Community discussions, sentiment, consensus views
3. **Web**: Recent articles, expert opinions, news

### Why Use It?

- **Save time**: Instead of manually searching multiple platforms, get a synthesized report
- **Get current info**: Focuses on the last 30 days, not outdated information
- **Verify sources**: Every insight links back to its original source
- **Structured output**: Information organized for easy understanding

### What Can You Research?

Almost anything! Examples:
- Technology trends
- Product comparisons
- Industry news
- Learning resources
- Current events
- Health topics
- Career advice
- Market trends

---

## How It Works

### The Research Process

When you run `/last-30-days <topic>`, the skill follows this process:

```
┌─────────────────────────────────────────────────────────────┐
│                    Phase 1: Parallel Search                  │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │  X/Twitter  │  │   Reddit    │  │     Web     │         │
│  │   Search    │  │   Search    │  │   Search    │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
│        │                │                │                  │
│        └────────────────┼────────────────┘                  │
│                         ▼                                   │
├─────────────────────────────────────────────────────────────┤
│                    Phase 2: Synthesis                        │
│  • Identify patterns across sources                         │
│  • Extract actionable insights                              │
│  • Track source attribution                                 │
│  • Summarize trends                                         │
├─────────────────────────────────────────────────────────────┤
│                    Phase 3: Present                          │
│  • Structured report with sections                          │
│  • Source tags on each finding                              │
│  • Audit trail with links                                   │
├─────────────────────────────────────────────────────────────┤
│                    Phase 4: Save                             │
│  • Markdown file saved to output/                           │
│  • Research date included                                   │
│  • Full audit trail preserved                               │
└─────────────────────────────────────────────────────────────┘
```

### Time Required

- **Typical research**: 30-60 seconds
- **Complex topics**: Up to 2 minutes
- **If X/Twitter times out**: Research continues with Reddit and Web

### What Happens Behind the Scenes

1. **X/Twitter Search**: Uses xAI's Grok model with the x_search tool to find recent posts, engagement metrics, and influential accounts

2. **Reddit Search**: Uses OpenAI's GPT-4 to analyze Reddit discussions, extract consensus views, and identify contrarian opinions

3. **Web Search**: Uses Claude's built-in web search to find recent articles and expert opinions

---

## Using the Skill

### Basic Command

```
/last-30-days <your topic here>
```

### Examples

```
/last-30-days machine learning frameworks

/last-30-days best project management tools

/last-30-days climate change solutions

/last-30-days startup funding trends
```

### Topic Formatting Tips

| Approach | Example | Quality |
|----------|---------|---------|
| Too vague | `/last-30-days AI` | Poor - too broad |
| Good | `/last-30-days AI coding assistants` | Good - specific |
| Better | `/last-30-days AI coding assistants comparison 2026` | Better - focused |
| Best | `/last-30-days Cursor vs GitHub Copilot developer reviews` | Best - very specific |

### Combining Topics

You can research compound topics:

```
/last-30-days Python vs JavaScript for backend development

/last-30-days remote work tools and productivity tips

/last-30-days electric cars versus hybrid cars 2026
```

---

## Understanding Results

### Report Structure

Every research report follows this structure:

#### 1. Key Discoveries

The most important findings, each tagged with its source:

```markdown
### Key Discoveries

- **The Memory Wall is the Real Bottleneck** `[source: X]`
- **Inference is Overtaking Training** `[source: Web]`
- **74% Prefer Hybrid Cloud** `[source: Reddit]`
```

The source tags tell you where each finding came from:
- `[source: X]` = Found on X/Twitter
- `[source: Reddit]` = Found on Reddit
- `[source: Web]` = Found on the web

#### 2. From X/Twitter

```markdown
### From X/Twitter

**Top Voices**: @user1, @user2, @user3

**Key Posts**:
| Author | Post | Engagement |
|--------|------|------------|
| @user1 | Post summary | 1,234 likes |

**Trending Angles**:
- Angle 1
- Angle 2

**Sentiment**: Positive/Negative/Mixed
```

#### 3. From Reddit

```markdown
### From Reddit

**Active Communities**: r/subreddit1, r/subreddit2

**Top Discussions**:
- "Thread title" (500 upvotes)

**Community Consensus**:
- Point 1
- Point 2

**Contrarian Views**:
- Alternative perspective
```

#### 4. From Web

```markdown
### From Web

**Recent Articles**:
- [Article title](url)

**Expert Opinions**:
- Expert view 1

**Emerging Trends**:
- Trend 1
```

#### 5. Actionable Takeaways

```markdown
### Actionable Takeaways

1. **Do this first** - Explanation
2. **Consider this** - Explanation
3. **Avoid this** - Explanation
```

#### 6. Audit Trail

Tables linking each insight to its source:

```markdown
## Audit Trail

### X/Twitter Sources
| Insight | Author | Post URL | Date |
|---------|--------|----------|------|
| Finding | @user  | [link]() | 2026-01-15 |

### Reddit Sources
| Insight | Subreddit | Thread | URL | Upvotes |
|---------|-----------|--------|-----|---------|
| Finding | r/sub     | Title  | [link]() | 500 |

### Web Sources
| Insight | Publication | Article | URL | Date |
|---------|-------------|---------|-----|------|
| Finding | Site        | Title   | [link]() | 2026-01-20 |
```

---

## Working with Output Files

### Where Are Files Saved?

All research results are saved to the `output/` folder in the project root:

```
last-30-days/
├── output/
│   ├── ai-coding-assistants-research-2026.md
│   ├── generative-ai-infrastructure-research-2026.md
│   └── [your-topic]-research-2026.md
```

### File Naming

Files are named based on your topic:
- Topic: "AI coding assistants"
- Filename: `ai-coding-assistants-research-2026.md`

### File Format

Files are in Markdown format (.md), which means:
- You can open them in any text editor
- They display nicely on GitHub
- You can convert them to PDF, HTML, etc.
- Links are clickable

### Opening Output Files

**In VS Code:**
```bash
code output/ai-coding-assistants-research-2026.md
```

**In any text editor:**
Just double-click the file or use File → Open

**On GitHub:**
Push to a repo and view in browser - Markdown renders automatically

### Sharing Research

You can share output files by:
1. Emailing the .md file
2. Copying content into a document
3. Converting to PDF using a Markdown tool
4. Pushing to GitHub for web viewing

---

## Tips for Better Research

### 1. Be Specific

| Instead of | Try |
|------------|-----|
| "programming" | "Python web development frameworks" |
| "cars" | "electric vehicles charging infrastructure" |
| "AI" | "AI image generation tools comparison" |

### 2. Add Time Context

```
/last-30-days React 19 new features
/last-30-days 2026 tech layoffs
/last-30-days latest GPU releases
```

### 3. Use Comparison Queries

```
/last-30-days Cursor vs GitHub Copilot
/last-30-days AWS vs Azure vs GCP
/last-30-days React vs Vue developer experience
```

### 4. Research Different Angles

For a complete picture, research multiple related topics:

```
# First research
/last-30-days remote work productivity

# Then research related topics
/last-30-days remote work tools
/last-30-days remote work burnout
/last-30-days hybrid work policies
```

### 5. Follow Up on Insights

After getting results, you can ask Claude to dig deeper:

```
User: /last-30-days AI coding assistants

[Results show Cursor is popular]

User: Tell me more about Cursor's Agent Mode feature
```

---

## Limitations

### What This Skill Cannot Do

1. **Real-time updates**: Results are from the search moment, not live
2. **Private content**: Cannot access private accounts or paywalled articles
3. **Historical data**: Focuses on last 30 days, not older content
4. **Guaranteed accuracy**: AI summaries may occasionally misinterpret content
5. **Complete coverage**: Cannot search every post or article

### API Limitations

| API | Limitation | Impact |
|-----|------------|--------|
| XAI (X/Twitter) | Requires credits | Search fails without credits |
| OpenAI (Reddit) | Rate limits | May slow down with heavy use |
| Web Search | Some sites blocked | May miss some sources |

### When Results May Be Limited

- **Very niche topics**: Less content available
- **Non-English topics**: Primarily searches English content
- **Recent events**: May not have enough discussion yet
- **Technical jargon**: May need more specific queries

---

## Frequently Asked Questions

### General Questions

**Q: How current is the data?**

A: The skill searches content from the last 30 days. The exact date range is shown in every report.

**Q: Is this free to use?**

A: The skill itself is free, but you need API credits:
- XAI: Pay-as-you-go pricing
- OpenAI: Pay-as-you-go pricing

**Q: How much does it cost per search?**

A: Typically a few cents per search, depending on:
- Length of results
- Number of API calls
- Current API pricing

**Q: Can I use this for commercial purposes?**

A: Check the API terms of service for XAI and OpenAI. The skill code is MIT licensed.

### Technical Questions

**Q: Why did the X/Twitter search fail?**

A: Common reasons:
1. No credits in your XAI account
2. API key not set correctly
3. Rate limit exceeded

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for solutions.

**Q: Can I search without X/Twitter?**

A: Yes, if X/Twitter search fails, the skill continues with Reddit and Web search. You'll still get useful results.

**Q: How do I update the skill?**

A: Pull the latest code:
```bash
git pull origin main
pip install -r .claude/skills/last-30-days/scripts/requirements.txt
```

### Output Questions

**Q: Where are my research files?**

A: In the `output/` folder in the project root.

**Q: Can I customize the output format?**

A: The output format is defined in `.claude/skills/last-30-days/skill.md`. You can modify it if you understand the skill syntax.

**Q: How do I convert Markdown to PDF?**

A: Options:
- VS Code with Markdown PDF extension
- Online converters like markdowntopdf.com
- Pandoc command-line tool

### Privacy Questions

**Q: Is my data stored anywhere?**

A: Your API keys are stored locally in `.env`. Search results are saved locally in `output/`. Nothing is sent to third parties except the API calls to XAI and OpenAI.

**Q: Are my searches logged?**

A: XAI and OpenAI may log API calls per their privacy policies. The skill itself does not log your searches.

---

## Next Steps

- **Having issues?** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Want to contribute?** See [DEVELOPER_GUIDE.md](DEVELOPER_GUIDE.md)
- **Curious about the architecture?** See [ARCHITECTURE.md](ARCHITECTURE.md)
