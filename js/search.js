(function () {
  'use strict';

  // 可检索区块映射：页面类型 -> 选择器
  const SELECTORS = {
    index: ['.level', '.card', '.fw', '.ladder-row', '.method', '.practice', '.tier', '.rm', '.toolcat', '.pack'],
    methods: ['.method'],
    tools: ['.toolcat', '.pack'],
    practices: ['.practice', '.rank-item', '.prompt-box', '.pack'],
    courses: ['.tier', '.rm']
  };

  function getPageType() {
    const path = location.pathname.split('/').pop() || 'index.html';
    if (path === 'methods.html') return 'methods';
    if (path === 'tools.html') return 'tools';
    if (path === 'practices.html') return 'practices';
    if (path === 'courses.html') return 'courses';
    return 'index';
  }

  function textOf(el) {
    return (el.innerText || el.textContent || '').trim();
  }

  function escapeRegExp(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function highlight(el, keyword) {
    if (!keyword) {
      el.innerHTML = el.getAttribute('data-raw') || el.innerHTML;
      return;
    }
    const raw = el.getAttribute('data-raw') || el.innerHTML;
    el.setAttribute('data-raw', raw);
    const re = new RegExp('(' + escapeRegExp(keyword) + ')', 'gi');
    el.innerHTML = raw.replace(re, '<mark>$1</mark>');
  }

  function filter() {
    const page = getPageType();
    const input = document.getElementById('site-search');
    const keyword = (input && input.value || '').trim();
    const selectors = SELECTORS[page] || SELECTORS.index;
    const nodes = [];
    selectors.forEach(sel => {
      document.querySelectorAll(sel).forEach(n => nodes.push(n));
    });

    const hasMark = keyword.length > 0;
    nodes.forEach(node => {
      const text = textOf(node);
      const match = !hasMark || text.toLowerCase().includes(keyword.toLowerCase());
      node.style.display = match ? '' : 'none';
      if (hasMark && match) {
        highlight(node, keyword);
      } else if (!hasMark) {
        const raw = node.getAttribute('data-raw');
        if (raw) node.innerHTML = raw;
      }
    });

    const empty = document.getElementById('search-empty');
    if (empty) empty.style.display = hasMark ? 'none' : 'none';

    if (input) input.setAttribute('aria-expanded', String(hasMark));
  }

  function init() {
    const input = document.getElementById('site-search');
    if (!input) return;

    input.addEventListener('input', filter);
    input.addEventListener('search', filter);

    const form = input.closest('form');
    if (form) {
      form.addEventListener('submit', e => {
        e.preventDefault();
        filter();
      });
    }

    // 快捷键：Ctrl/Cmd + K 聚焦搜索
    document.addEventListener('keydown', e => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        input.focus();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
