import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/components/HomePage.vue'
import UserCreatorLogin from '@/components/UserCreatorLogin.vue'
import Registration from '@/components/Registration.vue'
import AdminLogin from '@/components/AdminLogin.vue'
import UserDashboard from '@/components/UserDashboard.vue'
import NavBar from '@/components/NavBar.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage
    },
    {
      path: '/login',
      name: 'user-creator-login',
      component: UserCreatorLogin
    },
    {
      path: '/register',
      name: 'user-creator-register',
      component: Registration
    },
    {
      path: '/login/admin',
      name: 'admin-login',
      component: AdminLogin
    },
    {
      path: '/user/dashboard',
      name: 'user-dashboard',
      component: UserDashboard
    }
  ]
})

export default router
