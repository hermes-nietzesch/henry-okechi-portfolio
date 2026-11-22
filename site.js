(function () {
  'use strict';

  const EMAIL = 'enryvanie@gmail.com';
  const html = document.documentElement;

  // Apply saved theme before paint adjustments
  const savedTheme = localStorage.getItem('ho-theme');
  if (savedTheme === 'dark') {
    html.setAttribute('data-theme', 'dark');
  }

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
    toastTimer = setTimeout(() => el.classList.remove('is-visible'), 2600);
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

  document.querySelectorAll('[data-copy-email]').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      copyText(EMAIL, `Copied ${EMAIL}`);
    });
  });

  // Discreet Theme Toggle (Obsidian & Ivory default <-> All-Dark Editorial)
  const themeBtn = document.querySelector('[data-theme-toggle]');
  function syncThemeLabel() {
    if (!themeBtn) return;
    const isDark = html.getAttribute('data-theme') === 'dark';
    themeBtn.textContent = isDark ? '☀' : '◐';
    themeBtn.setAttribute('aria-label', isDark ? 'Switch to Obsidian & Ivory theme' : 'Switch to Dark reading theme');
    themeBtn.setAttribute('aria-pressed', String(isDark));
  }
  syncThemeLabel();
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const next = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      if (next === 'dark') html.setAttribute('data-theme', 'dark');
      else html.removeAttribute('data-theme');
      localStorage.setItem('ho-theme', next);
      syncThemeLabel();
    });
  }

  // Header scroll transition + 2px top progress bar
  const header = document.querySelector('[data-site-header]');
  const progressBar = document.querySelector('[data-scroll-progress]');
  let ticking = false;

  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      const y = window.scrollY || window.pageYOffset;
      if (header) {
        header.setAttribute('data-scrolled', y > 36 ? 'true' : 'false');
      }
      if (progressBar) {
        const docH = document.documentElement.scrollHeight - window.innerHeight;
        const pct = docH > 0 ? Math.min(100, Math.max(0, (y / docH) * 100)) : 0;
        progressBar.style.width = `${pct}%`;
      }
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Accessible Mobile Menu Drawer
  const menuBtn = document.querySelector('[data-menu-toggle]');
  const drawer = document.querySelector('[data-mobile-drawer]');
  if (menuBtn && drawer) {
    function setDrawer(open) {
      drawer.classList.toggle('is-open', open);
      menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.textContent = open ? 'Close' : 'Menu';
      document.body.style.overflow = open ? 'hidden' : '';
    }
    menuBtn.addEventListener('click', () => {
      setDrawer(!drawer.classList.contains('is-open'));
    });
    drawer.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => setDrawer(false));
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) {
        setDrawer(false);
        menuBtn.focus();
      }
    });
  }

  // Accessible Work Page Filters
  const filterBtns = [...document.querySelectorAll('[data-filter]')];
  const workItems = [...document.querySelectorAll('[data-work-item]')];
  if (filterBtns.length && workItems.length) {
    function applyFilter(code) {
      filterBtns.forEach((b) => {
        const active = b.dataset.filter === code;
        b.classList.toggle('is-active', active);
        b.setAttribute('aria-pressed', String(active));
      });
      let count = 0;
      workItems.forEach((item) => {
        const show =
          code === 'all' ||
          (code === 'live' && item.dataset.live === 'true') ||
          item.dataset.category === code;
        item.hidden = !show;
        if (show) {
          count += 1;
          item.classList.add('is-in');
        }
      });
      const countEl = document.querySelector('[data-result-count]');
      if (countEl) {
        countEl.textContent = `${count} ${count === 1 ? 'project' : 'projects'}`;
      }
    }
    filterBtns.forEach((btn) => {
      btn.addEventListener('click', () => applyFilter(btn.dataset.filter));
    });
    const initial = new URLSearchParams(window.location.search).get('filter');
    if (initial && filterBtns.some((b) => b.dataset.filter === initial)) {
      applyFilter(initial);
    }
  }

  // Interactive HTML5 Video Reel Player
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

  // Contact Brief Composer
  document.querySelectorAll('[data-contact-form]').forEach((form) => {
    const statusEl = form.querySelector('[data-form-status]');

    function buildPayload() {
      const fd = new FormData(form);
      const name = String(fd.get('name') || '').trim();
      const org = String(fd.get('org') || '').trim();
      const subject = String(fd.get('subject') || 'Portfolio Inquiry').trim();
      const message = String(fd.get('message') || '').trim();
      const body = [
        'Hi Henry,',
        '',
        name ? `From: ${name}${org ? ` (${org})` : ''}` : null,
        '',
        message,
      ].filter((l) => l !== null).join('\n');
      return { name, message, subject, body };
    }

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const { name, message, subject, body } = buildPayload();
      if (!name || !message) {
        if (statusEl) statusEl.textContent = 'Please include your name and a short note.';
        return;
      }
      window.location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
      if (statusEl) statusEl.textContent = 'Opening your email app—or use "Copy Brief" to paste directly into webmail.';
    });

    const copyBtn = form.querySelector('[data-copy-brief]');
    if (copyBtn) {
      copyBtn.addEventListener('click', () => {
        const { subject, body } = buildPayload();
        copyText(`To: ${EMAIL}\nSubject: ${subject}\n\n${body}`, 'Brief and email address copied');
        if (statusEl) statusEl.textContent = `Copied brief and ${EMAIL} to clipboard.`;
      });
    }
  });

  // Scroll Reveal Observer (progressive enhancement: never traps elements invisible)
  const reveals = [...document.querySelectorAll('.reveal')];
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduceMotion && reveals.length && 'IntersectionObserver' in window) {
    html.classList.add('js-motion');
    const revealInView = () => {
      const vh = window.innerHeight || 900;
      reveals.forEach((el) => {
        if (el.classList.contains('is-in')) return;
        const rect = el.getBoundingClientRect();
        if (rect.top < vh + 100 && rect.bottom > -40) {
          el.classList.add('is-in');
        }
      });
    };
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-in');
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.01, rootMargin: '120px 0px 120px 0px' }
    );
    reveals.forEach((el) => io.observe(el));
    revealInView();
    window.addEventListener('scroll', revealInView, { passive: true });
  } else {
    reveals.forEach((el) => el.classList.add('is-in'));
  }

  document.querySelectorAll('[data-year]').forEach((el) => {
    el.textContent = String(new Date().getFullYear());
  });
})();
