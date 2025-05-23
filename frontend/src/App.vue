<template>
  <div id="app">
    <Header />
    <ThemeToggle />
    <router-view /> 
  </div>
</template>

<script>
import Header from './components/Header.vue';
import ThemeToggle from './components/ThemeToggle.vue';

export default {
  name: 'App',
  components: {
    Header,
    ThemeToggle,
  },
  // Basic data fetching and state management will be added later
};
</script>

<style>
/* Global styles will be added here from styles.css */
</style>
