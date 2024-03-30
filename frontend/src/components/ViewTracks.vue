<template>
    <NavBar />
    <div v-if="$route.name === 'all-songs'" class="Songs">
        <h2>All Songs</h2>
        <div class="col">
            <SongCard v-for="song in songs.sort((a, b) => a.title.localeCompare(b.title)) " :key="song"
                :song="song.id" />
        </div>
    </div>
    <div v-else-if="$route.name === 'playlist'" class="Playlist">
        <div class="container">
            <h2 class="title">{{ playlist.name }}</h2>
            <router-link :to="`/user/playlist/${playlist.id}/edit`" class="btn btn-secondary btn-sm"
                style="background: cornflowerblue">
                Edit Playlist
            </router-link>
        </div>
        <div class="col">
            <SongCard v-for="song in songs.sort((a, b) => a.title.localeCompare(b.title))  " :key="song.id"
                :song="song" />
        </div>
    </div>
    <div v-else-if="$route.name === 'album' || $route.name==='admin-albums'" class="Albums">
        <h2>{{ album.name }}</h2>
        <div class="col">
            <SongCard v-for="song in songs.sort((a, b) => a.title.localeCompare(b.title)) " :key="song.id"
                :song="song" />
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

.btn {
    margin-top: 10px;
}
</style>

<script>
import NavBar from '@/components/NavBar.vue'
import SongCard from '@/components/SongCard.vue'
import axios from 'axios';

export default {
    components: {
        NavBar, SongCard,
    },
    data() {
        return {
            songs: [], // Initialize with an empty array
            playlist: [], // Initialize with an empty object
            album: [], // Initialize with an empty object
        };
    },
    methods: {
        fetchData() {
            // Make API requests based on route name
            if (this.$route.name === 'all-songs') {
                axios.get('http://127.0.0.1:5000/api/song')
                    .then(response => {
                        this.songs = response.data; // Update songs data
                    })
                    .catch(error => {
                        console.error(error); // Log error to console
                    });
            } else if (this.$route.name === 'playlist') {
                const playlistId = this.$route.params.id;
                axios.get(`http://127.0.0.1:5000/api/playlist/${playlistId}`)
                    .then(response => {
                        this.playlist = response.data; // Update playlist data
                        this.songs = this.playlist.songs; // Update songs data
                    })
                    .catch(error => {
                        console.error(error); // Log error to console
                    });
            } else if (this.$route.name === 'album') {
                const albumId = this.$route.params.id;
                axios.get(`http://127.0.0.1:5000/api/album/${albumId}`)
                    .then(response => {
                        this.album = response.data; // Update album data
                        this.songs = this.album.songs; // Update songs data
                    })
                    .catch(error => {
                        console.error(error); // Log error to console
                    });
            }
        }
    },
    mounted() {
        this.fetchData();
    },

};
</script>
