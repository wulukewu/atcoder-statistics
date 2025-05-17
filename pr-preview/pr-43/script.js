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
    // Set animation for the default active tab
    const activeTab = document.querySelector('.tab.active');
    if (activeTab) {
        const tabId = activeTab.getAttribute('data-tab');
        setTableRowAnimations(tabId);
    }
    // Initialize theme icon
    const mode = document.documentElement.getAttribute('data-mode');
    updateThemeIcon(mode);
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

function setTableRowAnimations(tabId) {
    // Only select rows from the active tab's table
    const rows = document.querySelectorAll(`#${tabId} .stats-table tbody tr`);
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
function showTab(tabId) {
    // Hide all tab contents and remove active class from tabs
    document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
    // Show the selected tab content and set tab as active
    document.getElementById(tabId).classList.add('active');
    document.querySelector(`.tab[data-tab="${tabId}"]`).classList.add('active');
    // Set animation only for visible rows
    setTableRowAnimations(tabId);

    // Update latest contest label
    const label = document.getElementById('latest-contest-label');
    if (label) {
        let contestType = 'abc';
        if (tabId === 'table-arc') contestType = 'arc';
        else if (tabId === 'table-agc') contestType = 'agc';
        const latest = label.getAttribute(`data-latest-${contestType}`);
        label.textContent = `Latest Contest: ${latest}`;
    }
}

// Initialize color theme
(function() {
    const savedColorTheme = localStorage.getItem('color-theme') || 'green';
    document.documentElement.setAttribute('data-color', savedColorTheme);
    currentColorIndex = colorThemes.indexOf(savedColorTheme);
})();