(function () {
    const systemInitiatedDark = window.matchMedia('(prefers-color-scheme: dark)');

    function darkModePreferred() {
        const theme = sessionStorage.getItem('theme');
        return theme ? theme === 'dark' : systemInitiatedDark.matches;
    }

    function updateSiteElements(linkItem, textItem, isDark) {
        const themeName = isDark ? 'dark' : 'light';

        // Theme toggle text
        if (isDark) {
            linkItem.title = 'Switch to Light Mode';
            linkItem.setAttribute('aria-label', 'Switch to Light Mode');
            textItem.innerText = 'Light';
        }
        else {
            linkItem.title = 'Switch to Dark Mode';
            linkItem.setAttribute('aria-label', 'Switch to Dark Mode');
            textItem.innerText = 'Dark';
        }

        // Data theme for unrendered tweets
        document.querySelectorAll('.twitter-tweet').forEach(e => {
            e.dataset.theme = themeName;
        });

        // URL query value swap for rendered tweets
        document.querySelectorAll('[data-tweet-id]').forEach(e => {
            const url = new URL(e.getAttribute('src'));
            url.searchParams.set('theme', themeName);
            e.setAttribute('src', url.toString());
        });

        return themeName;
    }

    // Create the theme switcher list entry
    const themeSwitcher = document.createElement('button');

    const switcherIcon = Object.assign(document.createElement('i'), {
        className: 'theme-icon'
    });

    const switcherText = Object.assign(document.createElement('span'), {
        className: 'navbar-icon-text'
    });
    switcherText.setAttribute('aria-hidden', true);

    themeSwitcher.addEventListener('click', () => {

        const setDark = !darkModePreferred();
        document.documentElement.dataset.theme = updateSiteElements(themeSwitcher, switcherText, setDark);
        sessionStorage.setItem('theme', setDark ? 'dark' : 'light');
        if (typeof DISQUS !== 'undefined') {
            DISQUS.reset({ reload: true });
        };
    });


    themeSwitcher.append(switcherIcon, ' ', switcherText);

    const switcherLi = document.createElement('li');
    switcherLi.appendChild(themeSwitcher);

    document.getElementById('nav-menu')?.appendChild(switcherLi);

    updateSiteElements(themeSwitcher, switcherText, darkModePreferred())

    systemInitiatedDark.addEventListener('change', systemDark => {
        updateSiteElements(themeSwitcher, switcherText, systemDark.matches);
        delete document.documentElement.dataset.theme;
        sessionStorage.removeItem('theme');
        if (typeof DISQUS !== 'undefined') {
            DISQUS.reset({ reload: true });
        }
    });
})();
