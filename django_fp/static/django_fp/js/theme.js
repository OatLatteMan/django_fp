document.addEventListener('DOMContentLoaded', () => {
    const html = document.getElementById('html-root');
    const toggleBtn = document.getElementById('theme-toggle');

    // Check stored preference first
    let theme = localStorage.getItem('theme');

    // If no stored theme, check system preference
    if (!theme) {
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        theme = prefersDark ? 'dark' : 'light';
        localStorage.setItem('theme', theme);  // Save it so it's consistent across pages
    }

    // Apply the theme
    html.setAttribute('data-theme', theme);
    toggleBtn.textContent = theme === 'dark' ? '🌞' : '🌙';

    // Toggle theme on button click
    toggleBtn.addEventListener('click', () => {
        const current = html.getAttribute('data-theme');
        const newTheme = current === 'dark' ? 'light' : 'dark';
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        toggleBtn.textContent = newTheme === 'dark' ? '🌞' : '🌙';
    });
});