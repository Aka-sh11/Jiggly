s<template>
    <NavBar />
    <div class="container">
        <div class="row">
            <div class="box" style="display: unset">
                <div class="heading">
                    <h3 style="text-align: left; -webkit-text-fill-color: black;">Summary</h3>
                </div>
                <div class="row" style="padding-top: 8px">
                    <div class="col">
                        <em>Total Songs Uploaded</em> <br /><br />
                        <em>
                            <p>{{ songs.length }}</p>
                        </em>
                    </div>
                    <div class="col">
                        <em>Average Rating</em><br /><br />
                        <em>
                            <p>{{ average }}</p>
                        </em>
                    </div>
                    <div class="col">
                        <em>Total Likes</em><br /><br />
                        <p>{{ sumLikes }}</p>
                    </div>
                    <div class="col">
                        <em>Total Albums</em><br /><br />
                        <p>{{ albums.length }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="row-fluid">
            <div class="col-fluid">
                <div class="box-header">
                    <h3 style="text-align: left; -webkit-text-fill-color: black;">Songs</h3>
                    <ul class="nav">
                        <li class="nav-item">
                            <router-link to="/creator/song/upload" class="btn btn-primary btn-sm"
                                style="background: steelblue">Upload Song</router-link>
                        </li>
                    </ul>
                </div>
                <div class="row">
                    <div class="overflow-auto">
                        <div v-for="song in songs" :key="song.id" class="box"
                            style="margin-top: 15px; background-color: gainsboro; flex-direction: column;">
                            <div class="header">
                                <h5>{{ song.title }}</h5>
                                <ul class="nav">
                                    <li class="nav-item">
                                        <router-link :to="'/song/' + song.id" class="btn btn-info btn-sm">View
                                            Lyrics</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link :to="'/creator/song/' + song.id + '/edit'"
                                            class="btn btn-info btn-sm">Edit</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <button @click="deleteSong(song.id)" class="btn btn-info btn-sm">Delete</button>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-fluid">
                <div class="box-header">
                    <h3 style="text-align: left; -webkit-text-fill-color: black;">Albums</h3>
                    <ul class="nav">
                        <li class="nav-item">
                            <router-link to="/creator/album/create" class="btn btn-primary btn-sm"
                                style="background: steelblue">Create Album</router-link>
                        </li>
                    </ul>
                </div>
                <div class="row">
                    <div class="overflow-auto">
                        <div v-for="album in albums" :key="album.id" class="box"
                            style="margin-top: 15px; background-color: gainsboro; flex-direction: column;">
                            <div class="header">
                                <h5>{{ album.name }}</h5>
                                <ul class="nav">
                                    <li class="nav-item">
                                        <router-link :to="'/album/' + album.id" class="btn btn-info btn-sm">View
                                            Tracks</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link :to="'/creator/album/' + album.id + '/edit'"
                                            class="btn btn-info btn-sm">Edit</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <button @click="deleteAlbum(album.id)"
                                            class="btn btn-info btn-sm">Delete</button>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.header {
    display: flex;
    justify-content: center;
    align-items: center;
}

h3,
h5 {
    margin: 0 auto;
    text-align: left;
    margin-left: 0px;
}

@media only screen and (max-width: 600px) {
    .row-fluid {
        flex-direction: column;
    }
}

.btn {
    margin-left: 15px;
    margin-right: 15px;
    background: cadetblue;
}

.overflow-auto {
    height: 32vh;
    overflow-y: auto;
}

.overflow-auto::-webkit-scrollbar {
    /* For Chrome, Safari, and Opera */
    width: 8px;
    border-radius: 80px;
}

.overflow-auto::-webkit-scrollbar-thumb {
    /* For Chrome, Safari, and Opera */
    background: #999;
    border-radius: 80px;
}

.nav {
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

.box-header {
    display: flex;
    justify-content: center;
    align-items: center;
}

.row-fluid {
    display: flex;
}

.col-fluid {
    border: 1px solid #000;
    margin: auto;
    padding: 10px;
    text-align: center;
    border-radius: 25px;
    padding-bottom: 0px;

}

.row {
    margin-bottom: 20px;
}

.box {
    display: flex;
    border: 1px solid #000;
    margin: auto;
    padding: 20px;
    text-align: center;
    border-radius: 25px;
    margin-top: 10px;
}

.col {
    background-color: gainsboro;
    border: 1px solid #000;
    margin: auto;
    padding: 10px;
    text-align: center;
    border-radius: 25px;
    margin-left: 15px;
    margin-right: 15px;
    padding-bottom: 0px;
}
</style>

<script>
import axios from 'axios';
import NavBar from './NavBar.vue'
import { useAuthStore } from '@/stores/authStore'

export default {
    name: 'CreatorDashboard',
    components: {
        NavBar
    },
    data() {
        const store = useAuthStore()
        return {
            songs: [],
            albums: [],
            average: 0,
            user_id: store.user.id,
            accessToken: store.accessToken,
            sumLikes: 0
        };
    },
    created() {
        this.fetchSongs();
        this.fetchAlbums();
        this.fetchAverageRating();
    },
    methods: {
        fetchSongs() {
            axios.get('http://127.0.0.1:5000/api/song', {
                headers: {
                    'Authorization': `Bearer ${this.accessToken}`
                }
            })
                .then(response => {
                    this.songs = response.data.filter(song => song.user_id === this.user_id);
                    this.sumLikes = this.songs.reduce((sum, song) => sum + song.likes, 0);
                })
                .catch(error => {
                    alert(error);
                });
        },
        fetchAlbums() {
            axios.get('http://127.0.0.1:5000/api/album', {
                headers: {
                    'Authorization': `Bearer ${this.accessToken}`
                }
            })
                .then(response => {
                    this.albums = response.data.filter(album => album.user_id === this.user_id);
                })
                .catch(error => {
                    alert(error);
                });
        },
        deleteSong(id) {
            axios.delete(`http://127.0.0.1:5000/api/song/${id}`, {
                headers: {
                    'Authorization': `Bearer ${this.accessToken}`
                }
            })
                .then(() => {
                    this.fetchSongs(); // Refresh the list after deletion
                })
                .catch(error => {
                    alert(error);
                });
        },
        deleteAlbum(id) {
            axios.delete(`http://127.0.0.1:5000/api/album/${id}`, {
                headers: {
                    'Authorization': `Bearer ${this.accessToken}`
                }
            })
                .then(() => {
                    this.fetchAlbums(); // Refresh the list after deletion
                })
                .catch(error => {
                    alert(error);
                });
        },
        fetchAverageRating() {
            axios.get('http://127.0.0.1:5000/api/ratings', {
                headers: {
                    'Authorization': `Bearer ${this.accessToken}`
                }
            })
                .then(response => {
                    // Filter the ratings for the given user_id
                    const userRatings = response.data.filter(rating => rating.user_id === this.user_id);
                    // Calculate the average rating
                    const averageRating = userRatings.reduce((a, b) => a + b.rating, 0) / userRatings.length;
                    // Round the average rating to 2 decimal places
                    this.average = Math.round(averageRating * 100) / 100;
                })
                .catch(error => {
                    console.log(error);
                });
        }
    }
}
</script>