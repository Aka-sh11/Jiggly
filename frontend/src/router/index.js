import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/components/HomePage.vue'

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
      component: () => import('@/components/UserDashboard.vue')
    },
    {
      path: '/songs',
      name: 'all-songs',
      component: () => import('@/components/ViewTracks.vue')
    },
    {
      path: '/song/:id',
      name: 'song-details',
      component: () => import('@/components/SongDetails.vue')
    },
       {
      path: '/user/playlist/create',
      name: 'new-playlist',
      component: () => import('@/components/NewPlaylistAlbum.vue')
    },
    {
      path: '/user/playlist/playlist_name',
      name: 'playlist',
      component: () => import('@/components/ViewTracks.vue')
    },
    {
      path: '/user/playlist/playlist.name/edit',
      name: 'edit-playlist',
      component: () => import('@/components/EditPlaylistAlbum.vue')
    },
    {
      path: '/album/album_name',
      name: 'album',
      component: () => import('@/components/ViewTracks.vue')
    },
    {
      path: '/creator/dashboard',
      name: 'creator-dashboard',
      component: () => import('@/components/CreatorDashboard.vue')
    },
    {
      path: '/creator/song/upload',
      name: 'upload-song',
      component: () => import('@/components/NewSongEdit.vue')
    },
    {
      path: '/creator/songs/song_name/edit',
      name: 'edit-song',
      component: () => import('@/components/NewSongEdit.vue')
    },
    {
      path: '/creator/album/create',
      name: 'new-album',
      component: () => import('@/components/NewPlaylistAlbum.vue')
    },
    {
      path: '/creator/album/album_name/edit',
      name: 'edit-album',
      component: () => import('@/components/EditPlaylistAlbum.vue')
    },
    {
      path: '/admin/dashboard',
      name: 'admin-dashboard',
      component: () => import('@/components/AdminDashboard.vue')
    },
    {
      path: '/admin/tracks',
      name: 'admin-tracks',
      component: () => import('@/components/AdminTracks.vue')
    },
    {
      path: '/admin/albums',
      name: 'admin-albums',
      component: () => import('@/components/AdminAlbums.vue')
    },
    {
      path: '/admin/creators',
      name: 'admin-creators',
      component: () => import('@/components/AdminCreators.vue')
    }
  ]
})

export default router
