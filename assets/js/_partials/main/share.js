(function () {
    const btn = document.getElementById('share-btn');
    btn?.addEventListener('click', event => {
        event.preventDefault();
        const url = btn.href;
        if (navigator.share) {
            navigator.share({
                title: document.title,
                url: url
            }).catch(() => {});
        } else {
            navigator.clipboard.writeText(url).catch(() => {});
        }
    });
})();
