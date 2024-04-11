<template>
    <NavBar />
    <div v-if="$route.name === 'all-songs'" class="Songs">
        <h2>All Songs</h2>
        <div class="filter">
            <label for="rating-filter">Filter by Rating:</label>
            <select v-model="filterRating" id="rating-filter">
                <option value="0">All</option>
                <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
            </select>
        </div>
        <div class="col">
            <SongCard v-for="song in filteredSongs.sort((a, b) => a.title.localeCompare(b.title))" :key="song.id"
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
            <SongCard v-for="song in songs.sort((a, b) => (a.title || '').localeCompare(b.title || '')) " :key="song.id"
                :song="song" />
        </div>

    </div>
    <div v-else-if="$route.name === 'album' || $route.name === 'admin-albums'" class="Albums">
        <h2>{{ album.name }}</h2>
        <div class="col">
            <SongCard v-for="song in songs.sort((a, b) => a.title && b.title ? a.title.localeCompare(b.title) : 0)"
                :key="song.id" :song="song" />
        </div>

    </div>
</template>

<style scoped>
.filter {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
    margin-right: 20px;
}
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
import { useAuthStore } from '@/stores/authStore'

export default {
    components: {
        NavBar, SongCard,
    },
    data() {
        const store = useAuthStore()
        return {
            songs: [], // Initialize with an empty array
            playlist: [], // Initialize with an empty object
            album: [], // Initialize with an empty object
            user_id: store.user.id,
            accessToken: store.accessToken,
            filterRating: 0,
        };
    },
    computed: {
        filteredSongs() {
            if (this.filterRating === 0) {
                return this.songs;
            } else {
                return this.songs.filter(song => song.rating === this.filterRating);
            }
        }
    },
    methods: {
        fetchData() {
            // Make API requests based on route name
            if (this.$route.name === 'all-songs') {
                axios.get('http://127.0.0.1:5000/api/song',
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
                    .then(response => {
                        this.songs = response.data.map(song => {
                            // Fetch rating for each song
                            axios.get(`http://127.0.0.1:5000/api/ratings/${song.id}/${this.user_id}`,
                                { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
                                .then(ratingResponse => {
                                    song.rating = ratingResponse.data.rating; // Update song rating
                                })
                                .catch(error => {
                                    console.error(error); // Log error to console
                                });
                            return song;
                        });
                    })
                    .catch(error => {
                        console.error(error); // Log error to console
                    });

            } else if (this.$route.name === 'playlist') {
                const playlistId = this.$route.params.id;
                axios.get(`http://127.0.0.1:5000/api/playlist/${playlistId}`,
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
                    .then(response => {
                        this.playlist = response.data; // Update playlist data
                        this.songs = this.playlist.songs; // Update songs data
                    })
                    .catch(error => {
                        console.error(error); // Log error to console
                    });
            } else if (this.$route.name === 'album') {
                const albumId = this.$route.params.id;
                axios.get(`http://127.0.0.1:5000/api/album/${albumId}`,
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
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
    watch: {
        filterRating(newVal) {
            if (newVal === 0) {
                this.fetchData();
            }
        }
    },
    mounted() {
        this.fetchData();
    },

};
</script>
