// Component loader for navbar and footer
document.addEventListener('DOMContentLoaded', function() {
    // Determine the correct path to components based on current location
    const currentPath = window.location.pathname;
    const isInSubdirectory = currentPath.includes('/tissue-culture/') || currentPath.includes('/iron-ore/') || currentPath.includes('/coal-mining/');
    const componentsPath = isInSubdirectory ? '../components/' : 'components/';
    
    // Load navbar
    fetch(componentsPath + 'navbar.html')
        .then(response => response.text())
        .then(data => {
            const navbarContainer = document.getElementById('navbar-container');
            if (navbarContainer) {
                navbarContainer.innerHTML = data;
                
                // Initialize navbar functionality after loading
                initializeNavbar();
            }
        })
        .catch(error => console.error('Error loading navbar:', error));

    // Load footer
    fetch(componentsPath + 'footer.html')
        .then(response => response.text())
        .then(data => {
            const footerContainer = document.getElementById('footer-container');
            if (footerContainer) {
                footerContainer.innerHTML = data;
            }
        })
        .catch(error => console.error('Error loading footer:', error));
});

// Initialize navbar functionality
function initializeNavbar() {
    // Mobile menu toggle
    const mobileMenuButton = document.querySelector('[data-collapse-toggle="navbar-default"]');
    const mobileMenu = document.getElementById('navbar-default');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Navbar scroll effect
    window.addEventListener('scroll', function () {
        const navbar = document.getElementById('navbar');
        if (navbar) {
            const scrollPosition = window.scrollY;
            if (scrollPosition > 100) {
                navbar.classList.remove('bg-gradient-to-b', 'from-black', 'via-black/90', 'to-transparent');
                navbar.style.backgroundColor = '#0a3f0e';
            } else {
                navbar.classList.add('bg-gradient-to-b', 'from-black', 'via-black/90', 'to-transparent');
                navbar.style.backgroundColor = '';
            }
        }
    });
}