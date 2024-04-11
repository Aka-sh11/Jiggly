import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/components/HomePage.vue'
import { useAuthStore } from '@/stores/authStore'

// const store = useAuthStore()

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
      component: () => import('@/components/UserCreatorLogin.vue')
    },
    {
      path: '/register',
      name: 'user-creator-register',
      component: () => import('@/components/RegistrationPage.vue')
    },
    {
      path: '/login/admin',
      name: 'admin-login',
      component: () => import('@/components/AdminLogin.vue')
    },
    {
      path: '/user/dashboard',
      name: 'user-dashboard',
      component: () => import('@/components/UserDashboard.vue'),
      meta: { requiresAuth: true, role: 'User' }
    },
    {
      path: '/songs',
      name: 'all-songs',
      component: () => import('@/components/ViewTracks.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/albums',
      name: 'all-albums',
      component: () => import('@/components/CreatorAlbums.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/song/:id',
      name: 'song-details',
      component: () => import('@/components/SongDetails.vue'),
      meta: { requiresAuth:true }
    },
       {
      path: '/user/playlist/create',
      name: 'new-playlist',
      component: () => import('@/components/NewPlaylistAlbum.vue'),
      meta: { requiresAuth: true, role: 'User' }
    },
    {
      path: '/user/playlist/:id',
      name: 'playlist',
      component: () => import('@/components/ViewTracks.vue'),
      meta: { requiresAuth: true, role: 'User' }
    },
    {
      path: '/user/playlist/:id/edit',
      name: 'edit-playlist',
      component: () => import('@/components/EditPlaylistAlbum.vue'),
      meta: { requiresAuth: true, role: 'User' }
    },
    {
      path: '/album/:id',
      name: 'album',
      component: () => import('@/components/ViewTracks.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/creator/dashboard',
      name: 'creator-dashboard',
      component: () => import('@/components/CreatorDashboard.vue'),
      meta: { requiresAuth: true, role: 'Creator' }
    },
    {
      path: '/creator/song/upload',
      name: 'upload-song',
      component: () => import('@/components/NewSongEdit.vue'),
      meta: { requiresAuth: true, role: 'Creator' }
    },
    {
      path: '/creator/song/:id/edit',
      name: 'edit-song',
      component: () => import('@/components/NewSongEdit.vue'),
      meta: { requiresAuth: true, role: 'Creator' }
    },
    {
      path: '/creator/album/create',
      name: 'new-album',
      component: () => import('@/components/NewPlaylistAlbum.vue'),
      meta: { requiresAuth: true, role: 'Creator' }
    },
    {
      path: '/creator/album/:id/edit',
      name: 'edit-album',
      component: () => import('@/components/EditPlaylistAlbum.vue'),
      meta: { requiresAuth: true, role: 'Creator' }
    },
    {
      path: '/admin/dashboard',
      name: 'admin-dashboard',
      component: () => import('@/components/AdminDashboard.vue'),
      meta: { requiresAuth: true, role: 'Admin' }
    },
    {
      path: '/admin/tracks',
      name: 'admin-tracks',
      component: () => import('@/components/AdminTracks.vue'),
      meta: { requiresAuth: true, role: 'Admin' }
    },
    {
      path: '/admin/albums',
      name: 'admin-albums',
      component: () => import('@/components/AdminAlbums.vue'),
      meta: { requiresAuth: true, role: 'Admin' }
    },
    {
      path: '/admin/creators',
      name: 'admin-creators',
      component: () => import('@/components/AdminCreators.vue'),
      meta: { requiresAuth: true, role: 'Admin' }
    }
  ]
})

router.beforeResolve((to, from, next) => {
  const auth = useAuthStore()
  if (to.meta.requiresAuth) {
    if (auth.isUserLoggedIn) {
      // console.log('authenticated', to.meta.role, auth.user.role, to.path)
      if (to.meta.role && auth.user.role && auth.user.role !== to.meta.role) {
        alert('Not Authorized')
        router.push('/')
      } else {
        next()
      }
    } else {
      auth.returnURL = to.fullPath
      next({ path: '/login', query: { redirect: to.fullPath } })
    }
  } else {
    next()
  }
})

export default router
