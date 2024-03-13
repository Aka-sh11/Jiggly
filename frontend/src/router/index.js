import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '@/components/HomePage.vue'
import UserCreatorLogin from '@/components/UserCreatorLogin.vue'
import Registration from '@/components/Registration.vue'
import AdminLogin from '@/components/AdminLogin.vue'
import UserDashboard from '@/components/UserDashboard.vue'
import NewPlaylistAlbum from '@/components/NewPlaylistAlbum.vue'
import ViewTracks from '@/components/ViewTracks.vue'
import EditPlaylistAlbum from '@/components/EditPlaylistAlbum.vue'
import SongDetails from '@/components/SongDetails.vue'

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
    },
    {
      path: '/user/playlist/create',
      name: 'new-playlist',
      component: NewPlaylistAlbum
    },
    {
      path: '/user/songs',
      name: 'all-songs',
      component: ViewTracks
    },
    {
      path: '/user/playlist/playlist_name',
      name: 'playlist',
      component: ViewTracks
    },
    {
      path: '/album/album_name',
      name: 'album',
      component: ViewTracks
    },
    {
      path: '/user/playlist/playlist.name/edit',
      name: 'edit-playlist',
      component: EditPlaylistAlbum
    },
    {
      path: '/song/song_name',
      name: 'song-details',
      component: SongDetails
    }
  ]
})

export default router
