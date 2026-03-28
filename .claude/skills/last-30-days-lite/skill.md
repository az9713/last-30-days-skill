---
name: last-30-days-lite
description: Research any topic from the last 30 days using web search only. No API keys required. Great for quick research and demos.
allowed-tools:
  - WebSearch
  - WebFetch
  - Read
  - Write
---

# Last 30 Days Lite - Web-Only Research Skill

Research any topic using only the built-in WebSearch tool. **No API keys required.**

This is a lightweight version of the full `/last-30-days` skill that demonstrates the core research workflow using only free, built-in tools.

## Usage

```
/last-30-days-lite <topic>
```

## Arguments

- `$ARGUMENTS`: The topic to research (e.g., "AI coding assistants", "remote work trends", "electric vehicles")

## Workflow

### Phase 1: Multi-Angle Web Research

Run **5 targeted web searches** to cover different angles of the topic. Execute all searches simultaneously:

1. **News & Recent Developments**:
   Use WebSearch: `$ARGUMENTS latest news 2026`

2. **Expert Opinions & Analysis**:
   Use WebSearch: `$ARGUMENTS expert analysis trends`

3. **Community Discussions (Reddit/Forums)**:
   Use WebSearch: `$ARGUMENTS site:reddit.com OR site:news.ycombinator.com`

4. **Social Media Buzz (X/Twitter)**:
   Use WebSearch: `$ARGUMENTS site:x.com OR site:twitter.com`

5. **Practical Guides & How-Tos**:
   Use WebSearch: `$ARGUMENTS best practices guide 2026`

After the searches, use WebFetch on the **3-5 most promising URLs** from the results to get deeper content and details.

### Phase 2: Synthesis

After gathering results from all searches:

1. **Identify Key Patterns**: Look for recurring themes, frameworks, and strategies
2. **Extract Actionable Insights**: Distill findings into practical knowledge
3. **Note Top Sources**: Highlight influential voices and publications
4. **Summarize Trends**: Identify what's currently working and what's emerging
5. **Track Source Attribution**: For every insight, note which search found it

### Phase 3: Present Findings

Structure the output as:

```
## Research Summary: [Topic]
*Researched on [date] | Source: Web Search (no API keys required)*

### Key Discoveries
- [Finding 1] `[source: Web]`
- [Finding 2] `[source: Web]`
- [Finding 3] `[source: Web]`

### Recent News & Developments
- [Latest headlines and announcements]
- [Industry movements]

### Expert Analysis
- [Thought leader perspectives]
- [Industry reports and data]

### Community Sentiment
- [Reddit/HN discussions and opinions]
- [Common praise and complaints]
- [Emerging consensus]

### Practical Takeaways
1. [Specific recommendation with source]
2. [Strategy to apply]
3. [Tool or framework to try]

### Sources
- [Source Title](URL)
- [Source Title](URL)

---

## Audit Trail

### Web Sources
| Insight | Publication | Article Title | URL | Date |
|---------|-------------|---------------|-----|------|
| [Finding] | [site] | [title] | [link] | YYYY-MM-DD |
```

### Phase 4: Save Results

1. **Generate filename**: Use the topic to create a descriptive filename (e.g., `ai-coding-assistants-lite-research-2026.md`)
2. **Add metadata**: Include the research date and "Lite (web-only)" label at the top
3. **Include full audit trail**: The saved file MUST include complete source tables
4. **Save location**: Save to `output/` in the project root directory
5. **Confirm to user**: Let the user know where the file was saved

## Example Topics to Try

- `AI coding assistants` - Compare tools like Cursor, Copilot, Claude Code
- `remote work trends` - Latest policies, tools, and debates
- `electric vehicles` - New models, charging infrastructure, market shifts
- `startup funding` - VC trends, notable raises, emerging sectors
- `cybersecurity threats` - Recent breaches, new attack vectors, defenses
- `programming languages 2026` - Popularity shifts, new features, community growth
