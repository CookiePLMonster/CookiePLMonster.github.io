const systemInitiatedDark = window.matchMedia("(prefers-color-scheme: dark)");

function _changeIconTitle(isDark) {
    const elem = document.getElementById("theme-toggle");
    if (isDark) {
        elem.title = "Toggle Light Mode";
    } else {
        elem.title = "Toggle Dark Mode";
    }
}

function modeSwitcher() {
    const theme = sessionStorage.getItem('theme');
    let setDark = true;
    if (theme === "dark") {
        setDark = false;
    } else if (theme === "light") {
        setDark = true;
    } else if (systemInitiatedDark.matches) {
        setDark = false;
    }

    if (setDark) {
        document.documentElement.setAttribute('data-theme', 'dark');
        sessionStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        sessionStorage.setItem('theme', 'light');
    }
    _changeIconTitle(setDark);
    if (typeof DISQUS !== 'undefined') {
        DISQUS.reset({ reload: true });
    }
}

(function () {
    const theme = sessionStorage.getItem('theme');
    if (theme === "dark") {
        document.documentElement.setAttribute('data-theme', 'dark');
        _changeIconTitle(true);
    } else if (theme === "light") {
        document.documentElement.setAttribute('data-theme', 'light');
        _changeIconTitle(false);
    } else {
        _changeIconTitle(systemInitiatedDark.matches);
    }

    systemInitiatedDark.addEventListener('change', function (systemDark) {
        _changeIconTitle(systemDark.matches);
        document.documentElement.removeAttribute('data-theme');
        sessionStorage.removeItem('theme');
        if (typeof DISQUS !== 'undefined') {
            DISQUS.reset({ reload: true });
        }
    });
})();
