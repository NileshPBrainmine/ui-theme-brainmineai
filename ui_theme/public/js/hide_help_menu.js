(function removeHelpMenu() {
    // Try to remove Help dropdown
    const help_menu = document.querySelector('.dropdown-help');

    if (help_menu) {
        help_menu.remove();
        return; // stop if removed
    }

    // If navbar not ready, keep checking every 300ms
    setTimeout(removeHelpMenu, 300);
})();

// Also observe DOM changes (ERPNext re-renders navbar dynamically)
const observer = new MutationObserver(() => {
    const help_menu = document.querySelector('.dropdown-help');
    if (help_menu) help_menu.remove();
});

// Observe entire body for changes
observer.observe(document.body, { childList: true, subtree: true });
