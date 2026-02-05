# Claude Code Extensibility Reference

Complete reference for implementing skills, hooks, subagents, MCP servers, and plugins.

---

## Skills

Skills extend Claude's capabilities via `SKILL.md` files with YAML frontmatter + markdown instructions.

### Locations

| Location | Path | Scope |
|----------|------|-------|
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<skill-name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Where plugin is enabled |

### Skill File Structure

```
my-skill/
├── SKILL.md           # Main instructions (required)
├── template.md        # Optional template
├── examples/          # Example outputs
└── scripts/           # Executable scripts
```

### Frontmatter Reference

```yaml
---
name: my-skill                    # Display name (optional, defaults to directory name)
description: What this skill does # Recommended - Claude uses this to decide when to load
argument-hint: [issue-number]     # Hint for autocomplete
disable-model-invocation: true    # Only user can invoke (not Claude)
user-invocable: false             # Only Claude can invoke (hide from menu)
allowed-tools: Read, Grep, Glob   # Tools without permission prompts
model: sonnet                     # Model to use
context: fork                     # Run in forked subagent context
agent: Explore                    # Which subagent to use with context: fork
hooks:                            # Lifecycle hooks scoped to this skill
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./validate.sh"
---

Your skill instructions here...
```

### String Substitutions

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | All arguments passed when invoking |
| `$ARGUMENTS[N]` or `$N` | Specific argument by index (0-based) |
| `${CLAUDE_SESSION_ID}` | Current session ID |

### Dynamic Context Injection

Run shell commands before skill content is sent:

```yaml
---
name: pr-summary
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`

## Your task
Summarize this pull request...
```

### Running Skills in Subagents

Add `context: fork` to run in isolation:

```yaml
---
name: deep-research
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly...
```

---

## Subagents

Specialized AI assistants with their own context, tools, and permissions.

### Built-in Subagents

| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| **Explore** | Haiku | Read-only | Fast codebase exploration |
| **Plan** | Inherit | Read-only | Research during plan mode |
| **general-purpose** | Inherit | All | Complex multi-step tasks |

### Agent File Locations

| Location | Scope | Priority |
|----------|-------|----------|
| `--agents` CLI flag | Current session | 1 (highest) |
| `.claude/agents/` | Current project | 2 |
| `~/.claude/agents/` | All your projects | 3 |
| Plugin's `agents/` | Where plugin enabled | 4 (lowest) |

### Agent Frontmatter

```yaml
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep, Bash       # Allowlist
disallowedTools: Write, Edit        # Denylist
model: sonnet                       # sonnet, opus, haiku, or inherit
permissionMode: default             # default, acceptEdits, dontAsk, bypassPermissions, plan
skills:                             # Preload skills into context
  - api-conventions
  - error-handling-patterns
hooks:                              # Lifecycle hooks
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./validate.sh"
---

You are a code reviewer. Analyze code and provide feedback...
```

### CLI-defined Agents

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer",
    "prompt": "You are a senior code reviewer...",
    "tools": ["Read", "Grep", "Glob"],
    "model": "sonnet"
  }
}'
```

---

## Hooks

Shell commands or LLM prompts that execute at lifecycle events.

### Hook Events

| Event | When it fires | Can block? |
|-------|---------------|------------|
| `SessionStart` | Session begins/resumes | No |
| `UserPromptSubmit` | User submits prompt | Yes |
| `PreToolUse` | Before tool executes | Yes |
| `PermissionRequest` | Permission dialog shown | Yes |
| `PostToolUse` | After tool succeeds | No |
| `PostToolUseFailure` | After tool fails | No |
| `Notification` | Claude sends notification | No |
| `SubagentStart` | Subagent spawned | No |
| `SubagentStop` | Subagent finishes | Yes |
| `Stop` | Claude finishes responding | Yes |
| `PreCompact` | Before context compaction | No |
| `SessionEnd` | Session terminates | No |

### Hook Configuration

In `settings.json` or `.claude/settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "./scripts/lint.sh",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### Hook Types

| Type | Description |
|------|-------------|
| `command` | Run shell command |
| `prompt` | Single-turn LLM evaluation |
| `agent` | Multi-turn agent with tools |

### Hook Input (stdin JSON)

Common fields for all hooks:

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Bash",
  "tool_input": { "command": "npm test" }
}
```

### Exit Codes

| Exit Code | Effect |
|-----------|--------|
| 0 | Success - process JSON output if any |
| 2 | Block/deny (for events that support blocking) |
| Other | Non-blocking error, continue |

### PreToolUse Decision Control

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",       // allow, deny, or ask
    "permissionDecisionReason": "...",
    "updatedInput": { "command": "..." },
    "additionalContext": "..."
  }
}
```

### Async Hooks

```json
{
  "type": "command",
  "command": "./run-tests.sh",
  "async": true,
  "timeout": 120
}
```

---

## MCP (Model Context Protocol)

Connect Claude to external tools and data sources.

### Adding MCP Servers

```bash
# HTTP server
claude mcp add --transport http notion https://mcp.notion.com/mcp

# SSE server (deprecated, prefer HTTP)
claude mcp add --transport sse asana https://mcp.asana.com/sse

# Local stdio server
claude mcp add --transport stdio airtable \
  --env AIRTABLE_API_KEY=YOUR_KEY \
  -- npx -y airtable-mcp-server
```

### MCP Scopes

| Scope | Location | Shared |
|-------|----------|--------|
| `local` | `~/.claude.json` (per-project) | No |
| `project` | `.mcp.json` | Yes (git) |
| `user` | `~/.claude.json` | No |

### .mcp.json Format

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    },
    "local-db": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "postgresql://..."],
      "env": {
        "DB_URL": "${DB_URL}"
      }
    }
  }
}
```

### Environment Variable Expansion

```json
{
  "url": "${API_BASE_URL:-https://api.example.com}/mcp",
  "headers": {
    "Authorization": "Bearer ${API_KEY}"
  }
}
```

---

## Memory (CLAUDE.md)

Persistent instructions across sessions.

### Memory Locations

| Type | Location | Shared |
|------|----------|--------|
| Managed | `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS) | Org-wide |
| Project | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team (git) |
| Project Rules | `./.claude/rules/*.md` | Team (git) |
| User | `~/.claude/CLAUDE.md` | Personal |
| Project Local | `./CLAUDE.local.md` | Personal (gitignored) |

### CLAUDE.md Imports

```markdown
See @README for project overview.
Git workflow: @docs/git-instructions.md
Personal: @~/.claude/my-project-instructions.md
```

### Path-Specific Rules

`.claude/rules/api-rules.md`:

```yaml
---
paths:
  - "src/api/**/*.ts"
  - "lib/**/*.ts"
---

# API Development Rules

- All API endpoints must include input validation
- Use standard error response format
```

---

## Plugins

Package and distribute skills, agents, hooks, and MCP servers.

### Plugin Structure

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json      # Required manifest
├── commands/            # Legacy skills (markdown files)
├── skills/              # Skills with SKILL.md
├── agents/              # Subagent definitions
├── hooks/
│   └── hooks.json       # Hook configuration
├── .mcp.json            # MCP servers
└── .lsp.json            # LSP servers
```

### plugin.json Manifest

```json
{
  "name": "my-plugin",
  "description": "Plugin description",
  "version": "1.0.0",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  },
  "homepage": "https://docs.example.com",
  "repository": "https://github.com/user/plugin",
  "license": "MIT",
  "keywords": ["keyword1", "keyword2"]
}
```

### Environment Variables

- `${CLAUDE_PLUGIN_ROOT}` - Absolute path to plugin directory

### Plugin CLI Commands

```bash
claude plugin install <plugin> [--scope user|project|local]
claude plugin uninstall <plugin>
claude plugin enable <plugin>
claude plugin disable <plugin>
claude plugin update <plugin>
```

### Local Development

```bash
claude --plugin-dir ./my-plugin
```

---

## Settings

### Settings Precedence (highest to lowest)

1. **Managed** - System-level, cannot override
2. Command line arguments
3. **Local** - `.claude/settings.local.json`
4. **Project** - `.claude/settings.json`
5. **User** - `~/.claude/settings.json`

### Permission Rules

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(git commit *)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl *)",
      "Read(./.env)",
      "Read(./secrets/**)"
    ],
    "ask": [
      "Bash(git push *)"
    ],
    "additionalDirectories": ["../docs/"],
    "defaultMode": "default"
  }
}
```

### Permission Modes

| Mode | Description |
|------|-------------|
| `default` | Prompts for permission on first use |
| `acceptEdits` | Auto-accept file edits |
| `plan` | Read-only, no modifications |
| `dontAsk` | Auto-deny unless pre-approved |
| `bypassPermissions` | Skip all prompts (dangerous) |

### Rule Syntax

| Pattern | Effect |
|---------|--------|
| `Bash` | All Bash commands |
| `Bash(npm run *)` | Commands starting with `npm run` |
| `Read(./.env)` | Specific file |
| `Read(./secrets/**)` | Directory recursively |
| `WebFetch(domain:example.com)` | Specific domain |
| `mcp__server__*` | All tools from MCP server |
| `Task(Explore)` | Specific subagent |

---

## Key Implementation Notes

### For "Last 30 Days" Skill

1. **Skill Location**: `.claude/skills/last-30-days/SKILL.md`

2. **API Keys Required**:
   - OpenAI API key (for Reddit access via partnership)
   - XAI/Grok API key (for X/Twitter search)

3. **MCP Integration Option**: Could use MCP servers for API access

4. **Suggested Structure**:
   ```
   .claude/skills/last-30-days/
   ├── SKILL.md                 # Main skill file
   ├── scripts/
   │   ├── search-reddit.py     # Reddit search via OpenAI
   │   ├── search-x.py          # X search via XAI
   │   └── web-search.py        # General web search
   └── templates/
       └── research-output.md   # Output template
   ```

5. **Frontmatter Options**:
   ```yaml
   ---
   name: last-30-days
   description: Research any topic from the last 30 days using X, Reddit, and web sources
   allowed-tools: Bash, Read, Write, WebFetch, WebSearch
   ---
   ```

6. **Dynamic Context**: Use `!`command`` syntax to inject live API results

7. **Compound Engineering Integration**: Can chain with other skills/agents for project planning
