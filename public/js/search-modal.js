// static/js/search-modal.js
document.addEventListener('DOMContentLoaded', function() {
  const searchButtons = document.querySelectorAll('[data-search-toggle]');
  const searchWrapper = document.getElementById('search-wrapper');
  searchButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      if (searchWrapper.classList.contains('hidden')) {
        document.body.classList.add('search-active');
      } else {
        document.body.classList.remove('search-active');
      }
    });
  });
  const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      if (mutation.target.classList.contains('hidden')) {
        document.body.classList.remove('search-active');
      }
    });
  });
  if (searchWrapper) {
    observer.observe(searchWrapper, { attributes: true, attributeFilter: ['class'] });
  }
});
