<template>
    <NavBar />
    <div class="container">
        <div class="header">
            <h2>All Creators</h2>
        </div>
        <div class="row-fluid">
            <div class="box">
                <div class="overflow-auto">
                    <div v-for="creator in creators" :key="creator.id" class="box-s">
                        <div class="header">
                            <h6><b>{{ creator.username }}</b>&nbsp;(<a :href="'mailto:' + creator.email">{{ creator.email
                                    }}</a>)</h6>

                            <ul class="nav">
                                <li class="nav-item">
                                    <div class=" btn btn-info btn-sm">
                                        Songs : {{ getCreatorSongs(creator).length }}
                                    </div>
                                    <div class=" btn btn-info btn-sm">
                                        Albums: {{ getCreatorAlbums(creator).length }}
                                    </div>
                                    <div class=" btn btn-info btn-sm">
                                        Avg Rating: {{ creator.avgRating }}
                                    </div>
                                    <div class=" btn btn-info btn-sm">
                                        Likes: {{ creator.likes }}
                                    </div>
                                </li>
                                <li class="nav-item">
                                    <button class="btn btn-info btn-sm"
                                        :style="{ background: creator.blacklisted ? 'rgb(240 71 71)' : '#79eb79' }"
                                        @click="toggleBlacklist(creator)">{{ creator.blacklisted ? 'Blacklist' :
                                        'Whitelist'
                                        }}</button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>
</template>

<style scoped>
b{
    color: chocolate;
    font-size: x-large;
    padding-left: 25px;

}
button {
    width: 100px;
}

@media only screen and (max-width: 600px) {
    .row-fluid {
        flex-direction: column;
    }
}

.row-fluid {
    /* display: flex; */
    flex-wrap: wrap;
    justify-content: space-around;
    align-content: center;
    align-items: center;
    margin-bottom: 20px;
    /* width: 70%; */
}

.overflow-auto {
    height: 70vh;
    overflow-y: auto;
}

.overflow-auto::-webkit-scrollbar {
    /* For Chrome, Safari, and Opera */
    width: 8px;
    border-radius: 100px;
}

.overflow-auto::-webkit-scrollbar-thumb {
    /* For Chrome, Safari, and Opera */
    background: #999;
    border-radius: 100px;
}

h2,
h6 {
    margin: 0 auto;
    text-align: left;
    margin-left: 0px;
}

.box {
    background-color: inherit;
    border: 1px solid #000;
    margin: auto;
    text-align: center;
    border-radius: 25px;
    margin-top: 20px;
    margin-bottom: 15px;
    margin-left: 12px;
    margin-right: 12px;
    padding-top: 7px;
    padding-left: 12px;
    padding-right: 12px;
    padding-bottom: 12px;
}

.box-s {
    background-color: gainsboro;
    border: 1px solid #000;
    margin: auto;
    text-align: center;
    border-radius: 25px;
    margin-top: 20px;
    margin-left: 12px;
    margin-right: 12px;
    padding-top: 7px;
    padding-left: 12px;
    padding-right: 12px;
    padding-bottom: 12px;
    display: flow;
}

.nav {
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

.btn {
    background: rgb(184, 235, 236);
    margin-left: 15px;
    margin-right: 15px;
}

.header {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 8px;
    /* padding-left: 25px; */
}
</style>

<script>
import NavBar from './NavBar.vue'
import axios from 'axios';
import { useAuthStore } from '@/stores/authStore';

export default {
    name: 'AdminCreators',
    components: {
        NavBar
    },
    data() {
        const store = useAuthStore();
        return {
            accessToken: store.accessToken,
            user_id: store.user.id,
            creators: [],
            songs: [],
            albums: []
        }
    },
    created() {
        this.fetchData();
    },
    methods: {
        async fetchData() {
            try {
                const response = await axios.get('http://localhost:5000/api/user',
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } });
                this.creators = response.data.filter(user => user.role === 'Creator');

                const songsResponse = await axios.get('http://localhost:5000/creatorSongs',
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } });
                this.songs = songsResponse.data;
                // let totalLikes = this.songs.reduce((sum, song) => sum + song.likes, 0);
                // this.likes = totalLikes;
                

                const albumsResponse = await axios.get('http://localhost:5000/creatorAlbums',
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } });
                this.albums = albumsResponse.data;

                // Fetch ratings and calculate average for each creator
                const ratingsResponse = await axios.get('http://localhost:5000/api/ratings',
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } });
                this.creators.forEach(creator => {
                    const creatorRatings = ratingsResponse.data.filter(rating => rating.user_id === creator.id);
                    const sum = creatorRatings.reduce((a, b) => a + b.rating, 0);
                    creator.avgRating = (sum / creatorRatings.length) || 0;
                    creator.avgRating = parseFloat(creator.avgRating.toFixed(2));
                });
            } catch (error) {
                console.error(error);
            }
        },
        toggleBlacklist(creator) {
            creator.blacklisted = !creator.blacklisted;

            axios.put(`http://localhost:5000/blacklist/${creator.id}`, {
                blacklisted: creator.blacklisted,
            }, { headers: { 'Authorization': `Bearer ${this.accessToken}` }
            })
                .then(response => {
                    console.log(response);
                })
                .catch(error => {
                    console.log(error);
                });
        },
        getCreatorSongs(creator) {
            const creatorSongs = this.songs.filter(song => song.user_id === creator.id);
            creator.likes = creatorSongs.reduce((sum, song) => sum + song.likes, 0);
            return creatorSongs;
        },
        getCreatorAlbums(creator) {
            return this.albums.filter(album => album.user_id === creator.id);
        }
    },
}
</script>