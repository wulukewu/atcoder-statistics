import React, { useEffect } from "react";

const COLOR_THEMES = ["green", "blue", "purple", "orange", "pink"];

function WebsiteButton() {
  return(
    <div
      className="floating-button"
      onClick={() =>
        window.open("https://kenkoooo.com/atcoder/#/table", "_blank")
      }
      title="Open AtCoder Problems Table"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        width="24"
        height="24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
        />
      </svg>
    </div>
  );
}

function ThemeToggleButton() {
  const toggleTheme = () => {
    const root = document.documentElement;
    const mode = root.getAttribute("data-mode") === "dark" ? "light" : "dark";
    root.setAttribute("data-mode", mode);
    localStorage.setItem("theme-mode", mode);
  };
  return (
    <div className="theme-toggle" onClick={toggleTheme} title="Toggle Theme">
      <svg
        className="sun-icon"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        width="24"
        height="24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
        />
      </svg>
      <svg
        className="moon-icon"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        width="24"
        height="24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
        />
      </svg>
    </div>
  );
}

function CycleThemeButton() {
  const cycleThemeColor = () => {
    const root = document.documentElement;
    const current = root.getAttribute("data-color") || "green";
    const idx = COLOR_THEMES.indexOf(current);
    const next = COLOR_THEMES[(idx + 1) % COLOR_THEMES.length];
    root.setAttribute("data-color", next);
    localStorage.setItem("theme-color", next);
  };
  return(
    <div
      className="color-theme-toggle"
      onClick={cycleThemeColor}
      title="Cycle Theme Color"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        width="24"
        height="24"
      >
        <path
          strokeLinecap="round"
          strokeLinejoin="round"
          strokeWidth="2"
          d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01"
        ></path>
      </svg>
    </div>
  );
}

function Buttons() {
  // Theme and color toggling
  useEffect(() => {
    const savedMode = localStorage.getItem("theme-mode");
    const savedColor = localStorage.getItem("theme-color");
    if (savedMode) {
      document.documentElement.setAttribute("data-mode", savedMode);
    } else if (!document.documentElement.getAttribute("data-mode")) {
      document.documentElement.setAttribute("data-mode", "light");
    }
    if (savedColor) {
      document.documentElement.setAttribute("data-color", savedColor);
    } else if (!document.documentElement.getAttribute("data-color")) {
      document.documentElement.setAttribute("data-color", "green");
    }
  }, []);
  return (
    <div className="floating-buttons">
      <WebsiteButton />
      <ThemeToggleButton />
      <CycleThemeButton />
    </div>
  );
}

export default Buttons;