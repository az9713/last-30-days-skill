# Last 30 Days Research Skill

## Project Overview

This is a Claude Code skill that researches any topic using real-time data from X/Twitter, Reddit, and web sources. It synthesizes findings into actionable insights with full source attribution.

## Quick Reference

```bash
# Research any topic
/last-30-days <topic>

# Examples
/last-30-days AI coding assistants
/last-30-days remote work trends
/last-30-days electric vehicles
```

## Project Structure

```
.claude/skills/last-30-days/    # Skill definition and scripts
output/                          # Research results (markdown files)
docs/                            # Documentation
```

## Key Files

- `.claude/skills/last-30-days/skill.md` - Skill workflow definition
- `.claude/skills/last-30-days/scripts/search_x.py` - X/Twitter search (uses xai-sdk)
- `.claude/skills/last-30-days/scripts/search_reddit.py` - Reddit search (uses OpenAI)
- `output/` - Saved research results with audit trails

## Environment Variables Required

```
XAI_API_KEY=     # For X/Twitter search via xAI Grok API
OPENAI_API_KEY=  # For Reddit search via OpenAI API
```

## How the Skill Works

1. **Phase 1**: Parallel search across X/Twitter, Reddit, and web (run simultaneously)
2. **Phase 2**: Synthesize findings, identify patterns, track source attribution
3. **Phase 3**: Present structured findings with audit trail
4. **Phase 4**: Save results to `output/` directory

## Output Format

Research results include:
- Key discoveries with source tags `[source: X|Reddit|Web]`
- Sections for each source (X/Twitter, Reddit, Web)
- Actionable takeaways
- Audit trail tables linking insights to original sources

## Technical Notes

### X/Twitter Search
- Uses native `xai-sdk` package with Agent Tools API
- Model: `grok-4-1-fast`
- Tool: `x_search()` with date range filtering
- Requires xAI account with credits

### Reddit Search
- Uses OpenAI API with GPT-4
- Synthesizes Reddit discussions and sentiment
- Returns structured analysis

### Common Issues

1. **X search fails with "no credits"**: Add credits at https://console.x.ai
2. **Missing dependencies**: Run `pip install -r .claude/skills/last-30-days/scripts/requirements.txt`
3. **API key not found**: Ensure `.env` file exists with valid keys

## Code Style

- Python scripts use type hints
- JSON output for machine readability
- Error handling returns structured error objects
- Scripts are standalone and can be run directly

## Testing

```bash
# Test X/Twitter search
python .claude/skills/last-30-days/scripts/search_x.py "test topic"

# Test Reddit search
python .claude/skills/last-30-days/scripts/search_reddit.py "test topic"
```

## Documentation

See `docs/` folder for comprehensive documentation:
- `QUICK_START.md` - Get started in 5 minutes
- `USER_GUIDE.md` - Complete user documentation
- `DEVELOPER_GUIDE.md` - Technical documentation
- `ARCHITECTURE.md` - System design
- `TROUBLESHOOTING.md` - Common issues and solutions
