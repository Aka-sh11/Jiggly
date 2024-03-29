<template>
    <div class="card text-center" style="width: fit-content;">
        <div class="card-body">
            <div class="card-title">{{ Data.name }}</div>
            <div class="card-content">
                <router-link :to="`/user/playlist/${Data.id}`" class="btn btn-info btn-sm">View Tracks</router-link>
            </div>
        </div>
    </div>
</template>


<style scoped>
.card {
    background-image: url('../assets/card/9.jpg');
    background-size: cover;
    border-radius: 25px;
    border: 1px solid aquamarine;
    margin-top: 12px;
    /* margin-bottom: 12px;
    margin-left: 35px;
    margin-right: 25px; */
}

.btn {
    background: cadetblue;
}

.card-title {
    color: darkturquoise;
}

.card-body {
    padding: 10px;
}
</style>


<script>
import axios from 'axios';

export default {
    name: 'PlaylistCard',
    props: ['playlist'],
    data() {
        return {
            Data: {}
        };
    },
    methods: {
        async fetchData() {
            try {
                const response = await axios.get('http://localhost:5000/api/playlist/' + this.playlist);
                this.Data = response.data;
            } catch (error) {
                console.error(error);
            }
        }
    },
    mounted() {
        this.fetchData();
    }
}
</script>