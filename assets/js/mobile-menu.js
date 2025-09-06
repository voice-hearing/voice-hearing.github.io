// Simple: Auto-close mobile menu when search opens
document.addEventListener('DOMContentLoaded', function() {
  const searchButtons = document.querySelectorAll('[data-search-toggle]');
  const navToggle = document.getElementById('nav-toggle');
  
  searchButtons.forEach(function(searchButton) {
    searchButton.addEventListener('click', function() {
      // Simply close the mobile menu
      if (navToggle && navToggle.checked) {
        navToggle.checked = false;
      }
    });
  });
});
