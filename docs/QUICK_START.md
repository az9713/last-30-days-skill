# Quick Start Guide

Get up and running with the Last 30 Days Research Skill in 5 minutes.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation Step by Step](#installation-step-by-step)
3. [Your First Research](#your-first-research)
4. [10 Example Use Cases](#10-example-use-cases)
5. [Understanding the Output](#understanding-the-output)
6. [Next Steps](#next-steps)

---

## Prerequisites

Before you begin, make sure you have:

### 1. Python 3.10 or Higher

**Check if Python is installed:**
```bash
python --version
```

You should see something like `Python 3.10.0` or higher.

**If Python is not installed:**
- **Windows**: Download from https://www.python.org/downloads/ and run the installer. Check "Add Python to PATH" during installation.
- **Mac**: Run `brew install python` (requires Homebrew) or download from python.org
- **Linux**: Run `sudo apt install python3 python3-pip` (Ubuntu/Debian)

### 2. Claude Code CLI

**Check if Claude Code is installed:**
```bash
claude --version
```

**If Claude Code is not installed:**
1. Visit https://docs.anthropic.com/en/docs/claude-code
2. Follow the installation instructions for your operating system
3. Log in with your Anthropic account

### 3. API Keys

You need two API keys:

| API | Purpose | Where to Get |
|-----|---------|--------------|
| XAI API Key | Search X/Twitter | https://console.x.ai |
| OpenAI API Key | Search Reddit | https://platform.openai.com |

**Getting your XAI API Key:**
1. Go to https://console.x.ai
2. Create an account or sign in with your X (Twitter) account
3. Click on "API Keys" in the left menu
4. Click "Create API Key"
5. Copy the key (you won't see it again!)
6. **Important**: Add credits to your account - the API requires payment

**Getting your OpenAI API Key:**
1. Go to https://platform.openai.com
2. Create an account or sign in
3. Click your profile icon → "API Keys"
4. Click "Create new secret key"
5. Copy the key (you won't see it again!)
6. **Important**: Add credits to your account under "Billing"

---

## Installation Step by Step

### Step 1: Download the Project

**Option A: Using Git (recommended)**
```bash
git clone https://github.com/yourusername/last-30-days.git
cd last-30-days
```

**Option B: Download ZIP**
1. Download the ZIP file from GitHub
2. Extract it to a folder on your computer
3. Open a terminal and navigate to that folder:
   ```bash
   cd path/to/last-30-days
   ```

### Step 2: Install Python Dependencies

Run this command in the project folder:

```bash
pip install -r .claude/skills/last-30-days/scripts/requirements.txt
```

**What this does:** Installs the Python packages needed to search X/Twitter and Reddit.

**Expected output:**
```
Successfully installed xai-sdk-1.6.1 openai-1.x.x python-dotenv-1.x.x ...
```

**If you see errors:**
- Try `pip3` instead of `pip`
- On Windows, try `python -m pip install -r ...`
- See [Troubleshooting](TROUBLESHOOTING.md) for more help

### Step 3: Set Up Your API Keys

**Create the environment file:**
```bash
# Copy the example file
cp .env.example .env
```

**Edit the .env file:**

Open `.env` in any text editor (Notepad, VS Code, etc.) and add your keys:

```
XAI_API_KEY=your_xai_key_here
OPENAI_API_KEY=your_openai_key_here
```

**Important:**
- Replace `your_xai_key_here` with your actual XAI API key
- Replace `your_openai_key_here` with your actual OpenAI API key
- Do NOT add quotes around the keys
- Do NOT share this file with anyone

### Step 4: Start Claude Code

In the project folder, run:

```bash
claude
```

You should see the Claude Code interface. You're ready to research!

---

## Your First Research

Type this in Claude Code:

```
/last-30-days artificial intelligence
```

**What happens:**
1. Claude searches X/Twitter for recent posts about AI
2. Claude searches Reddit for discussions about AI
3. Claude searches the web for recent articles
4. Claude synthesizes everything into a structured report
5. The report is saved to the `output/` folder

**Expected time:** 30-60 seconds (depends on your internet connection)

---

## 10 Example Use Cases

Here are 10 practical examples to help you get started. Each one demonstrates a different use case.

### Use Case 1: Research a Technology Trend

**Command:**
```
/last-30-days AI coding assistants
```

**What you'll learn:**
- Which AI coding tools are trending (Cursor, Copilot, Claude Code)
- What developers like and dislike about each
- Emerging features and capabilities

**Why this is useful:** Stay current with tools that can boost your productivity.

---

### Use Case 2: Explore a Business Topic

**Command:**
```
/last-30-days remote work productivity
```

**What you'll learn:**
- Current best practices for remote work
- Tools and techniques teams are using
- Common challenges and solutions

**Why this is useful:** Improve your own remote work setup or help your team.

---

### Use Case 3: Research Before a Purchase

**Command:**
```
/last-30-days best laptops for programming 2026
```

**What you'll learn:**
- Which laptops developers recommend
- Pros and cons of popular models
- Price-to-performance insights

**Why this is useful:** Make an informed buying decision based on real user experiences.

---

### Use Case 4: Understand a Controversy

**Command:**
```
/last-30-days AI ethics debates
```

**What you'll learn:**
- Current ethical concerns about AI
- Different perspectives from experts
- Proposed solutions and frameworks

**Why this is useful:** Form your own informed opinion on important topics.

---

### Use Case 5: Learn About a New Framework

**Command:**
```
/last-30-days React vs Vue vs Svelte
```

**What you'll learn:**
- Current developer preferences
- Performance comparisons
- When to use each framework

**Why this is useful:** Choose the right tool for your next project.

---

### Use Case 6: Health and Wellness Research

**Command:**
```
/last-30-days intermittent fasting research
```

**What you'll learn:**
- Latest scientific findings
- Real user experiences
- Common approaches and schedules

**Why this is useful:** Get balanced information from multiple sources.

---

### Use Case 7: Career Development

**Command:**
```
/last-30-days software engineer salary trends
```

**What you'll learn:**
- Current salary ranges by role and location
- In-demand skills
- Job market sentiment

**Why this is useful:** Prepare for salary negotiations or career planning.

---

### Use Case 8: Investment Research

**Command:**
```
/last-30-days electric vehicle market trends
```

**What you'll learn:**
- Industry developments
- Consumer sentiment
- Emerging players and technologies

**Why this is useful:** Stay informed about market trends (not investment advice).

---

### Use Case 9: Learning a New Skill

**Command:**
```
/last-30-days best way to learn Python programming
```

**What you'll learn:**
- Recommended learning resources
- Common beginner mistakes to avoid
- Learning path suggestions

**Why this is useful:** Learn from others' experiences.

---

### Use Case 10: Current Events

**Command:**
```
/last-30-days generative AI regulations
```

**What you'll learn:**
- Recent regulatory developments
- Different countries' approaches
- Industry reactions

**Why this is useful:** Understand how regulations might affect you or your work.

---

## Understanding the Output

When you run a research command, you get a structured report:

### Key Discoveries
The most important findings, each tagged with its source:
```
- [Finding 1] [source: X]
- [Finding 2] [source: Reddit]
- [Finding 3] [source: Web]
```

### From X/Twitter
- **Top voices**: Influential accounts discussing the topic
- **Key posts**: High-engagement posts with links
- **Trending angles**: What aspects are getting attention

### From Reddit
- **Active subreddits**: Where discussions are happening
- **Top discussions**: Popular threads with upvote counts
- **Community sentiment**: Overall opinion (positive/negative/mixed)

### From Web
- **Recent articles**: Published in the last 30 days
- **Expert opinions**: What thought leaders are saying
- **Emerging trends**: New developments

### Actionable Takeaways
Practical recommendations you can act on.

### Audit Trail
Tables linking every insight to its original source, so you can:
- Verify information yourself
- Explore topics in more depth
- Cite sources if needed

---

## Next Steps

Now that you've completed the Quick Start:

1. **Try more topics**: Research anything you're curious about
2. **Read the User Guide**: Learn advanced features in [USER_GUIDE.md](USER_GUIDE.md)
3. **Check your output folder**: See saved research in the `output/` directory
4. **Explore the audit trail**: Click links to see original sources

### Tips for Better Results

- **Be specific**: "Python web frameworks 2026" works better than just "Python"
- **Add context**: "AI for healthcare diagnostics" is better than just "AI healthcare"
- **Check multiple topics**: Research related angles for a complete picture

### Getting Help

- **Troubleshooting**: See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Full documentation**: See [USER_GUIDE.md](USER_GUIDE.md)
- **Report issues**: Open a GitHub issue
