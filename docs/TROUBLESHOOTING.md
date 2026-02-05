# Troubleshooting Guide

Solutions for common issues with the Last 30 Days Research Skill.

## Table of Contents

1. [Installation Issues](#installation-issues)
2. [API Key Issues](#api-key-issues)
3. [X/Twitter Search Errors](#xtwitter-search-errors)
4. [Reddit Search Errors](#reddit-search-errors)
5. [Skill Execution Errors](#skill-execution-errors)
6. [Output Issues](#output-issues)
7. [Performance Issues](#performance-issues)
8. [Getting More Help](#getting-more-help)

---

## Installation Issues

### Python Not Found

**Symptom:**
```
'python' is not recognized as an internal or external command
```

**Cause:** Python is not installed or not in your PATH.

**Solution:**

**Windows:**
1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. **CHECK** "Add Python to PATH" during installation
4. Restart your terminal

**Mac:**
```bash
brew install python
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**Verify:**
```bash
python --version
# or
python3 --version
```

---

### pip Not Found

**Symptom:**
```
'pip' is not recognized as an internal or external command
```

**Solution:**

Try `pip3` instead of `pip`:
```bash
pip3 install -r .claude/skills/last-30-days/scripts/requirements.txt
```

Or use Python's module syntax:
```bash
python -m pip install -r .claude/skills/last-30-days/scripts/requirements.txt
```

---

### Package Installation Fails

**Symptom:**
```
ERROR: Could not install packages due to an OSError
```

**Solutions:**

**1. Permission error:**
```bash
# Windows (run as Administrator)
pip install --user -r .claude/skills/last-30-days/scripts/requirements.txt

# Mac/Linux
pip install --user -r .claude/skills/last-30-days/scripts/requirements.txt
# or
sudo pip install -r .claude/skills/last-30-days/scripts/requirements.txt
```

**2. Outdated pip:**
```bash
python -m pip install --upgrade pip
```

**3. Virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
pip install -r .claude/skills/last-30-days/scripts/requirements.txt
```

---

### xai-sdk Installation Fails

**Symptom:**
```
ERROR: Could not find a version that satisfies the requirement xai-sdk
```

**Cause:** Python version too old or pip needs update.

**Solution:**
```bash
# Ensure Python 3.10+
python --version

# Update pip
python -m pip install --upgrade pip

# Try again
pip install xai-sdk>=1.3.1
```

---

## API Key Issues

### API Key Not Found

**Symptom:**
```json
{"error": "XAI_API_KEY not set"}
```
or
```json
{"error": "OPENAI_API_KEY not set"}
```

**Solutions:**

**1. Check .env file exists:**
```bash
# In project root
ls -la .env
```

If not found:
```bash
cp .env.example .env
```

**2. Check .env file contents:**
```bash
cat .env
```

Should look like:
```
XAI_API_KEY=xai-abc123...
OPENAI_API_KEY=sk-abc123...
```

**Common mistakes:**
- Don't add quotes: `XAI_API_KEY="key"` ❌
- Don't add spaces: `XAI_API_KEY = key` ❌
- Do this: `XAI_API_KEY=key` ✓

**3. Reload environment:**
Close and reopen your terminal, or:
```bash
source .env  # Mac/Linux
```

**4. Test directly:**
```bash
# Mac/Linux
export XAI_API_KEY=your_key_here
python .claude/skills/last-30-days/scripts/search_x.py "test"

# Windows (PowerShell)
$env:XAI_API_KEY="your_key_here"
python .claude/skills/last-30-days/scripts/search_x.py "test"
```

---

### Invalid API Key

**Symptom:**
```
Error: Invalid API key
```
or
```
401 Unauthorized
```

**Solution:**

1. Verify your API key is correct (no extra spaces or characters)
2. Generate a new key if needed:
   - XAI: https://console.x.ai → API Keys
   - OpenAI: https://platform.openai.com/api-keys
3. Update .env with the new key

---

## X/Twitter Search Errors

### No Credits Error

**Symptom:**
```
PERMISSION_DENIED: Your newly created team doesn't have any credits or licenses yet.
```

**Cause:** Your xAI account needs credits to make API calls.

**Solution:**

1. Go to the URL shown in the error message, or https://console.x.ai
2. Navigate to Billing
3. Add credits to your account
4. Try the search again

---

### Live Search Deprecated (HTTP 410)

**Symptom:**
```
Error code: 410 - {'error': 'Live search is deprecated. Please switch to the Agent Tools API'}
```

**Cause:** Using old API format.

**Solution:**

This is already fixed in the current version. If you see this error:

1. Update to the latest code:
```bash
git pull origin main
```

2. Reinstall dependencies:
```bash
pip install -r .claude/skills/last-30-days/scripts/requirements.txt
```

The fix uses `xai-sdk` with the new Responses API instead of the deprecated Chat Completions Live Search.

---

### Unknown Variant Error

**Symptom:**
```
Failed to deserialize the JSON body: tools[0].type: unknown variant `search`
```

**Cause:** Using incorrect tool type in API call.

**Solution:** Same as above - update to the latest code.

---

### Rate Limit Exceeded

**Symptom:**
```
Rate limit exceeded
```
or
```
429 Too Many Requests
```

**Solution:**

1. Wait a few minutes and try again
2. Reduce search frequency
3. Check your xAI account for rate limit details

---

## Reddit Search Errors

### OpenAI API Error

**Symptom:**
```
OpenAI API error: ...
```

**Solutions:**

**1. Check API key:**
Ensure `OPENAI_API_KEY` is set correctly in `.env`

**2. Check credits:**
Go to https://platform.openai.com/usage to check your balance

**3. Rate limits:**
Wait and retry if you've made many requests

---

### Insufficient Credits

**Symptom:**
```
You exceeded your current quota
```

**Solution:**

1. Go to https://platform.openai.com/account/billing
2. Add credits to your account
3. Try again

---

## Skill Execution Errors

### Skill Not Found

**Symptom:**
Claude doesn't recognize `/last-30-days`

**Solutions:**

**1. Check you're in the right directory:**
```bash
pwd
# Should show: /path/to/last-30-days
```

**2. Check skill file exists:**
```bash
ls .claude/skills/last-30-days/skill.md
```

**3. Check file syntax:**
The skill.md should start with valid YAML frontmatter:
```yaml
---
name: last-30-days
description: ...
---
```

---

### Script Execution Error

**Symptom:**
```
Command failed: python .claude/skills/last-30-days/scripts/search_x.py
```

**Solutions:**

**1. Test script directly:**
```bash
python .claude/skills/last-30-days/scripts/search_x.py "test topic"
```

This will show you the actual error.

**2. Check Python is working:**
```bash
python --version
```

**3. Check dependencies:**
```bash
pip list | grep -E "xai-sdk|openai"
```

---

### Permission Denied

**Symptom:**
```
Permission denied: .claude/skills/last-30-days/scripts/search_x.py
```

**Solution (Mac/Linux):**
```bash
chmod +x .claude/skills/last-30-days/scripts/*.py
```

---

## Output Issues

### Output File Not Created

**Symptom:**
No file appears in `output/` folder

**Solutions:**

**1. Check output folder exists:**
```bash
ls -la output/
```

If not:
```bash
mkdir output
```

**2. Check permissions:**
```bash
touch output/test.txt
rm output/test.txt
```

If this fails, fix folder permissions.

**3. Check Claude completed the task:**
The skill should show a confirmation message when saving.

---

### Output File Has Wrong Format

**Symptom:**
Output file is missing sections or has incorrect format

**Solution:**

1. Check skill.md wasn't accidentally modified
2. Restore from git:
```bash
git checkout .claude/skills/last-30-days/skill.md
```

---

## Performance Issues

### Search Takes Too Long

**Symptom:**
Research takes more than 2 minutes

**Possible causes:**

1. **Slow internet:** Check your connection
2. **API slowdown:** Try again later
3. **Complex topic:** Simpler topics are faster

**Solutions:**

1. Check your internet connection
2. Try a simpler topic first
3. Wait and retry during off-peak hours

---

### Claude Runs Out of Context

**Symptom:**
Claude stops mid-research or gives incomplete results

**Solution:**

1. Try a shorter, more specific topic
2. Start a new Claude session
3. Break research into smaller queries

---

## Getting More Help

### Debug Mode

Run scripts with debug output:

```bash
# Add to the script temporarily
python -c "
import os
print('XAI_API_KEY exists:', bool(os.getenv('XAI_API_KEY')))
print('OPENAI_API_KEY exists:', bool(os.getenv('OPENAI_API_KEY')))
"
```

### Check Logs

If you've enabled logging in scripts:
```bash
cat debug.log
```

### Verify Installation

Run this diagnostic script:
```bash
python -c "
import sys
print('Python:', sys.version)

try:
    import xai_sdk
    print('xai-sdk: OK')
except ImportError:
    print('xai-sdk: NOT INSTALLED')

try:
    import openai
    print('openai: OK')
except ImportError:
    print('openai: NOT INSTALLED')

try:
    from dotenv import load_dotenv
    print('python-dotenv: OK')
except ImportError:
    print('python-dotenv: NOT INSTALLED')

import os
print('XAI_API_KEY:', 'SET' if os.getenv('XAI_API_KEY') else 'NOT SET')
print('OPENAI_API_KEY:', 'SET' if os.getenv('OPENAI_API_KEY') else 'NOT SET')
"
```

### Report Issues

If you can't solve the problem:

1. Run the diagnostic script above
2. Note the exact error message
3. Note what you were trying to do
4. Open an issue on GitHub with this information

### Community Help

- Check existing GitHub issues
- Ask in the Claude Code community
- Check xAI and OpenAI documentation for API-specific issues
