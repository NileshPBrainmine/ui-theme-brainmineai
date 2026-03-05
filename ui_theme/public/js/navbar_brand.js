frappe.after_ajax(() => {
    const insertCompanyName = () => {
        const appLogo = document.querySelector('.navbar .app-logo');

        if (appLogo && !document.querySelector('.brainmine-link')) {

            // Create span wrapper
            const link = document.createElement('span');
            link.classList.add('brainmine-link');
            link.style.display = 'inline-flex';
            link.style.alignItems = 'center';
            link.style.marginLeft = '10px';
            link.style.textDecoration = 'none';
            link.style.zIndex = '9999';
            link.style.cursor = 'default';

            // ❗ BLOCK ALL MOUSE INTERACTION
            link.style.pointerEvents = 'none';

            const text = document.createElement('span');
            text.textContent = 'Brainmine.AI';
            text.style.color = '#ffffff';
            text.style.fontWeight = '600';
            text.style.fontSize = '18px';
            text.style.letterSpacing = '0.5px';
            text.style.transition = 'opacity 0.3s ease';

            // Hover effect still works visually (optional)
            link.addEventListener('mouseover', () => (text.style.opacity = '0.8'));
            link.addEventListener('mouseout', () => (text.style.opacity = '1'));

            link.appendChild(text);

            const logoAnchor = appLogo.closest("a.navbar-home");
            logoAnchor.insertAdjacentElement("afterend", link);
        }
    };

    const checkNavbar = setInterval(() => {
        if (document.querySelector('.navbar .app-logo')) {
            insertCompanyName();
            clearInterval(checkNavbar);
        }
    }, 500);
});
