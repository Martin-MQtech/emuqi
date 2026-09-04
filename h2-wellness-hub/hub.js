/**
 * H2 Wellness Hub - Client-Side Interaction Runtime
 * Clean editorial filtering and navigation interactions.
 */

(function () {
  'use strict';

  /**
   * Filter cards in Industry Pulse or Project Cases sections
   * @param {string} group - 'pulse' or 'cases'
   * @param {string} filter - tag value to match or 'all'
   * @param {HTMLElement} btn - The clicked button element
   */
  function filterGroup(group, filter, btn) {
    const container = document.querySelector(group === 'pulse' ? '.hub-pulse-grid' : '.hub-cases-grid');
    if (!container) return;

    const cards = container.querySelectorAll(group === 'pulse' ? '.hub-pulse-card' : '.hub-case-card-v2');
    if (btn && btn.parentElement) {
      const pills = btn.parentElement.querySelectorAll('.hub-filter-pill');
      pills.forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
    }

    cards.forEach(card => {
      const tag = card.getAttribute(group === 'pulse' ? 'data-pulse-tag' : 'data-case-tag') || '';
      if (filter === 'all' || tag.includes(filter)) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  }

  // Export to global scope for onclick handlers
  window.filterGroup = filterGroup;

  // Initialize smooth scroll for anchor links
  document.addEventListener('DOMContentLoaded', () => {
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
      link.addEventListener('click', e => {
        const targetId = link.getAttribute('href').slice(1);
        if (!targetId) return;
        const targetEl = document.getElementById(targetId);
        if (targetEl) {
          e.preventDefault();
          targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
          history.pushState(null, null, '#' + targetId);
        }
      });
    });
  });
})();
