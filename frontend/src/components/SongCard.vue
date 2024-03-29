<template>
    <div class="card text-center" style="width: fit-content;">
        <div class="card-body">
            <div class="card-title">{{ songData.title }}</div>
            <div class="card-content">
                <audio ref="audio" controls>
                    <source :src="'/audio/' + songData.filename" type="audio/mp3" />
                </audio>

                <br />
                <router-link :to="`/song/${songData.id}`" class="btn btn-info btn-sm">Read Lyrics</router-link>
            </div>
        </div>
    </div>
</template>


<style scoped>
.card {
    background-image: url('../assets/card/19.jpg');
    background-size: cover;
    border-radius: 25px;
    border: 1px solid magenta;
    margin-top: 12px;
    margin-bottom: 12px;
    margin-left: 15px;
    margin-right: 25px;
}

.card-title {
    color: deeppink;
}

.card-body {
    padding: 10px;
    padding-bottom: 8px;
}

audio {
    width: 255px;
}

.btn {
    margin-top: 8px;
}
</style>


<script>
import axios from 'axios';

export default {
    name: 'SongCard',
    props: ['song'],
    data() {
        return {
            songData: {}, // Store song data for each ID
            audioSource: null // Initialize audio source
        };
    },
    methods: {
        async fetchSongData() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/song/' + this.song);
                this.songData = response.data; // Update songData with the fetched data
            } catch (error) {
                console.error('Error fetching song data:', error);
            }
        }
    },
    updated() {
        this.$refs.audio.load();
        // this.$refs.audio.play();
    },
    mounted() {
        this.fetchSongData();
    }
};
</script>
