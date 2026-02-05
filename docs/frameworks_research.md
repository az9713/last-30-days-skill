# Frameworks & APIs Research

Research compiled for the "Last 30 Days" Claude Code skill.

---

## 1. AIDA Framework

**Attention → Interest → Desire → Action**

A copywriting framework developed by Elias St. Elmo Lewis in 1898 that remains highly effective for cold emails:

| Stage | Cold Email Application |
|-------|------------------------|
| **Attention** | Hook with subject line + opening that identifies their specific problem |
| **Interest** | Share your specific solution; differentiate from competitors |
| **Desire** | Use social proof and results to show what they'll miss (95% of buyers read reviews) |
| **Action** | Single CTA with urgency/scarcity; low commitment ask |

**Key insight**: Emails with a single CTA increased clicks by 371%. Keep cold emails short—the action should be "request more info" or "set up a call," not buy.

**Sources**:
- https://www.gmass.co/blog/aida-formula/
- https://blog.hubspot.com/marketing/aida-model
- https://mailshake.com/blog/aida-model-sales-emails/

---

## 2. Three Ps (Praise-Picture-Push)

A psychological cold email framework:

| Component | Function |
|-----------|----------|
| **Praise** | Open with sincere compliment—receiving compliments triggers the same brain reward as cash |
| **Picture** | Use cause-and-effect reasoning to paint how your solution delivers; builds trust |
| **Push** | Clear ask for commitment |

**Why it works**: The praise creates reciprocity, the picture builds logical trust, and the push converts while goodwill is high.

**Sources**:
- https://www.aiprm.com/prompts/1800533987249356800/
- https://www.gmass.co/blog/promise-picture-proof-push/

---

## 3. Intent Data Triggers

A behavior-based outreach framework where emails are triggered by prospect actions:

### Signal Types
- Pricing page visits
- Whitepaper downloads
- Email opens/clicks
- Website browsing patterns

### Best Practices
- Send within **1-4 hours** of trigger event
- Weight first-party intent data at 80%, third-party at 20%
- Segment accounts: cold → engaged → hot demand
- Hot accounts get case studies + product demos

**Results**: 93% of B2B marketers report success with intent-based targeting.

**Sources**:
- https://reply.io/blog/intent-data/
- https://www.salesforge.ai/blog/how-to-use-intent-data-for-cold-email-outreach
- https://www.warmly.ai/p/blog/intent-data

---

## 4. OpenAI for Reddit Access

### Partnership Details (announced May 2024)
- OpenAI has exclusive access to Reddit's Data API for real-time posts and comments
- Reddit content now appears in ChatGPT
- OpenAI became a Reddit ad partner
- Reddit reported **450% YoY increase** in non-ad revenue from data licensing deals

### Why "Last 30 Days" uses OpenAI key
Direct Reddit API is expensive ($12k+/year commercial). The OpenAI partnership provides a workaround—ChatGPT/OpenAI models have Reddit data baked in, accessible via standard OpenAI API calls.

**Sources**:
- https://openai.com/index/openai-and-reddit-partnership/
- https://techcrunch.com/2024/05/16/openai-inks-deal-to-train-ai-on-reddit-data/

---

## 5. XAI for X/Twitter Search

### Why required
You cannot search X with a regular X account via API. XAI's Grok API provides this access.

### Available Tools

| Tool | Function |
|------|----------|
| `x_search` | Search X posts, filter by handles/date ranges (up to 10 handles) |
| `web_search` | Real-time web search + page browsing |
| **Live Search** | Real-time X data, internet, trending news (currently **free in beta**) |

### Features
- Analyze images/videos in X posts
- Real-time sentiment analysis
- Filter by date ranges and specific handles

**Getting started**: Create account at https://x.ai and generate API key.

**Sources**:
- https://docs.x.ai/docs/overview
- https://docs.x.ai/docs/guides/tools/search-tools
- https://x.com/xai/status/1925244461875175616

---

## 6. Direct Reddit API Integration

### Current State (2025-2026)

| Tier | Cost | Notes |
|------|------|-------|
| Free | $0 | Personal projects only, strict rate limits |
| Commercial | $12,000+/year | Enterprise agreements required |

### Limitations
- Rate limits restrictive for large-scale collection
- Requires programming knowledge + infrastructure
- 2025 crackdown: pre-approval now required for personal projects

### Alternatives
- **PRAW** (Python) / **Snoowrap** (JS): Open-source wrappers for flexibility
- **Pipedream**: No-code integration with 3,000+ apps
- **OpenAI API**: Indirect access via ChatGPT's Reddit data (what "Last 30 Days" uses)

**Developer Platform**: Reddit has a new platform in closed beta for building apps that launch directly on Reddit.

**Sources**:
- https://support.reddithelp.com/hc/en-us/articles/14945211791892-Developer-Platform-Accessing-Reddit-Data
- https://painonsocial.com/blog/how-much-does-reddit-api-cost
- https://zuplo.com/learning-center/reddit-api-guide

---

## Summary for "Last 30 Days" Skill

The skill's API architecture makes sense:

| API Key | Purpose |
|---------|---------|
| **XAI key** | Only way to search X/Twitter programmatically |
| **OpenAI key** | Cheaper Reddit access via partnership data vs. $12k+/year direct API |

Matt Van Horn mentioned exploring direct Reddit API as a "weekend project" to improve results, but cost/complexity is the barrier.
