(function () {
  const saved = sessionStorage.getItem('theme');
  if (saved) {
    document.documentElement.dataset.theme = saved;
  }
})();
