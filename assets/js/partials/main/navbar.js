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
    const main = document.getElementById('main');
    if (main) {
        let imageAspect = 0, imageHeight = 0;
        if (main.style.backgroundSize == 'cover') {
            const imageUrl = main.style.backgroundImage.replace(/url\((['"])?(.*?)\1\)/gi, '$2').split(',')[0];
            var image = new Image();
            image.onload = () => {
                imageHeight = image.naturalHeight;
                imageAspect = image.naturalWidth / image.naturalHeight;
            };
            image.src = imageUrl;
        }
        window.addEventListener('scroll', () => {
            const containerAspect = main.offsetWidth / main.offsetHeight;
            let offset = 0;
            if (containerAspect > imageAspect) {
                offset = -(window.scrollY || document.body.scrollTop);
                if (imageHeight > 0) {
                    const imageMaxOffset = (imageHeight * (imageAspect / containerAspect)) - imageHeight;
                    offset = Math.max(offset, imageMaxOffset);
                }
            }
            main.style.backgroundPosition = 'center ' + (offset / 3) + 'px';
        });
    }
})();
