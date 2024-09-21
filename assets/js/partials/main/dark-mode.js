const modeSwitcher = (function () {
    const systemInitiatedDark = window.matchMedia('(prefers-color-scheme: dark)');

    function updateSiteElements(isDark) {
        const themeName = isDark ? 'dark' : 'light';

        // HTML data theme
        document.documentElement.setAttribute('data-theme', themeName);

        // Theme toggle text
        document.getElementById('theme-toggle').title = isDark ? 'Toggle Light Mode' : 'Toggle Dark Mode';

        // Data theme for unrendered tweets
        document.querySelectorAll('.twitter-tweet').forEach(e => {
            e.setAttribute('data-theme', themeName);
        });

        // URL query value swap for rendered tweets
        document.querySelectorAll('[data-tweet-id]').forEach(e => {
            const url = new URL(e.getAttribute('src'));
            url.searchParams.set('theme', themeName);
            e.setAttribute('src', url.toString());
        });
    }

    function modeSwitcher() {
        const theme = sessionStorage.getItem('theme');
        let setDark;
        if (theme === 'dark') {
            setDark = false;
        } else if (theme === 'light') {
            setDark = true;
        } else {
            setDark = !systemInitiatedDark.matches;
        }

        sessionStorage.setItem('theme', setDark ? 'dark' : 'light');
        updateSiteElements(setDark);
        if (typeof DISQUS !== 'undefined') {
            DISQUS.reset({ reload: true });
        }
    }

    const theme = sessionStorage.getItem('theme');
    if (theme === 'dark') {
        updateSiteElements(true);
    } else if (theme === 'light') {
        updateSiteElements(false);
    } else {
        updateSiteElements(systemInitiatedDark.matches);
    }

    systemInitiatedDark.addEventListener('change', systemDark => {
        updateSiteElements(systemDark.matches);
        sessionStorage.removeItem('theme');
        if (typeof DISQUS !== 'undefined') {
            DISQUS.reset({ reload: true });
        }
    });

    return modeSwitcher;
})();
