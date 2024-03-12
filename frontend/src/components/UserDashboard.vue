<template>
  <NavBar />
  <div class="container-fluid">
    <div class="row-fluid">
      <div class="d-flex justify-content-between">
        <h5 class="text-start">Latest Songs</h5>
        <div class="text-end">
          <router-link to="/user/songs" class="btn btn-secondary btn-sm" style="background: cornflowerblue">
            Show More
          </router-link>
        </div>
      </div>
      <div class="col">
        <SongCard v-for="n in 4" :key="n" />
      </div>
    </div>
    <div class="row-fluid">
      <div class="d-flex justify-content-between">
        <h5 class="text-start">Playlist</h5>
        <div class="text-end">
          <router-link to="/playlist/create" class="btn btn-secondary btn-sm" style="background: cornflowerblue">
            New Playlist
          </router-link>
        </div>
      </div>
      <div class="col">
        <PlaylistCard v-for="n in 6" :key="n" />
      </div>
    </div>
    <div class="row-fluid">
      <div class="d-flex justify-content-between">
        <h5 class="text-start">Albums</h5>
      </div>
      <div class="col-a">
        <AlbumCard v-for="n in 5" :key="n" />
      </div>
    </div>
    <div class="row-fluid">
      <div class="d-flex justify-content-between">
        <h5 class="text-start">Genres</h5>
      </div>
      <div class="col">
        <SongCard v-for="n in 4" :key="n" />
      </div>
    </div>
  </div>
</template>

<style scoped>
.col {
  display: flex;
  justify-content: space-around;
  padding-top: 10px;
}

.col-a {
  display: flex;
  justify-content: space-evenly;
  padding-top: 8px;
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

export default {
  components: {
    NavBar, SongCard, AlbumCard, PlaylistCard
  },
  data() {
    return {
      song: {
        title: '',
        filename: '',
        id: ''
      }
    }
  }
}
</script>
