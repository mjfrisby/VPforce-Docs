/**
 * vpforce-navbar.js — Interaction layer for the VPforce navbar.
 *
 * The navbar HTML lives in partials/vpforce-navbar.html (Jinja include).
 * It uses Material's .md-header class infrastructure for positioning.
 * This script handles mobile toggle, CSS-var sync, active link marking,
 * and patching the Material header-title into the navbar.
 */

(function () {
    var navbar = document.querySelector('.md-header.vpforce-navbar');
    if (!navbar) return;

    // ── Mobile toggle ────────────────────────────────────────────────────────
    var toggle = navbar.querySelector('.vpforce-navbar__toggle');
    var links  = navbar.querySelector('.vpforce-navbar__links');

    function close() {
        navbar.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Open navigation menu');
        document.body.style.overflow = '';
    }

    toggle.addEventListener('click', function () {
        var isOpen = navbar.classList.toggle('is-open');
        toggle.setAttribute('aria-expanded', isOpen);
        toggle.setAttribute('aria-label',
            isOpen ? 'Close navigation menu' : 'Open navigation menu');
        document.body.style.overflow = isOpen ? 'hidden' : '';
    });

    links.addEventListener('click', function (e) {
        if (e.target.closest('a')) close();
    });

    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && navbar.classList.contains('is-open')) {
            close();
            toggle.focus();
        }
    });

    // ── CSS-var sync — keeps Material header offset and sidebar calcs current ─
    function sync() {
        var h = navbar.offsetHeight + 'px';
        document.documentElement.style.setProperty('--vpf-navbar-height', h);
    }
    sync();
    new ResizeObserver(sync).observe(navbar);

    // ── Active link marker ───────────────────────────────────────────────────
    var currentHost = location.hostname;
    var currentPath = location.pathname.replace(/\/$/, '') || '/';
    navbar.querySelectorAll('.vpforce-navbar__links a:not(.vpforce-navbar__cta)')
        .forEach(function (a) {
            try {
                var url = new URL(a.href);
                var linkPath = url.pathname.replace(/\/$/, '') || '/';
                if (url.hostname === currentHost && linkPath === currentPath) {
                    a.setAttribute('aria-current', 'page');
                }
            } catch (_) { /* ignore */ }
        });

    // ── Patch Material header-title into navbar ──────────────────────────────
    var titleEl = document.querySelector('.md-header:not(.vpforce-navbar) .md-header__title');
    var slot    = navbar.querySelector('.vpforce-navbar__title');
    if (titleEl && slot) {
        slot.appendChild(titleEl);
    }
})();
