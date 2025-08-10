(function (d, disqus_shortname) {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                const s = d.createElement('script');
                s.src = '//' + disqus_shortname + '.disqus.com/embed.js';
                s.setAttribute('data-timestamp', +new Date());
                (d.head || d.body).appendChild(s);

                observer.unobserve(entry.target);
            }
        });
    });

    // Start listening:
    const mountNode = document.querySelector("#disqus_thread");
    observer.observe(mountNode);
})(document, document.currentScript.getAttribute('data-shortname'));
