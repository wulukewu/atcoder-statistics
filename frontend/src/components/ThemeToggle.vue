<template>
  <div class="theme-toggle-container">
    <button @click="toggleTheme" class="theme-button">
      Theme: {{ currentTheme === 'light' ? '🌞 Light' : '🌜 Dark' }}
    </button>
    <button @click="toggleColorScheme" class="theme-button">
      Colors: {{ currentColorScheme === 'normal' ? '🎨 Normal' : '🌈 Difficulty' }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'ThemeToggle',
  data() {
    return {
      currentTheme: 'light', // Default theme
      currentColorScheme: 'normal', // Default color scheme
    };
  },
  methods: {
    applyTheme() {
      document.documentElement.setAttribute('data-theme', this.currentTheme);
      localStorage.setItem('theme', this.currentTheme);
    },
    applyColorScheme() {
      document.documentElement.setAttribute('data-color-scheme', this.currentColorScheme);
      localStorage.setItem('colorScheme', this.currentColorScheme);
    },
    toggleTheme() {
      this.currentTheme = this.currentTheme === 'light' ? 'dark' : 'light';
      this.applyTheme();
    },
    toggleColorScheme() {
      this.currentColorScheme = this.currentColorScheme === 'normal' ? 'difficulty' : 'normal';
      this.applyColorScheme();
    },
    loadPreferences() {
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme) {
        this.currentTheme = savedTheme;
      }
      const savedColorScheme = localStorage.getItem('colorScheme');
      if (savedColorScheme) {
        this.currentColorScheme = savedColorScheme;
      }
      this.applyTheme();
      this.applyColorScheme();
    }
  },
  mounted() {
    this.loadPreferences();
  }
};
</script>

<style scoped>
.theme-toggle-container {
  padding: 1rem;
  text-align: right; /* Aligns buttons to the right */
  position: fixed; /* Fixes position relative to the viewport */
  top: 10px;
  right: 10px;
  z-index: 1000; /* Ensures it's above other content */
}

.theme-button {
  background-color: var(--button-bg, #007bff); /* Uses CSS variable with fallback */
  color: var(--button-text, #fff); /* Uses CSS variable with fallback */
  border: none;
  padding: 0.6em 1.2em; /* Slightly larger padding */
  margin-left: 0.8em; /* Spacing between buttons */
  cursor: pointer;
  border-radius: 5px; /* Rounded corners */
  font-size: 0.9em; /* Adjust font size as needed */
  transition: background-color 0.2s ease-in-out, transform 0.1s ease;
}

.theme-button:hover {
  opacity: 0.85; /* Slightly more subtle hover effect */
}

.theme-button:active {
  transform: scale(0.95); /* Click effect */
}
</style>
