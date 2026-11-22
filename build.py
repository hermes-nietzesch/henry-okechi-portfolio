"""Build the Obsidian & Ivory editorial portfolio for Henry Okechi.
Usage: python build.py
"""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent
PROJECTS = json.loads((ROOT / "projects.json").read_text(encoding="utf-8"))

FILTER_GROUPS = [
    ("all", "All (12)"),
    ("live", "Live & Playable (7)"),
    ("health", "Healthcare"),
    ("ai", "AI"),
    ("products", "Products"),
    ("games", "Games"),
    ("creative", "Cinema"),
    ("web3", "Web3"),
]

CAPABILITIES = [
    (
        "01",
        "AI & Intelligent Systems",
        "LLM output evaluation, RLHF rubric execution, and custom GPU model training on Runpod for visual character consistency—grounded in multi-modal annotation experience at Appen.",
        "RLHF · Model Evaluation · Runpod LoRA · Prompt Architecture · Anthropic API",
    ),
    (
        "02",
        "Healthcare & Medical Technology",
        "Licensed MBBS physician applying frontline diagnostic reasoning and patient-safety standards to clinical AI evaluation, medical writing, and healthcare interface prototypes.",
        "Clinical Medicine · Medical Verification · MedFlash · MedForge AI · VitalPulse",
    ),
    (
        "03",
        "Product Engineering",
        "Turning ideas into deployed web software—combining React, TypeScript, Firebase authentication and security tests, serverless functions, and fast static hosting.",
        "React · TypeScript · Firebase & Firestore · Vitest · Netlify & Cloudflare",
    ),
    (
        "04",
        "Games & Interactive Experiences",
        "Directing and shipping zero-install 3D browser games end to end—spanning gameplay loops, multiplayer room codes, AI-assisted 3D character pipelines, and spatial audio.",
        "3D WebGL · Multiplayer Lobbies · Kasala · Wayo · Naija Undead",
    ),
    (
        "05",
        "Research & Creative Production",
        "Six years of finance and economics scriptwriting paired with generative cinema production across Kling AI and Seedance, translating dense topics into coherent narratives.",
        "Scriptwriting · Technical Writing · Kling AI · Seedance · Shot Continuity",
    ),
    (
        "06",
        "Web3 Growth & Ecosystem Development",
        "Account sales, partnerships, high-traffic community stewardship, and blockchain product founding—communicating fluently across English, Russian (B1), and French (A2).",
        "Partnerships · 50+ Campaigns · 75K+ Reach · Irysnameservice · Trust & Safety",
    ),
]

EXPERIENCE = [
    (
        "2026",
        "AI Model Trainer",
        "Runpod (GPU Infrastructure)",
        "Trained custom character-consistency LoRA models (azarun_god_v1) on Runpod GPUs and evaluated checkpoint quality across multi-shot generations.",
        "Trained custom AI character-consistency LoRA models (azarun_god_v1) on Runpod GPUs; ran iterative training experiments, evaluated checkpoint outputs, and refined datasets and prompts to maintain visual continuity across shots.",
    ),
    (
        "2026 — Present",
        "AI & Content Specialist",
        "Kling AI",
        "Directed and produced the Azarun AI cinematic trailer across Kling AI, Seedance, Gemini, and GPT.",
        "Created an AI-generated cinematic trailer introducing Azarun, an African mythological hero—leading prompt architecture, shot planning, and visual iteration across Kling AI, Seedance, Gemini, and GPT.",
    ),
    (
        "2026 — Present",
        "AI Product & Game Builder",
        "Independent",
        "Built and deployed live web apps and 3D browser games including MedFlash, Project Mucci, Kasala, Wayo, and Naija Undead.",
        "Directed and deployed web products and mobile-first 3D browser games including Kasala (Cloudflare Workers), Wayo (Netlify), Naija Undead, Project Mucci (Firebase + Vitest), and MedFlash.",
    ),
    (
        "2024 — Present",
        "Founder & Partnerships Lead",
        "Irysnameservice · HERMES ALPHA ZONE · Gem Jungle",
        "Founded Irysnameservice (#1 Irys dApp per CV) and delivered 50+ paid crypto campaigns across 75K+ combined community reach.",
        "Founded a blockchain domain-minting and on-chain identity service on Irys with EVM/Solana wallets, mutable-reference transfers, and interactive flashcards (documented in CV as reaching #1 dApp in the Irys ecosystem), while operating HERMES ALPHA ZONE & Gem Jungle (75K+ reach, 50+ paid campaigns).",
    ),
    (
        "2025 — 2026",
        "Account Sales, Marketing & Advisory",
        "Cointracts · Beraskool · Webacy",
        "Account sales at Cointracts, product growth at Beraskool, and project/content advisory at Webacy.",
        "Ambassador & Account Sales at Cointracts (2025–2026); Product Marketer & Growth at Beraskool (2025–2026); Project & Content Advisor at Webacy (2024–2025).",
    ),
    (
        "2019 — 2021",
        "AI Data Annotator",
        "Appen",
        "Annotated and evaluated multi-modal text, image, and audio ML datasets under strict quality guidelines.",
        "Annotated and labeled text, image, and audio datasets for machine-learning pipelines—executing categorization, relevance rating, and content evaluation under evolving quality rubrics.",
    ),
    (
        "2018 — 2024",
        "Research & Script Writer",
        "Savvy Economist",
        "Six years researching and writing long-form finance and economics scripts for a public educational YouTube channel.",
        "Six years researching, structuring, and writing long-form finance and economics scripts for a public educational YouTube channel with consistent voice and editorial rigor.",
    ),
    (
        "2021 — 2026",
        "Content Writer & Community Comms",
        "DTCSI Academy",
        "Authored educational program copy, announcements, and technical Web3 explainers.",
        "Authored educational program copy, announcements, and clear technical Web3 explanations for both newcomers and experienced members.",
    ),
    (
        "2021 — 2025",
        "Web3 Community & Project Manager",
        "DeGods · Pudgy Penguins · Beraskool · Primates · Anavrin DAO",
        "Managed high-traffic moderation, trust & safety, and DAO project operations across global Web3 communities.",
        "Managed and moderated high-traffic communities with disciplined guidelines, content review, and trust & safety judgment; previously Project Manager at Anavrin DAO (2022–2023).",
    ),
]


def e(val) -> str:
    return escape(str(val), quote=True)


def header(active: str, prefix: str = "", light_top: bool = False) -> str:
    nav_items = [
        (f"{prefix}work.html", "Work", "work"),
        (f"{prefix}about.html", "About", "about"),
        (f"{prefix}index.html#experience", "Experience", "experience"),
        (f"{prefix}contact.html", "Contact", "contact"),
    ]
    links_html = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if active == key else ""}>{label}</a>'
        for href, label, key in nav_items
    )
    drawer_links = "".join(
        f'<a href="{href}">{label}</a>'
        for href, label, _ in [
            (f"{prefix}index.html", "Overview", "home"),
            *nav_items,
            (f"{prefix}assets/Henry_Okechi_CV.pdf", "Curriculum Vitae (PDF)", "cv"),
        ]
    )
    cls = "site-header is-light-top" if light_top else "site-header"
    return f"""
<div class="scroll-progress" data-scroll-progress aria-hidden="true"></div>
<a class="skip-link" href="#main">Skip to content</a>
<header class="{cls}" data-site-header data-scrolled="false">
  <div class="container nav-inner">
    <a class="brand-wordmark" href="{prefix}index.html" aria-label="Henry Okechi home">
      <span class="brand-monogram" aria-hidden="true">HO</span>
      <span>HENRY OKECHI</span>
    </a>
    <div class="nav-right">
      <nav class="nav-links" aria-label="Primary navigation">
        {links_html}
      </nav>
      <button type="button" class="theme-btn" data-theme-toggle aria-label="Toggle reading theme" aria-pressed="false">◐</button>
      <button type="button" class="nav-toggle" data-menu-toggle aria-expanded="false" aria-controls="mobile-drawer">Menu</button>
    </div>
  </div>
</header>
<div class="mobile-drawer" id="mobile-drawer" data-mobile-drawer>
  <nav aria-label="Mobile navigation">
    {drawer_links}
  </nav>
  <div class="mobile-drawer-foot">
    <span>enryvanie@gmail.com</span>
    <span>t.me/enryvanie · @Vanieofweb3</span>
  </div>
</div>
"""


def closing_contact_band(prefix: str = "", include_cta_block: bool = True) -> str:
    cta_html = ""
    if include_cta_block:
        cta_html = f"""
    <div class="closing-spread reveal">
      <div>
        <div class="eyebrow">Contact</div>
        <h2 class="closing-headline">Have something ambitious <em>in mind?</em></h2>
        <p class="closing-copy">I'm open to thoughtful collaborations, remote roles, and meaningful challenges across AI, healthcare, product engineering, and Web3 ecosystems.</p>
        <div class="oversized-email-wrap">
          <a class="oversized-email" href="mailto:enryvanie@gmail.com">enryvanie@gmail.com</a>
          <button type="button" class="btn-primary" data-copy-email>Copy Email Address</button>
        </div>
      </div>

      <div class="closing-directory">
        <dl class="closing-meta-grid">
          <div>
            <dt>Availability</dt>
            <dd>Remote Worldwide · UTC+1</dd>
          </div>
          <div>
            <dt>Languages</dt>
            <dd>English · Russian (B1) · French (A2)</dd>
          </div>
        </dl>
        <nav class="closing-dir-list" aria-label="Direct contact channels">
          <a class="closing-dir-row" href="https://t.me/enryvanie" target="_blank" rel="noopener noreferrer">
            <span>Telegram (@enryvanie)</span>
            <span>Direct Message ↗</span>
          </a>
          <a class="closing-dir-row" href="https://www.linkedin.com/in/henry-okechi-b20283422" target="_blank" rel="noopener noreferrer">
            <span>LinkedIn</span>
            <span>Profile ↗</span>
          </a>
          <a class="closing-dir-row" href="https://x.com/Vanieofweb3" target="_blank" rel="noopener noreferrer">
            <span>X (@Vanieofweb3)</span>
            <span>Social ↗</span>
          </a>
          <a class="closing-dir-row" href="https://github.com/hermes-nietzesch" target="_blank" rel="noopener noreferrer">
            <span>GitHub (hermes-nietzesch)</span>
            <span>Repositories ↗</span>
          </a>
          <a class="closing-dir-row" href="{prefix}assets/Henry_Okechi_CV.pdf" download>
            <span>Curriculum Vitae (PDF)</span>
            <span>Download ↓</span>
          </a>
          <a class="closing-dir-row" href="{prefix}contact.html">
            <span>Compose a Structured Brief</span>
            <span>Contact Page →</span>
          </a>
        </nav>
      </div>
    </div>
"""
    return f"""
<footer class="band-obsidian closing-frame" id="contact">
  <div class="container">
    {cta_html}
    <div class="site-footer-bar">
      <span>© <span data-year>2026</span> Henry Okechi — Medicine, AI, Product &amp; Web3</span>
      <span>Nigeria · Remote Worldwide (UTC+1)</span>
    </div>
  </div>
</footer>
<script src="{prefix}site.js" defer></script>
"""


def page_shell(active: str, title: str, description: str, body: str, prefix: str = "", light_top: bool = False, include_closing_cta: bool = True) -> str:
    full_title = title if "Henry Okechi" in title else f"{title} — Henry Okechi"
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#10131A">
  <meta name="description" content="{e(description)}">
  <meta property="og:title" content="{e(full_title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="website">
  <title>{e(full_title)}</title>
  <link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{prefix}style.css">
</head>
<body>
  {header(active, prefix, light_top=light_top)}
  <main id="main">
    {body}
  </main>
  {closing_contact_band(prefix, include_cta_block=include_closing_cta)}
</body>
</html>
"""


def render_work_item(p: dict, prefix: str = "", allow_dark_plate: bool = True, idx_pos: int = 0, display_index: str = None) -> str:
    case_href = f"{prefix}projects/{e(p['slug'])}.html"
    img_src = f"{prefix}{e(p['image'])}"
    shown_idx = display_index or p["index"]
    frame_cls = "work-media-frame"
    if p.get("image_style") == "framed-ui":
        frame_cls += " is-ui"
    elif p.get("image_style") == "framed-portrait":
        frame_cls += " is-portrait"

    is_dark = allow_dark_plate and p.get("feature_layout") == "obsidian-full"
    is_reversed = (not is_dark) and (p.get("feature_layout") == "ivory-right" or (idx_pos % 2 == 1 and p.get("feature_layout") != "ivory-left"))
    wrapper_cls = "work-feature-dark reveal" if is_dark else ("work-row is-reversed reveal" if is_reversed else "work-row reveal")

    primary_action = ""
    if p.get("video_reel"):
        lbl = "Watch Trailer Reel" if len(p["video_reel"]) > 1 else "Watch Product Demo"
        primary_action = f'<a class="btn-link" href="{case_href}#media-player">{lbl} <span class="arrow">→</span></a>'
    elif p.get("links"):
        first = p["links"][0]
        primary_action = f'<a class="btn-link" href="{e(first["url"])}" target="_blank" rel="noopener noreferrer">{e(first["label"])} <span class="arrow">↗</span></a>'

    stack_text = " · ".join(p["stack"][:4])

    return f"""
<article class="{wrapper_cls}" data-work-item data-category="{e(p['category'])}" data-live="{str(bool(p.get('live'))).lower()}">
  <a href="{case_href}" class="work-media" aria-label="View {e(p['name'])} case study">
    <div class="{frame_cls}">
      <img src="{img_src}" alt="{e(p['name'])} — {e(p['short'])}" loading="lazy">
    </div>
    <div class="work-media-bar">
      <span>{e(p['media_label'])}</span>
      <span class="status-txt">{e(p['stage'])}</span>
    </div>
  </a>
  <div class="work-info">
    <div class="work-index">
      <strong>{e(shown_idx)}</strong>
      <span>— {e(p['category_label'])}</span>
    </div>
    <h3 class="work-title"><a href="{case_href}">{e(p['name'])}</a></h3>
    <p class="work-tagline">{e(p['tagline'])}</p>
    <dl class="work-meta-list">
      <div>
        <dt>Role</dt>
        <dd>{e(p['role'])}</dd>
      </div>
      <div>
        <dt>Stack &amp; Craft</dt>
        <dd>{e(stack_text)}</dd>
      </div>
    </dl>
    <div class="work-links">
      <a class="btn-primary" href="{case_href}">Read Case Study →</a>
      {primary_action}
    </div>
  </div>
</article>
"""


def render_capabilities_tiered() -> str:
    primary = CAPABILITIES[:3]
    secondary = CAPABILITIES[3:]
    return f"""
    <div class="cap-tier-label reveal">
      <span>Primary Focus — AI, Healthcare &amp; Product Engineering</span>
      <span>01 — 03</span>
    </div>
    <div class="cap-grid is-primary">
      {''.join(f'''
      <article class="cap-item is-primary reveal">
        <span class="cap-num">{e(num)}</span>
        <h3>{e(title)}</h3>
        <p>{e(desc)}</p>
        <div class="cap-detail">{e(detail)}</div>
      </article>
      ''' for num, title, desc, detail in primary)}
    </div>

    <div class="cap-tier-label is-secondary reveal">
      <span>Extended Practice — Interactive Media, Research &amp; Web3</span>
      <span>04 — 06</span>
    </div>
    <div class="cap-grid">
      {''.join(f'''
      <article class="cap-item is-secondary reveal">
        <span class="cap-num">{e(num)}</span>
        <h3>{e(title)}</h3>
        <p>{e(desc)}</p>
        <div class="cap-detail">{e(detail)}</div>
      </article>
      ''' for num, title, desc, detail in secondary)}
    </div>
"""


# =========================================================
# 1. HOMEPAGE (EXACT OBSIDIAN & IVORY EDITORIAL SEQUENCE)
# =========================================================
HOME_FEATURED_SLUGS = ["azarun", "mcq-recall", "project-mucci", "kasala"]
featured = [next(p for p in PROJECTS if p["slug"] == slug) for slug in HOME_FEATURED_SLUGS]
archive_rest = [p for p in PROJECTS if p["slug"] not in HOME_FEATURED_SLUGS]

home_body = f"""
<!-- 01. HERO: OBSIDIAN -->
<section class="band-obsidian hero">
  <div class="container">
    <div class="hero-top-meta hero-stagger-1">
      <span class="eyebrow">Independent Creative Technologist / Nigeria</span>
      <span class="availability-note"><span class="status-dot" aria-hidden="true"></span>Available for Remote Roles &amp; Collaborations · UTC+1</span>
    </div>

    <div class="hero-main">
      <div>
        <h1 class="hero-headline hero-stagger-2">Building at the intersection of <em>intelligence and imagination.</em></h1>
        <p class="hero-sub hero-stagger-3">
          I'm Henry Okechi — a licensed medical doctor, AI practitioner, and multidisciplinary product builder creating digital experiences across healthcare, education, gaming, and emerging technology.
        </p>
        <div class="hero-actions hero-stagger-4">
          <a class="btn-primary" href="#work">Explore selected work →</a>
          <a class="btn-link" href="about.html">About me <span class="arrow">→</span></a>
          <a class="btn-link" href="assets/Henry_Okechi_CV.pdf" download>Curriculum Vitae <span class="arrow">↓</span></a>
        </div>
      </div>

      <div class="hero-portrait-col hero-stagger-3">
        <figure class="editorial-portrait" style="margin:0">
          <div class="editorial-portrait-frame">
            <img src="assets/images/henry-headshot.jpg" alt="Portrait of Dr. Henry Okechi">
          </div>
          <figcaption>
            <span class="portrait-name">Dr. Henry Okechi</span>
            <span class="portrait-role">MBBS · AI · Product</span>
          </figcaption>
        </figure>
      </div>
    </div>

    <div class="hero-bottom hero-stagger-4">
      <div class="hero-stat">
        <small>Clinical Foundation</small>
        <span>MBBS · Licensed Medical Doctor</span>
      </div>
      <div class="hero-stat">
        <small>AI Systems</small>
        <span>Runpod GPU LoRA · Appen RLHF &amp; QA</span>
      </div>
      <div class="hero-stat">
        <small>Shipped Work</small>
        <span>Live Web Apps, 3D Games &amp; Playable Reels</span>
      </div>
      <div class="hero-stat">
        <small>Global Reach</small>
        <span>English (Native) · Russian (B1) · French (A2)</span>
      </div>
    </div>
  </div>
</section>

<!-- 02. INTRODUCTION: WARM IVORY -->
<section class="band-ivory section" id="intro">
  <div class="container">
    <div class="intro-grid reveal">
      <div>
        <div class="eyebrow"><span class="eyebrow-num">01</span> The Intelligent Polymath</div>
        <h2 class="intro-statement">Curiosity is the thread <em>connecting everything.</em></h2>
      </div>
      <div class="intro-prose">
        <p>Most careers ask you to choose one lane: clinical rigor, technical engineering, creative storytelling, or commercial distribution. My work lives where those disciplines reinforce each other.</p>
        <p>Medical training sharpens diagnostic judgment and respect for accuracy when stakes are real. Years of AI data evaluation, custom GPU model training on Runpod, six years of economics scriptwriting, and hands-on product building turn that judgment into software, interactive worlds, and clear communication.</p>
        <dl class="intro-facts">
          <div class="intro-fact">
            <dt>Disciplines</dt>
            <dd>Medicine · AI · Product · Web3</dd>
          </div>
          <div class="intro-fact">
            <dt>Working Style</dt>
            <dd>Research-led, bias to live artifacts</dd>
          </div>
          <div class="intro-fact">
            <dt>Languages</dt>
            <dd>English · Russian (B1) · French (A2)</dd>
          </div>
        </dl>
      </div>
    </div>
  </div>
</section>

<!-- 03. SELECTED WORK: WARM IVORY + OCCASIONAL OBSIDIAN FEATURE PLATES -->
<section class="band-soft section" id="work">
  <div class="container">
    <div class="section-header reveal">
      <div>
        <div class="eyebrow"><span class="eyebrow-num">02</span> Selected Work</div>
        <h2 class="section-title">Products, games &amp; <em>intelligent systems.</em></h2>
      </div>
      <p class="section-intro">Every live product uses actual deployment captures or native demo video; conceptual prototypes are labeled transparently alongside their repositories.</p>
    </div>

    <div class="editorial-works">
      {''.join(render_work_item(p, allow_dark_plate=True, idx_pos=i, display_index=f'{i+1:02d}') for i, p in enumerate(featured))}
    </div>

    <div class="archive-index reveal">
      <div class="archive-head">
        <span class="eyebrow">Catalogue Index — 8 Additional Projects</span>
        <a class="btn-link" href="work.html">Explore full 12-project catalogue <span class="arrow">→</span></a>
      </div>
      <div>
        {''.join(f'''
        <a class="archive-row" href="projects/{e(p['slug'])}.html">
          <span class="archive-num">{e(p['index'])}</span>
          <span class="archive-name">{e(p['name'])}</span>
          <span class="archive-desc">{e(p['short'])}</span>
          <span class="archive-stage">{e(p['stage'])} →</span>
        </a>
        ''' for p in archive_rest)}
      </div>
    </div>
  </div>
</section>

<!-- 04. CAPABILITIES: OBSIDIAN -->
<section class="band-obsidian section" id="capabilities">
  <div class="container">
    <div class="section-header reveal">
      <div>
        <div class="eyebrow"><span class="eyebrow-num">03</span> Capabilities</div>
        <h2 class="section-title">Six disciplines, one <em>cohesive practice.</em></h2>
      </div>
      <p class="section-intro">Anchored in AI systems, clinical medicine, and product engineering—extended across interactive media, research, and Web3.</p>
    </div>

    {render_capabilities_tiered()}
  </div>
</section>

<!-- 05. WEB3 GROWTH & ECOSYSTEM DEVELOPMENT: WARM IVORY -->
<section class="band-ivory section" id="web3">
  <div class="container">
    <div class="section-header reveal">
      <div>
        <div class="eyebrow"><span class="eyebrow-num">04</span> Commercial &amp; Community Operations</div>
        <h2 class="section-title">Web3 Growth &amp; <em>Ecosystem Development.</em></h2>
      </div>
      <p class="section-intro">Five years operating across account sales, partner campaigns, high-traffic community moderation, and on-chain product founding—communicating across English, Russian (B1), and French (A2).</p>
    </div>

    <div class="web3-metrics reveal">
      <div class="web3-metric">
        <strong>50+</strong>
        <span>Paid Campaigns</span>
        <small>NFTs, DeFi &amp; trading platforms across X, Telegram &amp; Discord (CV)</small>
      </div>
      <div class="web3-metric">
        <strong>75K+</strong>
        <span>Combined Reach</span>
        <small>Owned communities: HERMES ALPHA ZONE &amp; Gem Jungle (CV)</small>
      </div>
      <div class="web3-metric">
        <strong>#1 dApp</strong>
        <span>Irysnameservice</span>
        <small>Founded on-chain naming product in the Irys ecosystem (CV)</small>
      </div>
      <div class="web3-metric">
        <strong>5 Yrs</strong>
        <span>Ecosystem Ops</span>
        <small>DeGods, Pudgy Penguins, Cointracts, Beraskool &amp; Webacy</small>
      </div>
    </div>

    <div class="web3-columns">
      <div class="web3-block reveal">
        <div class="web3-block-meta">
          <span>01 · Partnerships &amp; Account Delivery</span>
          <span>HERMES ALPHA ZONE · Gem Jungle · Cointracts</span>
        </div>
        <h3>Campaign Scoping &amp; Commercial Execution</h3>
        <p>Paired owned Telegram and X distribution with direct B2B account sales (Cointracts) and growth marketing (Beraskool)—aligning partner goals with clear narrative positioning.</p>
        <ul class="editorial-list">
          <li><strong>Account Management:</strong> Scoped deliverables, timelines, and messaging across international crypto teams.</li>
          <li><strong>Narrative Clarity:</strong> Translated DeFi, trading, and NFT product updates into structured briefings rather than empty hype.</li>
          <li><strong>Cross-Channel Rollout:</strong> Coordinated launches across X, Telegram, and Discord.</li>
        </ul>
        <a class="btn-link" href="projects/hermes-growth.html">Read campaign &amp; partnerships study <span class="arrow">→</span></a>
      </div>

      <div class="web3-block reveal">
        <div class="web3-block-meta">
          <span>02 · Community Stewardship &amp; Product</span>
          <span>DeGods · Pudgy Penguins · Irys · Webacy</span>
        </div>
        <h3>Trust, Safety &amp; Blockchain Founding</h3>
        <p>Stewarded high-traffic communities during peak visibility cycles while founding Irysnameservice and advising projects on content and security positioning.</p>
        <ul class="editorial-list">
          <li><strong>Trust &amp; Safety:</strong> Enforced moderation guidelines and clear holder communications for DeGods, Pudgy Penguins, Beraskool, and Primates.</li>
          <li><strong>Advisory &amp; Comms:</strong> Project &amp; Content Advisor at Webacy, Project Manager at Anavrin DAO, and technical writer at DTCSI Academy.</li>
          <li><strong>On-Chain Product:</strong> Founded Irysnameservice with EVM/Solana wallets, mutable-reference transfers, and interactive flashcards.</li>
        </ul>
        <a class="btn-link" href="projects/irysnameservice.html">Inspect Irysnameservice demo <span class="arrow">→</span></a>
      </div>
    </div>
  </div>
</section>

<!-- 06. EXPERIENCE: SOFT WHITE / WARM IVORY TIMELINE -->
<section class="band-soft section" id="experience">
  <div class="container">
    <div class="section-header reveal">
      <div>
        <div class="eyebrow"><span class="eyebrow-num">05</span> Experience</div>
        <h2 class="section-title">A decade across research, <em>AI &amp; communities.</em></h2>
      </div>
      <div>
        <p class="section-intro">Concise, scannable record across model training, evaluation, product engineering, scriptwriting, and Web3 leadership.</p>
        <div style="margin-top:16px">
          <a class="btn-link" href="about.html">Full biography &amp; credentials <span class="arrow">→</span></a>
        </div>
      </div>
    </div>

    <div class="timeline">
      {''.join(f'''
      <div class="timeline-row reveal">
        <span class="timeline-date">{e(dates)}</span>
        <div class="timeline-role">
          <h3>{e(role)}</h3>
          <span>{e(org)}</span>
        </div>
        <p class="timeline-desc">{e(short_desc)}</p>
      </div>
      ''' for dates, role, org, short_desc, _full in EXPERIENCE[:6])}
      <div class="timeline-row reveal">
        <span class="timeline-date">MBBS</span>
        <div class="timeline-role">
          <h3>Bachelor of Medicine, Bachelor of Surgery</h3>
          <span>Ebonyi State University College of Health Sciences</span>
        </div>
        <p class="timeline-desc">Licensed Medical Doctor. Certifications in IBM Watson AI, Google IT Support, and IT Security.</p>
      </div>
    </div>
    <div style="margin-top:28px" class="reveal">
      <a class="btn-link" href="about.html#full-timeline">View complete experience archive (all roles &amp; details) <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""

(ROOT / "index.html").write_text(
    page_shell(
        "home",
        "Henry Okechi — Medicine, AI, Product & Web3",
        "Portfolio of Dr. Henry Okechi (MBBS): licensed medical doctor, AI practitioner, multidisciplinary product builder, and Web3 growth & partnerships specialist.",
        home_body,
        light_top=False,
    ),
    encoding="utf-8",
)


# =========================================================
# 2. WORK PAGE (ALL 12 PROJECTS WITH ACCESSIBLE FILTERS)
# =========================================================
filter_btns_html = "".join(
    f'<button type="button" class="filter-btn{" is-active" if i == 0 else ""}" data-filter="{e(code)}" aria-pressed="{str(i == 0).lower()}">{e(label)}</button>'
    for i, (code, label) in enumerate(FILTER_GROUPS)
)
work_body = f"""
<section class="band-obsidian page-header">
  <div class="container">
    <div class="eyebrow">Selected Work — 12 Projects</div>
    <h1>Products, games, AI cinema &amp; <em>prototypes.</em></h1>
    <p>Every entry distinguishes deployed web products and playable demos from interface prototypes and codebase studies.</p>
  </div>
</section>

<section class="band-ivory section-compact">
  <div class="container">
    <div class="filter-bar">
      <div class="filter-group" role="group" aria-label="Filter projects by category">
        {filter_btns_html}
      </div>
      <span class="mono-meta" aria-live="polite" data-result-count>{len(PROJECTS)} projects</span>
    </div>

    <div class="editorial-works">
      {''.join(render_work_item(p, allow_dark_plate=True, idx_pos=i) for i, p in enumerate(PROJECTS))}
    </div>
  </div>
</section>
"""

(ROOT / "work.html").write_text(
    page_shell(
        "work",
        "Selected Work",
        "Explore 12 projects spanning AI model training, healthcare tools, full-stack platforms, 3D browser games, generative cinema, and Web3 ecosystems.",
        work_body,
        light_top=False,
    ),
    encoding="utf-8",
)


# =========================================================
# 3. ABOUT PAGE (MULTIDISCIPLINARY EDITORIAL BIO)
# =========================================================
about_body = f"""
<section class="band-obsidian page-header">
  <div class="container">
    <div class="eyebrow">About Henry Okechi</div>
    <h1>Curiosity is the thread <em>connecting everything.</em></h1>
    <p>Medicine, artificial intelligence, product engineering, interactive entertainment, research, and Web3—approached as one disciplined craft.</p>
  </div>
</section>

<section class="band-ivory section">
  <div class="container about-grid">
    <aside class="about-sidebar">
      <div class="about-portrait">
        <img src="assets/images/henry-headshot.jpg" alt="Portrait of Dr. Henry Okechi">
      </div>
      <dl class="about-facts">
        <div><dt>Name</dt><dd>Dr. Henry Okechi</dd></div>
        <div><dt>Credential</dt><dd>MBBS · Licensed MD</dd></div>
        <div><dt>Location</dt><dd>Nigeria (Remote · UTC+1)</dd></div>
        <div><dt>Languages</dt><dd>EN · RU (B1) · FR (A2)</dd></div>
        <div><dt>Direct</dt><dd><a href="mailto:enryvanie@gmail.com">enryvanie@gmail.com</a></dd></div>
        <div><dt>Telegram</dt><dd><a href="https://t.me/enryvanie" target="_blank" rel="noopener noreferrer">@enryvanie ↗</a></dd></div>
      </dl>
      <div style="display:grid;gap:12px">
        <a class="btn-primary" href="assets/Henry_Okechi_CV.pdf" download>Download Full CV (PDF) ↓</a>
        <a class="btn-link" href="contact.html">Start a Conversation <span class="arrow">→</span></a>
      </div>
    </aside>

    <div class="intro-prose">
      <div class="eyebrow">Perspective</div>
      <h2 class="section-title" style="margin-bottom:28px">Medicine. Technology. <em>Human imagination.</em></h2>
      <p>I graduated with a Bachelor of Medicine, Bachelor of Surgery (MBBS) from Ebonyi State University College of Health Sciences and am a licensed medical doctor. Long before completing clinical training, I worked across AI data evaluation at Appen, six years of economics and finance scriptwriting for Savvy Economist, and high-traffic Web3 communities including DeGods and Pudgy Penguins.</p>
      <p>Those parallel tracks shaped how I build today. Clinical training instilled precision, verification discipline, and calm judgment under ambiguity. Software prototyping, Runpod GPU model training, and generative cinema on Kling AI turned analytical rigor into tangible work people can play, inspect, and rely on.</p>
      <p>Whether evaluating clinical AI models, managing international Web3 partner accounts, or shipping a web product from scratch, the standard stays the same: clarity over noise, and real artifacts over slides.</p>

      <div class="eyebrow" style="margin-top:64px">Education &amp; Certifications</div>
      <div class="timeline" style="margin-top:20px">
        <div class="timeline-row">
          <span class="timeline-date">MBBS</span>
          <div class="timeline-role">
            <h3>Bachelor of Medicine, Bachelor of Surgery</h3>
            <span>Ebonyi State University College of Health Sciences</span>
          </div>
          <p class="timeline-desc">Licensed Medical Doctor.</p>
        </div>
        <div class="timeline-row">
          <span class="timeline-date">2020</span>
          <div class="timeline-role">
            <h3>AI, IT Support &amp; Security</h3>
            <span>IBM &amp; Google</span>
          </div>
          <p class="timeline-desc">Getting Started with AI using IBM Watson · Google IT Support Specialization · IT Security: Defense against the digital dark arts.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="band-obsidian section-compact">
  <div class="container">
    <div class="section-header">
      <div>
        <div class="eyebrow">Capabilities</div>
        <h2 class="section-title">Where I create <em>leverage.</em></h2>
      </div>
    </div>
    {render_capabilities_tiered()}
  </div>
</section>

<section class="band-soft section-compact" id="full-timeline">
  <div class="container">
    <div class="section-header">
      <div>
        <div class="eyebrow">Timeline</div>
        <h2 class="section-title">Complete experience <em>archive.</em></h2>
      </div>
    </div>
    <div class="timeline">
      {''.join(f'''
      <div class="timeline-row">
        <span class="timeline-date">{e(dates)}</span>
        <div class="timeline-role">
          <h3>{e(role)}</h3>
          <span>{e(org)}</span>
        </div>
        <p class="timeline-desc">{e(full_desc)}</p>
      </div>
      ''' for dates, role, org, _short, full_desc in EXPERIENCE)}
    </div>
  </div>
</section>
"""

(ROOT / "about.html").write_text(
    page_shell(
        "about",
        "About",
        "Biography, clinical credentials, AI training, product building, and Web3 experience of Dr. Henry Okechi (MBBS).",
        about_body,
        light_top=False,
    ),
    encoding="utf-8",
)


# =========================================================
# 4. CONTACT PAGE
# =========================================================
contact_body = f"""
<section class="band-obsidian page-header">
  <div class="container">
    <div class="eyebrow">Contact</div>
    <h1>Have something ambitious <em>in mind?</em></h1>
    <p>I'm open to thoughtful collaborations, remote roles, and meaningful challenges across AI, healthcare, Web3 partnerships, and creative technology.</p>
  </div>
</section>

<section class="band-ivory section">
  <div class="container contact-layout">
    <div>
      <div class="eyebrow">Direct Channels</div>
      <h2 class="section-title" style="font-size:clamp(34px,4vw,52px)">Reach me <em>directly.</em></h2>
      <p style="margin:18px 0 0;color:var(--ink-soft)">Email or Telegram are the fastest routes. You can also prepare a structured message with the form and either open it in your mail client or copy it to your clipboard.</p>

      <div class="channel-list">
        <a class="channel-item" href="mailto:enryvanie@gmail.com">
          <div><small>Email</small><strong>enryvanie@gmail.com</strong></div>
          <span class="mono-meta">Email ↗</span>
        </a>
        <a class="channel-item" href="#" data-copy-email>
          <div><small>Clipboard</small><strong>Copy email address</strong></div>
          <span class="mono-meta">Copy</span>
        </a>
        <a class="channel-item" href="https://t.me/enryvanie" target="_blank" rel="noopener noreferrer">
          <div><small>Telegram</small><strong>@enryvanie · t.me/enryvanie</strong></div>
          <span class="mono-meta">Message ↗</span>
        </a>
        <a class="channel-item" href="https://www.linkedin.com/in/henry-okechi-b20283422" target="_blank" rel="noopener noreferrer">
          <div><small>LinkedIn</small><strong>henry-okechi-b20283422</strong></div>
          <span class="mono-meta">Connect ↗</span>
        </a>
        <a class="channel-item" href="https://x.com/Vanieofweb3" target="_blank" rel="noopener noreferrer">
          <div><small>X (Twitter)</small><strong>@Vanieofweb3</strong></div>
          <span class="mono-meta">Profile ↗</span>
        </a>
        <a class="channel-item" href="https://github.com/hermes-nietzesch" target="_blank" rel="noopener noreferrer">
          <div><small>GitHub</small><strong>hermes-nietzesch</strong></div>
          <span class="mono-meta">Code ↗</span>
        </a>
      </div>
    </div>

    <form class="editorial-form" data-contact-form>
      <div class="eyebrow" style="margin-bottom:24px">Compose Inquiry</div>
      <div class="form-grid">
        <div class="field">
          <label for="c-name">Your Name</label>
          <input id="c-name" name="name" autocomplete="name" required placeholder="Your name">
        </div>
        <div class="field">
          <label for="c-org">Organization</label>
          <input id="c-org" name="org" autocomplete="organization" placeholder="Company or studio (optional)">
        </div>
      </div>
      <div class="field">
        <label for="c-subject">Subject</label>
        <input id="c-subject" name="subject" required placeholder="AI role, Web3 partnership, or product build">
      </div>
      <div class="field">
        <label for="c-message">Message</label>
        <textarea id="c-message" name="message" required placeholder="Share a brief overview of what you're working on..."></textarea>
      </div>
      <div class="form-actions">
        <button type="submit" class="btn-primary">Open Email Draft ↗</button>
        <button type="button" class="btn-link" data-copy-brief>Copy Formatted Brief <span class="arrow">→</span></button>
      </div>
      <p class="form-status" aria-live="polite" data-form-status></p>
    </form>
  </div>
</section>
"""

(ROOT / "contact.html").write_text(
    page_shell(
        "contact",
        "Contact",
        "Contact Dr. Henry Okechi for collaborations and remote roles across AI, healthcare, product engineering, and Web3.",
        contact_body,
        light_top=False,
        include_closing_cta=False,
    ),
    encoding="utf-8",
)


# =========================================================
# 5. CASE STUDIES (SECTION 7 EDITORIAL STRUCTURE)
# =========================================================
(ROOT / "projects").mkdir(exist_ok=True)
for idx, p in enumerate(PROJECTS):
    prev_p = PROJECTS[(idx - 1) % len(PROJECTS)]
    next_p = PROJECTS[(idx + 1) % len(PROJECTS)]

    # Hero media block: interactive video player if available, else crisp framed visual
    if p.get("video_reel"):
        first_vid = p["video_reel"][0]
        tabs_block = ""
        if len(p["video_reel"]) > 1:
            tabs_html = "".join(
                f'''<button type="button" class="reel-tab{" is-active" if i == 0 else ""}" role="tab" aria-selected="{str(i == 0).lower()}"
                  data-reel-tab
                  data-src="../{e(v['src'])}"
                  data-poster="../{e(v['poster'])}"
                  data-title="{e(v['title'])}"
                  data-meta="{e(v['meta'])}">
                  <small>Clip 0{i+1}</small>
                  <strong>{e(v['title'].split('—', 1)[-1].strip())}</strong>
                </button>'''
                for i, v in enumerate(p["video_reel"])
            )
            tabs_block = f'<div class="reel-tabs" role="tablist" aria-label="Select clip">{tabs_html}</div>'
        media_block = f"""
    <div class="video-reel" id="media-player" data-video-reel>
      <div class="reel-bar">
        <strong data-reel-title>{e(first_vid['title'])}</strong>
        <span data-reel-meta>{e(first_vid['meta'])}</span>
      </div>
      <div class="reel-stage">
        <video data-reel-video controls playsinline preload="metadata" poster="../{e(first_vid['poster'])}" src="../{e(first_vid['src'])}"></video>
      </div>
      {tabs_block}
    </div>
"""
    else:
        cls = "case-hero-media"
        if p.get("image_style") == "framed-ui":
            cls += " is-ui"
        elif p.get("image_style") == "framed-portrait":
            cls += " is-portrait"
        media_block = f"""
    <div class="{cls}" id="media-player">
      <img src="../{e(p['image'])}" alt="{e(p['name'])} — {e(p['short'])}">
      <div class="case-caption">{e(p['media_label'])} — {e(p['image_caption'])}</div>
    </div>
"""

    gallery_html = ""
    if p.get("gallery"):
        g_cls = "case-gallery is-ui-contain" if p.get("gallery_style") == "ui-contain" else "case-gallery"
        g_cards = "".join(
            f'''<figure>
              <img src="../{e(g['src'])}" alt="{e(g['caption'])}" loading="lazy">
              <figcaption>{e(g['caption'])}</figcaption>
            </figure>'''
            for g in p["gallery"]
        )
        gallery_html = f"""
        <h2>{e(p.get('gallery_title', 'Visual Documentation'))}</h2>
        <p>{e(p.get('gallery_subtitle', ''))}</p>
        <div class="{g_cls}">{g_cards}</div>
"""

    aside_btns = "".join(
        f'<a class="{"btn-primary" if lnk.get("primary") else "btn-link"}" href="{e(lnk["url"])}" target="_blank" rel="noopener noreferrer">{e(lnk["label"])} ↗</a>'
        for lnk in p.get("links", [])
    )
    if p.get("video_reel"):
        vid_lbl = "Watch Trailer Reel" if len(p["video_reel"]) > 1 else "Watch Product Demo"
        aside_btns = f'<a class="btn-primary" href="#media-player">{vid_lbl}</a>' + aside_btns
    if not aside_btns:
        aside_btns = '<a class="btn-primary" href="../contact.html">Inquire About This Project →</a>'
    else:
        aside_btns += '<a class="btn-link" href="../contact.html">Discuss a Similar Build <span class="arrow">→</span></a>'

    case_body = f"""
<section class="band-obsidian page-header" style="padding-bottom:44px">
  <div class="container">
    <a class="btn-link" href="../work.html" style="margin-bottom:28px;color:var(--champagne)">← Back to Selected Work</a>
    <div class="eyebrow" style="display:flex">{e(p['index'])} — {e(p['category_label'])}</div>
    <h1>{e(p['name'])}<em>.</em></h1>
    <p>{e(p['tagline'])}</p>
  </div>
</section>

<section class="band-obsidian" style="padding-bottom:clamp(52px,6vw,84px)">
  <div class="container">
    {media_block}
  </div>
</section>

<section class="band-ivory section">
  <div class="container">
    <div class="case-layout">
      <div class="case-prose">
        <h2>Overview</h2>
        <p>{e(p['overview'])}</p>

        <h2>The Problem</h2>
        <p>{e(p['problem'])}</p>

        <h2>Product Concept</h2>
        <p>{e(p['concept'])}</p>

        <h2>Approach &amp; Implementation</h2>
        <p>{e(p['approach'])}</p>

        <h2>Key Features</h2>
        <ul class="editorial-list">
          {''.join(f'<li>{e(f)}</li>' for f in p['features'])}
        </ul>

        <h2>Challenges &amp; Decisions</h2>
        <p>{e(p['decisions'])}</p>

        <h2>Outcome &amp; Current Status</h2>
        <p>{e(p['outcome'])}</p>

        {gallery_html}
      </div>

      <aside class="case-aside" aria-label="Project metadata">
        <dl>
          <dt>Status</dt>
          <dd>{e(p['stage'])}</dd>
          <dt>Category</dt>
          <dd>{e(p['category_label'])}</dd>
          <dt>My Role</dt>
          <dd>{e(p['role'])}</dd>
          <dt>Year</dt>
          <dd>{e(p['year'])}</dd>
          <dt>Technology Stack</dt>
          <dd>{e(' · '.join(p['stack']))}</dd>
        </dl>
        <div class="case-aside-actions">
          {aside_btns}
        </div>
      </aside>
    </div>

    <div class="case-nav">
      <a class="btn-link" href="{e(prev_p['slug'])}.html">← {e(prev_p['index'])} {e(prev_p['name'])}</a>
      <a class="btn-link" href="{e(next_p['slug'])}.html">{e(next_p['index'])} {e(next_p['name'])} →</a>
    </div>
  </div>
</section>
"""

    (ROOT / "projects" / f"{p['slug']}.html").write_text(
        page_shell(
            "work",
            f"{p['name']} — Case Study",
            p["tagline"],
            case_body,
            prefix="../",
            light_top=False,
        ),
        encoding="utf-8",
    )


# =========================================================
# 6. REFINED OBSIDIAN & CHAMPAGNE FAVICON + README
# =========================================================
(ROOT / "assets" / "favicon.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<rect width="64" height="64" rx="4" fill="#10131A"/>'
    '<rect x="5" y="5" width="54" height="54" rx="2" fill="none" stroke="#C5A879" stroke-width="2"/>'
    '<text x="32" y="42" text-anchor="middle" font-family="Georgia,serif" font-size="27" fill="#F4F1EA" letter-spacing="1">HO</text>'
    '</svg>',
    encoding="utf-8",
)

(ROOT / "README.md").write_text(
    """# Henry Okechi — Portfolio (Obsidian & Ivory Editorial Redesign)

An editorial, minimalist personal portfolio built around the **Obsidian & Ivory** design system (`Instrument Serif` + `Manrope` + `IBM Plex Mono`).

## Preview Locally
```bash
python -m http.server 4173
```
Then visit `http://localhost:4173`.

## Regenerating Static Pages
`projects.json` is the single source of truth for all 12 project entries and case studies. After editing `projects.json` or `build.py`, run:
```bash
python build.py
```
""",
    encoding="utf-8",
)

print(f"Built Obsidian & Ivory editorial redesign: index, work, about, contact + {len(PROJECTS)} case studies.")
