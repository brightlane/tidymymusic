#!/usr/bin/env python3
"""
Stream-Hub Meta Generator
Generates: sitemap.xml, sitemap2.xml+ (when needed), robots.txt, llms.txt, 404.html
Auto-discovers all HTML pages and blog posts in the repo
Splits sitemap at 50,000 URLs into additional sitemaps
Run via GitHub Actions daily at 9:30 AM UTC
"""

import os, base64, requests
from datetime import datetime, timezone

AFF       = "https://try.restream.io/rwapmhjhzv2z"
SITE_NAME = "Stream-Hub"
BRAND     = "Brightlane Media"
SITE_URL  = "https://brightlane.github.io/Stream-Hub"
SITE_DESC = "Restream.io reviews, multistreaming guides, OBS tutorials, and live streaming growth strategies for gamers, churches, coaches, and businesses worldwide."
GH_USER   = os.environ.get("GH_USER", "brightlane")
GH_REPO   = os.environ.get("GH_REPO", "Stream-Hub")
GH_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
SITEMAP_LIMIT = 50000

HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json"
}

HIGH_PRIORITY_PAGES = {
    "index.html", "comparison.html", "faq.html",
    "multistreaming.html", "platforms.html"
}

def get_all_repo_files(path=""):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200:
        return []
    items = r.json()
    files = []
    for item in items:
        if item["type"] == "file":
            files.append(item["path"])
        elif item["type"] == "dir" and not item["name"].startswith("."):
            files.extend(get_all_repo_files(item["path"]))
    return files

def build_url_list(files):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    urls = [{
        "loc": f"{SITE_URL}/",
        "lastmod": today,
        "priority": "1.0",
        "changefreq": "daily"
    }]

    for f in sorted(files):
        if not f.endswith(".html"):
            continue
        if f in ("index.html", "404.html"):
            continue

        if f.startswith("blog/"):
            priority, changefreq = "0.6", "monthly"
        elif f == "blog-index.html":
            priority, changefreq = "0.8", "daily"
        elif f in HIGH_PRIORITY_PAGES:
            priority, changefreq = "0.9", "weekly"
        else:
            priority, changefreq = "0.75", "weekly"

        urls.append({
            "loc": f"{SITE_URL}/{f}",
            "lastmod": today,
            "priority": priority,
            "changefreq": changefreq
        })

    return urls

def build_sitemap_xml(urls):
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
        '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
        '        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9',
        '        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">'
    ]
    for u in urls:
        lines += [
            "  <url>",
            f"    <loc>{u['loc']}</loc>",
            f"    <lastmod>{u['lastmod']}</lastmod>",
            f"    <changefreq>{u['changefreq']}</changefreq>",
            f"    <priority>{u['priority']}</priority>",
            "  </url>"
        ]
    lines.append("</urlset>")
    return "\n".join(lines)

def build_sitemap_index_xml(num_sitemaps):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    for i in range(1, num_sitemaps + 1):
        fname = "sitemap.xml" if i == 1 else f"sitemap{i}.xml"
        lines += [
            "  <sitemap>",
            f"    <loc>{SITE_URL}/{fname}</loc>",
            f"    <lastmod>{today}</lastmod>",
            "  </sitemap>"
        ]
    lines.append("</sitemapindex>")
    return "\n".join(lines)

def build_robots(num_sitemaps):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /data/",
        "",
        "# Sitemaps"
    ]
    for i in range(1, num_sitemaps + 1):
        fname = "sitemap.xml" if i == 1 else f"sitemap{i}.xml"
        lines.append(f"Sitemap: {SITE_URL}/{fname}")
    if num_sitemaps > 1:
        lines.append(f"Sitemap: {SITE_URL}/sitemap-index.xml")
    lines += ["", "# AI Crawlers", f"Sitemap: {SITE_URL}/llms.txt"]
    return "\n".join(lines)

def build_llms(urls):
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        f"# {SITE_NAME}",
        f"> {SITE_URL}",
        "",
        SITE_DESC,
        "",
        f"Updated: {today}",
        f"Brand: {BRAND}",
        "",
        "## Affiliate",
        "- Product: Restream.io",
        "- URL: https://try.restream.io/rwapmhjhzv2z",
        "- Type: Live streaming / multistreaming platform",
        "",
        "## Main Pages"
    ]
    for u in urls:
        if "/blog/" not in u["loc"] and u["loc"] != f"{SITE_URL}/":
            slug = u["loc"].replace(f"{SITE_URL}/", "")
            lines.append(f"- [{slug}]({u['loc']})")

    lines += ["", "## Blog Posts"]
    blog_urls = [u for u in urls if "/blog/" in u["loc"]]
    if blog_urls:
        for u in blog_urls[-20:]:
            slug = u["loc"].split("/blog/")[-1]
            lines.append(f"- [{slug}]({u['loc']})")
    else:
        lines.append("- Blog posts published daily at 9AM UTC")

    lines += [
        "",
        "## Topics Covered",
        "- Restream.io reviews and tutorials",
        "- Multistreaming to Twitch, YouTube, Facebook, TikTok, LinkedIn",
        "- OBS Studio setup and tips",
        "- Live streaming for gamers, churches, coaches, and businesses",
        "- StreamYard vs Restream comparison",
        "- Website embedding of live streams",
        "- Live streaming growth strategies 2026"
    ]
    return "\n".join(lines)

def build_404():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Page Not Found | Stream-Hub</title>
<meta name="robots" content="noindex, follow">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:'Inter',sans-serif;background:#f9fafb;color:#222;min-height:100vh;display:flex;flex-direction:column;}}
nav{{background:#1a0533;padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between;height:62px;}}
.nav-logo{{color:#fff;font-weight:800;font-size:1.1rem;text-decoration:none;}}
.nav-logo span{{color:#a78bfa;}}
.nav-cta{{background:#6a11cb;color:#fff!important;padding:7px 16px;border-radius:8px;font-weight:700;font-size:0.85rem;text-decoration:none;}}
.main{{flex:1;display:flex;align-items:center;justify-content:center;padding:3rem 1.5rem;text-align:center;}}
.box{{background:#fff;border-radius:16px;padding:3rem 2rem;box-shadow:0 8px 32px rgba(106,17,203,0.1);max-width:540px;width:100%;border:1px solid #ede8f8;}}
.emoji{{font-size:4rem;margin-bottom:1rem;}}
h1{{font-size:1.8rem;font-weight:800;color:#1a0533;margin-bottom:0.75rem;}}
p{{color:#555;margin-bottom:1.5rem;font-size:0.97rem;}}
.btn{{display:inline-block;padding:12px 26px;border-radius:8px;font-weight:700;font-size:0.9rem;margin:0.4rem;text-decoration:none;transition:transform 0.2s;}}
.btn:hover{{transform:translateY(-2px);}}
.btn-purple{{background:#6a11cb;color:#fff;}}
.btn-outline{{border:2px solid #6a11cb;color:#6a11cb;}}
.links{{margin-top:1.5rem;display:flex;flex-wrap:wrap;gap:0.5rem;justify-content:center;}}
.link-tag{{background:#f3eeff;color:#6a11cb;padding:0.3rem 0.8rem;border-radius:20px;font-size:0.82rem;font-weight:600;text-decoration:none;}}
.link-tag:hover{{background:#e9d8fd;}}
footer{{background:#1a0533;color:rgba(255,255,255,0.5);text-align:center;padding:1.2rem;font-size:0.8rem;}}
footer a{{color:#a78bfa;text-decoration:none;}}
</style>
</head>
<body>
<nav>
  <a href="{SITE_URL}/index.html" class="nav-logo" style="text-decoration:none;">📡 Stream<span>Hub</span></a>
  <a href="{AFF}" class="nav-cta" target="_blank" rel="nofollow">Try Restream Free →</a>
</nav>

<div class="main">
  <div class="box">
    <div class="emoji">📡</div>
    <h1>Page Not Found</h1>
    <p>This page doesn't exist or was moved. Head back to Stream-Hub for the best multistreaming guides and Restream.io reviews.</p>

    <a href="{SITE_URL}/index.html" class="btn btn-purple">← Back to Home</a>
    <a href="{AFF}" class="btn btn-outline" target="_blank" rel="nofollow">Try Restream Free →</a>

    <div class="links">
      <a href="{SITE_URL}/multistreaming.html" class="link-tag">Multistreaming Guide</a>
      <a href="{SITE_URL}/comparison.html" class="link-tag">Compare Platforms</a>
      <a href="{SITE_URL}/gamers.html" class="link-tag">For Gamers</a>
      <a href="{SITE_URL}/churches.html" class="link-tag">For Churches</a>
      <a href="{SITE_URL}/coaches.html" class="link-tag">For Coaches</a>
      <a href="{SITE_URL}/obs-setup.html" class="link-tag">OBS Setup</a>
      <a href="{SITE_URL}/faq.html" class="link-tag">FAQ</a>
      <a href="{SITE_URL}/blog-index.html" class="link-tag">Blog</a>
    </div>
  </div>
</div>

<footer>
  <p>&copy; 2026 {BRAND} | Stream-Hub | <a href="{SITE_URL}/disclosure.html">Affiliate Disclosure</a></p>
</footer>
</body>
</html>"""

def gh_put(path, content, msg):
    url = f"https://api.github.com/repos/{GH_USER}/{GH_REPO}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    sha = r.json().get("sha") if r.status_code == 200 else None
    payload = {
        "message": msg,
        "content": base64.b64encode(content.encode()).decode()
    }
    if sha:
        payload["sha"] = sha
    resp = requests.put(url, headers=HEADERS, json=payload)
    icon = "✅" if resp.status_code in (200, 201) else "❌"
    print(f"{icon} {path} ({resp.status_code}) — {len(content):,} chars")

if __name__ == "__main__":
    print(f"🔍 Scanning repo: {GH_USER}/{GH_REPO}...")
    all_files = get_all_repo_files()
    html_files = [f for f in all_files if f.endswith(".html") and f != "404.html"]
    print(f"📄 Found {len(html_files)} HTML files")

    urls = build_url_list(html_files)
    total_urls = len(urls)
    print(f"🗺️  Total URLs: {total_urls}")

    chunks = [urls[i:i+SITEMAP_LIMIT] for i in range(0, max(total_urls,1), SITEMAP_LIMIT)]
    num_sitemaps = len(chunks)
    print(f"📦 Sitemap files needed: {num_sitemaps}")

    for i, chunk in enumerate(chunks):
        fname = "sitemap.xml" if i == 0 else f"sitemap{i+1}.xml"
        gh_put(fname, build_sitemap_xml(chunk), f"Meta: {fname} ({len(chunk)} URLs)")

    if num_sitemaps > 1:
        gh_put("sitemap-index.xml", build_sitemap_index_xml(num_sitemaps),
               f"Meta: sitemap-index.xml ({num_sitemaps} sitemaps)")

    gh_put("robots.txt", build_robots(num_sitemaps), "Meta: robots.txt")
    gh_put("llms.txt",   build_llms(urls),           "Meta: llms.txt")
    gh_put("404.html",   build_404(),                "Meta: 404.html")

    print(f"\n✅ Done! {num_sitemaps} sitemap(s) + robots.txt + llms.txt + 404.html")
    print(f"   Total URLs indexed: {total_urls}")
    if num_sitemaps > 1:
        print(f"   ⚡ Split into {num_sitemaps} sitemaps + sitemap-index.xml")
