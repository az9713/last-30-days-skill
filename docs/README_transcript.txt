https://www.youtube.com/watch?v=71ES9jzqa0Q&t=5s


I sit down with Matt Van Horn, creator of the "Last 30 Days" skill for Claude Code, as he demonstrates how this tool turns anyone into a real-time research expert. By pulling trending data from X, Reddit, and the web, Last 30 Days supercharges Claude Code prompts with current intelligence. Matt walks through live demos, from discovering popular rap songs to generating cold emails to building a Moltbot competitor, showing how non-engineers can ship products using AI tools with almost no coding background.

Timestamps
00:00 – Intro
01:39 – What Is "Last 30 Days"
03:29 – Live Demo: Most Popular Rap Songs
04:47 – Cold Email Frameworks Demo
07:04 – Growing an X Following Using Recent Data
07:49 – Researching Moltbot to Build a Competitor
08:26 – Best Practices for Last 30 days
09:26 – Growing an X Following Using Recent Data Results
11:17 – Best Practices for Webdesign Research
13:44 – Building an Enterprise Moltbot Clone Live
17:43 – Generating Figma Prompts and Nano Banana Images
21:54 – Advice for Non-Engineers Getting Started with Claude Code

Links Mentioned:
Last 30 Days Skill: https://startup-ideas-pod.link/last30...

Key Points

Last 30 Days searches X, Reddit, and the web for content from the past month, creating highly optimized prompts for Claude Code.
The tool requires Claude Code access, an OpenAI API key (for Reddit data), and an XAI key (for X/Twitter access).
Matt demonstrates using minimal prompts to generate cold email frameworks, research trending topics, and kickstart new product builds.
Compound Engineering serves as a planning tool to turn research into structured project roadmaps.
Non-engineers can ship functional products by combining Claude Code with ChatGPT for troubleshooting errors via screenshots.

Numbered Section Summaries

1. What Is "Last 30 Days"Matt explains the core problem: AI and online conversations move too fast to track manually. Last 30 Days solves this by aggregating real-time data from X, Reddit, and web searches into a single Claude Code skill, letting users become instant experts on any topic.

2. API Setup and How It WorksThe skill pulls together multiple API connections—OpenAI for Reddit access, XAI for X/Twitter search, plus standard web search. Matt notes he is exploring direct Reddit API integration to improve results further.

3. Cold Email Frameworks DemoMatt prompts the tool to research high-performing cold email techniques from the last 30 days, then uses that research to generate personalized outreach emails. The tool surfaces frameworks like AIDA, Three Ps (Praise-Picture-Push), and Intention Data Triggers—all without Matt reading the underlying research.

4. From Research to Product BuildThe episode moves into building a Moltbot competitor. Matt shows how he uses Last 30 Days to research Moltbot use cases, then feeds that intelligence into Compound Engineering to plan an enterprise-grade product from scratch.

5. Trending Web Design for Landing PagesMatt queries what website designs are getting the most love on X right now. Results include the Shopify "Winner Edition" page and a praised YC landing page. He then prompts Claude Code to generate a Figma-ready design spec for a SaaS productivity app.

6. Building Without Engineering SkillsMatt emphasizes he has not shipped production code since high school. His workflow involves running Claude Code in the terminal, taking screenshots of errors, pasting them into ChatGPT for debugging help, and iterating. The biggest unlock: learning to paste screenshots with Control+V instead of Command+V.

7. Getting Started RecommendationsMatt advises signing up for Claude Code's $20 plan, using ChatGPT as a troubleshooting copilot, and experimenting with skills like Last 30 Days and Compound Engineering. Trial and error, combined with lots of terminal windows, is the path forward.


In this video



Chapters

Transcript
Intro
0:00
There's a way to tune your clawed code
0:02
so you get absolute superpowers. Some of
0:05
my smartest friends are using this tool
0:08
and it's called Last 30 Days. It just
0:10
came out and I had the founder Matt Van
0:12
Horn come on the podcast to show how to
0:14
use it. What last 30 days does is it
0:17
uses trending data on places like Axe
0:19
and Reddit as the starting point for
0:21
your prompts on cloud code. The cool
0:24
part is you end up getting way more out
0:26
of cloud code because the prompts are
0:28
way more dialed and optimized. Enjoy the
0:30
episode. Let me know if you think this
0:32
is cool and I'll see you in there.
0:44
I feel like I'm in I know I'm in for a
0:46
treat. Matt Van Horn is on the podcast
0:49
and he's going to demo something very
0:52
special. met by the end of this episode.
0:54
What are people going to learn?
0:56
They will have a new superpower in cloud
0:58
code. It's called slashlast30 days and
1:01
uh it's going to for any topic you could
1:04
possibly imagine from best prompting
1:07
techniques for a particular tool to how
1:09
should I use claudebot to what are the
1:12
greatest rap songs right now. It's going
1:14
to search X, Twitter, and the web for
1:17
only things that have happened in the
1:18
last 30 days and give you a great result
1:20
and help you be expert.
1:22
My smartest friends are using this right
1:24
now, so I had to ask Matt to come on and
1:26
showcase how to use this. So, thank you,
1:28
Matt. Uh, I say we just get right into
1:31
it.
1:32
All right, yolo. Let's uh let's go. I
1:36
can just uh dive in. So we are in cloud
What Is "Last 30 Days"
1:41
code and so this is a skill for cloud
1:43
code and so once you install it you just
1:46
type in last 30 days. So research any
1:49
topic from the last 30 days. So
1:53
uh can be anything. So let's say I want
1:57
um let's kick one off right here. Um
2:01
most popular
2:04
rap
2:06
songs. So, let's kick that one off. And
2:09
so, and then I'll I'll show some ones
2:11
some pre-en ones that I've done. So,
2:12
using the last 30 days school, let's
2:14
research most popular rap songs. Let me
2:15
research some popular rap songs from the
2:17
last 30 days. And so, right here, it's
2:20
Reddit reading what Redditors are
2:21
saying. X reading the timeline. And then
2:24
it's also running a a web search. So, so
2:27
is the is the thinking like is the
2:29
reason why you created this is there's
2:31
so much good data on the internet and
2:33
you want to use that as like the jumping
2:34
off point. Is that why
2:36
the the reason that I built this tool is
2:39
I feel like everything is moving so
2:42
quickly in AI and it's nearly impossible
2:46
to keep up with the conversation on X on
2:48
Reddit on GitHub and I wanted a tool
2:54
that gives you superpowers
2:56
to be able to just become expert on any
3:00
topic based on what's happening on
3:02
Reddit X and the web. very very quickly
3:05
because the prompts are changing so
3:07
quickly. What's happened to like look at
3:09
you know Maltbot? What's happened there?
3:11
It's changing so quickly. And so being
3:15
able to just become expert at something
3:16
it kind of reminds me in the Matrix when
3:18
he gets plugged in and it's like I know
3:20
kung fu, right? So to be able to do that
3:22
for any topic very very quickly is is
3:26
why I built this and honestly so I could
3:28
use it for myself. Looks like our our
Live Demo: Most Popular Rap Songs
3:30
rap
3:32
research. So, I found one Reddit thread,
3:34
19 expost, and the most popular rap
3:37
songs right now.
3:39
So, it kind of dug in and into hip-hop
3:42
heads, some expos, Billboard data, some
3:45
Spotify data, hip-hop heads, hip-hop all
3:47
day, rap complex, and created this uh
3:51
this reply.
3:52
So, someone in the comment section is
3:54
going to be like, well, I could have
3:55
used perplexity or chat GBT to do that.
3:58
Why should I use this?
4:00
Yeah. So, absolutely could, but it's uh
4:04
and again I'm I'm not fully up to date
4:06
on which which tools have what access
4:08
but to set up last 30 days. So you need
4:13
cloud code, right? So you're already
4:14
paying for cloud code, right? So you
4:15
need that account. You need a open AI
4:18
key because OpenAI has a deal with
4:21
Reddit that gives you that Reddit
4:22
access. Uh
4:25
I'm actually see looking into Reddit API
4:27
keys if that's an option to make the the
4:29
product better. That's what I was um
4:31
that's one of the things my my weekend
4:33
projects. And then the the third is you
4:36
can't search X using your X account. You
4:39
have to use an XAI key. And so last 30
4:43
days pulls in all these API keys and
4:45
pulls it all together if that makes
Cold Email Frameworks Demo
4:47
sense. So this is one
4:51
that I did right before we started. So I
4:53
said last 30 days highest performing
4:55
cold email frameworks for ICP output
4:59
three email variants subject line.
5:02
So it went on X went on Twitter found
5:06
Reddit threads expost web pages and what
5:09
what's interesting how I use this tool
5:11
is I often don't even read what it says.
5:14
Like sure it's interesting to see what
5:16
it learned but mostly I just wanted it
5:17
to write a good email. So I said, "Can
5:19
you write me some cold emails for
5:20
getting on Greg Eisenberg's podcast?"
5:23
Uh, sorry I spelled your name wrong.
5:24
Good target startup ideas later is all
5:26
about unconventional startup ideas,
5:27
community building unique relevance. You
5:29
know, what's your angle? What's your
5:31
credibility signal? Any connection
5:32
points to Greg mutual follows. What
5:34
timely uh talk about AI tools I'm
5:37
working on and I once made a smart oven.
5:40
Uh, smart oven details gold unexpected
5:42
founders who shipped hardware and
5:44
software. That's your hook. Here are
5:45
three email variants.
5:48
subject smart oven AI tools not the P
5:50
Greg I went from building smart oven to
5:51
building AI tools that might sound weird
5:53
until you hear it turns out the hardest
5:55
part of hardware taught me exactly
5:56
what's broken and how people interact
5:57
with AI I'm building the fixed
6:00
what is smart oven taught me about AI so
6:02
anyway I literally did nothing here I
6:05
barely gave it any context and it had
6:08
become expert in different cold emailing
6:12
concepts the three Ps framework praise
6:14
picture push ADA attention I've never
6:16
read any of these in my life
6:17
intentionbased data trigger framework
6:20
and then it just did it for me if that
6:22
makes sense without even me having to
6:24
read the research. Yeah. I think what's
6:26
really cool about this is these
6:29
frameworks. I mean, ADA has been around
6:32
for forever like you know OG David
6:34
Oglevie days, but other than you know
6:36
the other ones like it feels like those
6:39
are timely frameworks
6:41
like these emails like I'm reading these
6:43
emails and they're I get a lot of cold
6:45
email and these are actually ones that
6:47
would break through the noise. So that's
6:49
what's really cool about this.
6:51
And I didn't even give it much effort. I
6:53
literally said, "I'm a former smart oven
6:55
entrepreneur."
6:58
You couldn't have given it like less
7:00
context.
7:01
And it did. Okay.
7:02
Yeah.
7:03
And then another one I I just tried last
Growing an X Following Using Recent Data
7:06
30 days how to get X followers. I
7:07
researched people actually saying um and
7:12
what I learned reply is the number one
7:14
growth strategy. Multiple X power users
7:16
all credit becoming a reply guy as the
7:19
fastest path to growth. shows 380
7:22
thoughtful replies, daily engagement, 40
7:23
before posting. Find larger accounts.
7:25
Reply first consistently. Post at least
7:27
1x a day, 5 days a week. U Reddit
7:31
threads, X threads, Instagram marketing,
7:33
Facebook ads, and share your vision.
7:36
What's your account and what's
7:37
followers? Uh, I'm M. Van Horn and I
7:41
made an AI tool for claw code. I don't
7:45
know what it's going to do now.
7:48
That's the exciting part. one one other
Researching Moltbot to Build a Competitor
7:50
let's spin up another last 30 days
7:53
window. Sorry for all the all the
7:56
windows.
7:58
So all right so last 30 days of research
8:05
cla
8:08
bot
8:10
so I can
8:13
build an enterprise competitor to make
8:18
money and not give it away for free.
8:21
Maybe I'm giving too much context but I
8:22
should have just said research clav um
8:25
actually I'm going to do that. I mean,
Best Practices for Last 30 days
8:27
what do you recommend when you're, you
8:29
know, is it shorter prompts, medium
8:31
prompts, long prompts? Like, how do
8:32
getting the most out of
8:34
I think it's a it's kind of you prime
8:36
the engine by first doing just research
8:38
cloudbot top use cases. So, what my my
8:43
vision for this thread of what we're
8:45
going to do is it's going to learn about
8:47
Cloudbot, right? Check X, check Reddit,
8:50
and then what I'm going to do is
8:51
actually load one of my favorite tools,
8:54
Compound Engineering. Uh, shout out to
8:56
to Kevin Rose for introducing me to it.
8:58
And compound engineering is when I'm
9:01
starting a new project is where I do my
9:03
planning. And so what I want to do here
9:07
is take this research on from last 30
9:10
days from Cloudbot and use that as the
9:14
starting point to kick off a enterprise
9:19
version of Cloudbot and to build it. So
9:23
let's let's let this run and see how our
9:25
other stuff is going. All right. I'm in
Growing an X Following Using Recent Data Results
9:28
I'm in A tool for cloud code. A tools
9:30
are hot right now. Here's a growth
9:31
playbook for you. Morning. 40 minutes
9:33
for your first post. Reply to tip from
9:35
anthropic. Alex Burch Labs. Cloud power
9:37
users. Add genuine value. Share a tip.
9:39
Ask a smart question. Content type tool
9:41
demo. Build X today. What it does. Cloud
9:43
code tip. Five things I learned X. Build
9:46
in public. Ship. By the way, I I'm not
9:47
going to do this. I think this was just
9:49
I I actually asked chat GPT for
9:51
suggestions of what I should demo on
9:53
your show and it gave me this one but
9:56
quickest wins. Pin your best demo tweet.
9:58
Show the tool in action. Bio formula I
10:00
build tool one logo shipping AI tools
10:02
for cloud code.
10:03
That's not bad.
10:05
No, it's it's not bad.
10:07
So all right, let's close this one out.
10:09
All right, we got cloud code best use
10:12
overnight coding agent management daily
10:13
briefings and morning. Do you want to
10:15
dive deeper? Okay. So now I'm going to
10:16
call in another tool. Let's plan throw
10:18
in workflows plan. Take the context
10:23
above about Claudebot
10:26
and
10:28
propose an enterprise
10:31
version that could make a lot of money.
10:36
Just do that. Keep it simple.
10:39
Yeah. I mean this is this is
10:40
interesting, right? like you know you're
10:43
taking a trend open source trend and
10:45
you're like okay how can I build a
10:48
product that you know gets me paid and
10:51
it's interesting because there's so many
10:53
trends that are happening right now on X
10:56
as like a data source and Reddit as a
10:58
data source that you know
11:00
if this if this is actually good is
11:02
going to help give you ideas and sort of
11:05
eventually a PRD right
11:07
yep anyway so it's still making our plan
11:10
it's researching still doing an
11:13
analysis.
11:14
So, we'll we'll we'll see where that
11:16
adds up. But anyway, do you want you
Best Practices for Webdesign Research
11:18
want to try a last 30-day prompt? Yeah.
11:20
I mean, I'm curious like I mean you
11:22
you're seeing all the all these prompts.
11:24
So, like the people that listen to this
11:25
show, these are people these are
11:27
founders, solopreneurs, people building
11:29
businesses. Um they're always looking
11:32
for unfair advantages. Um like what sort
11:35
of what sort of prompt do you would you
11:38
suggest that type of person someone who
11:41
wants to build a business? Um you know
11:44
is it competitive research? Is it um you
11:49
know what what are some ideas you have?
11:52
Good good question. Um I mean I think
11:55
it's it's very good for competitive
11:57
research. I think it's very good for
11:59
looking at at hot topics. Um, you know,
12:03
I think it's, you know, we could
12:04
probably do something like, um, you
12:08
know, let's try it for your your web
12:11
design idea, right? You kind of describe
12:13
poke.com, which I missed, right? So, um,
12:17
what webpage designs are getting the
12:22
most love right now? Yeah, because
12:24
that's interesting because if we, you
12:25
know, knowing the trend is just so
12:29
important. And
12:32
uh it also helps like give, you know,
12:35
when I'm when I'm designing something,
12:37
it helps give me ideas. It gives it's so
12:39
overwhelming sometimes when you have
12:41
like a blank page and you don't know
12:42
where to start.
12:43
Yep.
12:44
We've all been there. And I kind of my
12:48
kind of the the the thing that inspired
12:51
this tool was I used to before I would
12:53
uh jump into any type of vibe coding
12:57
session, I would go on chat GBT 5.2 and
13:02
I would just say in thinking mode and be
13:04
like go
13:07
uh this was for design. I would say go
13:10
on Reddit and research Nana Banana Pro
13:12
best
13:13
uh prompting techniques and I would do
13:16
that at the beginning and then I
13:18
wouldn't even read what it would say and
13:19
then I would just be like, "Okay, give
13:21
me a prompt." And so it's it's kind of
13:23
this like hack of, you know, learning
13:27
kung fu, learning the prompts that
13:29
everyone's using without actually
13:30
needing to read about it, if that makes
13:33
sense. you kind of just like, okay,
13:35
let's just trust the the the mind crowd,
13:39
the the world that's out there and and
13:42
use those best practices. All right,
Building an Enterprise Moltbot Clone Live
13:45
we've got a plan. Let's uh I guess let's
13:48
open the plan in uh BBEdit. All right,
13:53
so this is the plan for for the audio
13:54
listeners. So this is the plan for the
13:57
the mobile
13:59
enterprise commercial SAS platform. So
14:02
again, this is not a business plan. This
14:03
is actually a plan to how to build the
14:08
software architecture and I could just
14:10
then tell compound engineering to just
14:12
go build it. So transform maltbot form
14:15
cloud into an open source AI into a
14:17
multi-tenant enterprise SAS platform
14:19
called moltra enterprise or cloud cloud.
14:21
This capitalizes on the viral growth.
14:23
GitHub stars B2B adoption enterprise AI
14:26
assistance are 30 blah blah blah. Why
14:29
enterprise can't use multipart today? No
14:31
multi-tensity, no RBA security
14:33
vulnerabilities, no audit logging.
14:36
Uh there move wise required by service
14:38
now for market validation. proposed
14:39
solution of fully managed
14:41
enterprisegrade maltbot
14:44
commercial I really don't like the name
14:46
cloud cloud come on come on lm cloud
14:50
architecture slack web hook discord
14:52
gateway team hooks message radar core
14:55
technical components and so kind of it
14:58
used last 30 days as the basis for its
15:00
expertise to learn about maltbot and
15:04
then it did the rest and now I could
15:08
just say okay build it.
15:10
So,
15:11
dude, that's crazy. It also that that
15:14
was a pretty that was pretty dialed.
15:15
Like, that was pretty dialed.
15:19
I'm impressed.
15:20
And and LLMs knew nothing about
15:23
Claudebot because it didn't exist before
15:28
didn't exist till very very recently.
15:32
All right. Phase one only build a
15:34
multi-tenant foundation postcress but
15:37
has full MVP. Uh I guess let's uh let's
15:41
build the proof of concept. So So
15:44
basically,
15:46
you know, it asked if you wanted to do
15:47
an MVP. It asked if you wanted to do a
15:49
bigger build. Is that is that what I
15:50
saw?
15:50
Yeah, exactly. And so I just said,
15:52
"Okay, let's just do the the demo."
15:55
Yeah.
15:56
I typed something else. New repo. Also,
16:00
can you please give it a better name?
16:02
Greg, you're you're you live with this
16:03
world. What should we call this thing?
16:05
I mean, why not? I actually don't hate
16:09
uh Claude Cloud. It just Well,
16:12
well, they got in trouble for using
16:14
claw.
16:15
Exactly. So, why not just call it molt
16:17
cloud?
16:18
But then we're getting in trouble with
16:19
malt.
16:21
Mold. Um, okay. So, why don't we call it
16:24
Should we go lobster?
16:27
Um, I was going to say, why don't we
16:30
call it red lobster?
16:32
But I think that
16:34
All right. All right. Let's go with
16:35
Let's go with lead Speak.
16:38
Let's go with Red Lava.
16:40
That's cool.
16:41
This describes a 40week product surveys.
16:43
What scope do you want to do? I don't
16:46
know. Just Just do it.
16:47
Just do it. Why are you asking me so
16:49
many questions?
16:51
All right. Um All right. What do we ask
16:53
here? What web designs are getting the
16:55
most love right now?
16:56
Um the most love Shopify winter edition.
16:59
Yes, I remember. I saw that one. That
17:01
was really
17:01
That was really awesome. That was
17:03
beautiful.
17:04
Look, 3,000 likes, 320 retweets, the YC
17:08
landing page. So, what's funny is I saw
17:09
this. I didn't actually look at it yet,
17:11
but I saw that it was getting love and
17:12
hype. Praise for scrappy humble
17:14
beginnings. Shop web landing all like
17:18
jewelry, craft works, design,
17:21
all agents reported back. Reddit didn't
17:23
find anything topic too visual for text
17:25
discussions, but found uh what tool do
17:27
you want to use to create designs? So
17:29
it's like, okay, now that I've
17:30
researched these things, what do you
17:32
what do you want to design in, right?
17:35
Um, so it's kind of it's kind of pushing
17:38
you to be like, okay, I've now learned
17:40
this expertise. Now, let's do something
17:42
with it.
Generating Figma Prompts and Nano Banana Images
17:44
So So this could literally pump out a
17:46
Figma design. Is that possible?
17:49
Uh, I I haven't spent enough time in
17:51
Figma in in the AI era. All my Figma
17:53
time was preai, so I don't know what
17:56
like prompting Figma even means in 2026,
17:59
but uh I don't I could just say one and
18:01
see what happens.
18:04
Now, what are you designing? All right.
18:06
Now, it's it's diving in.
18:09
Um a portfolio
18:12
landing page for productivity app is
18:15
fine.
18:17
What are the suggestions?
18:20
It says, "What are you designing a SAS
18:21
landing page, a portfolio site, an
18:23
e-commerce homepage for skincare brand
18:25
agency website hero?"
18:28
And so I keep coming back to this, but
18:31
it's it is impressive how little you're
18:33
giving like how short your prompts are.
18:37
Mhm.
18:38
Here we go. Here's a prompt for Figma.
18:40
Apparently, that's a thing.
18:42
Wow.
18:42
2026 forward. Design that feels warm and
18:45
human, not cold sass up layout.
18:46
Anti-grid composition hero section use
18:48
asymmetrical balance headline left
18:50
product screenshots floating right at
18:52
angle sections below flow organic with
18:54
varied spacing not rigid 12 column
18:56
uniformity typography. One oversized
18:59
display headline paired with small body
19:01
text. Add a single handdrawn underline
19:03
or circle accent on the keyword.
19:05
Consider variable font like Satoshi or
19:07
General Sons. Nature distilled warm
19:10
cream background. charcoal text, one
19:12
muted accent, avoid harsh pure white or
19:14
saturated blues, glass morphism element,
19:17
feature card. I want to see this. It's
19:19
too bad I don't have Figma AI set up.
19:24
But um so
19:26
that's pretty cool.
19:27
Let's see if it can do this for like a
19:30
nano banana prompt. Like, hey, you know,
19:32
I wonder if it can do that. Can you make
19:34
this a nano banana
19:36
prompt?
19:39
Yep. But I didn't ask it to become
19:41
expert in
19:43
a nano banana.
19:45
But I didn't ask it to become a nano
19:47
banana prompt expert. So, who knows
19:48
what's gonna happen.
19:50
Yeah.
19:52
Back to Telegram and let's see what
19:55
happens. We should get three images.
19:59
Your maltbot is typing. That's a cool
20:02
feeling, like watching your maltbot
20:05
type.
20:07
Someone needs to visualize that with
20:09
like a lobster on a keyboard.
20:11
Yeah.
20:17
Why did you choose Telegram over
20:19
iMessage or Discord or something else?
20:23
Cuz my LM told me to. Uh because I'm I'm
20:26
on a a $4 a month shell account uh for
20:29
my I don't have the Mac Mac Mini setup.
20:32
And so, um, the, um,
20:38
you can't use iMessage or WhatsApp, I
20:40
believe, when you're just on a shell. I
20:41
think you need to run some sort of Mac
20:44
software.
20:46
And so, Telegram seems to be the default
20:48
where you when you don't have that.
20:50
And for people who don't know what a
20:51
shell account is, can can you just
20:53
expand on that?
20:55
Yeah, sorry. Uh, by the way, this is our
20:58
Cloudbot competitor that it's building.
21:00
I don't know what is going on or what
21:02
it's building.
21:05
It's adding a demo script showing tenant
21:07
isolation. Then oh, it already set up
21:09
TypeScript and NodeJS. That's nice.
21:11
Wow, that's cool.
21:14
Here we go.
21:16
Oh yeah,
21:18
not bad. I bet it' be nicer in Figma.
21:20
Yeah, that was pretty solid. And again,
21:22
that was by using slast 30 days. What
21:25
are the hottest webpage designs that the
21:27
world is excited about right now? what's
21:29
trendy and then okay now use that to for
21:32
my SAS productivity app. I like how it
21:35
like circled random words flow
21:37
effortlessly more.
21:39
That's awesome. Yeah, I like that. It
21:41
feels like handdrawn.
21:43
It's uh it's pretty wild. It's it's wild
21:45
times. It's uh the rate at what we're
21:49
we're able to build things and how fast
21:50
things change is absolutely wild.
Advice for Non-Engineers Getting Started with Claude Code
21:54
So Matt to to this has been fun. um you
21:58
know if people want to get started they
22:00
want to like what advice do you have you
22:04
know in terms of getting the most out of
22:07
this product?
22:08
Yeah. So one of the things I'll say is I
22:11
uh I am not a software engineer. I have
22:13
not shipped anything of value since high
22:16
school and could argue the web pages I
22:18
was shipping in high school were not of
22:19
value either. But at least I could write
22:22
some some basic HTML or some basic
22:24
scripts. And so what's
22:28
um what's amazing is
22:31
being uh not a software engineer and
22:35
being able to go into cloud code. Like
22:37
it seems intimidating. You're in the
22:40
terminal. Setting up a cloudbot seems
22:43
intimidating. And my recommendation for
22:45
starting out is set up set up claude
22:49
code. It's magical. Sign up for the $20
22:52
account. if you'll be on the $100 and
22:55
the $200 account probably real soon if
22:57
you're uh if you're successful. Um, and
23:01
and what I what I do is I um have keep a
23:06
chat GPT window open to ask questions
23:09
to. And so I'm kind of moving back and
23:11
forth and posting lots of screenshots be
23:13
like there's some error. I don't know
23:15
what's going on. Help me. And so chat
23:17
GBT52 thinking will be like, "Okay,
23:20
great. In your in your shell, in your
23:21
terminal, this is what's going on. This
23:23
is why it broke." And I'm like, "Okay,
23:25
great. What do I do? Help." And then
23:27
it's just like, "Copy this into the
23:28
terminal." I'm like, "Okay." And I again
23:30
don't even have to read it, don't have
23:31
to overthink it. And so kind of just
23:32
like screenshot trial and error back and
23:35
forth between chat GPT and my terminal.
23:38
And like I couldn't figure out actually
23:39
how to post screenshots into my
23:40
terminal. So I asked chat GPT and it's
23:42
like, oh, you have to use controlV
23:44
instead of commandV. And once that that
23:47
was the biggest unlock for me in the
23:49
terminal, figuring out that I could post
23:50
screenshots with controlV. And anyway,
23:54
so I recommend getting into cloud code
23:56
and and try last 30 days obviously uh
24:00
because it it gives you superpowers, but
24:02
use tools like compound engineering, use
24:06
skills like uh there's another one
24:08
called superpowers which is getting a
24:10
lot of love right now and you just kind
24:12
of enter these plan modes and you try
24:16
and you build things. And I had this
24:18
idea for the last 30 days and I've never
24:21
looked at the code for the skill that I
24:24
wrote quote unquote. And it was just a
24:27
lot of trial and error and running more
24:28
and more terminal windows and testing it
24:30
and testing it and being like, "Hey,
24:32
figure out how I can get access to this
24:33
API. Hey, figure out how I could do
24:34
this. Hey, how can my users do this?"
24:37
And going from there.
24:38
I love that, man. Well, I'll include uh
24:41
a link to last 30 days in the show
24:43
notes, in the description, link where
24:46
where you can follow Matt Van Horn on X.
24:48
And dude, this is this is really cool
24:52
and it's crazy that this is just sort of
24:53
like a project that you started and it's
24:56
gaining so much traction and I think
24:59
people are just, you know, obsessed with
25:01
Claude Code for,
25:04
you know, for good reason. Um, but I
25:06
think people are just trying to get the
25:07
most out of it. So, this this came at a
25:09
a very perfect time and and uh can't
25:12
wait to see how it evolves. And thanks
25:14
for doing a little show and tell for us.
25:16
Of course. It was fun being here. Thank
25:17
you so much, Craig.
25:18
I appreciate it, Matt. Till next time.
