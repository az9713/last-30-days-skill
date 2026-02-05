# Contributing Guide

Thank you for your interest in contributing to the Last 30 Days Research Skill! This guide will help you get started.

## Table of Contents

1. [Ways to Contribute](#ways-to-contribute)
2. [Development Setup](#development-setup)
3. [Making Changes](#making-changes)
4. [Submitting Changes](#submitting-changes)
5. [Code Standards](#code-standards)
6. [Documentation](#documentation)
7. [Getting Help](#getting-help)

---

## Ways to Contribute

### 1. Report Bugs

Found a bug? Please open an issue with:
- What you were trying to do
- What happened instead
- Steps to reproduce
- Your environment (OS, Python version, etc.)

### 2. Suggest Features

Have an idea? Open an issue with:
- The problem you're trying to solve
- Your proposed solution
- Any alternatives you considered

### 3. Improve Documentation

Documentation can always be better! You can:
- Fix typos
- Add examples
- Clarify confusing sections
- Translate to other languages

### 4. Submit Code

Ready to code? See the sections below for our workflow.

---

## Development Setup

### Prerequisites

- Python 3.10 or higher
- Git
- A GitHub account
- API keys for testing (XAI, OpenAI)

### Step 1: Fork the Repository

1. Go to the repository on GitHub
2. Click "Fork" button
3. Clone your fork:

```bash
git clone https://github.com/YOUR_USERNAME/last-30-days.git
cd last-30-days
```

### Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r .claude/skills/last-30-days/scripts/requirements.txt
```

### Step 4: Configure Environment

```bash
cp .env.example .env
# Edit .env with your API keys
```

### Step 5: Verify Setup

```bash
# Test scripts work
python .claude/skills/last-30-days/scripts/search_x.py "test"
python .claude/skills/last-30-days/scripts/search_reddit.py "test"
```

---

## Making Changes

### Step 1: Create a Branch

Always work on a branch, never directly on `main`:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

**Branch naming conventions:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation changes
- `refactor/` - Code refactoring

### Step 2: Make Your Changes

Edit files as needed. Keep changes focused on one thing.

### Step 3: Test Your Changes

```bash
# Test scripts manually
python .claude/skills/last-30-days/scripts/search_x.py "test topic"

# Test the full skill in Claude Code
claude
# Then: /last-30-days test topic
```

### Step 4: Commit Your Changes

```bash
# Stage changes
git add .

# Commit with a clear message
git commit -m "type: short description

Longer description if needed.

- Bullet point for change 1
- Bullet point for change 2"
```

**Commit message types:**
- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation
- `refactor:` - Code refactoring
- `test:` - Adding tests
- `chore:` - Maintenance

**Good commit messages:**
```
feat: add date range parameter to X search

Allow users to specify custom date ranges for X/Twitter search.
Default remains 30 days for backward compatibility.

- Add from_days parameter to search_x()
- Update skill.md to document new parameter
- Add tests for custom date ranges
```

---

## Submitting Changes

### Step 1: Push Your Branch

```bash
git push origin feature/your-feature-name
```

### Step 2: Create Pull Request

1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. Fill out the PR template:

```markdown
## Description
[What does this PR do?]

## Related Issue
[Link to issue if applicable]

## Changes Made
- [Change 1]
- [Change 2]

## Testing Done
- [How you tested]

## Checklist
- [ ] Code follows project style
- [ ] Tests pass
- [ ] Documentation updated
- [ ] No sensitive data in commits
```

### Step 3: Respond to Review

- Address any feedback from reviewers
- Push additional commits if needed
- Be patient - reviews take time

---

## Code Standards

### Python Style

We follow PEP 8 with these specifics:

```python
# Use type hints
def search_x(topic: str) -> dict:
    """
    Search X/Twitter for a topic.

    Args:
        topic: The topic to search for

    Returns:
        Dictionary with search results
    """
    pass

# Use descriptive variable names
date_range = f"{start_date} to {end_date}"  # Good
dr = f"{s} to {e}"  # Bad

# Handle errors gracefully
try:
    result = api_call()
except Exception as e:
    return {"error": str(e)}
```

### JSON Output

Scripts should return consistent JSON:

```python
# Success
{
    "source": "Source Name",
    "topic": "searched topic",
    "content": "results",
    ...
}

# Error
{
    "error": "What went wrong",
    "fix": "How to fix it (optional)",
    "topic": "searched topic",
    "source": "Source Name"
}
```

### Markdown Style

For skill.md and documentation:

```markdown
# Heading 1
## Heading 2
### Heading 3

- Bullet point
- Another point

1. Numbered item
2. Another item

**Bold text**
`inline code`

```python
code block
```
```

---

## Documentation

### When to Update Docs

Update documentation when you:
- Add a new feature
- Change how something works
- Fix a confusing issue
- Deprecate functionality

### Documentation Files

| File | Purpose | Update When |
|------|---------|-------------|
| README.md | Project overview | Major changes |
| CLAUDE.md | Claude Code context | Skill changes |
| docs/QUICK_START.md | Getting started | Setup changes |
| docs/USER_GUIDE.md | User documentation | Feature changes |
| docs/DEVELOPER_GUIDE.md | Developer docs | Technical changes |
| docs/ARCHITECTURE.md | System design | Architecture changes |
| docs/TROUBLESHOOTING.md | Problem solving | New issues found |
| docs/API_REFERENCE.md | API details | API changes |

### Documentation Style

- Write for beginners (assume no prior knowledge)
- Use step-by-step instructions
- Include examples
- Explain the "why" not just the "what"

---

## Getting Help

### Questions About Contributing

- Check existing issues for similar questions
- Open a new issue with the "question" label

### Stuck on Something?

1. Re-read the relevant documentation
2. Check the troubleshooting guide
3. Search existing issues
4. Ask in the issue tracker

### Response Times

- We aim to respond to issues within 1 week
- PR reviews may take 1-2 weeks
- Be patient - maintainers are volunteers

---

## Recognition

Contributors are recognized in:
- GitHub's contributor graph
- Release notes for significant contributions

Thank you for contributing! Your help makes this project better for everyone.
