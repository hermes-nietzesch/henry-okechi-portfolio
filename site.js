(function () {
  'use strict';

  const EMAIL = 'enryvanie@gmail.com';
  const rootPrefix = document.body.dataset.root || '';

  // Toast helper
  let toastTimer = null;
  function showToast(msg) {
    let el = document.querySelector('[data-toast]');
    if (!el) {
      el = document.createElement('div');
      el.className = 'toast';
      el.setAttribute('role', 'status');
      el.setAttribute('aria-live', 'polite');
      el.setAttribute('data-toast', '');
      document.body.appendChild(el);
    }
    el.textContent = msg;
    el.classList.add('is-visible');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => el.classList.remove('is-visible'), 2800);
  }

  async function copyText(text, label) {
    try {
      await navigator.clipboard.writeText(text);
      showToast(label || 'Copied to clipboard');
    } catch {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      ta.remove();
      showToast(label || 'Copied to clipboard');
    }
  }

  // Copy email buttons
  document.querySelectorAll('[data-copy-email]').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      copyText(EMAIL, `Copied ${EMAIL} to clipboard`);
    });
  });

  // Mobile nav toggle
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-menu]');
  if (toggle && menu) {
    toggle.addEventListener('click', () => {
      const open = menu.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    menu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        menu.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // Hero Interactive Proof Console
  const consoleEl = document.querySelector('[data-proof-console]');
  if (consoleEl) {
    const tabs = [...consoleEl.querySelectorAll('[data-console-tab]')];
    const img = consoleEl.querySelector('[data-console-img]');
    const stage = consoleEl.querySelector('[data-console-stage]');
    const urlEl = consoleEl.querySelector('[data-console-url]');
    const statusEl = consoleEl.querySelector('[data-console-status]');
    const titleEl = consoleEl.querySelector('[data-console-title]');
    const subEl = consoleEl.querySelector('[data-console-sub]');
    const ctaEl = consoleEl.querySelector('[data-console-cta]');

    let idx = 0;
    let paused = false;

    function activateTab(tab) {
      tabs.forEach((t) => {
        const active = t === tab;
        t.classList.toggle('is-active', active);
        t.setAttribute('aria-selected', String(active));
      });
      if (img) {
        img.src = tab.dataset.img;
        img.alt = tab.dataset.title;
      }
      if (stage) {
        stage.classList.toggle('is-portrait', tab.dataset.portrait === 'true');
      }
      if (urlEl) urlEl.textContent = tab.dataset.urlLabel;
      if (statusEl) {
        const isLive = tab.dataset.live === 'true';
        statusEl.innerHTML = isLive
          ? '<span class="pulse-dot"></span>LIVE'
          : 'AI FILM';
        statusEl.style.color = isLive ? 'var(--emerald)' : 'var(--gold-bright)';
      }
      if (titleEl) titleEl.textContent = tab.dataset.title;
      if (subEl) subEl.textContent = tab.dataset.sub;
      if (ctaEl) {
        ctaEl.href = tab.dataset.href;
        ctaEl.textContent = tab.dataset.cta;
        if (tab.dataset.external === 'true') {
          ctaEl.target = '_blank';
          ctaEl.rel = 'noopener noreferrer';
        } else {
          ctaEl.removeAttribute('target');
          ctaEl.removeAttribute('rel');
        }
      }
      idx = tabs.indexOf(tab);
    }

    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        paused = true;
        activateTab(tab);
      });
    });

    consoleEl.addEventListener('mouseenter', () => { paused = true; });
    consoleEl.addEventListener('mouseleave', () => { paused = false; });

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!reduceMotion && tabs.length > 1) {
      setInterval(() => {
        if (!paused) {
          idx = (idx + 1) % tabs.length;
          activateTab(tabs[idx]);
        }
      }, 5200);
    }
  }

  // Interactive Hiring Lens Tabs
  const lensTabs = [...document.querySelectorAll('[data-lens-tab]')];
  const lensPanels = [...document.querySelectorAll('[data-lens-panel]')];
  if (lensTabs.length && lensPanels.length) {
    lensTabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        const target = tab.dataset.lensTab;
        lensTabs.forEach((t) => {
          const active = t === tab;
          t.classList.toggle('is-active', active);
          t.setAttribute('aria-selected', String(active));
        });
        lensPanels.forEach((p) => {
          p.classList.toggle('is-active', p.dataset.lensPanel === target);
        });
      });
    });
  }

  // Pre-select brief chip when clicking track CTAs
  document.querySelectorAll('[data-prefill-topic]').forEach((el) => {
    el.addEventListener('click', () => {
      const topic = el.dataset.prefillTopic;
      const chip = document.querySelector(`[data-topic-chip="${topic}"]`);
      if (chip) chip.click();
    });
  });

  // Work page filters (with optional ?filter= query)
  const filterBtns = [...document.querySelectorAll('[data-filter]')];
  const projectCards = [...document.querySelectorAll('[data-project-category]')];
  if (filterBtns.length && projectCards.length) {
    function applyFilter(code) {
      filterBtns.forEach((b) => {
        const active = b.dataset.filter === code;
        b.classList.toggle('is-active', active);
        b.setAttribute('aria-pressed', String(active));
      });
      let visible = 0;
      projectCards.forEach((card) => {
        const show =
          code === 'all' ||
          (code === 'live' && card.dataset.projectLive === 'true') ||
          card.dataset.projectCategory === code;
        card.hidden = !show;
        if (show) visible += 1;
      });
      const countEl = document.querySelector('[data-result-count]');
      if (countEl) {
        countEl.textContent = `${visible} ${visible === 1 ? 'project' : 'projects'} shown`;
      }
    }

    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => applyFilter(btn.dataset.filter));
    });

    const params = new URLSearchParams(window.location.search);
    const initial = params.get('filter');
    if (initial && filterBtns.some((b) => b.dataset.filter === initial)) {
      applyFilter(initial);
    }
  }

  // Interactive Hire / Brief Composer (Homepage & Contact page)
  document.querySelectorAll('[data-brief-form]').forEach((form) => {
    const topicChips = [...form.querySelectorAll('[data-topic-chip]')];
    const timelineChips = [...form.querySelectorAll('[data-timeline-chip]')];
    let selectedTopic = topicChips.find((c) => c.classList.contains('is-selected'))?.dataset.topicChip || 'AI Training & Clinical Evaluation';
    let selectedTimeline = timelineChips.find((c) => c.classList.contains('is-selected'))?.dataset.timelineChip || 'Immediate';

    topicChips.forEach((chip) => {
      chip.addEventListener('click', () => {
        topicChips.forEach((c) => c.classList.remove('is-selected'));
        chip.classList.add('is-selected');
        selectedTopic = chip.dataset.topicChip;
      });
    });

    timelineChips.forEach((chip) => {
      chip.addEventListener('click', () => {
        timelineChips.forEach((c) => c.classList.remove('is-selected'));
        chip.classList.add('is-selected');
        selectedTimeline = chip.dataset.timelineChip;
      });
    });

    function buildPayload() {
      const fd = new FormData(form);
      const name = String(fd.get('name') || '').trim();
      const org = String(fd.get('org') || '').trim();
      const notes = String(fd.get('notes') || '').trim();
      const subject = `[${selectedTopic}] ${org ? org + ' — ' : ''}Inquiry from ${name || 'Hiring / Project Lead'}`;
      const body = [
        `Hi Henry,`,
        ``,
        `Inquiry Type: ${selectedTopic}`,
        `Timeline: ${selectedTimeline}`,
        name ? `From: ${name}${org ? ' (' + org + ')' : ''}` : null,
        ``,
        notes || 'Would love to connect about working together.',
        ``,
        `— Sent via henryokechi portfolio`
      ].filter((line) => line !== null).join('\n');
      return { name, notes, subject, body };
    }

    const statusEl = form.querySelector('[data-form-status]');

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const { name, notes, subject, body } = buildPayload();
      if (!name || !notes) {
        if (statusEl) {
          statusEl.style.color = 'var(--gold-bright)';
          statusEl.textContent = 'Add your name and a quick note about the role or project first.';
        }
        return;
      }
      window.location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      if (statusEl) {
        statusEl.style.color = 'var(--emerald)';
        statusEl.textContent = 'Opening your email app with the brief ready—or click "Copy Brief" for Gmail/browser email.';
      }
    });

    const copyBtn = form.querySelector('[data-copy-brief]');
    if (copyBtn) {
      copyBtn.addEventListener('click', () => {
        const { subject, body } = buildPayload();
        copyText(`To: ${EMAIL}\nSubject: ${subject}\n\n${body}`, 'Full inquiry brief & email copied!');
        if (statusEl) {
          statusEl.style.color = 'var(--emerald)';
          statusEl.textContent = `Copied brief + ${EMAIL} to clipboard—paste straight into Gmail or LinkedIn.`;
        }
      });
    }
  });

  // Command Palette (⌘K / Ctrl+K)
  const cmdItems = [
    { label: 'Home — Overview & Hiring Tracks', meta: 'Page', action: () => (window.location.href = `${rootPrefix}index.html`) },
    { label: 'All 10 Case Studies & Live Builds', meta: 'Page', action: () => (window.location.href = `${rootPrefix}work.html`) },
    { label: 'About, Clinical Credentials & Experience', meta: 'Page', action: () => (window.location.href = `${rootPrefix}about.html`) },
    { label: 'Hire Henry / Scope a Role or Sprint', meta: 'Contact', action: () => (window.location.href = `${rootPrefix}contact.html`) },
    { label: 'Copy Email (enryvanie@gmail.com)', meta: 'Action', action: () => copyText(EMAIL, `Copied ${EMAIL}`) },
    { label: 'Message on Telegram (@enryvanie)', meta: 'Telegram ↗', action: () => window.open('https://t.me/enryvanie', '_blank', 'noopener') },
    { label: 'Download CV (PDF)', meta: 'PDF', action: () => (window.location.href = `${rootPrefix}assets/Henry_Okechi_CV.pdf`) },
    { label: 'Play Kasala — 3D Battle Royale', meta: 'Live ↗', action: () => window.open('https://kasala.kasala.workers.dev', '_blank', 'noopener') },
    { label: 'Launch MedFlash — Board Review App', meta: 'Live ↗', action: () => window.open('https://mcqrecall.netlify.app', '_blank', 'noopener') },
    { label: 'Open Project Mucci — Mentorship Platform', meta: 'Live ↗', action: () => window.open('https://project-mucci.web.app', '_blank', 'noopener') },
    { label: 'Play Wayo — 3D Prop Hunt', meta: 'Live ↗', action: () => window.open('https://playwayo.netlify.app', '_blank', 'noopener') },
    { label: 'Play Naija Undead — 3D Zombie Survival', meta: 'Live ↗', action: () => window.open('https://naijaundead.fun', '_blank', 'noopener') },
    { label: 'Case Study: Azarun (Generative Cinema + Runpod)', meta: 'Case', action: () => (window.location.href = `${rootPrefix}projects/azarun.html`) },
    { label: 'Case Study: MedForge AI (Clinical Workspace)', meta: 'Case', action: () => (window.location.href = `${rootPrefix}projects/medforge.html`) },
    { label: 'Case Study: Hodos (Anthropic API Career App)', meta: 'Case', action: () => (window.location.href = `${rootPrefix}projects/hodos.html`) },
    { label: 'Case Study: VitalPulse (Blood Donation UX)', meta: 'Case', action: () => (window.location.href = `${rootPrefix}projects/vitalpulse.html`) },
    { label: 'Web3 Growth, Community & Ecosystem Section', meta: 'Web3', action: () => (window.location.href = `${rootPrefix}index.html#web3-growth`) },
    { label: 'Case Study: HERMES ALPHA ZONE (50+ Campaigns · 75K+)', meta: 'Web3', action: () => (window.location.href = `${rootPrefix}projects/hermes-growth.html`) },
    { label: 'Case Study: Tier-1 Web3 Ops (DeGods · Pudgy Penguins)', meta: 'Web3', action: () => (window.location.href = `${rootPrefix}projects/web3-community-ops.html`) },
    { label: 'Case Study: Irysnameservice (#1 Irys dApp)', meta: 'Web3', action: () => (window.location.href = `${rootPrefix}projects/irysnameservice.html`) }
  ];

  const backdrop = document.querySelector('[data-cmd-backdrop]');
  const cmdInput = document.querySelector('[data-cmd-input]');
  const cmdList = document.querySelector('[data-cmd-list]');

  if (backdrop && cmdInput && cmdList) {
    function renderCmd(query) {
      const q = (query || '').toLowerCase().trim();
      const filtered = cmdItems.filter((item) =>
        item.label.toLowerCase().includes(q) || item.meta.toLowerCase().includes(q)
      );
      cmdList.innerHTML = '';
      filtered.forEach((item) => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'cmd-item';
        btn.innerHTML = `<span>${item.label}</span><small>${item.meta}</small>`;
        btn.addEventListener('click', () => {
          closeCmd();
          item.action();
        });
        cmdList.appendChild(btn);
      });
      if (!filtered.length) {
        const empty = document.createElement('div');
        empty.className = 'cmd-item';
        empty.textContent = 'No matching actions or projects.';
        cmdList.appendChild(empty);
      }
    }

    function openCmd() {
      backdrop.classList.add('is-open');
      cmdInput.value = '';
      renderCmd('');
      setTimeout(() => cmdInput.focus(), 20);
    }

    function closeCmd() {
      backdrop.classList.remove('is-open');
    }

    document.querySelectorAll('[data-cmd-open]').forEach((btn) => {
      btn.addEventListener('click', openCmd);
    });

    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) closeCmd();
    });

    cmdInput.addEventListener('input', () => renderCmd(cmdInput.value));

    document.addEventListener('keydown', (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (backdrop.classList.contains('is-open')) closeCmd();
        else openCmd();
      } else if (e.key === 'Escape' && backdrop.classList.contains('is-open')) {
        closeCmd();
      }
    });
  }

  // Scroll reveal
  const reveals = [...document.querySelectorAll('.reveal')];
  if (reveals.length && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-in');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: '0px 0px -30px 0px' }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add('is-in'));
  }

  // Interactive Video Reel Player (Azarun)
  document.querySelectorAll('[data-video-reel]').forEach((reel) => {
    const video = reel.querySelector('[data-reel-video]');
    const titleEl = reel.querySelector('[data-reel-title]');
    const metaEl = reel.querySelector('[data-reel-meta]');
    const tabs = [...reel.querySelectorAll('[data-reel-tab]')];

    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        tabs.forEach((t) => {
          const active = t === tab;
          t.classList.toggle('is-active', active);
          t.setAttribute('aria-selected', String(active));
        });
        if (video) {
          video.pause();
          video.poster = tab.dataset.poster || '';
          video.src = tab.dataset.src || '';
          video.load();
          video.play().catch(() => {});
        }
        if (titleEl) titleEl.textContent = tab.dataset.title || '';
        if (metaEl) metaEl.textContent = tab.dataset.meta || '';
      });
    });
  });

  // Dynamic year
  document.querySelectorAll('[data-year]').forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });
})();
