"""Build the static Henry Okechi portfolio (v3.1) from projects.json.
Usage: python build.py
"""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent
PROJECTS = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))

GROUPS = [
    ("all", "All Projects (12)"),
    ("live", "Live & Playable (7)"),
    ("web3", "Web3 & Account Growth (3)"),
    ("health", "Clinical & MedTech"),
    ("creative", "AI Training & Cinema"),
    ("products", "Full-Stack"),
    ("games", "3D Web Games"),
    ("ai", "AI & Career"),
]

# Editable endorsements — swap in exact client/manager names & links anytime.
TESTIMONIALS = [
    (
        "Clinical AI & Evaluation",
        "Henry brings a rare combination of medical-school rigor and hands-on AI fluency. He catches subtle factual and reasoning errors quickly, follows complex evaluation rubrics without hand-holding, and communicates edge cases with editorial clarity.",
        "AI Evaluation & Operations Lead",
        "Remote LLM Training & Data Quality Team",
    ),
    (
        "Web3 Account Management",
        "Across campaign scoping, partner onboarding, and community execution, Henry runs accounts with calm ownership. He translates technical token and product narratives clearly for clients, delivers on tight timelines, and keeps stakeholders aligned across time zones.",
        "Head of Partnerships & Growth",
        "Crypto & Web3 Ecosystem Client",
    ),
    (
        "Editorial & 0→1 Execution",
        "Whether researching complex economic topics for long-form scripts or shipping working web applications from scratch, Henry consistently raises the quality bar. You can hand him an ambiguous brief and trust him to come back with something sharp and usable.",
        "Executive Producer & Product Founder",
        "Digital Media & Software Collaboration",
    ),
]

EXPERIENCE = [
    (
        "2026",
        "AI Model Trainer (GPU Infrastructure)",
        "Runpod",
        "Model Training",
        "Trained custom character-consistency LoRA models (azarun_god_v1) on Runpod GPUs to lock visual identity across multi-shot image and video generations; ran systematic checkpoint evaluations, prompt benchmarks, and dataset refinements.",
    ),
    (
        "2026 — Present",
        "AI & Content Specialist",
        "Kling AI",
        "Generative AI",
        "Directed and produced Azarun, a cinematic AI trailer showcasing African mythology—owning prompt architecture, multi-shot visual continuity, and iterative QA across Kling AI, Seedance, Gemini, and GPT.",
    ),
    (
        "2025 — 2026",
        "Ambassador, Account Sales & Growth",
        "Cointracts · Beraskool · Webacy",
        "Account Mgmt",
        "Managed client relationships, outbound account sales, and partner onboarding at Cointracts; drove product marketing and growth at Beraskool; served as Project & Content Advisor at Webacy (2024–2025).",
    ),
    (
        "2024 — Present",
        "Partnerships Lead & Community Founder",
        "HERMES ALPHA ZONE & Gem Jungle",
        "50+ Campaigns",
        "Closed and delivered 50+ paid crypto client campaigns (NFTs, DeFi, trading platforms) across X, Telegram, and Discord while scaling owned communities to 75K+ combined reach.",
    ),
    (
        "2024 — Present",
        "Founder",
        "Irysnameservice",
        "#1 Irys dApp",
        "Founded an on-chain domain-minting service on the Irys blockchain and led ecosystem partnerships and GTM adoption to become the #1 dApp in the Irys ecosystem.",
    ),
    (
        "2026 — Present",
        "AI Product & Game Builder",
        "Independent Studio",
        "5 Live Builds",
        "Architected and deployed live full-stack web apps and 3D browser games including MedFlash, Project Mucci (Firebase RBAC + Vitest), Kasala (Cloudflare Workers), Wayo, and Naija Undead.",
    ),
    (
        "2021 — 2026",
        "Content Writer & Community Comms",
        "DTCSI Academy",
        "Technical Comms",
        "Authored educational marketing copy, product announcements, and clear technical explainers bridging Web3 newcomers and advanced community stakeholders.",
    ),
    (
        "2021 — 2025",
        "Web3 Community Manager & Project Manager",
        "DeGods, Pudgy Penguins, Primates & Anavrin DAO",
        "Trust & Safety",
        "Managed and moderated high-traffic global Web3 communities at scale with disciplined content review and trust & safety judgment; previously Project Manager at Anavrin DAO (2022–2023).",
    ),
    (
        "2019 — 2021",
        "AI Data Annotator & Evaluator",
        "Appen",
        "RLHF & Data QA",
        "Annotated and evaluated text, image, and audio datasets for machine-learning pipelines—performing relevance rating, categorization, and QA under strict, rapidly evolving rubrics.",
    ),
    (
        "2018 — 2024",
        "Research & Script Writer",
        "Savvy Economist (YouTube)",
        "6 Yrs Editorial",
        "Six years researching, structuring, and writing long-form finance and economics scripts—turning dense technical and financial systems into accurate, high-retention narratives.",
    ),
]


def e(val) -> str:
    return escape(str(val), quote=True)


def header(active: str, prefix: str = "") -> str:
    links = [
        (f"{prefix}index.html", "Overview", "home"),
        (f"{prefix}work.html", "Selected Work", "work"),
        (f"{prefix}about.html", "Background", "about"),
        (f"{prefix}contact.html", "Hire Me", "contact"),
    ]
    nav_html = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if active == key else ""}>{label}</a>'
        for href, label, key in links
    )
    return f"""
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="{prefix}index.html" aria-label="Dr. Henry Okechi home">
      <span class="brand-mark">HO</span>
      <span class="brand-text">
        <strong>Henry Okechi</strong>
        <small>MD (MBBS) · Clinical AI · Web3 AM</small>
      </span>
    </a>
    <nav class="nav-links" id="site-navigation" data-menu aria-label="Primary navigation">
      {nav_html}
    </nav>
    <div class="nav-utilities">
      <button type="button" class="cmd-trigger" data-cmd-open aria-label="Open quick jump menu">
        <span>Quick Jump</span>
        <kbd>⌘K</kbd>
      </button>
      <a class="nav-cv" href="{prefix}assets/Henry_Okechi_CV.pdf" download>CV ↓</a>
      <a class="nav-hire" href="{prefix}contact.html">Work With Me ↗</a>
      <button type="button" class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" aria-controls="site-navigation" data-menu-toggle>☰</button>
    </div>
  </div>
</header>
"""


def command_palette() -> str:
    return """
<div class="cmd-backdrop" data-cmd-backdrop role="dialog" aria-modal="true" aria-label="Quick jump command palette">
  <div class="cmd-dialog">
    <div class="cmd-input-wrap">
      <span class="mono" style="color:var(--gold);font-size:13px">⌘</span>
      <input type="text" data-cmd-input placeholder="Jump to Clinical AI proof, Web3 track, Azarun reel, CV, or email..." autocomplete="off">
    </div>
    <div class="cmd-list" data-cmd-list></div>
    <div class="cmd-foot">
      <span>Type to filter · Click to open</span>
      <span>ESC to close</span>
    </div>
  </div>
</div>
"""


def footer(prefix: str = "") -> str:
    return f"""
<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <a class="brand" href="{prefix}index.html">
        <span class="brand-mark">HO</span>
        <span class="brand-text">
          <strong>Dr. Henry Okechi</strong>
          <small>Clinical AI Training · Web3 Account Management · Product Builder</small>
        </span>
      </a>
      <div class="footer-links">
        <a href="mailto:enryvanie@gmail.com">enryvanie@gmail.com</a>
        <a href="https://t.me/enryvanie" target="_blank" rel="noopener noreferrer">Telegram (@enryvanie) ↗</a>
        <a href="https://www.linkedin.com/in/henry-okechi-b20283422" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>
        <a href="https://x.com/Vanieofweb3" target="_blank" rel="noopener noreferrer">X ↗</a>
        <a href="https://github.com/hermes-nietzesch" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
        <a href="{prefix}assets/Henry_Okechi_CV.pdf" download>Download CV ↓</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Dr. Henry Okechi · Remote Worldwide (UTC+1 · Lagos, Nigeria)</span>
      <span>English (Native) · Russian (B1) · French (A2)</span>
    </div>
  </div>
</footer>
{command_palette()}
<script src="{prefix}site.js" defer></script>
"""


def page_shell(active: str, title: str, description: str, body: str, prefix: str = "") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#08080a">
  <meta name="description" content="{e(description)}">
  <meta property="og:title" content="{e(title)} — Henry Okechi">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="website">
  <title>{e(title)} — Henry Okechi</title>
  <link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}style.css">
</head>
<body data-root="{prefix}">
  {header(active, prefix)}
  <main id="main">
    {body}
  </main>
  {footer(prefix)}
</body>
</html>
"""


def project_card(p: dict, prefix: str = "") -> str:
    media_class = "card-media"
    if p.get("image_style") == "framed-light":
        media_class += " framed-light"
    elif p.get("image_style") == "framed-portrait":
        media_class += " framed-portrait"

    stage_badge = (
        f'<span class="badge badge-live"><span class="pulse-dot"></span>{e(p["stage"])}</span>'
        if p.get("live")
        else f'<span class="badge badge-stage">{e(p["stage"])}</span>'
    )

    live_link = ""
    if p.get("video_reel"):
        vid_label = "Watch Trailer Reel ▶" if len(p["video_reel"]) > 1 else "Watch Product Demo ▶"
        live_link = f'<a class="link-live" href="{prefix}projects/{e(p["slug"])}.html#trailer-reel">{vid_label}</a>'
    elif p.get("live") and p.get("links"):
        first = p["links"][0]
        live_link = f'<a class="link-live" href="{e(first["url"])}" target="_blank" rel="noopener noreferrer">{e(first["label"])} ↗</a>'
    elif p.get("links"):
        first = p["links"][0]
        btn_label = "GitHub" if "github.com" in first["url"] else first["label"]
        live_link = f'<a class="link-live" href="{e(first["url"])}" target="_blank" rel="noopener noreferrer">{e(btn_label)} ↗</a>'

    stack_html = "".join(f"<span>{e(s)}</span>" for s in p["stack"][:4])
    case_href = f"{prefix}projects/{e(p['slug'])}.html"
    img_src = f"{prefix}{e(p['image'])}"

    return f"""
<article class="project-card reveal" data-project-category="{e(p['category'])}" data-project-live="{str(bool(p.get('live'))).lower()}">
  <a href="{case_href}" class="{media_class}" aria-label="View {e(p['name'])} case study">
    <img src="{img_src}" alt="{e(p['name'])} — {e(p['short'])}" loading="lazy">
    <div class="media-badges">
      {stage_badge}
      <span class="badge badge-cat">{e(p['category_name'])}</span>
    </div>
  </a>
  <div class="card-body">
    <div class="card-title-row">
      <h3><a href="{case_href}">{e(p['name'])}</a></h3>
      <span class="card-year">{e(p['year'])}</span>
    </div>
    <div class="card-sub">{e(p['short'])}</div>
    <p class="card-desc">{e(p['tagline'])}</p>
    <div class="card-stack">{stack_html}</div>
    <div class="card-actions">
      <a class="link-case" href="{case_href}">Read Case Study →</a>
      {live_link}
    </div>
  </div>
</article>
"""


def web3_ecosystem_section(prefix: str = "", eyebrow_text: str = "03 / Web3 Growth, Community & Ecosystem Development") -> str:
    return f"""
<section class="section" id="web3-growth">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <div class="eyebrow">{e(eyebrow_text)}</div>
        <h2>Web3 Growth, Community &amp; <em>Ecosystem Development.</em></h2>
      </div>
      <p>The strategies, commercial ownership, and operational playbooks behind 50+ paid crypto campaigns, 75K+ reach, Tier-1 community leadership, and the #1 dApp on Irys.</p>
    </div>

    <div class="web3-shell reveal">
      <div class="web3-kpis">
        <div class="web3-kpi">
          <strong>50+</strong>
          <span>Paid Crypto Campaigns</span>
          <small>NFTs, DeFi &amp; trading platforms across X, Telegram &amp; Discord</small>
        </div>
        <div class="web3-kpi">
          <strong>75K+</strong>
          <span>Combined Community Reach</span>
          <small>Owned &amp; operated distribution via HERMES ALPHA ZONE &amp; Gem Jungle</small>
        </div>
        <div class="web3-kpi">
          <strong>#1 dApp</strong>
          <span>Irys Ecosystem Leader</span>
          <small>Founded &amp; scaled Irysnameservice from launch to top ecosystem rank</small>
        </div>
        <div class="web3-kpi">
          <strong>5+ Yrs</strong>
          <span>Web3 Account &amp; Community Ops</span>
          <small>DeGods, Pudgy Penguins, Cointracts, Beraskool, Webacy &amp; Anavrin DAO</small>
        </div>
      </div>

      <div class="web3-pillars">
        <article class="web3-pillar">
          <div class="web3-pillar-head">
            <span class="web3-pillar-num">01 · Paid Campaigns &amp; Account Management</span>
            <span class="web3-pillar-orgs">HERMES ALPHA ZONE · Gem Jungle · Cointracts</span>
          </div>
          <h3>Full-Cycle Client Delivery &amp; B2B Account Sales</h3>
          <p>Owned the end-to-end commercial pipeline—from outbound prospecting and partner onboarding (Cointracts) to scoping deliverables, crafting narratives, and executing multi-channel launches across owned Telegram and X distribution.</p>
          <ul class="web3-list">
            <li><strong>Campaign Scoping &amp; Alignment:</strong> Translated client acquisition and liquidity goals into structured cross-channel deliverables across X threads, Telegram briefings, and Discord activations.</li>
            <li><strong>Narrative Positioning:</strong> Converted complex DeFi, trading-platform, and NFT mechanics into clear, high-trust audience messaging that drives qualified click-throughs rather than empty impressions.</li>
            <li><strong>Partner Retention:</strong> Coordinated timelines across international founder/BD teams with transparent recaps and repeat campaign execution.</li>
          </ul>
          <div class="web3-outcome">Measurable result: 50+ paid campaigns delivered across 75K+ combined reach · <a href="{prefix}projects/hermes-growth.html" style="text-decoration:underline">Read Case Study →</a></div>
        </article>

        <article class="web3-pillar">
          <div class="web3-pillar-head">
            <span class="web3-pillar-num">02 · Community Leadership &amp; Trust / Safety</span>
            <span class="web3-pillar-orgs">DeGods · Pudgy Penguins · Beraskool · Primates</span>
          </div>
          <h3>High-Traffic Moderation &amp; Audience Retention</h3>
          <p>Operated on the front lines of Web3's highest-velocity global communities (2021–2025)—protecting brand reputation during major mints, market swings, and product rollouts.</p>
          <ul class="web3-list">
            <li><strong>Trust &amp; Safety at Scale:</strong> Enforced strict moderation guidelines, intercepted phishing/impersonation threats in real time, and maintained orderly high-volume channels across time zones.</li>
            <li><strong>Core-Team Communications:</strong> Bridged leadership announcements with everyday holders—defusing FUD with factual clarity and surfacing structured community feedback back to product teams.</li>
            <li><strong>Sustained Engagement:</strong> Structured welcoming onboarding, consistent community rituals, and high-signal conversation loops that keep members active beyond hype cycles.</li>
          </ul>
          <div class="web3-outcome">Measurable result: 4+ years of zero-compromise operations across blue-chip NFT &amp; Web3 communities · <a href="{prefix}projects/web3-community-ops.html" style="text-decoration:underline">Read Case Study →</a></div>
        </article>

        <article class="web3-pillar">
          <div class="web3-pillar-head">
            <span class="web3-pillar-num">03 · Partnerships, Growth &amp; Ecosystem Advisory</span>
            <span class="web3-pillar-orgs">Beraskool · Webacy · Anavrin DAO · DTCSI</span>
          </div>
          <h3>Go-To-Market, Co-Marketing &amp; Technical Comms</h3>
          <p>Advised and executed across product marketing, Web3 security positioning, DAO operations, and educational communications—connecting builders with users and strategic partners.</p>
          <ul class="web3-list">
            <li><strong>Product Marketing &amp; Growth (Beraskool):</strong> Positioned product launches, community incentives, and co-marketing activations to convert passive followers into active participants.</li>
            <li><strong>Advisory &amp; Program Delivery (Webacy &amp; Anavrin DAO):</strong> Provided content and project advisory for Web3 security (Webacy) and coordinated cross-functional milestones as Project Manager (Anavrin DAO).</li>
            <li><strong>Technical Education (DTCSI Academy):</strong> Authored clear announcements and educational copy demystifying crypto concepts for both newcomers and seasoned participants.</li>
          </ul>
          <div class="web3-outcome">Measurable result: Multi-project advisory &amp; GTM execution spanning security, DeFi, NFTs, and education.</div>
        </article>

        <article class="web3-pillar">
          <div class="web3-pillar-head">
            <span class="web3-pillar-num">04 · Blockchain Product Founding</span>
            <span class="web3-pillar-orgs">Irysnameservice · Irys Ecosystem</span>
          </div>
          <h3>From Zero to #1 Ecosystem dApp</h3>
          <p>Applied hands-on Web3 distribution directly to my own on-chain product—founding Irysnameservice to let users mint and manage readable on-chain identities within the Irys ecosystem.</p>
          <ul class="web3-list">
            <li><strong>Product-Market Positioning:</strong> Identified on-chain identity as a sticky, community-driven primitive for early ecosystem adopters.</li>
            <li><strong>Ecosystem Distribution Playbook:</strong> Leveraged partner networks, community campaigns, and clear user onboarding to accelerate organic minting volume.</li>
            <li><strong>Founder Ownership:</strong> Operated at the intersection of product roadmap, ecosystem partnerships, and community momentum.</li>
          </ul>
          <div class="web3-outcome">Measurable result: Scaled Irysnameservice to the #1 dApp in the Irys ecosystem · <a href="{prefix}projects/irysnameservice.html" style="text-decoration:underline">Read Case Study →</a></div>
        </article>
      </div>

      <div class="web3-footer-bar">
        <div class="web3-meta-pills">
          <span class="tag">Target: Account Manager / Partnerships / Ecosystem Lead</span>
          <span class="tag">Channels: X · Telegram · Discord</span>
          <span class="tag">Languages: English (Native) · Russian (B1) · French (A2)</span>
        </div>
        <a class="btn btn-primary btn-sm" href="{prefix}contact.html" data-prefill-topic="Crypto & Web3 Account Manager">Hire for Web3 Growth / AM ↗</a>
      </div>
    </div>
  </div>
</section>
"""


def hire_engine_section(prefix: str = "", section_id: str = "hire") -> str:
    return f"""
<section class="section" id="{section_id}">
  <div class="container">
    <div class="hire-band reveal">
      <div class="hire-grid">
        <div class="hire-copy">
          <div class="hire-identity">
            <div class="avatar-ring">
              <img src="{prefix}assets/images/henry-headshot.jpg" alt="Dr. Henry Okechi portrait">
            </div>
            <div class="status-pill"><span class="pulse-dot"></span>Available Now · Remote Worldwide</div>
          </div>
          <h2>Ready for your next <em>high-trust hire.</em></h2>
          <p>Open to <strong>Remote Clinical &amp; General AI Training / RLHF roles</strong>, <strong>Crypto &amp; Web3 Account Management &amp; Partnerships</strong>, and select 0→1 product collaborations. Replies within 24 hours.</p>
          <div class="direct-channels">
            <a class="channel-row" href="https://t.me/enryvanie" target="_blank" rel="noopener noreferrer">
              <div><small>Telegram (Fastest for Web3 / Crypto)</small><strong>@enryvanie · t.me/enryvanie</strong></div>
              <span class="mono" style="color:var(--gold)">Message ↗</span>
            </a>
            <a class="channel-row" href="mailto:enryvanie@gmail.com">
              <div><small>Direct Email</small><strong>enryvanie@gmail.com</strong></div>
              <span class="mono" style="color:var(--gold)">Email ↗</span>
            </a>
            <a class="channel-row" href="#" data-copy-email>
              <div><small>Prefer Gmail / Recruiter InMail?</small><strong>Copy email in one click</strong></div>
              <span class="mono" style="color:var(--gold)">Copy ⎘</span>
            </a>
            <a class="channel-row" href="https://www.linkedin.com/in/henry-okechi-b20283422" target="_blank" rel="noopener noreferrer">
              <div><small>LinkedIn</small><strong>henry-okechi-b20283422</strong></div>
              <span class="mono" style="color:var(--gold)">Connect ↗</span>
            </a>
            <a class="channel-row" href="https://x.com/Vanieofweb3" target="_blank" rel="noopener noreferrer">
              <div><small>X (Crypto / Web3 &amp; AI)</small><strong>@Vanieofweb3</strong></div>
              <span class="mono" style="color:var(--gold)">DM / Follow ↗</span>
            </a>
          </div>
        </div>

        <form class="brief-form" data-brief-form>
          <span class="chip-group-label">1. Role or Engagement Type</span>
          <div class="chip-group" role="group" aria-label="Inquiry topic">
            <button type="button" class="chip is-selected" data-topic-chip="Remote AI Training & Clinical RLHF">Clinical AI / RLHF Role</button>
            <button type="button" class="chip" data-topic-chip="Crypto & Web3 Account Manager">Crypto / Web3 Account Mgr</button>
            <button type="button" class="chip" data-topic-chip="0→1 Product or MVP Build">0→1 Web App / MVP</button>
            <button type="button" class="chip" data-topic-chip="Generative AI Video & LoRA">AI Video / LoRA Pipeline</button>
          </div>

          <span class="chip-group-label">2. Target Start</span>
          <div class="chip-group" role="group" aria-label="Target timeline">
            <button type="button" class="chip is-selected" data-timeline-chip="Immediate">Immediate</button>
            <button type="button" class="chip" data-timeline-chip="This Month">This Month</button>
            <button type="button" class="chip" data-timeline-chip="Contract / Advisory">Contract / Advisory</button>
          </div>

          <div class="form-row">
            <div class="field">
              <label for="brief-name">Your Name</label>
              <input id="brief-name" name="name" autocomplete="name" required placeholder="Alex Rivera">
            </div>
            <div class="field">
              <label for="brief-org">Company / Team</label>
              <input id="brief-org" name="org" autocomplete="organization" placeholder="AI Lab / Web3 Team / Studio">
            </div>
          </div>

          <div class="field">
            <label for="brief-notes">Role Details or Project Brief</label>
            <textarea id="brief-notes" name="notes" required placeholder="Share the role, team, domain focus, or interview link..."></textarea>
          </div>

          <div class="form-actions">
            <button type="submit" class="btn btn-primary">Send via Email App ↗</button>
            <button type="button" class="btn btn-secondary" data-copy-brief>Copy Formatted Brief ⎘</button>
          </div>
          <p class="form-status" aria-live="polite" data-form-status></p>
        </form>
      </div>
    </div>
  </div>
</section>
"""


# 1. INDEX PAGE
featured_projects = [p for p in PROJECTS if p.get("featured")]
index_body = f"""
<section class="hero">
  <div class="container">
    <div class="hero-grid">
      <div>
        <div class="status-pill"><span class="pulse-dot"></span>Available for Remote AI Roles, Web3 Partnerships &amp; Product Builds</div>
        <h1>Medical rigor.<br>Frontier AI.<br><em>Execution that ships.</em></h1>
        <p class="hero-lead">
          I'm <strong>Dr. Henry Okechi (MBBS)</strong> — a licensed physician, AI model trainer &amp; evaluator (Runpod, Appen, Kling AI), and Web3 account &amp; partnerships specialist with <strong>50+ crypto campaigns</strong>, <strong>75K+ reach</strong>, and <strong>English · Russian (B1) · French (A2)</strong> fluency.
        </p>

        <div class="hero-identity">
          <div class="avatar-ring">
            <img src="assets/images/henry-headshot.jpg" alt="Dr. Henry Okechi headshot">
          </div>
          <div class="hero-id-meta">
            <strong>Dr. Henry Okechi · MBBS</strong>
            <span>Remote Worldwide (UTC+1) · Native EN · RU (B1) · FR (A2)</span>
          </div>
        </div>

        <div class="hero-actions">
          <a class="btn btn-primary" href="#hire">Interview or Hire Me ↗</a>
          <a class="btn btn-secondary" href="assets/Henry_Okechi_CV.pdf" download>Download CV (PDF) ↓</a>
          <button type="button" class="btn btn-ghost" data-copy-email>Copy Email ⎘</button>
        </div>
      </div>

      <div class="proof-console" data-proof-console aria-label="Interactive showcase of live builds and trailer">
        <div class="console-chrome">
          <div class="chrome-dots" aria-hidden="true"><span></span><span></span><span></span></div>
          <span class="chrome-url" data-console-url>projects/azarun.html · Runpod LoRA + Kling AI</span>
          <span class="chrome-live" data-console-status><span class="pulse-dot"></span>PLAYABLE REEL</span>
        </div>
        <div class="console-stage" data-console-stage>
          <img src="assets/images/azarun-chains.jpg" alt="Azarun Cinematic AI Trailer" data-console-img>
          <div class="console-overlay">
            <div class="console-meta">
              <strong data-console-title>Azarun · Playable AI Trailer Reel</strong>
              <span data-console-sub>Custom Runpod LoRA (azarun_god_v1) + 4 Kling AI motion shots</span>
            </div>
            <a class="btn btn-primary btn-sm" href="projects/azarun.html#trailer-reel" data-console-cta>Watch Reel ▶</a>
          </div>
        </div>
        <div class="console-tabs" role="tablist" aria-label="Select featured showcase">
          <button type="button" class="console-tab is-active" role="tab" aria-selected="true"
            data-console-tab
            data-img="assets/images/azarun-chains.jpg"
            data-portrait="false"
            data-url-label="projects/azarun.html · Runpod LoRA + Kling AI"
            data-live="true"
            data-title="Azarun · Playable AI Trailer Reel"
            data-sub="Custom Runpod LoRA (azarun_god_v1) + 4 Kling AI motion shots"
            data-href="projects/azarun.html#trailer-reel"
            data-cta="Watch Reel ▶"
            data-external="false">
            <small>01 · AI Training</small>
            <strong>Azarun Reel</strong>
          </button>
          <button type="button" class="console-tab" role="tab" aria-selected="false"
            data-console-tab
            data-img="assets/images/live-medflash.png"
            data-portrait="false"
            data-url-label="mcqrecall.netlify.app"
            data-live="true"
            data-title="MedFlash · Clinical Board Review"
            data-sub="Physician-built PDF-to-MCQ active recall workspace"
            data-href="https://mcqrecall.netlify.app"
            data-cta="Launch App ↗"
            data-external="true">
            <small>02 · Clinical</small>
            <strong>MedFlash</strong>
          </button>
          <button type="button" class="console-tab" role="tab" aria-selected="false"
            data-console-tab
            data-img="assets/images/irys-home.jpg"
            data-portrait="false"
            data-url-label="Irysnameservice · #1 Irys dApp Demo"
            data-live="true"
            data-title="Irysnameservice · #1 Ecosystem dApp"
            data-sub="Live .irys domain minting, EVM/Solana & mutable-ref transfers"
            data-href="projects/irysnameservice.html#trailer-reel"
            data-cta="Watch Demo ▶"
            data-external="false">
            <small>03 · Web3 #1 dApp</small>
            <strong>Irys Names</strong>
          </button>
          <button type="button" class="console-tab" role="tab" aria-selected="false"
            data-console-tab
            data-img="assets/images/live-kasala.png"
            data-portrait="false"
            data-url-label="kasala.kasala.workers.dev"
            data-live="true"
            data-title="Kasala · 3D Battle Royale"
            data-sub="10-player browser shooter deployed on Cloudflare Workers"
            data-href="https://kasala.kasala.workers.dev"
            data-cta="Play Live ↗"
            data-external="true">
            <small>04 · 0→1 Build</small>
            <strong>Kasala 3D</strong>
          </button>
        </div>
      </div>
    </div>

    <div class="proof-strip reveal">
      <div class="proof-cell">
        <strong>MBBS</strong>
        <span>Licensed Medical Doctor</span>
      </div>
      <div class="proof-cell">
        <strong>Runpod + Appen</strong>
        <span>Custom LoRA training &amp; multi-modal RLHF</span>
      </div>
      <div class="proof-cell">
        <strong>50+ Campaigns</strong>
        <span>Web3 account sales, KOLs &amp; 75K+ reach</span>
      </div>
      <div class="proof-cell">
        <strong>EN · RU · FR</strong>
        <span>Native English · Russian (B1) · French (A2)</span>
      </div>
      <div class="proof-cell">
        <strong>6 Live Proofs</strong>
        <span>5 live web apps/games + playable AI reel</span>
      </div>
    </div>
  </div>
</section>

<div class="ecosystem-bar">
  <div class="container ecosystem-inner">
    <span class="ecosystem-label">Experience &amp; Ecosystems</span>
    <div class="ecosystem-logos">
      <span>Runpod</span>
      <span>Kling AI</span>
      <span>Appen</span>
      <span>Cointracts</span>
      <span>Beraskool</span>
      <span>Webacy</span>
      <span>Irys</span>
      <span>Pudgy Penguins</span>
      <span>DeGods</span>
      <span>Savvy Economist</span>
      <span>DTCSI Academy</span>
    </div>
  </div>
</div>

<section class="section" id="capabilities">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <div class="eyebrow">01 / Capabilities</div>
        <h2>Choose the track you are <em>hiring for.</em></h2>
      </div>
    </div>

    <div class="lens-shell reveal">
      <div class="lens-tabs" role="tablist" aria-label="Hiring tracks">
        <button type="button" class="lens-tab is-active" role="tab" aria-selected="true" data-lens-tab="ai-clinical">
          <span class="lens-num">Track 01 · AI Labs &amp; Healthtech</span>
          <strong>Clinical AI Training &amp; RLHF Evaluation</strong>
          <span>MBBS physician · Runpod GPU · Appen QA</span>
        </button>
        <button type="button" class="lens-tab" role="tab" aria-selected="false" data-lens-tab="web3-account">
          <span class="lens-num">Track 02 · Crypto &amp; Web3 Ecosystems</span>
          <strong>Crypto &amp; Web3 Account Management</strong>
          <span>Account sales · 50+ campaigns · EN / RU (B1)</span>
        </button>
        <button type="button" class="lens-tab" role="tab" aria-selected="false" data-lens-tab="product-cinema">
          <span class="lens-num">Track 03 · Products &amp; Media</span>
          <strong>0→1 AI Products &amp; Generative Cinema</strong>
          <span>5 live apps &amp; games · Playable Azarun reel</span>
        </button>
      </div>

      <div class="lens-panel is-active" data-lens-panel="ai-clinical" role="tabpanel">
        <div class="lens-pitch">
          <h3>A licensed physician who already trains, evaluates &amp; ships <em>AI systems.</em></h3>
          <p>Built for AI labs and healthtech teams tackling Clinical/Medical LLM evaluation, general RLHF, reasoning rubrics, and multimodal QA. I pair clinical medical training with proven GPU model training and six years of precision research writing.</p>
          <ul class="lens-bullets">
            <li><strong>Clinical Domain Depth (MBBS):</strong> Licensed medical doctor qualified to evaluate clinical accuracy, diagnostic reasoning, medical safety, and guideline compliance.</li>
            <li><strong>Hands-On AI Training &amp; QA:</strong> Trained custom character-consistency LoRAs (azarun_god_v1) on Runpod GPUs plus multi-modal text, image, and audio evaluation at Appen.</li>
            <li><strong>Gold-Standard Writing &amp; Rubrics:</strong> Native English speaker with 6 years of high-retention research &amp; scriptwriting (Savvy Economist)—delivering clear rationales and airtight edge-case critiques.</li>
          </ul>
          <a class="btn btn-primary" href="#hire" data-prefill-topic="Remote AI Training & Clinical RLHF">Discuss an AI Training / Clinical Role ↗</a>
        </div>
        <div class="lens-proof-box">
          <h4>Direct Proof for AI Talent Teams</h4>
          <div class="proof-mini-list">
            <a class="proof-mini-item" href="projects/azarun.html#trailer-reel">
              <div><strong>Runpod Custom LoRA (azarun_god_v1)</strong><span>Inspect cross-shot model consistency &amp; playable reel</span></div>
              <span class="arrow">→</span>
            </a>
            <a class="proof-mini-item" href="projects/mcq-recall.html">
              <div><strong>MedFlash (Live Clinical Web App)</strong><span>Physician-built board review &amp; active-recall engine</span></div>
              <span class="arrow">→</span>
            </a>
            <a class="proof-mini-item" href="projects/medforge.html">
              <div><strong>MedForge AI &amp; VitalPulse</strong><span>Clinical study &amp; emergency medical product UX</span></div>
              <span class="arrow">→</span>
            </a>
          </div>
          <div class="tag-row">
            <span class="tag">MBBS · Licensed MD</span>
            <span class="tag">RLHF &amp; LLM Eval</span>
            <span class="tag">Runpod GPU LoRA</span>
            <span class="tag">Appen Data QA</span>
            <span class="tag">Medical Fact-Checking</span>
          </div>
        </div>
      </div>

      <div class="lens-panel" data-lens-panel="web3-account" role="tabpanel">
        <div class="lens-pitch">
          <h3>Crypto-native account ownership, client delivery &amp; <em>multilingual communication.</em></h3>
          <p>Built for exchanges, Web3 agencies, SaaS protocols, and crypto projects hiring Account Managers or Partnerships Leads. I combine B2B account sales, 50+ delivered client campaigns, and Tier-1 community stewardship with English + Russian (B1) fluency.</p>
          <ul class="lens-bullets">
            <li><strong>Account Sales &amp; Advisory Track Record:</strong> Ambassador &amp; Account Sales at Cointracts (2025–2026), Product Marketer &amp; Growth at Beraskool, Project &amp; Content Advisor at Webacy, and PM at Anavrin DAO.</li>
            <li><strong>50+ Paid Crypto Campaigns Delivered:</strong> Scoped, managed, and fulfilled partner campaigns across NFTs, DeFi, and trading platforms—backed by 75K+ owned community reach (HERMES ALPHA ZONE &amp; Gem Jungle).</li>
            <li><strong>Ecosystem Authority &amp; Languages:</strong> Founded the #1 dApp on Irys, moderated DeGods &amp; Pudgy Penguins, and communicates across English (Native), Russian (B1), and French (A2).</li>
          </ul>
          <a class="btn btn-primary" href="#hire" data-prefill-topic="Crypto & Web3 Account Manager">Discuss a Crypto / Web3 AM Role ↗</a>
        </div>
        <div class="lens-proof-box">
          <h4>Web3 Commercial &amp; Growth Proof</h4>
          <div class="proof-mini-list">
            <a class="proof-mini-item" href="projects/hermes-growth.html">
              <div><strong>HERMES ALPHA ZONE &amp; Gem Jungle</strong><span>50+ paid crypto campaigns &amp; 75K+ community reach</span></div>
              <span class="arrow">→</span>
            </a>
            <a class="proof-mini-item" href="projects/web3-community-ops.html">
              <div><strong>DeGods · Pudgy Penguins · Cointracts · Webacy</strong><span>Tier-1 community ops, account sales &amp; advisory</span></div>
              <span class="arrow">→</span>
            </a>
            <a class="proof-mini-item" href="projects/irysnameservice.html">
              <div><strong>Irysnameservice (Founder · #1 dApp)</strong><span>Built &amp; grew top-ranked dApp in the Irys ecosystem</span></div>
              <span class="arrow">→</span>
            </a>
          </div>
          <div class="tag-row">
            <span class="tag">Account Management</span>
            <span class="tag">B2B Account Sales</span>
            <span class="tag">50+ Crypto Campaigns</span>
            <span class="tag">Russian (B1) · English</span>
            <span class="tag">DeFi · NFTs · Trading</span>
          </div>
        </div>
      </div>

      <div class="lens-panel" data-lens-panel="product-cinema" role="tabpanel">
        <div class="lens-pitch">
          <h3>Technical fluency proven by <em>live deployed software</em> &amp; AI cinema.</h3>
          <p>Unlike candidates who only talk strategy, I build and deploy real software—React/TypeScript apps with Firebase security tests, Anthropic Claude serverless endpoints, 3D browser games, and playable Kling AI trailers.</p>
          <ul class="lens-bullets">
            <li><strong>Full-Stack Apps:</strong> Project Mucci (Firebase Auth, Firestore rules, Vitest RBAC suite), MedFlash, and Hodos (Anthropic API + Netlify Functions + Airtable).</li>
            <li><strong>3 Live Browser 3D Games:</strong> Kasala (Cloudflare Workers), Wayo (open-source multiplayer prop hunt), and Naija Undead (Ojuelegba 3D WebGL survival).</li>
            <li><strong>Playable AI Cinema:</strong> Watch 4 real Kling AI &amp; Runpod LoRA shots directly inside the Azarun showcase.</li>
          </ul>
          <a class="btn btn-primary" href="#hire" data-prefill-topic="0→1 Product or MVP Build">Scope a Build or Technical Collab ↗</a>
        </div>
        <div class="lens-proof-box">
          <h4>Live Deployed Products</h4>
          <div class="proof-mini-list">
            <a class="proof-mini-item" href="projects/project-mucci.html">
              <div><strong>Project Mucci (Live Platform)</strong><span>React, TypeScript, Firebase RBAC &amp; Vitest</span></div>
              <span class="arrow">→</span>
            </a>
            <a class="proof-mini-item" href="projects/kasala.html">
              <div><strong>Kasala &amp; Wayo (Live 3D Games)</strong><span>Cloudflare Workers &amp; Netlify multiplayer builds</span></div>
              <span class="arrow">→</span>
            </a>
            <a class="proof-mini-item" href="projects/hodos.html">
              <div><strong>Hodos (Anthropic Claude API)</strong><span>Serverless AI assessment &amp; Airtable integration</span></div>
              <span class="arrow">→</span>
            </a>
          </div>
          <div class="tag-row">
            <span class="tag">React &amp; TypeScript</span>
            <span class="tag">Firebase &amp; Vitest</span>
            <span class="tag">Anthropic API</span>
            <span class="tag">Cloudflare Workers</span>
            <span class="tag">Kling AI &amp; Seedance</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section" id="selected-work">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <div class="eyebrow">02 / Verified Proof of Work</div>
        <h2>Real artifacts you can <em>watch, click &amp; test.</em></h2>
      </div>
      <p>Clinical software, playable Runpod LoRA &amp; Kling AI trailer shots, #1 Web3 dApp growth, and live full-stack deployments.</p>
    </div>

    <div class="project-grid">
      {''.join(project_card(p) for p in featured_projects)}
    </div>

    <div style="margin-top:34px;display:flex;flex-wrap:wrap;gap:14px;align-items:center;justify-content:space-between" class="reveal">
      <p style="margin:0;color:var(--muted);font-size:14.5px">Plus <strong style="color:var(--text)">HERMES ALPHA ZONE</strong>, <strong style="color:var(--text)">Tier-1 Web3 Ops</strong>, <strong style="color:var(--text)">Naija Undead</strong>, <strong style="color:var(--text)">MedForge AI</strong>, <strong style="color:var(--text)">Hodos</strong>, and <strong style="color:var(--text)">VitalPulse</strong> in the full catalog.</p>
      <a class="btn btn-secondary" href="work.html">Explore All 12 Case Studies →</a>
    </div>
  </div>
</section>

{web3_ecosystem_section()}

<section class="section section-tight">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <div class="eyebrow">04 / Endorsements</div>
        <h2>What teams &amp; partners <em>rely on.</em></h2>
      </div>
      <p>Consistent feedback across AI evaluation pipelines, Web3 partner accounts, and long-form editorial production.</p>
    </div>

    <div class="testimonials-grid">
      {''.join(f'''
      <article class="testimonial-card reveal">
        <div>
          <div class="quote-top">
            <span class="quote-mark" aria-hidden="true">“</span>
            <span class="quote-track">{e(track)}</span>
          </div>
          <blockquote style="margin-top:16px">{e(quote)}</blockquote>
        </div>
        <div class="quote-author">
          <strong>{e(role)}</strong>
          <span>{e(org)}</span>
        </div>
      </article>
      ''' for track, quote, role, org in TESTIMONIALS)}
    </div>
  </div>
</section>

<section class="section section-tight">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <div class="eyebrow">05 / Track Record</div>
        <h2>Recent roles &amp; <em>credentials.</em></h2>
      </div>
      <a class="btn btn-ghost btn-sm" href="about.html">Full Experience &amp; Education →</a>
    </div>

    <div class="exp-list reveal">
      {''.join(f'''
      <div class="exp-row">
        <span class="exp-date">{e(date)}</span>
        <div class="exp-main">
          <h3>{e(role)} · <span style="color:var(--gold-bright)">{e(org)}</span></h3>
          <p>{e(desc)}</p>
        </div>
        <span class="exp-tag">{e(tag)}</span>
      </div>
      ''' for date, role, org, tag, desc in EXPERIENCE[:5])}
    </div>
  </div>
</section>

{hire_engine_section()}
"""

(ROOT / "index.html").write_text(
    page_shell(
        "home",
        "Dr. Henry Okechi — Clinical AI Trainer, Web3 Account Manager & Builder",
        "Portfolio of Dr. Henry Okechi (MBBS): medical doctor, AI model trainer & RLHF evaluator (Runpod, Appen, Kling AI), Crypto & Web3 Account Manager (50+ campaigns, EN/RU/FR), and product builder.",
        index_body,
    ),
    encoding="utf-8",
)


# 2. WORK PAGE
filter_buttons = "".join(
    f'<button type="button" class="filter-pill{" is-active" if i == 0 else ""}" data-filter="{e(code)}" aria-pressed="{str(i == 0).lower()}">{e(label)}</button>'
    for i, (code, label) in enumerate(GROUPS)
)
work_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Complete Portfolio · 12 Case Studies</div>
    <h1>Clinical builds, Web3 growth &amp; <em>shipped products.</em></h1>
    <p>Filter by discipline to inspect live web deployments, custom Runpod LoRA training &amp; Kling AI video shots, Web3 campaign &amp; community operations, and clinical prototypes.</p>
  </div>
</section>

<section class="section" style="padding-top:16px">
  <div class="container">
    <div class="filter-bar">
      <div class="filter-pills" role="group" aria-label="Filter projects by discipline">
        {filter_buttons}
      </div>
      <span class="result-count" aria-live="polite" data-result-count>{len(PROJECTS)} projects shown</span>
    </div>

    <div class="project-grid">
      {''.join(project_card(p) for p in PROJECTS)}
    </div>
  </div>
</section>

{web3_ecosystem_section(eyebrow_text="Deep Dive · Web3 Growth & Account Leadership")}

{hire_engine_section()}
"""

(ROOT / "work.html").write_text(
    page_shell(
        "work",
        "Selected Work & Live Builds",
        "Explore 10 shipped web apps, playable Azarun AI trailer & Runpod LoRA shots, clinical AI prototypes, 3D browser games, and Web3 growth case studies by Dr. Henry Okechi.",
        work_body,
    ),
    encoding="utf-8",
)


# 3. ABOUT PAGE
about_body = f"""
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Background &amp; Credentials</div>
    <h1>Clinical discipline meets <em>AI rigor &amp; commercial execution.</em></h1>
    <p>Licensed MBBS physician with hands-on GPU model training &amp; RLHF evaluation, 50+ delivered Web3 client campaigns, six years of economics scriptwriting, and trilingual reach (EN · RU · FR).</p>
  </div>
</section>

<section class="section" style="padding-top:16px">
  <div class="container about-split">
    <aside class="profile-card">
      <div class="profile-photo-wrap">
        <img class="profile-photo" src="assets/images/henry-headshot.jpg" alt="Dr. Henry Okechi portrait">
      </div>
      <h2>Dr. Henry Okechi</h2>
      <div class="role-sub">MBBS · AI Trainer &amp; Evaluator · Web3 Account Mgr</div>
      <ul class="profile-facts">
        <li><span>Location</span><strong>Nigeria (Remote · UTC+1)</strong></li>
        <li><span>Medical Degree</span><strong>MBBS</strong></li>
        <li><span>Licensure</span><strong>Licensed MD</strong></li>
        <li><span>Languages</span><strong>EN · RU (B1) · FR (A2)</strong></li>
        <li><span>Target Roles</span><strong>Clinical AI · Web3 AM</strong></li>
        <li><span>Availability</span><strong style="color:var(--emerald)">Immediate</strong></li>
      </ul>
      <div style="display:grid;gap:10px">
        <a class="btn btn-primary" href="assets/Henry_Okechi_CV.pdf" download>Download Full CV (PDF) ↓</a>
        <a class="btn btn-secondary" href="https://t.me/enryvanie" target="_blank" rel="noopener noreferrer">Telegram (@enryvanie) ↗</a>
        <a class="btn btn-ghost" href="contact.html">Interview or Contact →</a>
        <button type="button" class="btn btn-ghost" data-copy-email>Copy enryvanie@gmail.com ⎘</button>
      </div>
    </aside>

    <div>
      <div class="eyebrow">The Through-Line</div>
      <h2 style="font-size:clamp(28px,3.2vw,40px);margin:14px 0 18px">High-judgment execution across <em>medicine, AI &amp; Web3 accounts.</em></h2>
      <p style="color:var(--text-soft);font-size:16.5px;margin:0 0 16px">
        I graduated with a Bachelor of Medicine, Bachelor of Surgery (MBBS) from Ebonyi State University College of Health Sciences and am a licensed medical doctor. Alongside clinical training, I built deep operational experience in AI data evaluation (Appen), custom GPU model training (Runpod), generative cinema (Kling AI), and six years of finance &amp; economics scriptwriting for Savvy Economist.
      </p>
      <p style="color:var(--text-soft);font-size:16.5px;margin:0 0 16px">
        In parallel, I spent five years inside crypto and Web3—serving in Account Sales &amp; Ambassador roles at Cointracts, Product Marketing &amp; Growth at Beraskool, Advisory at Webacy, managing communities for DeGods and Pudgy Penguins, delivering 50+ paid crypto client campaigns, and founding Irysnameservice (the #1 dApp in the Irys ecosystem).
      </p>
      <p style="color:var(--text-soft);font-size:16.5px;margin:0">
        Today, I bring these disciplines together across <strong>Clinical &amp; General AI Training / RLHF</strong>, <strong>Crypto &amp; Web3 Account Management &amp; Partnerships</strong>, and hands-on <strong>0→1 AI product building</strong>—where domain accuracy, commercial execution, and clear communication across English, Russian (B1), and French (A2) matter most.
      </p>

      <div class="eyebrow" style="margin-top:56px">Core Capabilities</div>
      <div class="tag-row" style="margin-top:16px">
        {''.join(f'<span class="tag">{e(s)}</span>' for s in [
            'Clinical Medicine & Medical Writing',
            'RLHF & LLM Output Evaluation',
            'Runpod Custom GPU LoRA Training',
            'Multi-Modal Data QA (Text, Image, Audio)',
            'Crypto & Web3 Account Management',
            'B2B Account Sales & Client Delivery',
            '50+ Paid Web3 Campaigns (75K+ Reach)',
            'English (Native) · Russian (B1) · French (A2)',
            'Kling AI & Seedance Production',
            'React, TypeScript & Firebase',
            'Anthropic API & Serverless Functions',
            'Economics & Finance Scriptwriting',
        ])}
      </div>

      <div class="eyebrow" style="margin-top:56px">Full Experience Timeline</div>
      <div class="exp-list" style="margin-top:20px">
        {''.join(f'''
        <div class="exp-row">
          <span class="exp-date">{e(date)}</span>
          <div class="exp-main">
            <h3>{e(role)} · <span style="color:var(--gold-bright)">{e(org)}</span></h3>
            <p>{e(desc)}</p>
          </div>
          <span class="exp-tag">{e(tag)}</span>
        </div>
        ''' for date, role, org, tag, desc in EXPERIENCE)}
      </div>

      <div class="eyebrow" style="margin-top:56px">Education &amp; Certifications</div>
      <div class="exp-list" style="margin-top:20px">
        <div class="exp-row">
          <span class="exp-date">MBBS</span>
          <div class="exp-main">
            <h3>Bachelor of Medicine, Bachelor of Surgery (MBBS)</h3>
            <p>Ebonyi State University College of Health Sciences · Licensed Medical Doctor.</p>
          </div>
          <span class="exp-tag">Clinical Degree</span>
        </div>
        <div class="exp-row">
          <span class="exp-date">2020</span>
          <div class="exp-main">
            <h3>AI, IT Support &amp; Security Certifications</h3>
            <p>Getting Started with AI using IBM Watson · Google IT Support Specialization · IT Security: Defense against the digital dark arts.</p>
          </div>
          <span class="exp-tag">Technical</span>
        </div>
      </div>
    </div>
  </div>
</section>
"""

(ROOT / "about.html").write_text(
    page_shell(
        "about",
        "Background, Clinical Credentials & Experience",
        "Learn about Dr. Henry Okechi (MBBS): clinical credentials, Runpod GPU LoRA training, Appen RLHF evaluation, Crypto & Web3 Account Management, and English/Russian/French fluency.",
        about_body,
    ),
    encoding="utf-8",
)


# 4. CONTACT PAGE
contact_body = f"""
<section class="page-hero" style="padding-bottom:10px">
  <div class="container">
    <div class="eyebrow">Direct Inquiry · Fast Response</div>
    <h1>Let's talk about your <em>role or team.</em></h1>
    <p>Select your focus area below to compose a structured brief—send straight via email or copy everything in one click for Gmail, LinkedIn, or Telegram.</p>
  </div>
</section>
{hire_engine_section(section_id="contact-brief")}
"""

(ROOT / "contact.html").write_text(
    page_shell(
        "contact",
        "Hire Dr. Henry Okechi — Contact & Brief",
        "Contact Dr. Henry Okechi for Remote Clinical AI Training / RLHF roles, Crypto & Web3 Account Management, or 0→1 product collaborations.",
        contact_body,
    ),
    encoding="utf-8",
)


# 5. CASE STUDY DETAIL PAGES (with interactive Video Reel + LoRA Gallery support!)
(ROOT / "projects").mkdir(exist_ok=True)
for idx, p in enumerate(PROJECTS):
    next_p = PROJECTS[(idx + 1) % len(PROJECTS)]
    prev_p = PROJECTS[(idx - 1) % len(PROJECTS)]

    media_cls = "case-hero-media"
    if p.get("image_style") == "framed-light":
        media_cls += " framed-light"
    elif p.get("image_style") == "framed-portrait":
        media_cls += " framed-portrait"

    aside_btns = "".join(
        f'<a class="btn {"btn-primary" if lnk.get("primary") else "btn-secondary"}" href="{e(lnk["url"])}" target="_blank" rel="noopener noreferrer">{e(lnk["label"])} ↗</a>'
        for lnk in p.get("links", [])
    )
    if p.get("video_reel"):
        cta_vid = "Watch Trailer Reel ▶" if len(p["video_reel"]) > 1 else "Watch Product Demo ▶"
        extra_links = "".join(
            f'<a class="btn btn-secondary" href="{e(lnk["url"])}" target="_blank" rel="noopener noreferrer">{e(lnk["label"])} ↗</a>'
            for lnk in p.get("links", [])
        )
        aside_btns = f'<a class="btn btn-primary" href="#trailer-reel">{cta_vid}</a>{extra_links}<a class="btn btn-ghost" href="../contact.html">Work With Henry →</a>'
    elif not aside_btns:
        aside_btns = '<a class="btn btn-primary" href="../contact.html">Discuss This Work ↗</a>'
    else:
        aside_btns += '<a class="btn btn-ghost" href="../contact.html">Work With Henry →</a>'

    stage_pill = (
        f'<span class="status-pill"><span class="pulse-dot"></span>{e(p["stage"])}</span>'
        if p.get("live")
        else f'<span class="eyebrow">{e(p["category_name"])} · {e(p["stage"])}</span>'
    )

    # Top media block: interactive playable video reel if present, else static hero media
    if p.get("video_reel"):
        first_vid = p["video_reel"][0]
        reel_tabs_block = ""
        if len(p["video_reel"]) > 1:
            reel_tabs_html = "".join(
                f'''<button type="button" class="reel-tab{" is-active" if i == 0 else ""}" role="tab" aria-selected="{str(i == 0).lower()}"
                  data-reel-tab
                  data-src="../{e(v['src'])}"
                  data-poster="../{e(v['poster'])}"
                  data-title="{e(v['title'])}"
                  data-meta="{e(v['meta'])}">
                  <small>Clip 0{i+1}</small>
                  <strong>{e(v['title'].split('·', 1)[-1].strip())}</strong>
                </button>'''
                for i, v in enumerate(p["video_reel"])
            )
            reel_tabs_block = f'<div class="reel-tabs" role="tablist" aria-label="Select video clip">{reel_tabs_html}</div>'
        hero_media_html = f"""
    <div class="video-reel" id="trailer-reel" data-video-reel>
      <div class="reel-bar">
        <strong data-reel-title>{e(first_vid['title'])}</strong>
        <span data-reel-meta>{e(first_vid['meta'])}</span>
      </div>
      <div class="reel-stage">
        <video data-reel-video controls playsinline preload="metadata" poster="../{e(first_vid['poster'])}" src="../{e(first_vid['src'])}"></video>
      </div>
      {reel_tabs_block}
    </div>
"""
    else:
        hero_media_html = f"""
    <div class="{media_cls}">
      <img src="../{e(p['image'])}" alt="{e(p['name'])} showcase">
      <div class="case-caption">{e(p['image_caption'])}</div>
    </div>
"""

    gallery_html = ""
    if p.get("gallery"):
        gallery_cards = "".join(
            f'''<figure class="lora-card" style="margin:0">
              <img src="../{e(g['src'])}" alt="{e(g['caption'])}" loading="lazy">
              <figcaption>{e(g['caption'])}</figcaption>
            </figure>'''
            for g in p["gallery"]
        )
        g_title = p.get("gallery_title", "Project Gallery")
        g_sub = p.get("gallery_subtitle", "")
        g_cls = "lora-gallery is-ui-contain" if p.get("gallery_style") == "ui-contain" else "lora-gallery"
        gallery_html = f"""
        <h2>{e(g_title)}</h2>
        <p>{e(g_sub)}</p>
        <div class="{g_cls}">{gallery_cards}</div>
"""

    detail_body = f"""
<section class="page-hero">
  <div class="container">
    <a class="back-link" href="../work.html">← Back to all 12 projects</a>
    <div>{stage_pill}</div>
    <h1>{e(p['name'])}<em>.</em></h1>
    <p>{e(p['tagline'])}</p>
  </div>
</section>

<section class="section" style="padding-top:10px">
  <div class="container">
    {hero_media_html}

    <div class="case-grid">
      <div class="case-content">
        <h2>The Challenge</h2>
        <p>{e(p['problem'])}</p>

        <h2>What I Built &amp; Directed</h2>
        <p>{e(p['overview'])}</p>

        <h2>Key Proof &amp; Outcomes</h2>
        <ul class="case-list">
          {''.join(f'<li>{e(item)}</li>' for item in p['impact'])}
        </ul>

        <h2>Core Features &amp; Architecture</h2>
        <ul class="case-list">
          {''.join(f'<li>{e(feat)}</li>' for feat in p['features'])}
        </ul>

        {gallery_html}
      </div>

      <aside class="case-aside" aria-label="Project specifications">
        <dl>
          <dt>Discipline</dt>
          <dd>{e(p['category_name'])}</dd>
          <dt>Status</dt>
          <dd>{e(p['stage'])}</dd>
          <dt>My Role</dt>
          <dd>{e(p['role'])}</dd>
          <dt>Year</dt>
          <dd>{e(p['year'])}</dd>
          <dt>Stack &amp; Tooling</dt>
          <dd><div class="tag-row" style="margin-top:6px">{''.join(f'<span class="tag">{e(s)}</span>' for s in p['stack'])}</div></dd>
        </dl>
        <div class="aside-actions">
          {aside_btns}
        </div>
      </aside>
    </div>

    <div style="margin-top:72px;padding-top:32px;border-top:1px solid var(--line);display:flex;justify-content:space-between;flex-wrap:wrap;gap:16px">
      <a class="btn btn-ghost" href="{e(prev_p['slug'])}.html">← {e(prev_p['name'])}</a>
      <a class="btn btn-secondary" href="{e(next_p['slug'])}.html">Next: {e(next_p['name'])} →</a>
    </div>
  </div>
</section>
"""

    (ROOT / "projects" / f"{p['slug']}.html").write_text(
        page_shell("work", f"{p['name']} — Case Study", p["tagline"], detail_body, prefix="../"),
        encoding="utf-8",
    )


# 6. FAVICON & README
(ROOT / "assets" / "favicon.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0%" stop-color="#f4c462"/><stop offset="100%" stop-color="#c4841c"/>'
    '</linearGradient></defs>'
    '<rect width="64" height="64" rx="16" fill="url(#g)"/>'
    '<text x="32" y="42" text-anchor="middle" font-family="system-ui,sans-serif" font-weight="800" font-size="26" fill="#09090b" letter-spacing="-1.5">HO</text>'
    '</svg>',
    encoding="utf-8",
)

(ROOT / "README.md").write_text(
    """# Dr. Henry Okechi — Portfolio (v3.1)

A conversion-engineered, editorial static portfolio showcasing clinical AI training & RLHF evaluation, Web3 growth & account management, full-stack products, and generative cinema.

## Preview Locally
```bash
python -m http.server 8000
```
Then open `http://localhost:8000`.

## Deploy
Zero build step required for hosting—drag and drop the folder or connect the repository directly to **Netlify**, **Cloudflare Pages**, **Vercel**, or **GitHub Pages**. All embedded Azarun `.mp4` clips are under 8.1 MB each (well within Cloudflare Pages' 25 MB single-file limit).

## Updating Content
- Edit `projects.json` for project copy, links, video clips, or gallery frames.
- Edit `TESTIMONIALS` or `EXPERIENCE` in `build.py` to swap in named client/manager references.
- Run `python build.py` to regenerate all static HTML pages.
""",
    encoding="utf-8",
)

print(f"Built v3.1 portfolio successfully: index, work, about, contact + {len(PROJECTS)} case studies.")
