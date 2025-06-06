// Prevent flash of unstyled content
(function () {
  const mode =
    localStorage.getItem("mode") ||
    (window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light");
  const colorTheme = localStorage.getItem("color-theme") || "green";
  document.documentElement.setAttribute("data-mode", mode);
  document.documentElement.setAttribute("data-color", colorTheme);
})();

document.addEventListener("DOMContentLoaded", function () {
  // Initialize progress circles
  initializeProgressCircles();
  // Set animation for the default active tab
  const activeTab = document.querySelector(".tab.active");
  if (activeTab) {
    const tabId = activeTab.getAttribute("data-tab");
    setTableRowAnimations(tabId);
  }
  // Initialize theme icon
  const mode = document.documentElement.getAttribute("data-mode");
  updateThemeIcon(mode);
});

function initializeProgressCircles() {
  const circles = document.querySelectorAll(".progress-circle");
  circles.forEach((circle) => {
    const percent = parseFloat(circle.getAttribute("data-percent"));
    const innerCircle = circle.querySelector(".progress-circle-inner");
    setTimeout(() => {
      innerCircle.style.height = percent + "%";
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
  const currentMode = document.documentElement.getAttribute("data-mode");
  const newMode = currentMode === "dark" ? "light" : "dark";

  // Add transition class to body
  document.body.classList.add("theme-transition");

  // Update mode
  document.documentElement.setAttribute("data-mode", newMode);
  localStorage.setItem("mode", newMode);
  updateThemeIcon(newMode);

  // Remove transition class after transition completes
  setTimeout(() => {
    document.body.classList.remove("theme-transition");
  }, 300);
}

function updateThemeIcon(mode) {
  const sunIcon = document.querySelector(".sun-icon");
  const moonIcon = document.querySelector(".moon-icon");
  if (mode === "dark") {
    sunIcon.style.display = "none";
    moonIcon.style.display = "block";
  } else {
    sunIcon.style.display = "block";
    moonIcon.style.display = "none";
  }
}

// Theme color cycling
const colorThemes = ["green", "blue", "purple", "orange", "pink"];
let currentColorIndex = 0;

function cycleThemeColor() {
  currentColorIndex = (currentColorIndex + 1) % colorThemes.length;
  const newColorTheme = colorThemes[currentColorIndex];
  document.documentElement.setAttribute("data-color", newColorTheme);
  localStorage.setItem("color-theme", newColorTheme);
}

function showTab(tabId) {
  // Hide all tab contents and remove active class from tabs
  document
    .querySelectorAll(".tab-content")
    .forEach((tab) => tab.classList.remove("active"));
  document
    .querySelectorAll(".tab")
    .forEach((tab) => tab.classList.remove("active"));
  // Show the selected tab content and set tab as active
  document.getElementById(tabId).classList.add("active");
  document.querySelector(`.tab[data-tab="${tabId}"]`).classList.add("active");
  setTableRowAnimations(tabId);

  // Animate the latest contest label by replacing the element
  const oldLabel = document.getElementById("latest-contest-label");
  if (oldLabel) {
    let contestType = "abc";
    if (tabId === "table-arc") contestType = "arc";
    else if (tabId === "table-agc") contestType = "agc";
    const latest = oldLabel.getAttribute(`data-latest-${contestType}`);

    // Create a new label element
    const newLabel = oldLabel.cloneNode(false);
    newLabel.id = "latest-contest-label";
    newLabel.textContent = `Latest Contest: ${latest}`;
    newLabel.style.opacity = "0";
    newLabel.style.animation =
      "labelFadeIn 1.2s cubic-bezier(0.4,0,0.2,1) forwards";
    // Replace the old label with the new one
    oldLabel.parentNode.replaceChild(newLabel, oldLabel);
  }
}

// Initialize color theme
(function () {
  const savedColorTheme = localStorage.getItem("color-theme") || "green";
  document.documentElement.setAttribute("data-color", savedColorTheme);
  currentColorIndex = colorThemes.indexOf(savedColorTheme);
})();
