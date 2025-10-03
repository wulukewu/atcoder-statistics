export function initializeTheme() {
  const mode = localStorage.getItem('mode') || 
    (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  const colorTheme = localStorage.getItem('color-theme') || 'green';
  
  document.documentElement.setAttribute('data-mode', mode);
  document.documentElement.setAttribute('data-color', colorTheme);
  
  return { mode, colorTheme };
}

export function toggleTheme() {
  const currentMode = document.documentElement.getAttribute('data-mode');
  const newMode = currentMode === 'dark' ? 'light' : 'dark';
  
  document.documentElement.setAttribute('data-mode', newMode);
  localStorage.setItem('mode', newMode);
  
  return newMode;
}

export function cycleColorTheme() {
  const colorThemes = ['green', 'blue', 'purple', 'orange', 'pink'];
  const currentColor = document.documentElement.getAttribute('data-color');
  const currentIndex = colorThemes.indexOf(currentColor);
  const nextIndex = (currentIndex + 1) % colorThemes.length;
  const newColor = colorThemes[nextIndex];
  
  document.documentElement.setAttribute('data-color', newColor);
  localStorage.setItem('color-theme', newColor);
  
  return newColor;
}
