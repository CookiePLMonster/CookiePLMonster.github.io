(function () {
    /*
     * Display the menu items on smaller screens
     */
    const pull = document.getElementById('pull');
    const menu = document.querySelector('nav ul');

    ['click', 'touch'].forEach(e => {
        pull?.addEventListener(e, () => {
            menu.classList.toggle('hide');
        }, false);
    });

    /*
     * Make the header images move on scroll
     */
    window.addEventListener('scroll', () => {
        const offset = -(window.scrollY || document.body.scrollTop) / 3;
        const main = document.getElementById('main');
        if (main) {
            main.style.backgroundPosition = '100% ' + offset + 'px' + ', 0%, center top';
        }
    });
})();
