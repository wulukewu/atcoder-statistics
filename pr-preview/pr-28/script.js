// Prevent flash of unstyled content
(function() {
    const mode = localStorage.getItem('mode') || 
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    const colorTheme = localStorage.getItem('color-theme') || 'green';
    document.documentElement.setAttribute('data-mode', mode);
    document.documentElement.setAttribute('data-color', colorTheme);
})();

document.addEventListener('DOMContentLoaded', function() {
    // Initialize progress circles
    initializeProgressCircles();

    // Set dynamic animation delays for table rows
    setTableRowAnimations();

    // Initialize theme icon
    const mode = document.documentElement.getAttribute('data-mode');
    updateThemeIcon(mode);

    // Initialize tab functionality
    initializeTabs();
});

function initializeProgressCircles() {
    const circles = document.querySelectorAll('.progress-circle');
    circles.forEach(circle => {
        const percent = parseFloat(circle.getAttribute('data-percent'));
        const innerCircle = circle.querySelector('.progress-circle-inner');
        setTimeout(() => {
            innerCircle.style.height = percent + '%';
        }, 500);
    });
}

function setTableRowAnimations() {
    const rows = document.querySelectorAll('.stats-table tbody tr');
    rows.forEach((row, index) => {
        row.style.animationDelay = `${(index + 1) * 0.1}s`;
    });
}

function toggleTheme() {
    const currentMode = document.documentElement.getAttribute('data-mode');
    const newMode = currentMode === 'dark' ? 'light' : 'dark';
    
    // Add transition class to body
    document.body.classList.add('theme-transition');
    
    // Update mode
    document.documentElement.setAttribute('data-mode', newMode);
    localStorage.setItem('mode', newMode);
    updateThemeIcon(newMode);
    
    // Remove transition class after transition completes
    setTimeout(() => {
        document.body.classList.remove('theme-transition');
    }, 300);
}

function updateThemeIcon(mode) {
    const sunIcon = document.querySelector('.sun-icon');
    const moonIcon = document.querySelector('.moon-icon');
    if (mode === 'dark') {
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'block';
    } else {
        sunIcon.style.display = 'block';
        moonIcon.style.display = 'none';
    }
}

// Theme color cycling
const colorThemes = ['green', 'blue', 'purple', 'orange', 'pink'];
let currentColorIndex = 0;

function cycleThemeColor() {
    currentColorIndex = (currentColorIndex + 1) % colorThemes.length;
    const newColorTheme = colorThemes[currentColorIndex];
    document.documentElement.setAttribute('data-color', newColorTheme);
    localStorage.setItem('color-theme', newColorTheme);
}

// Initialize color theme
(function() {
    const savedColorTheme = localStorage.getItem('color-theme') || 'green';
    document.documentElement.setAttribute('data-color', savedColorTheme);
    currentColorIndex = colorThemes.indexOf(savedColorTheme);
})();

// Tab functionality
function initializeTabs() {
    const tabs = document.querySelectorAll('.tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            // Remove active class from all tabs and content
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));

            // Add active class to clicked tab
            tab.classList.add('active');

            // Show corresponding content
            const tabId = tab.getAttribute('data-tab');
            document.getElementById(tabId + '-content').classList.add('active');

            // Re-initialize progress circles for newly visible content
            initializeProgressCircles();
        });
    });
}