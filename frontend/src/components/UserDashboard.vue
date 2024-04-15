<template>
  <NavBar />
  <div class="container-fluid">
    <div class="row-fluid">
      <div class="d-flex justify-content-between">
        <h5 class="text-start">Latest Songs</h5>
        <div class="text-end">
          <router-link to="/songs" class="btn btn-secondary btn-sm" style="background: cornflowerblue">
            Show More
          </router-link>
        </div>
      </div>
      <div class="col" v-if="songs">
        <SongCard v-for="song in songs.sort((a, b) => b.id - a.id).slice(0, 4) " :key="song" :song="song.id" />
      </div>

    </div>
    <div class="row-fluid" style="padding-top: 15px;">
      <div class="d-flex justify-content-between">
        <h5 class="text-start">Playlist</h5>
        <div class="text-end">
          <router-link to="/user/playlist/create" class="btn btn-secondary btn-sm" style="background: cornflowerblue">
            New Playlist
          </router-link>
        </div>
      </div>
      <div class="col-p">
        <PlaylistCard v-for="playlist in playlists" :key="playlist" :playlist="playlist.id" />
      </div>
    </div>
    <div class="row-fluid">
      <div class="d-flex justify-content-between">
        <h5 class="text-start">Albums</h5>
      </div>
      <div class="col-a">
        <AlbumCard v-for="album in albums" :key="album" :album="album.id" />
      </div>
    </div>
    <div v-for="genre in genres" :key="genre">
      <div class="row-fluid">
        <div class="d-flex justify-content-between">
          <h5 class="text-start">{{ genre }}</h5>
        </div>
        <div class="col-g" style="padding-bottom: 10px;">
          <SongCard v-for="song in songs.filter(song => song.genre === genre) " :key="song" :song="song.id" />
        </div>
      </div>
    </div>

  </div>
</template>

<style scoped>
h5 {
  font-weight: bold;
  color: chocolate;
}

.col{
  display: flex;
  /* flex-wrap: wrap; */
  justify-content: space-evenly;
}
@media screen and (max-width: 720px)
{
  .col{
    flex-wrap: wrap;
  }
}
.col-p {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.col-g {
  display: inline-flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.col-a {
  display: flex;
  justify-content: space-evenly;
  flex-wrap: wrap;
}

.row-fluid {
  padding-top: 20px;
}
</style>

<script>
import NavBar from '@/components/NavBar.vue'
import SongCard from '@/components/SongCard.vue'
import AlbumCard from '@/components/AlbumCard.vue'
import PlaylistCard from '@/components/PlaylistCard.vue'
import axios from 'axios'
import { useAuthStore } from '@/stores/authStore'

export default {
  components: {
    NavBar, SongCard, PlaylistCard, AlbumCard
  },
  data() {
    const store = useAuthStore()
    return {
      user_id: store.user.id,
      accessToken: store.accessToken,
      songs: [], // Initialize with an empty array
      playlists: [], // Initialize with an empty object
      albums: [], // Initialize with an empty object
      genres: [], // Initialize with an empty object
    };
  },
  methods: {
    async loadSongs() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/song',
          {
            headers: {
              'Authorization': `Bearer ${this.accessToken}`
            }
          });
        this.songs = response.data; // Update songs data
        const genres = new Set(this.songs.map(song => song.genre));
        this.genres = Array.from(genres);
      } catch (error) {
        console.error(error);
      }
    },
    async loadPlaylists() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/playlist',
          {
            headers: { 'Authorization': `Bearer ${this.accessToken}` }
          });
        this.playlists = response.data.filter(playlist=>playlist.user_id===this.user_id); // Update songs data
      } catch (error) {
        console.error(error);
      }
    },
    async loadAlbums() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/album',
          {
            headers: { 'Authorization': `Bearer ${this.accessToken}` }
          });
        this.albums = response.data; // Update songs data
      } catch (error) {
        console.error(error);
      }
    },
  },
  mounted() {
    this.loadSongs();
    this.loadPlaylists();
    this.loadAlbums();
  },
}
</script>
