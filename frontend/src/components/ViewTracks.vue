<template>
    <NavBar />
    <div v-if="$route.name === 'all-songs'" class="Songs">
        <h2>All Songs</h2>
        <div class="col">
            <SongCard v-for="n in 8" :key="n" />
        </div>
    </div>
    <div v-else-if="$route.name === 'playlist'" class="Playlist">
        <div class="container">
            <h2 class="title">playlist.name</h2>
            <router-link :to="`/user/playlist/playlist.name/edit`" class="btn btn-secondary btn-sm"
                style="background: cornflowerblue">
                Edit Playlist
            </router-link>
        </div>
        <div class="col">
            <SongCard v-for="n in 8" :key="n" />
        </div>
    </div>
    <div v-else-if="$route.name === 'album'" class="Albums">
        <h2>Album.name</h2>
        <div class="col">
            <SongCard v-for="n in 8" :key="n" />
        </div>
    </div>
</template>

<style scoped>
.col {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding-top: 10px;
}

.container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.title {
    margin: 0;
}
h2 {
    text-align: center;
    margin-top: 5px;
    color: chocolate;
}
.btn{
    margin-top: 10px;
}
</style>

<script>
import NavBar from '@/components/NavBar.vue'
import SongCard from '@/components/SongCard.vue'

export default {
    components: {
        NavBar, SongCard,
    }
}
</script>
