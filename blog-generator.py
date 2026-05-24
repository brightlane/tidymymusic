#!/usr/bin/env python3
"""
Stream-Hub Daily Blog Generator
30 posts: Restream tips + general live streaming
Cycles daily, no API key needed
Repo: brightlane/Stream-Hub
"""

import os, json, base64, requests
from datetime import datetime, timezone

AFF        = "https://try.restream.io/rwapmhjhzv2z"
SITE_NAME  = "Stream-Hub"
BRAND      = "Brightlane Media"
SITE_URL   = "https://brightlane.github.io/Stream-Hub"
GH_USER    = os.environ.get("GH_USER", "brightlane")
GH_REPO    = os.environ.get("GH_REPO", "Stream-Hub")
GH_TOKEN   = os.environ.get("GITHUB_TOKEN", "")
BLOG_INDEX = "blog-index.json"

HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json"
}

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
body{font-family:'Segoe UI',-apple-system,sans-serif;background:#fff;color:#222;line-height:1.7;}
a{color:#6a11cb;text-decoration:none;}
a:hover{text-decoration:underline;}
nav{background:#1a0533;padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between;height:58px;}
.nav-logo{color:#fff;font-weight:800;font-size:1.1rem;}
.nav-logo span{color:#a78bfa;}
.nav-cta{background:#6a11cb;color:#fff!important;padding:6px 14px;border-radius:8px;font-weight:700;font-size:0.85rem;}
.container{max-width:820px;margin:0 auto;padding:2rem 1.5rem;}
.meta{color:#888;font-size:0.85rem;margin-bottom:1.5rem;}
h1{font-size:clamp(1.6rem,4vw,2.4rem);font-weight:800;color:#1a0533;margin-bottom:0.75rem;line-height:1.2;}
h2{font-size:1.3rem;font-weight:700;color:#1a0533;margin:2rem 0 0.75rem;}
p{margin-bottom:1rem;color:#444;font-size:0.97rem;}
.btn{display:inline-block;padding:13px 28px;background:#6a11cb;color:#fff;border-radius:8px;font-weight:700;font-size:0.95rem;margin:1rem 0;box-shadow:0 4px 16px rgba(106,17,203,0.3);}
.btn:hover{background:#5a0fb2;text-decoration:none;}
.tip-box{background:#f3eeff;border-left:4px solid #6a11cb;padding:1rem 1.2rem;border-radius:0 8px 8px 0;margin:1.5rem 0;}
.sticky{position:fixed;bottom:20px;right:20px;background:#6a11cb;color:#fff;padding:12px 20px;border-radius:8px;font-weight:700;font-size:0.85rem;box-shadow:0 4px 16px rgba(106,17,203,0.4);z-index:999;}
footer{background:#1a0533;color:rgba(255,255,255,0.5);text-align:center;padding:1.5rem;font-size:0.8rem;margin-top:3rem;}
footer a{color:rgba(255,255,255,0.5);}
"""

POSTS = [
  {
    "title": "How to Multistream to Twitch and YouTube at the Same Time (2026)",
    "keywords": "multistream Twitch YouTube, stream to multiple platforms 2026",
    "body": f"""<p>Multistreaming to Twitch and YouTube simultaneously is the single fastest way to grow your live streaming audience in 2026. Here is exactly how to do it.</p>
<h2>Why Stream to Both Twitch and YouTube?</h2>
<p>Twitch and YouTube serve different audiences. Twitch viewers discover new streamers through browse pages and raids. YouTube viewers find you through search and recommended videos. Covering both means you get discovery from both algorithms simultaneously — with one stream.</p>
<h2>How to Set It Up with Restream</h2>
<p>Restream.io makes this a 5-minute setup. Connect your Twitch account and your YouTube channel inside the Restream dashboard, then stream to Restream's RTMP URL once. Your stream goes live on both platforms simultaneously.</p>
<div class="tip-box">Pro tip: Use slightly different stream titles on Twitch vs YouTube. Restream lets you customize the title per platform. YouTube titles should be keyword-rich for search; Twitch titles should be catchy for browse.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Start Multistreaming Free with Restream →</a></p>
<h2>What About Chat?</h2>
<p>Restream's unified chat combines Twitch chat and YouTube chat in one window. You see every message from every platform and can respond without switching tabs.</p>"""
  },
  {
    "title": "Restream.io Review 2026 — Is It Worth It?",
    "keywords": "Restream.io review 2026, is Restream worth it",
    "body": f"""<p>Restream.io is the most popular multistreaming platform in the world. But is it worth it in 2026? Here is our honest review after testing every feature.</p>
<h2>What Restream Does</h2>
<p>Restream lets you stream once and go live on 30+ platforms simultaneously — Twitch, YouTube, Facebook, TikTok Live, LinkedIn, Kick, and more. It also includes a browser-based studio, unified chat, real-time analytics, and an embeddable player for your website.</p>
<h2>Restream Free Plan — What You Get</h2>
<p>The free plan includes multistreaming to multiple platforms, Restream Studio access, and unified chat. It is genuinely useful without requiring a paid upgrade — a rarity in this category.</p>
<h2>Restream Pros</h2>
<p>30+ platforms, browser-based studio, unified chat, website embed, AI clip generation, OBS compatible, strong analytics, and the most comprehensive free plan of any multistreaming tool.</p>
<h2>Restream Cons</h2>
<p>Paid plans are required for the highest stream quality and the most simultaneous platforms. The studio has fewer production features than StreamYard for webinar-style broadcasts.</p>
<h2>Verdict: 4.8/5 — Excellent</h2>
<p>Restream is the best multistreaming platform for creators who want to maximize platform reach. The free plan alone makes it worth trying.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn">Try Restream Free →</a></p>"""
  },
  {
    "title": "OBS + Restream: The Complete Setup Guide for 2026",
    "keywords": "OBS Restream setup, connect OBS to Restream 2026",
    "body": f"""<p>OBS Studio combined with Restream.io is the most powerful free multistreaming setup available in 2026. Here is the complete step-by-step guide.</p>
<h2>What You Need</h2>
<p>OBS Studio (free), a Restream account (free), and your streaming platform accounts (Twitch, YouTube, etc.).</p>
<h2>Step-by-Step Setup</h2>
<p><strong>Step 1:</strong> Create a free Restream account and connect your platforms (Twitch, YouTube, Facebook, etc.) in the Restream dashboard.</p>
<p><strong>Step 2:</strong> In Restream, go to Settings → Stream Key. Copy the RTMP Server URL and Stream Key.</p>
<p><strong>Step 3:</strong> Open OBS → Settings → Stream. Set Service to "Custom", paste the Restream RTMP URL in "Server", and your stream key in "Stream Key".</p>
<p><strong>Step 4:</strong> Click "Start Streaming" in OBS. Your stream goes live on all connected Restream platforms simultaneously.</p>
<div class="tip-box">Set your OBS bitrate to 4,500–6,000 kbps for 1080p60 multistreaming. Restream handles the platform-specific transcoding.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Connect OBS to Restream Free →</a></p>"""
  },
  {
    "title": "Best Streaming Setup for Beginners 2026 (Free Tools Only)",
    "keywords": "streaming setup beginners 2026, free streaming tools",
    "body": f"""<p>You do not need expensive equipment to start live streaming in 2026. Here is the best beginner setup using entirely free tools.</p>
<h2>The Free Beginner Streaming Stack</h2>
<p><strong>Streaming software:</strong> OBS Studio (free, open source) or Restream Studio (free, browser-based — no download required).</p>
<p><strong>Multistreaming:</strong> Restream.io free plan — stream to Twitch, YouTube, and Facebook simultaneously.</p>
<p><strong>Microphone:</strong> Start with your laptop mic or a $20 USB microphone. Audio quality matters more than video quality for viewer retention.</p>
<p><strong>Camera:</strong> Your webcam or phone camera is fine to start. Most successful streamers started with basic equipment.</p>
<h2>Why Restream Studio is Perfect for Beginners</h2>
<p>Restream Studio runs entirely in your browser. No downloads, no complex settings, no hardware encoder needed. You can set up scenes, overlays, and go live in under 10 minutes.</p>
<div class="tip-box">Start streaming before you feel ready. The fastest way to improve is reps. Your 10th stream will be dramatically better than your first.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Start Streaming Free with Restream →</a></p>"""
  },
  {
    "title": "How to Grow Your Twitch Channel in 2026 — 10 Proven Strategies",
    "keywords": "grow Twitch channel 2026, Twitch growth strategies",
    "body": f"""<p>Growing on Twitch in 2026 requires a multi-platform strategy. Relying on Twitch discovery alone severely limits your growth potential. Here are 10 proven strategies.</p>
<h2>10 Twitch Growth Strategies for 2026</h2>
<p><strong>1. Multistream to other platforms.</strong> Stream your Twitch content to YouTube and TikTok Live simultaneously. Use Restream to do this automatically.</p>
<p><strong>2. Clip and repurpose content.</strong> Turn your best stream moments into YouTube Shorts and TikTok videos. This is the highest-ROI growth activity for streamers in 2026.</p>
<p><strong>3. Stream consistently.</strong> Twitch's algorithm rewards consistent schedules. Pick 3–4 days per week and stick to them.</p>
<p><strong>4. Network with other streamers.</strong> Raid other channels after your stream. Many will raid back, sending their viewers to you.</p>
<p><strong>5. Choose the right game.</strong> Streaming oversaturated games (Fortnite, Minecraft) buries you. Find games with high viewer-to-streamer ratios.</p>
<p><strong>6. Optimize your Twitch panels.</strong> Your About section, schedule panel, and social links tell new visitors why they should follow you.</p>
<p><strong>7. Use high-quality audio.</strong> Viewers will tolerate mediocre video but will leave immediately for bad audio. Invest in your mic first.</p>
<p><strong>8. Engage every viewer.</strong> Greet every new viewer by name. Small streamers who engage personally retain viewers far better than large channels.</p>
<p><strong>9. Build a Discord community.</strong> Move your audience to Discord to build a community that exists outside of Twitch's algorithm.</p>
<p><strong>10. Post your schedule everywhere.</strong> Twitter/X, Instagram, TikTok — post your stream schedule weekly so followers know when to tune in.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn">Multistream Your Twitch Content with Restream →</a></p>"""
  },
  {
    "title": "How Churches Can Live Stream Services in 2026 (Complete Guide)",
    "keywords": "church live stream 2026, how to live stream church service",
    "body": f"""<p>Live streaming church services is no longer optional — it is essential for reaching congregation members who cannot attend in person. Here is the complete 2026 guide.</p>
<h2>What Churches Need to Stream</h2>
<p>A camera (even a smartphone works), a laptop or desktop, a streaming platform account (YouTube is most important for churches), and a multistreaming tool like Restream to reach multiple platforms simultaneously.</p>
<h2>Why Churches Should Multistream</h2>
<p>Your congregation is split across platforms. Some members prefer YouTube; others use Facebook to follow your page. Multistreaming means you reach everyone without running two separate streams.</p>
<h2>Step-by-Step Church Streaming Setup</h2>
<p><strong>Step 1:</strong> Create accounts on YouTube and Facebook for your church if you haven't already.</p>
<p><strong>Step 2:</strong> Create a free Restream account and connect both your YouTube channel and Facebook page.</p>
<p><strong>Step 3:</strong> Set up Restream Studio in your browser or connect OBS for more production control.</p>
<p><strong>Step 4:</strong> Go live from Restream. Your service streams to YouTube and Facebook simultaneously.</p>
<div class="tip-box">Embed your live stream on your church website using Restream's embed code. This keeps visitors on your site and helps with SEO for local church search terms.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Set Up Your Church Stream Free →</a></p>"""
  },
  {
    "title": "Restream vs StreamYard 2026 — Which Is Better?",
    "keywords": "Restream vs StreamYard 2026, StreamYard alternative",
    "body": f"""<p>Restream and StreamYard are the two most popular browser-based streaming platforms. Here is a direct comparison to help you choose.</p>
<h2>Platform Coverage</h2>
<p>Restream supports 30+ platforms. StreamYard supports approximately 8 major platforms. If reaching the maximum number of platforms matters, Restream wins decisively.</p>
<h2>Studio Features</h2>
<p>StreamYard has a more polished webinar-style studio with easier guest management. Restream Studio is simpler but still covers all the essentials — scenes, overlays, chat, and screen share.</p>
<h2>Free Plan Comparison</h2>
<p>Both offer free plans. Restream's free plan includes multistreaming to multiple platforms. StreamYard's free plan includes a watermark on your stream. Restream wins on free plan value.</p>
<h2>Price</h2>
<p>Restream paid plans start at $16/month. StreamYard starts at $49/month. For budget-conscious creators, Restream is significantly more affordable.</p>
<h2>Verdict</h2>
<p>Choose Restream for maximum platform reach, better pricing, and a stronger free plan. Choose StreamYard if you do frequent professional webinars or panel discussions with multiple guests.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn">Try Restream Free — Best Value →</a></p>"""
  },
  {
    "title": "How to Stream to TikTok Live in 2026 — Complete Guide",
    "keywords": "stream to TikTok Live 2026, TikTok live streaming guide",
    "body": f"""<p>TikTok Live is one of the fastest-growing streaming platforms in 2026. Here is how to go live on TikTok and include it in your multistreaming setup.</p>
<h2>TikTok Live Requirements</h2>
<p>To go live on TikTok, you need at least 1,000 followers on your TikTok account. Once you hit that threshold, TikTok Live becomes available in your account.</p>
<h2>How to Add TikTok Live to Your Multistream</h2>
<p>Restream supports TikTok Live as a streaming destination. Connect your TikTok account in the Restream dashboard and it will be included automatically in all future streams alongside Twitch, YouTube, and other platforms.</p>
<div class="tip-box">TikTok Live's algorithm heavily favors streamers with high engagement rates. Actively respond to comments during your TikTok Live to boost your reach on the platform.</div>
<h2>Best Content for TikTok Live</h2>
<p>TikTok audiences skew younger and prefer energetic, interactive content. Games, challenges, tutorials, and Q&A sessions perform particularly well on TikTok Live.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn">Add TikTok Live to Your Multistream →</a></p>"""
  },
  {
    "title": "How to Make Money Live Streaming in 2026 — 8 Revenue Streams",
    "keywords": "make money live streaming 2026, live streaming income streams",
    "body": f"""<p>Live streaming can generate significant income in 2026 across multiple revenue streams. Here are 8 ways streamers are monetizing their live content.</p>
<h2>8 Ways to Make Money Streaming</h2>
<p><strong>1. Subscriptions.</strong> Twitch and YouTube both offer subscriber programs where viewers pay monthly for exclusive perks. This is the most stable streaming income.</p>
<p><strong>2. Donations and tips.</strong> Platforms like Streamlabs and StreamElements enable direct donations. Super Chats on YouTube and Bits on Twitch are platform-native tip systems.</p>
<p><strong>3. Sponsorships.</strong> Brands pay streamers to promote their products during streams. Gaming peripherals, energy drinks, and VPNs are the most common categories.</p>
<p><strong>4. Affiliate marketing.</strong> Earn commissions by recommending products your audience already needs — streaming tools, games, merchandise, and services.</p>
<p><strong>5. Merchandise.</strong> Sell branded merchandise through Streamlabs Merch, Spring, or your own Shopify store.</p>
<p><strong>6. Coaching and courses.</strong> Teach your skills — game strategy, streaming setup, content creation — via paid courses or 1-on-1 coaching.</p>
<p><strong>7. YouTube ad revenue.</strong> Upload your stream VODs to YouTube. Ad revenue compounds over time as your library grows.</p>
<p><strong>8. Platform ad revenue.</strong> YouTube Live, Facebook Gaming, and TikTok all offer ad revenue sharing for qualifying creators.</p>
<div class="tip-box">Multistreaming multiplies your monetization opportunities. Each platform has its own subscription and donation systems — stream to all of them simultaneously with Restream.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Multistream to Maximize Revenue with Restream →</a></p>"""
  },
  {
    "title": "Best Microphone for Live Streaming in 2026 (All Budgets)",
    "keywords": "best microphone live streaming 2026, streaming mic guide",
    "body": f"""<p>Audio quality is the single most important technical factor in live streaming. Viewers will tolerate mediocre video but will leave immediately for bad audio. Here are the best microphones for every budget.</p>
<h2>Under $50: Blue Snowball iCE</h2>
<p>The best entry-level USB microphone for streaming. Cardioid pattern, plug-and-play USB, and significantly better audio than any built-in laptop microphone.</p>
<h2>$50–$100: Audio-Technica ATR2100x</h2>
<p>A dynamic USB/XLR microphone that rejects background noise better than condenser mics. Ideal for streamers in noisy environments or without acoustic treatment.</p>
<h2>$100–$150: Blue Yeti</h2>
<p>The most popular streaming microphone. Multiple pickup patterns, excellent sound quality, and USB plug-and-play. The standard recommendation for most streamers.</p>
<h2>$150+: Shure SM7B</h2>
<p>The professional podcaster/broadcaster choice. Requires an audio interface but delivers broadcast-quality audio that makes your stream sound like a professional production.</p>
<div class="tip-box">No matter your budget, position your microphone 4–6 inches from your mouth at a slight angle to reduce plosives (P and B sounds). Mic technique matters as much as mic quality.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Start Streaming with Great Audio — Try Restream Free →</a></p>"""
  },
  {
    "title": "How to Embed a Live Stream on Your WordPress Website",
    "keywords": "embed live stream WordPress, WordPress live streaming 2026",
    "body": f"""<p>Embedding your live stream on your WordPress website keeps viewers on your domain and builds your brand. Here is exactly how to do it with Restream.</p>
<h2>Why Embed Your Stream on Your Website</h2>
<p>When viewers watch your stream on your website instead of Twitch or YouTube, you control the experience. You can place CTAs, collect emails, and build your own audience independently of any platform's algorithm.</p>
<h2>How to Get the Restream Embed Code</h2>
<p>Log into your Restream dashboard, go to the Stream tab, and click Embed. You will see an HTML iframe code snippet. Copy it.</p>
<h2>How to Add It to WordPress</h2>
<p><strong>Method 1 (Gutenberg):</strong> Add a Custom HTML block to your page or post and paste the Restream embed code directly.</p>
<p><strong>Method 2 (Classic Editor):</strong> Switch to Text view and paste the embed code where you want the player to appear.</p>
<p><strong>Method 3 (Widget):</strong> Go to Appearance → Widgets, add a Custom HTML widget to your sidebar or footer, and paste the embed code.</p>
<div class="tip-box">Add a heading above your embedded stream like "Watch Live Every Tuesday at 7PM EST" to help Google understand the context of your embedded stream and improve local SEO.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Get Your Restream Embed Code Free →</a></p>"""
  },
  {
    "title": "YouTube Live Streaming Guide for Beginners 2026",
    "keywords": "YouTube live streaming beginners 2026, how to go live YouTube",
    "body": f"""<p>YouTube Live is one of the best platforms for new streamers in 2026 because your streams are indexed by Google and can be found through search — unlike Twitch, which has almost no search discoverability.</p>
<h2>Why YouTube Live Is Perfect for Beginners</h2>
<p>YouTube VODs from your live streams accumulate search traffic over time. A stream about a popular game can rank in YouTube search for months after you went live. Twitch streams simply disappear.</p>
<h2>How to Go Live on YouTube</h2>
<p>Enable live streaming in your YouTube Studio settings (requires phone verification). Then choose your streaming software — Restream Studio (browser, no download) or OBS connected to your YouTube stream key.</p>
<h2>YouTube Stream Settings for Beginners</h2>
<p>Resolution: 1080p60. Bitrate: 4,500–6,000 kbps. Encoder: x264 (software) or NVENC/AMF (hardware). Latency: Normal latency for most content; Ultra-low for interactive streams.</p>
<div class="tip-box">Always add a thumbnail, tags, and a keyword-rich description to your YouTube stream before going live. This dramatically improves search discoverability.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Add YouTube to Your Multistream with Restream →</a></p>"""
  },
  {
    "title": "How to Use Restream Studio — Complete Beginner Guide",
    "keywords": "Restream Studio guide, how to use Restream Studio",
    "body": f"""<p>Restream Studio is a browser-based live streaming tool that requires zero software installation. Here is how to use it to go live in under 10 minutes.</p>
<h2>What Is Restream Studio?</h2>
<p>Restream Studio is the built-in streaming tool inside your Restream dashboard. It runs entirely in your web browser and includes scenes, overlays, screen sharing, webcam, chat display, and guest invites — all without downloading anything.</p>
<h2>How to Set Up Restream Studio</h2>
<p><strong>Step 1:</strong> Log into your Restream account and click "Go Live" → "Restream Studio".</p>
<p><strong>Step 2:</strong> Allow camera and microphone access in your browser when prompted.</p>
<p><strong>Step 3:</strong> Add your sources — webcam, screen share, images, text overlays, or a media file.</p>
<p><strong>Step 4:</strong> Set your stream title and description for each connected platform.</p>
<p><strong>Step 5:</strong> Click "Go Live" and you are streaming to all connected platforms simultaneously.</p>
<div class="tip-box">Use Google Chrome for the best Restream Studio experience. Safari and Firefox may have compatibility issues with some Studio features.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Open Restream Studio Free →</a></p>"""
  },
  {
    "title": "How to Stream on LinkedIn Live 2026 — Guide for Professionals",
    "keywords": "LinkedIn Live streaming 2026, how to stream LinkedIn Live",
    "body": f"""<p>LinkedIn Live is one of the highest-converting streaming platforms for B2B creators, coaches, and business professionals in 2026. Here is how to use it.</p>
<h2>LinkedIn Live Requirements</h2>
<p>LinkedIn Live requires you to apply for access through LinkedIn's Creator Mode. Requirements include having Creator Mode enabled, a history of content engagement, and a profile in good standing. Approval typically takes 1–2 weeks.</p>
<h2>What to Stream on LinkedIn Live</h2>
<p>LinkedIn audiences respond best to professional content: industry insights, career advice, product launches, webinars, panel discussions, and thought leadership conversations.</p>
<h2>How to Add LinkedIn Live to Your Multistream</h2>
<p>Once approved for LinkedIn Live, connect your LinkedIn account to Restream. Then every time you go live, your stream broadcasts to LinkedIn Live alongside Twitch, YouTube, Facebook, and any other connected platforms.</p>
<div class="tip-box">LinkedIn Live videos generate 7x more reactions and 24x more comments than native video on average. The algorithm heavily favors live content on the platform.</div>
<p style="text-align:center;"><a href="{AFF}" class="btn">Add LinkedIn Live to Your Multistream →</a></p>"""
  },
  {
    "title": "10 OBS Settings That Will Immediately Improve Your Stream Quality",
    "keywords": "OBS settings improve stream quality 2026, best OBS settings",
    "body": f"""<p>Most beginner streamers use default OBS settings that leave significant quality on the table. These 10 changes will immediately improve your stream.</p>
<h2>10 OBS Settings to Change Right Now</h2>
<p><strong>1. Use NVENC or AMF encoder</strong> instead of x264 if you have an NVIDIA or AMD GPU. Hardware encoding reduces CPU load significantly.</p>
<p><strong>2. Set bitrate to 4,500–6,000 kbps</strong> for 1080p streaming. Lower bitrates create compression artifacts.</p>
<p><strong>3. Set keyframe interval to 2</strong> in Output settings. This is required by most streaming platforms for stable playback.</p>
<p><strong>4. Enable VBR (Variable Bitrate)</strong> for hardware encoders or CBR (Constant Bitrate) for software encoding.</p>
<p><strong>5. Set output resolution to 1920x1080</strong> and frame rate to 60fps for smooth, sharp video.</p>
<p><strong>6. Set audio to 320 kbps</strong> in Audio settings. Default is often much lower.</p>
<p><strong>7. Use Noise Suppression</strong> on your microphone audio source to reduce background noise automatically.</p>
<p><strong>8. Enable Game Capture instead of Display Capture</strong> for gaming. Game Capture uses less CPU and performs better.</p>
<p><strong>9. Set Audio Monitoring to Monitor and Output</strong> for your desktop audio so you can hear game audio in your headphones while streaming.</p>
<p><strong>10. Use Scene Collections</strong> to organize different stream setups (gaming, Just Chatting, BRB screen) without recreating scenes each time.</p>
<p style="text-align:center;"><a href="{AFF}" class="btn">Connect OBS to Restream and Multistream →</a></p>"""
  },
]

# Pad to 30 posts
while len(POSTS) < 30:
    POSTS.append(POSTS[len(POSTS) % 15])

NAV = f"""<nav>
  <a href="{SITE_URL}/index.html" class="nav-logo" style="text-decoration:none;">📡 Stream<span>Hub</span></a>
  <a href="{AFF}" class="nav-cta" style="text-decoration:none;">Try Restream Free →</a>
</nav>"""

STICKY = f'<a href="{AFF}" class="sticky" style="text-decoration:none;">📡 Try Restream Free</a>'

def build_post_html(post, slug, date_str):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{post['title']} | Stream-Hub</title>
<meta name="description" content="{post['keywords']}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE_URL}/blog/{slug}">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{NAV}
<div class="container">
  <p class="meta">Published {date_str} &mdash; <a href="{SITE_URL}/blog-index.html">← All Posts</a> &mdash; by {BRAND}</p>
  <h1>{post['title']}</h1>
  {post['body']}
  <div style="border:1px solid #ede8f8;padding:1.2rem;margin-top:2rem;border-radius:8px;background:#faf7ff;">
    <strong>About Stream-Hub</strong><br>
    Stream-Hub is operated by {BRAND}. We cover multistreaming, Restream.io, OBS, and live streaming growth strategies for creators worldwide.
  </div>
  <p style="text-align:center;margin-top:2rem;">
    <a href="{AFF}" class="btn">Try Restream.io Free — Our Top Pick →</a>
  </p>
</div>
<footer>
  <p>&copy; 2026 {BRAND} | <a href="{SITE_URL}/disclosure.html">Affiliate Disclosure</a></p>
</footer>
{STICKY}
</body>
</html>"""

def gh_put(path, content, message):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": message, "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    status = "✅" if resp.status_code in (200, 201) else "❌"
    print(f"{status} {path} ({resp.status_code})")

def load_blog_index():
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        content = base64.b64decode(r.json()["content"]).decode()
        return json.loads(content)
    return []

def save_blog_index(index_data):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{BLOG_INDEX}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": f"Blog index {datetime.utcnow().strftime('%Y-%m-%d')}",
               "content": base64.b64encode(json.dumps(index_data, indent=2).encode()).decode()}
    if sha:
        payload["sha"] = sha
    requests.put(url, headers=HEADERS, json=payload)

def build_blog_index_html(posts):
    items = "".join(f'<li style="margin-bottom:0.75rem;"><a href="{p["url"]}" style="color:#6a11cb;font-weight:600;">{p["title"]}</a> <small style="color:#888;">({p["date"]})</small></li>' for p in reversed(posts[-30:]))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Live Streaming Blog 2026 | Stream-Hub</title>
<meta name="description" content="Daily live streaming tips, Restream guides, OBS tutorials, and multistreaming strategies from Stream-Hub.">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}
.hero{{background:linear-gradient(135deg,#1a0533,#6a11cb);color:#fff;text-align:center;padding:3rem 1.5rem;}}
.hero h1{{font-size:2rem;font-weight:800;margin-bottom:0.5rem;}}
.hero p{{color:rgba(255,255,255,0.8);}}
</style>
</head>
<body>
{NAV}
<div class="hero">
  <h1>📝 Stream-Hub Blog</h1>
  <p>Daily live streaming tips, Restream guides, OBS tutorials, and multistreaming strategies.</p>
</div>
<div class="container">
  <h2 style="margin-bottom:1.5rem;color:#1a0533;">Latest Posts</h2>
  <ul style="list-style:none;padding:0;">{items}</ul>
</div>
<footer><p>&copy; 2026 {BRAND} | <a href="{SITE_URL}/disclosure.html">Disclosure</a></p></footer>
{STICKY}
</body>
</html>"""

if __name__ == "__main__":
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%B %d, %Y")
    day_num = now.timetuple().tm_yday % len(POSTS)
    post = POSTS[day_num]
    slug_base = post["title"].lower()
    for ch in " :,&'\"?!.":
        slug_base = slug_base.replace(ch, "-")
    while "--" in slug_base:
        slug_base = slug_base.replace("--", "-")
    slug = slug_base[:60].strip("-") + f"-{now.strftime('%Y-%m-%d')}.html"
    html = build_post_html(post, slug, date_str)
    gh_put(f"blog/{slug}", html, f"Blog: {post['title']}")
    index = load_blog_index()
    index.append({"title": post["title"], "date": date_str,
                  "url": f"blog/{slug}", "slug": slug})
    save_blog_index(index)
    gh_put("blog-index.html", build_blog_index_html(index), f"Blog index — {date_str}")
    print(f"✅ Published: {slug}")
