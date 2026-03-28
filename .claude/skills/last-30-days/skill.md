---
name: last-30-days
description: Research any topic from the last 30 days using X, Reddit, and web sources. Use when you need current trends, recent discussions, or up-to-date information on any subject.
allowed-tools:
  - WebSearch
  - WebFetch
  - Read
  - Write
---

# Last 30 Days Research Skill

Research any topic using recent data from X/Twitter, Reddit, and web sources. This skill discovers current best practices, frameworks, and techniques through live research.

## Usage

```
/last-30-days <topic>
```

## Arguments

- `$ARGUMENTS`: The topic to research (e.g., "cold email frameworks", "AI coding assistants", "growth hacking strategies")

## Workflow

### Phase 1: Parallel Research

Run all three searches simultaneously to gather comprehensive data:

1. **X/Twitter Search** (via WebSearch):
   Use WebSearch: `$ARGUMENTS site:x.com OR site:twitter.com`

2. **Reddit Search** (via WebSearch):
   Use WebSearch: `$ARGUMENTS site:reddit.com`

3. **Web Search** (via WebSearch tool):
   Use the WebSearch tool to find recent articles, blog posts, and discussions about the topic.

After the searches, use WebFetch on the **3-5 most promising URLs** from the results to get deeper content and details.

### Phase 2: Synthesis

After gathering results from all three sources:

1. **Identify Key Patterns**: Look for recurring themes, frameworks, and strategies mentioned across sources
2. **Extract Actionable Insights**: Distill findings into practical, applicable knowledge
3. **Note Top Sources**: Highlight influential accounts, subreddits, and websites
4. **Summarize Trends**: Identify what's currently working and what's emerging
5. **Track Source Attribution**: For every insight, note which source it came from (X, Reddit, or Web) for the audit trail

### Phase 3: Present Findings

Structure the output as:

```
## Research Summary: [Topic]

### Key Discoveries
- [Framework/technique 1] `[source: X|Reddit|Web]`
- [Framework/technique 2] `[source: X|Reddit|Web]`
- [Trend or insight] `[source: X|Reddit|Web]`

### From X/Twitter
- Top voices: [accounts discussing this]
- Key posts: [notable discussions]
- Engagement patterns: [what resonates]

### From Reddit
- Active subreddits: [relevant communities]
- Top discussions: [popular threads]
- Community sentiment: [overall opinion]

### From Web
- Recent articles: [notable publications]
- Expert opinions: [thought leaders]
- Emerging trends: [what's new]

### Actionable Takeaways
1. [Specific recommendation]
2. [Strategy to apply]
3. [Framework to use]

### Sources
- [Source Title](URL)
- [Source Title](URL)

---

## Audit Trail

### X/Twitter Sources
| Insight | Author/Account | Post URL | Date |
|---------|----------------|----------|------|
| [Finding] | @handle | [link] | YYYY-MM-DD |

### Reddit Sources
| Insight | Subreddit | Thread Title | URL | Upvotes |
|---------|-----------|--------------|-----|---------|
| [Finding] | r/subreddit | [title] | [link] | N |

### Web Sources
| Insight | Publication | Article Title | URL | Date |
|---------|-------------|---------------|-----|------|
| [Finding] | [site] | [title] | [link] | YYYY-MM-DD |
```

**Audit Trail Guidelines:**
- Every key discovery and actionable takeaway should be traceable to at least one source
- Include direct URLs whenever possible so users can verify and explore further
- For X/Twitter: capture the @handle and link to the specific post
- For Reddit: include subreddit, thread title, and upvote count as credibility signal
- For Web: note the publication name, article title, and publication date
- If a source search fails (e.g., API error), note this in the audit trail section

### Phase 4: Save Results

After presenting findings, save the research to a markdown file:

1. **Generate filename**: Use the topic to create a descriptive filename (e.g., `ai-coding-assistants-research-2026.md`)
2. **Add metadata**: Include the research date at the top of the file
3. **Include full audit trail**: The saved file MUST include the complete audit trail tables so users can trace any insight back to its original source
4. **Save location**: Save to `output/` in the project root directory
5. **Confirm to user**: Let the user know where the file was saved

## Follow-up Application

After research is complete, the user can give minimal context and Claude will apply the discovered knowledge:

**Example Flow:**
```
User: /last-30-days highest performing cold email frameworks
[Skill discovers: AIDA, Three Ps, Intention Data Triggers]

User: Write me cold emails for getting on Greg's podcast. I once made a smart oven.
[Claude applies discovered frameworks without user reading research]
```

## Environment Requirements

No API keys or Python dependencies required. This skill uses only built-in Claude Code tools (WebSearch, WebFetch).
