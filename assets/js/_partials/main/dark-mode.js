(function () {
    const systemInitiatedDark = window.matchMedia('(prefers-color-scheme: dark)');

    function updateSiteElements(linkItem, textItem, isDark) {
        const themeName = isDark ? 'dark' : 'light';

        // HTML data theme
        document.documentElement.setAttribute('data-theme', themeName);

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
            e.setAttribute('data-theme', themeName);
        });

        // URL query value swap for rendered tweets
        document.querySelectorAll('[data-tweet-id]').forEach(e => {
            const url = new URL(e.getAttribute('src'));
            url.searchParams.set('theme', themeName);
            e.setAttribute('src', url.toString());
        });
    }

    // Create the theme switcher list entry
    const themeSwitcher = Object.assign(document.createElement('button'), {});

    const switcherIcon = Object.assign(document.createElement('i'), {
        className: 'theme-icon'
    });

    const switcherText = Object.assign(document.createElement('span'), {
        className: 'navbar-icon-text'
    });
    switcherText.setAttribute('aria-hidden', true);

    themeSwitcher.addEventListener('click', () => {

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
        updateSiteElements(themeSwitcher, switcherText, setDark);
        if (typeof DISQUS !== 'undefined') {
            DISQUS.reset({ reload: true });
        };
    });


    themeSwitcher.append(switcherIcon, ' ', switcherText);

    const switcherLi = document.createElement('li');
    switcherLi.appendChild(themeSwitcher);

    document.getElementById('nav-menu')?.appendChild(switcherLi);

    const theme = sessionStorage.getItem('theme');
    if (theme === 'dark') {
        updateSiteElements(themeSwitcher, switcherText, true);
    } else if (theme === 'light') {
        updateSiteElements(themeSwitcher, switcherText, false);
    } else {
        updateSiteElements(themeSwitcher, switcherText, systemInitiatedDark.matches);
    }

    systemInitiatedDark.addEventListener('change', systemDark => {
        updateSiteElements(themeSwitcher, switcherText, systemDark.matches);
        sessionStorage.removeItem('theme');
        if (typeof DISQUS !== 'undefined') {
            DISQUS.reset({ reload: true });
        }
    });
})();
