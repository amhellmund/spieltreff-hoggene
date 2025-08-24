document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.querySelector('.navbar-toggle');
    const navbarMenu = document.querySelector('.navbar-menu');
    const navLinks = document.querySelectorAll('.navbar-menu a');

    // Ensure the menu is collapsed on page load
    navbarMenu.classList.remove('active');

    // Toggle menu on hamburger button click
    toggleButton.addEventListener('click', () => {
        navbarMenu.classList.toggle('active');
    });

    // Collapse menu when clicking any navigation link
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 768) { // Only collapse on mobile
                navbarMenu.classList.remove('active');
            }
        });
    });

    // Update menu visibility on window resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 768) {
            navbarMenu.classList.remove('active');
        }
    });
});
