import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue'; // We'll create this view component next

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView,
  },
  // We can add more routes later if needed, for example, for a dedicated problem list page
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
