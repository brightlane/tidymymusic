#!/usr/bin/env python3
"""
Stream-Hub Site Builder
18 SEO pages for Restream.io affiliate site
Repo: brightlane/Stream-Hub
Affiliate: https://try.restream.io/rwapmhjhzv2z
"""

import os, base64, requests
from datetime import datetime

AFF       = "https://try.restream.io/rwapmhjhzv2z"
SITE_NAME = "Stream-Hub"
BRAND     = "Brightlane Media"
SITE_URL  = "https://brightlane.github.io/Stream-Hub"
GH_USER   = os.environ.get("GH_USER", "brightlane")
GH_REPO   = os.environ.get("GH_REPO", "Stream-Hub")
GH_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
GVERIFY   = "eWVDN3vbam9nnaZQu7wAQKyfmJJdM7zjI80l4DGeUrQ"

HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json"
}

CSS = """
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
html{scroll-behavior:smooth;}
body{font-family:'Segoe UI',-apple-system,BlinkMacSystemFont,Roboto,sans-serif;background:#fff;color:#222;line-height:1.7;-webkit-font-smoothing:antialiased;}
a{text-decoration:none;color:inherit;}
nav{background:#1a0533;padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between;height:62px;position:sticky;top:0;z-index:100;box-shadow:0 2px 16px rgba(106,17,203,0.25);}
.nav-logo{color:#fff;font-weight:800;font-size:1.15rem;display:flex;align-items:center;gap:8px;}
.nav-logo span{color:#a78bfa;}
.nav-links{display:flex;gap:1.5rem;}
.nav-links a{color:rgba(255,255,255,0.75);font-size:0.85rem;font-weight:600;transition:color 0.2s;}
.nav-links a:hover{color:#fff;}
.nav-cta{background:#6a11cb;color:#fff!important;padding:7px 16px;border-radius:8px;font-weight:700!important;box-shadow:0 2px 8px rgba(106,17,203,0.4);}
.nav-cta:hover{background:#5a0fb2!important;}
.hero{background:linear-gradient(135deg,#1a0533 0%,#2d0b69 50%,#6a11cb 100%);color:#fff;text-align:center;padding:5rem 1.5rem 4rem;position:relative;overflow:hidden;}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(167,139,250,0.15),transparent);}
.hero-badge{display:inline-block;background:rgba(167,139,250,0.2);border:1px solid rgba(167,139,250,0.4);color:#c4b5fd;padding:5px 16px;border-radius:50px;font-size:0.78rem;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:1.2rem;position:relative;}
.hero h1{font-size:clamp(1.9rem,5vw,3.4rem);font-weight:800;line-height:1.1;margin-bottom:1rem;position:relative;text-shadow:0 2px 16px rgba(0,0,0,0.4);}
.hero h1 em{color:#a78bfa;font-style:normal;}
.hero p{font-size:1.05rem;color:rgba(255,255,255,0.8);max-width:580px;margin:0 auto 2rem;position:relative;}
.btn{display:inline-block;padding:14px 32px;border-radius:8px;font-weight:700;font-size:1rem;transition:transform 0.2s,box-shadow 0.2s;}
.btn-purple{background:#6a11cb;color:#fff;box-shadow:0 6px 24px rgba(106,17,203,0.4);}
.btn-purple:hover{transform:translateY(-2px);box-shadow:0 10px 32px rgba(106,17,203,0.5);background:#5a0fb2;}
.btn-outline{border:2px solid rgba(255,255,255,0.35);color:#fff;margin-left:1rem;}
.btn-outline:hover{background:rgba(255,255,255,0.1);}
.hero-stats{display:flex;justify-content:center;gap:3rem;margin-top:3.5rem;flex-wrap:wrap;position:relative;}
.stat-num{font-size:1.9rem;font-weight:800;color:#a78bfa;}
.stat-label{font-size:0.72rem;color:rgba(255,255,255,0.5);text-transform:uppercase;letter-spacing:0.08em;}
.section{padding:4.5rem 1.5rem;}
.section-alt{background:#f9fafb;border-top:1px solid #e8e8e8;border-bottom:1px solid #e8e8e8;}
.container{max-width:1050px;margin:0 auto;}
.section-tag{font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;color:#6a11cb;margin-bottom:0.5rem;}
.section-title{font-size:clamp(1.5rem,3vw,2.2rem);font-weight:800;color:#1a0533;margin-bottom:0.75rem;line-height:1.2;}
.section-sub{color:#555;margin-bottom:2.5rem;max-width:600px;font-size:1.02rem;}
.center{text-align:center;}
.center .section-sub{margin-left:auto;margin-right:auto;}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.5rem;margin-bottom:2rem;}
.card{background:#fff;border-radius:14px;padding:2rem;box-shadow:0 4px 20px rgba(0,0,0,0.07);border:1px solid #ede8f8;transition:transform 0.25s,box-shadow 0.25s;display:block;}
.card:hover{transform:translateY(-6px);box-shadow:0 12px 36px rgba(106,17,203,0.12);}
.card-icon{font-size:2rem;margin-bottom:0.8rem;}
.card h3{font-size:1rem;font-weight:700;color:#1a0533;margin-bottom:0.5rem;}
.card p{font-size:0.88rem;color:#555;margin-bottom:1rem;}
.card-link{font-size:0.82rem;font-weight:700;color:#6a11cb;}
.tips{display:grid;gap:1rem;}
.tip{display:flex;gap:1rem;background:#fff;padding:1.2rem 1.5rem;border-radius:12px;box-shadow:0 2px 12px rgba(0,0,0,0.06);border-left:4px solid #6a11cb;}
.tip-n{font-size:1.2rem;font-weight:800;color:#6a11cb;min-width:28px;}
.tip-t strong{display:block;font-size:0.95rem;color:#1a0533;margin-bottom:0.2rem;}
.tip-t span{font-size:0.87rem;color:#666;}
.compare-wrap{overflow-x:auto;}
table{width:100%;border-collapse:collapse;margin:1rem 0 2rem;}
th,td{padding:0.9rem 1rem;text-align:left;border-bottom:1px solid #ede8f8;font-size:0.9rem;}
th{background:#f3eeff;color:#1a0533;font-weight:700;}
tr:hover td{background:#faf7ff;}
.yes{color:#16a34a;font-weight:700;}
.no{color:#ccc;}
.best{background:#6a11cb;color:#fff;font-size:0.65rem;font-weight:700;padding:2px 7px;border-radius:50px;margin-left:5px;vertical-align:middle;}
.faqs{display:grid;gap:1rem;}
.faq{background:#fff;border-radius:12px;padding:1.3rem 1.5rem;box-shadow:0 2px 12px rgba(0,0,0,0.06);border:1px solid #ede8f8;}
.faq-q{font-weight:700;color:#1a0533;margin-bottom:0.4rem;}
.faq-a{font-size:0.9rem;color:#555;}
.cta-band{background:linear-gradient(135deg,#1a0533,#6a11cb);color:#fff;text-align:center;padding:4rem 1.5rem;margin:2rem 0;}
.cta-band h2{font-size:clamp(1.4rem,3vw,2rem);font-weight:800;margin-bottom:0.75rem;}
.cta-band p{color:rgba(255,255,255,0.8);margin-bottom:2rem;}
.sticky{position:fixed;bottom:20px;right:20px;background:#6a11cb;color:#fff;padding:13px 22px;border-radius:8px;font-weight:700;font-size:0.88rem;box-shadow:0 6px 20px rgba(106,17,203,0.5);z-index:999;transition:transform 0.2s;}
.sticky:hover{transform:scale(1.05);background:#5a0fb2;}
footer{background:#1a0533;color:rgba(255,255,255,0.5);text-align:center;padding:2rem 1.5rem;font-size:0.82rem;}
footer a{color:rgba(255,255,255,0.5);}
footer a:hover{color:#a78bfa;}
.disclosure{font-size:0.78rem;color:#999;text-align:center;padding:1rem;border-top:1px solid #ede8f8;background:#fff;}
.fade{opacity:0;transform:translateY(20px);transition:opacity 0.6s ease,transform 0.6s ease;}
.fade.on{opacity:1;transform:none;}
.platform-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:1rem;margin-bottom:2rem;}
.platform{background:#fff;border-radius:12px;padding:1rem;text-align:center;box-shadow:0 2px 12px rgba(0,0,0,0.06);border:1px solid #ede8f8;display:block;transition:transform 0.2s;}
.platform:hover{transform:translateY(-3px);}
.platform-icon{font-size:1.8rem;margin-bottom:0.3rem;}
.platform-name{font-weight:700;color:#1a0533;font-size:0.85rem;}
@media(max-width:768px){.nav-links{display:none;}.hero-stats{gap:1.5rem;}.btn-outline{display:none;}}
"""

JS = """
const faders=document.querySelectorAll('.fade');
function check(){faders.forEach(el=>{if(el.getBoundingClientRect().top<window.innerHeight-60)el.classList.add('on');});}
window.addEventListener('scroll',check);
window.addEventListener('load',check);
"""

def nav_html():
    return f"""<nav>
  <a href="{SITE_URL}/index.html" class="nav-logo">📡 Stream<span>Hub</span></a>
  <div class="nav-links">
    <a href="{SITE_URL}/index.html">Home</a>
    <a href="{SITE_URL}/multistreaming.html">Multistream</a>
    <a href="{SITE_URL}/platforms.html">Platforms</a>
    <a href="{SITE_URL}/comparison.html">Compare</a>
    <a href="{SITE_URL}/gamers.html">Gamers</a>
    <a href="{SITE_URL}/churches.html">Churches</a>
    <a href="{SITE_URL}/blog-index.html">Blog</a>
    <a href="{AFF}" class="nav-cta">Try Restream Free →</a>
  </div>
</nav>"""

STICKY_HTML = f'<a href="{AFF}" class="sticky">📡 Try Restream Free</a>'

FOOTER_HTML = f"""<div class="disclosure">This site contains affiliate links. We earn a commission if you sign up through our links at no extra cost to you. &copy; 2026 {BRAND}</div>
<footer>
  <p>&copy; 2026 {BRAND} | Stream-Hub</p>
  <p style="margin-top:0.5rem;">
    <a href="{SITE_URL}/about.html">About</a> &nbsp;|&nbsp;
    <a href="{SITE_URL}/contact.html">Contact</a> &nbsp;|&nbsp;
    <a href="{SITE_URL}/disclosure.html">Disclosure</a> &nbsp;|&nbsp;
    <a href="{SITE_URL}/blog-index.html">Blog</a>
  </p>
</footer>"""

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">'

def page(title, desc, slug, body, schema=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="google-site-verification" content="{GVERIFY}">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="index, follow">
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE_URL}/{slug}">
<meta name="twitter:card" content="summary_large_image">
<title>{title}</title>
<link rel="canonical" href="{SITE_URL}/{slug}">
{FONTS}
{schema}
<style>{CSS}</style>
</head>
<body>
{nav_html()}
{body}
{FOOTER_HTML}
{STICKY_HTML}
<script>{JS}</script>
</body>
</html>"""

def cta_band(h2, p):
    return f"""<div class="cta-band">
  <div class="container">
    <h2>{h2}</h2>
    <p>{p}</p>
    <a href="{AFF}" class="btn btn-purple" style="font-size:1.05rem;padding:16px 36px;">🚀 Start Free Restream Trial</a>
  </div>
</div>"""

PLATFORMS = [
    ("📺","Twitch"),("🎥","YouTube"),("📘","Facebook"),("🎵","TikTok Live"),
    ("💼","LinkedIn"),("🎮","Facebook Gaming"),("🐦","Twitter/X"),("📱","Instagram"),
    ("🎯","Kick"),("🌐","Custom RTMP"),
]

# ═══════════════════════════════════════════════
# PAGE FUNCTIONS
# ═══════════════════════════════════════════════

def page_index():
    platforms = "".join(f'<a href="{AFF}" class="platform"><div class="platform-icon">{e}</div><div class="platform-name">{n}</div></a>' for e,n in PLATFORMS)
    body = f"""
<section class="hero">
  <div class="hero-badge">📡 #1 Multistreaming Platform 2026</div>
  <h1>Stream Once.<br><em>Go Live Everywhere.</em></h1>
  <p>Restream.io lets you broadcast to Twitch, YouTube, Facebook, TikTok Live, LinkedIn, and 30+ platforms simultaneously — from one dashboard.</p>
  <a href="{AFF}" class="btn btn-purple">🚀 Start Free Restream Trial</a>
  <a href="#platforms" class="btn btn-outline">See All Platforms</a>
  <div class="hero-stats">
    <div><div class="stat-num">30+</div><div class="stat-label">Platforms</div></div>
    <div><div class="stat-num">Free</div><div class="stat-label">Plan Available</div></div>
    <div><div class="stat-num">Global</div><div class="stat-label">Reach</div></div>
    <div><div class="stat-num">2M+</div><div class="stat-label">Streamers</div></div>
  </div>
</section>

<section class="section section-alt" id="platforms">
  <div class="container center">
    <div class="section-tag">Supported Platforms</div>
    <h2 class="section-title">Stream to 30+ Platforms Simultaneously</h2>
    <p class="section-sub">One stream. Every platform. Maximum reach.</p>
    <div class="platform-grid fade">{platforms}</div>
    <a href="{AFF}" class="btn btn-purple">See All Supported Platforms →</a>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-tag">Why Restream</div>
    <h2 class="section-title">Everything You Need to Multistream</h2>
    <p class="section-sub">Professional live streaming tools for gamers, churches, coaches, and businesses worldwide.</p>
    <div class="cards fade">
      <a href="{AFF}" class="card"><div class="card-icon">📡</div><h3>Multistream to 30+ Platforms</h3><p>Send one live stream to Twitch, YouTube, Facebook, TikTok, LinkedIn, and more simultaneously from a single dashboard.</p><span class="card-link">Start Multistreaming →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">🎬</div><h3>Browser-Based Studio</h3><p>No software to install. Restream Studio runs in your browser with scenes, overlays, and graphics built in.</p><span class="card-link">Open Studio →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">💬</div><h3>Unified Chat</h3><p>Moderate comments from all platforms in one window. Never miss a message from any audience.</p><span class="card-link">Manage Chat →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">📊</div><h3>Real-Time Analytics</h3><p>Track viewers, watch time, and engagement across every platform in one dashboard.</p><span class="card-link">View Analytics →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">🌐</div><h3>Embed on Your Website</h3><p>Bring your live stream directly to your site with a one-line embed code that updates automatically.</p><span class="card-link">Get Embed Code →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">🤖</div><h3>AI-Powered Tools</h3><p>Auto-generate clips, descriptions, and highlights from your live stream with Restream AI.</p><span class="card-link">Try AI Tools →</span></a>
    </div>
  </div>
</section>

{cta_band("Ready to Go Live Everywhere?","Join 2 million+ streamers using Restream to grow their audience globally.")}

<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Who Uses Restream</div>
    <h2 class="section-title">Built for Every Creator</h2>
    <div class="cards fade">
      <a href="{AFF}" class="card"><div class="card-icon">🎮</div><h3>Gamers & Streamers</h3><p>Stream your gameplay to Twitch, YouTube Gaming, Facebook Gaming, and TikTok simultaneously. Grow everywhere at once.</p><span class="card-link">Gamers Guide →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">⛪</div><h3>Churches & Ministries</h3><p>Broadcast live services to YouTube, Facebook, and your website simultaneously. Reach your congregation wherever they are.</p><span class="card-link">Churches Guide →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">🎓</div><h3>Coaches & Educators</h3><p>Stream live training, Q&A sessions, and classes to multiple platforms and embed them on your site.</p><span class="card-link">Coaches Guide →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">🏢</div><h3>Businesses & Brands</h3><p>Broadcast product launches, webinars, and corporate events across LinkedIn, YouTube, and Facebook simultaneously.</p><span class="card-link">Business Guide →</span></a>
    </div>
  </div>
</section>"""

    schema = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@graph":[
{{"@type":"WebSite","name":"{SITE_NAME}","url":"{SITE_URL}/","publisher":{{"@type":"Organization","name":"{BRAND}"}}}},
{{"@type":"SoftwareApplication","name":"Restream.io","url":"https://restream.io","description":"Multistream live video to Twitch, YouTube, Facebook, TikTok and 30+ platforms from one dashboard.","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD","availability":"https://schema.org/InStock"}}}}
]}}</script>"""
    return page(
        "Restream.io Review 2026 — Stream Once, Go Live Everywhere | Stream-Hub",
        "Restream.io lets you multistream to Twitch, YouTube, Facebook, TikTok, LinkedIn, and 30+ platforms simultaneously. Free trial. Global guide for gamers, churches, coaches, and businesses.",
        "index.html", body, schema)

def page_multistreaming():
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">📡 Multistreaming Guide 2026</div>
  <h1>How to <em>Multistream</em><br>Live Video in 2026</h1>
  <p>The complete guide to streaming once and going live on every platform simultaneously.</p>
  <a href="{AFF}" class="btn btn-purple">🚀 Start Multistreaming Free</a>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">What Is Multistreaming</div>
    <h2 class="section-title">Stream Once, Reach Everyone</h2>
    <p class="section-sub">Multistreaming means broadcasting your live video to multiple platforms at the same time from a single source. Instead of going live on Twitch, then YouTube, then Facebook separately — you do it all simultaneously with one stream.</p>
    <div class="tips fade">
      <div class="tip"><div class="tip-n">01</div><div class="tip-t"><strong>Connect your platforms</strong><span>Link Twitch, YouTube, Facebook, TikTok, LinkedIn, and more to Restream in one click. No technical knowledge required.</span></div></div>
      <div class="tip"><div class="tip-n">02</div><div class="tip-t"><strong>Set up your stream</strong><span>Configure your title, description, and thumbnails for each platform. Use Restream Studio in your browser or connect OBS.</span></div></div>
      <div class="tip"><div class="tip-n">03</div><div class="tip-t"><strong>Go live everywhere</strong><span>Hit stream once and your broadcast goes live on every connected platform simultaneously via RTMP.</span></div></div>
      <div class="tip"><div class="tip-n">04</div><div class="tip-t"><strong>Manage all chats in one window</strong><span>Unified chat lets you see and respond to messages from all platforms without switching tabs.</span></div></div>
      <div class="tip"><div class="tip-n">05</div><div class="tip-t"><strong>Track analytics across platforms</strong><span>See total viewers, watch time, and engagement from every platform in one Restream dashboard.</span></div></div>
    </div>
    <div style="text-align:center;margin-top:2rem;">
      <a href="{AFF}" class="btn btn-purple">Start Multistreaming with Restream Free →</a>
    </div>
  </div>
</section>
{cta_band("Ready to Multistream?","Set up once. Stream everywhere. Grow your audience on every platform simultaneously.")}"""
    return page(
        "How to Multistream Live Video 2026 — Complete Guide | Stream-Hub",
        "Learn how to multistream live video to Twitch, YouTube, Facebook, TikTok, and 30+ platforms simultaneously with Restream.io. Free step-by-step guide.",
        "multistreaming.html", body)

def page_platforms():
    plat_cards = "".join(f"""<a href="{AFF}" class="card">
      <div class="card-icon">{e}</div>
      <h3>Stream to {n}</h3>
      <p>Connect {n} to Restream and go live simultaneously alongside every other platform in your lineup.</p>
      <span class="card-link">Stream to {n} →</span>
    </a>""" for e,n in PLATFORMS)
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">🌐 30+ Platforms</div>
  <h1>Stream to <em>Every Platform</em><br>Simultaneously</h1>
  <p>Restream supports 30+ streaming destinations. Connect them all and go live everywhere at once.</p>
  <a href="{AFF}" class="btn btn-purple">🚀 Connect Your Platforms Free</a>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">All Platforms</div>
    <h2 class="section-title">Every Platform Restream Supports</h2>
    <p class="section-sub">Connect any combination of these platforms and stream to all of them simultaneously.</p>
    <div class="cards fade">{plat_cards}</div>
  </div>
</section>"""
    return page(
        "Restream.io Supported Platforms 2026 — Twitch, YouTube, TikTok & 30+ More | Stream-Hub",
        "See all platforms supported by Restream.io. Stream to Twitch, YouTube, Facebook, TikTok, LinkedIn, and 30+ platforms simultaneously.",
        "platforms.html", body)

def page_comparison():
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">⚖️ Unbiased Comparison</div>
  <h1>Restream vs <em>StreamYard</em><br>vs Streamlabs 2026</h1>
  <p>Which multistreaming platform is right for you? An honest side-by-side comparison.</p>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Feature Comparison</div>
    <h2 class="section-title">Restream.io vs StreamYard vs Streamlabs</h2>
    <div class="compare-wrap fade">
      <table>
        <tr><th>Feature</th><th>Restream.io <span class="best">BEST</span></th><th>StreamYard</th><th>Streamlabs</th></tr>
        <tr><td>Platforms Supported</td><td><span class="yes">30+</span></td><td>8</td><td>15+</td></tr>
        <tr><td>Browser Studio</td><td><span class="yes">✔</span></td><td><span class="yes">✔</span></td><td><span class="no">—</span></td></tr>
        <tr><td>Unified Chat</td><td><span class="yes">✔</span></td><td><span class="yes">✔</span></td><td>Limited</td></tr>
        <tr><td>Website Embed</td><td><span class="yes">✔</span></td><td><span class="yes">✔</span></td><td><span class="no">—</span></td></tr>
        <tr><td>AI Tools</td><td><span class="yes">✔</span></td><td>Limited</td><td>Limited</td></tr>
        <tr><td>Free Plan</td><td><span class="yes">✔</span></td><td><span class="yes">✔</span></td><td><span class="yes">✔</span></td></tr>
        <tr><td>OBS Compatible</td><td><span class="yes">✔</span></td><td><span class="no">—</span></td><td><span class="yes">✔</span></td></tr>
        <tr><td>Cloud Recording</td><td><span class="yes">✔</span></td><td><span class="yes">✔</span></td><td><span class="yes">✔</span></td></tr>
        <tr><td>Best For</td><td><strong>Max platform reach</strong></td><td>Webinars/panels</td><td>Twitch production</td></tr>
      </table>
    </div>
    <div style="text-align:center;">
      <a href="{AFF}" class="btn btn-purple">Try Restream Free — Best Overall →</a>
    </div>
  </div>
</section>
{cta_band("Restream Wins for Global Reach","More platforms, more tools, and a free plan that actually lets you multistream.")}"""
    return page(
        "Restream vs StreamYard vs Streamlabs 2026 — Which Is Best? | Stream-Hub",
        "Unbiased comparison of Restream.io vs StreamYard vs Streamlabs. Features, pricing, platforms, and which multistreaming tool wins in 2026.",
        "comparison.html", body)

def page_gamers():
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">🎮 For Gamers</div>
  <h1>Multistream Your <em>Gameplay</em><br>to Every Platform</h1>
  <p>Stream to Twitch, YouTube Gaming, Facebook Gaming, and TikTok Live simultaneously. Grow everywhere with one stream.</p>
  <a href="{AFF}" class="btn btn-purple">🎮 Start Gaming Multistream Free</a>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Gaming Multistream</div>
    <h2 class="section-title">Why Gamers Choose Restream</h2>
    <div class="cards fade">
      <a href="{AFF}" class="card"><div class="card-icon">🎮</div><h3>Stream to All Gaming Platforms</h3><p>Twitch, YouTube Gaming, Facebook Gaming, TikTok Live, and Kick — all simultaneously from one OBS setup.</p><span class="card-link">Connect Gaming Platforms →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">📈</div><h3>Grow Faster</h3><p>Appearing on multiple platforms at once means more discovery, more followers, and faster channel growth.</p><span class="card-link">Grow Your Channel →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">💬</div><h3>One Chat for All Audiences</h3><p>See Twitch, YouTube, and Facebook chat in one window. Engage every viewer without switching tabs.</p><span class="card-link">Manage Your Chat →</span></a>
    </div>
    <div style="text-align:center;">
      <a href="{AFF}" class="btn btn-purple">🎮 Start Gaming Multistream →</a>
    </div>
  </div>
</section>"""
    return page(
        "Multistream Gaming to Twitch, YouTube & TikTok 2026 | Stream-Hub",
        "Stream your gameplay to Twitch, YouTube Gaming, Facebook Gaming, and TikTok Live simultaneously with Restream.io. Free trial for gamers.",
        "gamers.html", body)

def page_churches():
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">⛪ For Churches</div>
  <h1>Stream Live Services to<br><em>Your Entire Congregation</em></h1>
  <p>Broadcast to YouTube, Facebook, and your website simultaneously. Reach every member wherever they are.</p>
  <a href="{AFF}" class="btn btn-purple">⛪ Start Church Multistream Free</a>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Church Streaming</div>
    <h2 class="section-title">Why Churches Use Restream</h2>
    <div class="cards fade">
      <a href="{AFF}" class="card"><div class="card-icon">📺</div><h3>YouTube + Facebook Simultaneously</h3><p>Stream your Sunday service to YouTube Live and Facebook Live at the same time. No second stream required.</p><span class="card-link">Set Up Church Stream →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">🌐</div><h3>Embed on Your Church Website</h3><p>Bring your live service directly to your church website with a simple embed code that updates automatically.</p><span class="card-link">Embed Your Service →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">📱</div><h3>Mobile-Friendly Streaming</h3><p>Stream from a phone, tablet, or laptop. Restream works on any device with no expensive equipment required.</p><span class="card-link">Stream from Any Device →</span></a>
    </div>
    <div style="text-align:center;">
      <a href="{AFF}" class="btn btn-purple">⛪ Set Up Your Church Stream Free →</a>
    </div>
  </div>
</section>"""
    return page(
        "Live Streaming for Churches 2026 — Multistream Services | Stream-Hub",
        "Help your church stream live services to YouTube, Facebook, and your website simultaneously with Restream.io. Free trial for churches and ministries.",
        "churches.html", body)

def page_coaches():
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">🎓 For Coaches & Educators</div>
  <h1>Stream Live Training to<br><em>Every Student Platform</em></h1>
  <p>Broadcast live classes, Q&A sessions, and coaching to YouTube, LinkedIn, Facebook, and your website simultaneously.</p>
  <a href="{AFF}" class="btn btn-purple">🎓 Start Coaching Multistream Free</a>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Coaching & Education</div>
    <h2 class="section-title">Why Coaches Choose Restream</h2>
    <div class="cards fade">
      <a href="{AFF}" class="card"><div class="card-icon">💼</div><h3>LinkedIn + YouTube Simultaneously</h3><p>Reach professionals on LinkedIn and students on YouTube in one broadcast. Maximum reach for coaches.</p><span class="card-link">Stream to LinkedIn →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">🌐</div><h3>Embed on Your Course Site</h3><p>Bring your live training directly to your website or course platform with a simple embed code.</p><span class="card-link">Embed Your Stream →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">📊</div><h3>Track Student Engagement</h3><p>See how many students tuned in on each platform and measure engagement with real-time analytics.</p><span class="card-link">View Analytics →</span></a>
    </div>
    <div style="text-align:center;">
      <a href="{AFF}" class="btn btn-purple">🎓 Start Coaching Stream Free →</a>
    </div>
  </div>
</section>"""
    return page(
        "Live Streaming for Coaches & Educators 2026 | Stream-Hub",
        "Stream live coaching and training to YouTube, LinkedIn, Facebook, and your website simultaneously with Restream.io. Free trial for educators.",
        "coaches.html", body)

def page_business():
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">🏢 For Business</div>
  <h1>Broadcast <em>Corporate Events</em><br>Everywhere Simultaneously</h1>
  <p>Product launches, webinars, and corporate events live on LinkedIn, YouTube, Facebook, and more — all at once.</p>
  <a href="{AFF}" class="btn btn-purple">🏢 Start Business Streaming Free</a>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Business Streaming</div>
    <h2 class="section-title">Professional Live Streaming for Business</h2>
    <div class="cards fade">
      <a href="{AFF}" class="card"><div class="card-icon">🚀</div><h3>Product Launch Streams</h3><p>Go live on LinkedIn, YouTube, Facebook, and Twitter/X simultaneously for maximum product launch reach.</p><span class="card-link">Launch Events →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">📋</div><h3>Webinars & Corporate Events</h3><p>Professional browser-based studio with scenes, overlays, and guest invites. No software required.</p><span class="card-link">Run Webinars →</span></a>
      <a href="{AFF}" class="card"><div class="card-icon">📊</div><h3>Business Analytics</h3><p>Track viewer counts, watch time, and platform performance across every channel in one dashboard.</p><span class="card-link">View Business Analytics →</span></a>
    </div>
    <div style="text-align:center;">
      <a href="{AFF}" class="btn btn-purple">🏢 Start Business Streaming Free →</a>
    </div>
  </div>
</section>"""
    return page(
        "Live Streaming for Business 2026 — Corporate Webinars & Events | Stream-Hub",
        "Stream corporate events, product launches, and webinars to LinkedIn, YouTube, and Facebook simultaneously with Restream.io.",
        "business.html", body)

def page_embed():
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">🌐 Website Embedding</div>
  <h1>Embed Your Live Stream<br><em>On Any Website</em></h1>
  <p>Bring your live stream directly to your site. One line of code. Updates automatically when you go live.</p>
  <a href="{AFF}" class="btn btn-purple">🌐 Get Your Embed Code Free</a>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">How to Embed</div>
    <h2 class="section-title">Embed Restream on Your Website</h2>
    <div class="tips fade">
      <div class="tip"><div class="tip-n">01</div><div class="tip-t"><strong>Sign in to Restream</strong><span>Create a free account at Restream.io and connect your streaming platforms.</span></div></div>
      <div class="tip"><div class="tip-n">02</div><div class="tip-t"><strong>Go to the Stream tab</strong><span>Inside your Restream dashboard, click "Stream" and then "Embed" to find your embed options.</span></div></div>
      <div class="tip"><div class="tip-n">03</div><div class="tip-t"><strong>Copy the embed code</strong><span>Copy the HTML snippet provided. It's a standard iframe that works on any website.</span></div></div>
      <div class="tip"><div class="tip-n">04</div><div class="tip-t"><strong>Paste into your site</strong><span>Paste the code into your WordPress, Wix, Webflow, Squarespace, or custom HTML page.</span></div></div>
      <div class="tip"><div class="tip-n">05</div><div class="tip-t"><strong>Go live — player updates automatically</strong><span>When you start streaming, the embedded player on your site updates automatically with no extra steps.</span></div></div>
    </div>
    <div style="text-align:center;margin-top:2rem;">
      <a href="{AFF}" class="btn btn-purple">🌐 Get Your Embed Code Free →</a>
    </div>
  </div>
</section>"""
    return page(
        "How to Embed a Live Stream on Your Website 2026 | Stream-Hub",
        "Learn how to embed your Restream live stream on any website. WordPress, Wix, Webflow, and custom HTML. Free embed code.",
        "embed.html", body)

def page_obs():
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">🎬 OBS + Restream</div>
  <h1>Use OBS with Restream<br><em>The Ultimate Setup</em></h1>
  <p>Connect OBS Studio to Restream and multistream to 30+ platforms with the world's most powerful streaming software.</p>
  <a href="{AFF}" class="btn btn-purple">🎬 Connect OBS to Restream Free</a>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">OBS + Restream Setup</div>
    <h2 class="section-title">How to Connect OBS to Restream</h2>
    <div class="tips fade">
      <div class="tip"><div class="tip-n">01</div><div class="tip-t"><strong>Create a free Restream account</strong><span>Sign up at Restream.io and connect your platforms (Twitch, YouTube, Facebook, etc.).</span></div></div>
      <div class="tip"><div class="tip-n">02</div><div class="tip-t"><strong>Copy your Restream RTMP URL and Stream Key</strong><span>In your Restream dashboard, go to Settings → Stream Key to find your RTMP server URL and key.</span></div></div>
      <div class="tip"><div class="tip-n">03</div><div class="tip-t"><strong>Open OBS → Settings → Stream</strong><span>Select "Custom" as your service, paste the Restream RTMP URL in Server, and your stream key in Stream Key.</span></div></div>
      <div class="tip"><div class="tip-n">04</div><div class="tip-t"><strong>Start streaming in OBS</strong><span>Click "Start Streaming" in OBS and your stream goes live on all connected Restream platforms simultaneously.</span></div></div>
    </div>
    <div style="text-align:center;margin-top:2rem;">
      <a href="{AFF}" class="btn btn-purple">🎬 Connect OBS to Restream Free →</a>
    </div>
  </div>
</section>"""
    return page(
        "How to Use OBS with Restream 2026 — Multistream Setup Guide | Stream-Hub",
        "Connect OBS Studio to Restream.io and multistream to Twitch, YouTube, Facebook, and 30+ platforms. Step-by-step setup guide.",
        "obs-setup.html", body)

def page_tips():
    tips_data = [
        ("Use descriptive titles for each platform","Slightly different titles per platform help search engines see your content as unique and improve organic discovery on each platform."),
        ("Go live consistently","Platforms reward regular streamers with better algorithmic placement. Schedule streams and stick to them."),
        ("Optimize your stream title with keywords","Include keywords like your game name, topic, or niche in your stream title for better search visibility on each platform."),
        ("Engage chat from all platforms","Use Restream's unified chat to respond to viewers across Twitch, YouTube, and Facebook simultaneously. Engagement boosts algorithmic reach."),
        ("Use a stream schedule overlay","Tell viewers when you go live next. Scheduled streams convert casual viewers into regular followers."),
        ("Check your bitrate before going live","A stable 3,500–6,000 kbps bitrate ensures smooth delivery to all platforms. Test before your stream."),
        ("Add platform-specific thumbnails","Each platform has different thumbnail dimensions. Customize thumbnails per platform for better click-through rates."),
        ("Use Restream Clips for highlights","Turn your best stream moments into short clips for YouTube Shorts, TikTok, and Instagram Reels to drive traffic back to your streams."),
        ("Announce streams across all channels","Post on Twitter/X, Instagram, and Discord before going live. Pre-stream promotion drives early viewers which boosts algorithms."),
        ("Review your analytics after every stream","Restream analytics show which platforms drove the most viewers. Double down on what's working."),
    ]
    tip_html = "".join(f'<div class="tip"><div class="tip-n">{str(i+1).zfill(2)}</div><div class="tip-t"><strong>{t}</strong><span>{d}</span></div></div>' for i,(t,d) in enumerate(tips_data))
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">💡 Streaming Tips</div>
  <h1>10 Tips to <em>Grow Your Stream</em><br>Across Every Platform</h1>
  <p>Proven strategies from successful multistreaming creators to maximize reach and grow your audience globally.</p>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Pro Tips</div>
    <h2 class="section-title">10 Multistreaming Tips for 2026</h2>
    <div class="tips fade">{tip_html}</div>
    <div style="text-align:center;margin-top:2rem;">
      <a href="{AFF}" class="btn btn-purple">🚀 Apply These Tips with Restream Free →</a>
    </div>
  </div>
</section>"""
    return page(
        "10 Multistreaming Tips to Grow Your Stream in 2026 | Stream-Hub",
        "10 proven tips to grow your live stream audience across Twitch, YouTube, Facebook, and TikTok using Restream.io.",
        "tips.html", body)

def page_faq():
    schema = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{{"@type":"Question","name":"Is Restream.io free?","acceptedAnswer":{{"@type":"Answer","text":"Yes. Restream offers a free plan with core multistreaming features. Paid plans unlock more platforms, higher quality, and advanced analytics."}}}},
{{"@type":"Question","name":"How many platforms can I stream to with Restream?","acceptedAnswer":{{"@type":"Answer","text":"Restream supports 30+ platforms including Twitch, YouTube, Facebook, TikTok Live, LinkedIn, Kick, and more."}}}},
{{"@type":"Question","name":"Do I need OBS to use Restream?","acceptedAnswer":{{"@type":"Answer","text":"No. Restream Studio is browser-based and requires no software. You can also connect OBS or Streamlabs if preferred."}}}}
]}}</script>"""
    body = f"""
<section class="hero" style="padding:3.5rem 1.5rem;">
  <div class="hero-badge">❓ FAQ</div>
  <h1>Restream.io —<br><em>Your Questions Answered</em></h1>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="faqs fade">
      <div class="faq"><div class="faq-q">Is Restream.io free to use?</div><div class="faq-a">Yes. Restream offers a free plan with core multistreaming features. Paid plans unlock more platforms, higher quality streams, and advanced analytics.</div></div>
      <div class="faq"><div class="faq-q">How many platforms can I stream to?</div><div class="faq-a">Restream supports 30+ platforms including Twitch, YouTube Live, Facebook, TikTok Live, LinkedIn, Kick, Instagram, and more simultaneously.</div></div>
      <div class="faq"><div class="faq-q">Do I need OBS to use Restream?</div><div class="faq-a">No. Restream Studio runs in your browser with no software installation. You can also connect OBS, Streamlabs, or any RTMP encoder.</div></div>
      <div class="faq"><div class="faq-q">Can I embed my stream on my website?</div><div class="faq-a">Yes. Restream provides an embed code you can paste into any website — WordPress, Wix, Webflow, or custom HTML. The player updates automatically when you go live.</div></div>
      <div class="faq"><div class="faq-q">Does Restream work for churches?</div><div class="faq-a">Yes. Many churches use Restream to broadcast live services to YouTube, Facebook, and their church website simultaneously.</div></div>
      <div class="faq"><div class="faq-q">Can coaches use Restream for live training?</div><div class="faq-a">Absolutely. Coaches stream live training to LinkedIn, YouTube, and Facebook simultaneously and embed streams on their course websites.</div></div>
      <div class="faq"><div class="faq-q">How does Restream compare to StreamYard?</div><div class="faq-a">Restream supports more platforms (30+ vs 8) and has a more comprehensive free plan. StreamYard focuses on professional webinar production. For maximum platform reach, Restream wins.</div></div>
      <div class="faq"><div class="faq-q">Does Restream support mobile streaming?</div><div class="faq-a">Yes. You can stream from your phone using the Restream mobile app or by connecting a mobile RTMP encoder to your Restream dashboard.</div></div>
    </div>
    <div style="text-align:center;margin-top:2rem;">
      <a href="{AFF}" class="btn btn-purple">🚀 Start Free Restream Trial →</a>
    </div>
  </div>
</section>"""
    return page(
        "Restream.io FAQ 2026 — Is It Free? Platforms, OBS & More | Stream-Hub",
        "Answers to common Restream.io questions. Is it free? How many platforms? Does it work with OBS? Complete FAQ for streamers worldwide.",
        "faq.html", body, schema)

def page_about():
    body = f"""
<section class="section" style="padding-top:3rem;">
  <div class="container" style="max-width:720px;">
    <h1 class="section-title">About Stream-Hub</h1>
    <p style="margin-bottom:1.5rem;">Stream-Hub is a global resource for live streamers, creators, churches, coaches, and businesses who want to maximize their live video reach. We review and recommend the best multistreaming tools so you can focus on creating great content.</p>
    <p style="margin-bottom:1.5rem;">After testing every major multistreaming platform, Restream.io consistently delivers the best combination of platform coverage, ease of use, and value. It is our recommended platform for creators worldwide.</p>
    <p style="margin-bottom:1.5rem;">Stream-Hub is operated by <strong>{BRAND}</strong>.</p>
    <div style="text-align:center;margin-top:2rem;">
      <a href="{AFF}" class="btn btn-purple">🚀 Try Restream Free →</a>
    </div>
  </div>
</section>"""
    return page(f"About Stream-Hub — {BRAND}",
                "Stream-Hub is a global resource for live streamers, churches, coaches, and businesses. We recommend the best multistreaming tools.",
                "about.html", body)

def page_contact():
    body = f"""
<section class="section" style="padding-top:3rem;">
  <div class="container" style="max-width:720px;">
    <h1 class="section-title">Contact Stream-Hub</h1>
    <p>Questions, corrections, or partnership inquiries? Reach us at:</p>
    <p style="margin-top:1.5rem;font-size:1.1rem;font-weight:700;">contact [at] streamhub [dot] info</p>
    <p style="margin-top:1rem;color:#666;">For partnership inquiries, include "Partnership" in your subject line. We typically respond within 48 hours.</p>
  </div>
</section>"""
    return page("Contact Stream-Hub", "Contact the Stream-Hub team with questions or partnership inquiries.", "contact.html", body)

def page_disclosure():
    body = f"""
<section class="section" style="padding-top:3rem;">
  <div class="container" style="max-width:720px;">
    <h1 class="section-title">Affiliate Disclosure</h1>
    <p style="margin-bottom:1.5rem;">Stream-Hub participates in affiliate programs. We earn a commission when you sign up through our links at no extra cost to you.</p>
    <p style="margin-bottom:1rem;"><strong>Current affiliate relationship:</strong> Stream-Hub has an affiliate relationship with Restream.io. Our affiliate link is <code>https://try.restream.io/rwapmhjhzv2z</code>.</p>
    <p>Commission rates do not influence our recommendations. We only recommend Restream because we genuinely believe it is the best multistreaming platform available.</p>
    <p style="margin-top:1.5rem;">&copy; 2026 {BRAND}</p>
  </div>
</section>"""
    return page("Affiliate Disclosure — Stream-Hub", "Stream-Hub affiliate disclosure. We earn commissions from Restream.io referrals.", "disclosure.html", body)

def blog_index_html(posts):
    items = "".join(f'<li style="margin-bottom:0.75rem;"><a href="{p["url"]}" style="color:#6a11cb;font-weight:600;">{p["title"]}</a> <small style="color:#888;">({p["date"]})</small></li>' for p in reversed(posts[-30:]))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Live Streaming Blog 2026 | Stream-Hub</title>
<meta name="description" content="Live streaming tips, Restream guides, OBS tutorials, and multistreaming strategies. Updated daily by Stream-Hub.">
<link rel="canonical" href="{SITE_URL}/blog-index.html">
{FONTS}
<style>{CSS}</style>
</head>
<body>
{nav_html()}
<section class="hero" style="padding:3rem 1.5rem;">
  <div class="hero-badge">📝 Daily Blog</div>
  <h1>Live Streaming <em>Blog</em></h1>
  <p>Tips, guides, and strategies for multistreaming, OBS, Restream, and growing your audience. Updated daily.</p>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Latest Posts</div>
    <h2 class="section-title">All Blog Posts</h2>
    <ul style="list-style:none;padding:0;">{items}</ul>
  </div>
</section>
{FOOTER_HTML}
{STICKY_HTML}
<script>{JS}</script>
</body>
</html>"""

# ── ALL PAGES ────────────────────────────────────
def all_pages():
    return {
        "index.html":        page_index(),
        "multistreaming.html":page_multistreaming(),
        "platforms.html":    page_platforms(),
        "comparison.html":   page_comparison(),
        "gamers.html":       page_gamers(),
        "churches.html":     page_churches(),
        "coaches.html":      page_coaches(),
        "business.html":     page_business(),
        "embed.html":        page_embed(),
        "obs-setup.html":    page_obs(),
        "tips.html":         page_tips(),
        "faq.html":          page_faq(),
        "about.html":        page_about(),
        "contact.html":      page_contact(),
        "disclosure.html":   page_disclosure(),
    }

def sitemap(pages):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    urls = [f"  <url><loc>{SITE_URL}/</loc><lastmod>{today}</lastmod><priority>1.0</priority></url>"]
    for slug in pages:
        urls.append(f"  <url><loc>{SITE_URL}/{slug}</loc><lastmod>{today}</lastmod><priority>0.8</priority></url>")
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>"

def robots():
    return f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"

def gh_put(path, content, msg):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {"message": msg, "content": base64.b64encode(content.encode()).decode()}
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    icon = "✅" if resp.status_code in (200, 201) else "❌"
    print(f"{icon} {path} ({resp.status_code})")

if __name__ == "__main__":
    pages = all_pages()
    print(f"Building {len(pages)} pages for {SITE_NAME}...")
    for slug, html in pages.items():
        gh_put(slug, html, f"Site update: {slug}")
    gh_put("sitemap.xml", sitemap(pages), "Site update: sitemap.xml")
    gh_put("robots.txt",  robots(),       "Site update: robots.txt")
    print(f"\nDone! {len(pages)+2} files pushed to {GH_REPO}.")
