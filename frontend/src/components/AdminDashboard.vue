<template>
    <NavBar />
    <div class="container">
        <div class="row">
            <div class="box overflow-auto" style="display: unset;">
                <div class="heading">
                    <h3 style="text-align: left; -webkit-text-fill-color: black;">App Performance</h3>
                </div>
                <div class="row" style="padding-top: 8px">
                    <div class="col">
                        <router-link to="/admin/tracks">
                            <h5>Tracks</h5>
                        </router-link> <br />
                        <em>
                            <p>{{ songData.length }}</p>
                        </em>
                    </div>
                    <div class="col">
                        <router-link to="/admin/creators">
                            <h5>Creators</h5>
                        </router-link><br />
                        <em>
                            <p>{{ creator.length }}</p>
                        </em>
                    </div>
                    <div class="col">
                        <router-link to="/admin/albums">
                            <h5>Albums</h5>
                        </router-link> <br />
                        <p>{{ albumData.length }}</p>
                    </div>
                </div>
                <div class="row-fluid">
                    <div class="col-fluid">
                        <h4>Total Likes</h4> <br />
                        <em>
                            <p>{{ sumLikes }} </p>
                        </em>
                    </div>
                    <div class="col-fluid">
                        <h4>Normal Users</h4> <br />
                        <em>
                            <p>{{ normalUser.length }} </p>
                        </em>
                    </div>
                    <div class="col-fluid">
                        <h4>Total Genres</h4> <br />
                        <em>
                            <p>{{ genres.length }}</p>
                        </em>
                    </div>
                </div>
                <div class="row-fluid" style="margin-bottom: 0px;">
                    <div class="col-fluid"
                        style="background: -webkit-linear-gradient(109.6deg, rgba(48, 207, 208, 1) 11.2%, rgb(218, 63, 153) 92.5%);">
                        <h3>Various Key Graphs</h3> <br />
                        <div style="display: flex; justify-content: space-between;">
                            <div style="margin-right: 20px;">
                                <PieChart />
                            </div>
                            <div>
                                <BarChart />
                            </div>
                        </div>
                        <br />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
a {
    text-decoration: none;
    align-items: center;
    color: rgb(209, 96, 96);
}

a:hover {
    color: rgb(122, 163, 245);
    ;
}

.overflow-auto {
    height: 85vh;
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

.col-fluid {
    background-color: gainsboro;
    /* background: -webkit-linear-gradient(109.6deg, rgba(48, 207, 208, 1) 11.2%, rgb(218, 63, 153) 92.5%); */
    border: 1px solid #000;
    margin: auto;
    padding: 10px;
    text-align: center;
    border-radius: 25px;
    padding-bottom: 0px;

}

@media only screen and (max-width: 600px) {
    .row-fluid {
        flex-direction: column;
    }
}

.row-fluid {
    display: flex;
    margin-bottom: 20px;
    justify-content: space-between;
}

.col {
    background-color: gainsboro;
    /* background: -webkit-linear-gradient(109.6deg, rgba(48, 207, 208, 1) 11.2%, rgb(218, 63, 153) 92.5%); */
    border: 1px solid #000;
    margin: auto;
    padding: 10px;
    text-align: center;
    border-radius: 25px;
    margin-left: 15px;
    margin-right: 15px;
    padding-bottom: 0px;
}

h3 {
    margin: 0 auto;
    text-align: center;
    margin-left: 0px;
}

.row {
    margin-bottom: 20px;
}

.box {
    /* background: -webkit-linear-gradient(109.6deg, rgba(48, 207, 208, 1) 11.2%, rgb(218, 63, 153) 92.5%); */
    display: flex;
    border: 1px solid #000;
    margin: auto;
    padding: 20px;
    text-align: center;
    border-radius: 25px;
    margin-top: 10px;
}

p {
    font-weight: bold;
    font-size: larger;
}
</style>

<script>
import axios from 'axios';
import NavBar from './NavBar.vue'
import PieChart from './PieChart.vue'
import BarChart from './BarChart.vue'
import { useAuthStore } from '@/stores/authStore';

export default {
    name: 'AdminDashboard',
    components: {
        NavBar,
        PieChart,
        BarChart
    },
    data() {
        const store = useAuthStore();
        return {
            songData: null,
            userData: null,
            albumData: null,
            genres: null,
            normalUser: null,
            creator: null,
            user_id: store.user.id,
            accessToken: store.accessToken,
            sumLikes: 0
        }
    },
    created() {
        this.fetchData();
    },
    methods: {
        async fetchData() {
            try {
                const songResponse = await axios.get('http://127.0.0.1:5000/api/song',
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } });
                this.songData = songResponse.data;
                this.sumLikes = this.songData.reduce((sum, song) => sum + song.likes, 0);
                this.genres = [...new Set(this.songData.map(song => song.genre))];

                const userResponse = await axios.get('http://127.0.0.1:5000/api/user',
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } });
                this.userData = userResponse.data;
                this.normalUser = this.userData.filter(user => user.role === 'User')
                this.creator = this.userData.filter(user => user.role === 'Creator')

                const albumResponse = await axios.get('http://127.0.0.1:5000/api/album',
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } });
                this.albumData = albumResponse.data;
            } catch (error) {
                console.error(error);
            }
        }
    }
}
</script>
