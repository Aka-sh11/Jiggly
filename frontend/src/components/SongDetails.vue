<template>
    <NavBar />
    <div class="box-m">
        <div class="overflow-auto">
            <div class="box">
                <div class="header">
                    <h2 v-if="song">{{ song.title }}</h2>
                    <nav>
                        <button class="btn btn-info btn-sm" @click="rateSong"
                            style="background-color: cadetblue;">Rate</button>

                        <div v-if="showRating">
                            <input type="range" id="rating" v-model.number="rating" min="0" max="5">
                            <span>{{ rating }}</span>
                        </div>
                    </nav>
                </div>
                <h6 v-if="song">{{ song.singer }} <b>|</b> {{ song.date.substring(0, 4) }}</h6>
                <audio controls v-if="song">
                    <source :src="'/audio/' + song.filename" type="audio/mp3" />
                </audio>
                <div class="box" style="background-color: gainsboro;">
                    <p v-if="song">{{ song.lyrics }}</p>
                </div>
                <br />
                <div class="emoji" v-for="( Icon, index ) in  reactionIcons " :key="index">
                    <button @click="triggerAnimation(index)" :class="{ pop: Icon.pop, float: Icon.float }"
                        style="font-size: 1.2rem;">
                        {{ Icon.icon }}
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
b {
    color: chocolate;
}

nav {
    display: flex;
    justify-content: flex-end;
    align-items: center;

}

.emoji {
    display: inline-flex;
    justify-content: flex-end;
}

button {
    /* font-size: 1.2rem; */
    padding: 8px;
    /* margin: 5px; */
    border: none;
    background: none;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}

.overflow-auto {
    height: 80vh;
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
    color: deeppink;
}

h6 {
    color: mediumorchid;
}

.header {
    display: flex;
    justify-content: center;
    align-items: center;
}

.box-m {
    padding-top: 0px;
    padding-bottom: 7px;
    padding-left: 18px;
    padding-right: 23px;
}

.box {
    display: flow;
    border: 1px solid #000;
    margin: auto;
    padding: 15px;
    text-align: center;
    border-radius: 25px;
    margin-top: 30px;
    margin-left: 12px;
    margin-right: 12px;
}

button.pop {
    transform: scale(1.8);
    /* Increase size to 120% */
}

button.float {
    animation: float 0.5s infinite;
}

/* button.float {
    animation: float 2s ease-in-out infinite;
} */

@keyframes float {
    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-20px);
    }

    100% {
        transform: translateY(0px);
    }
}
</style>

<script>
import NavBar from '@/components/NavBar.vue'
import { ref } from 'vue';
import axios from 'axios';
import { useAuthStore } from '@/stores/authStore'

export default {
    components: {
        NavBar
    },
    data() {
        const store = useAuthStore()
        return {
            song: null,
            rating: 0,
            showRating: false,
            user_id: store.user.id,
            ratingExists: false,
            ratingId: null,
            accessToken: store.accessToken
            // newRating: null
        };
    },
    methods: {
        rateSong() {
            this.showRating = true;
        },
        fetchSongDetails() {
            const song_id = this.$route.params.id;
            axios.get(`http://127.0.0.1:5000/api/song/${song_id}`,
                { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
                .then(response => {
                    this.song = response.data;
                })
                .catch(error => {
                    console.log(error);
                });
        },
        fetchRatingDetails(song_id, user_id) {
            axios.get(`http://127.0.0.1:5000/api/ratings/${song_id}/${user_id}`,
                { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
                .then(response => {
                    if (response.data.length > 0) {
                        this.rating = response.data[0].rating;
                        this.ratingExists = true;
                        this.ratingId = response.data[0].id;
                    }
                })
                .catch(error => {
                    console.log(error);
                });
        },
        updateRating(newRating) {
            if (this.ratingExists && rating !== this.rating) {
                // If rating exists and new rating is different, make a PUT request
                axios.put(`http://127.0.0.1:5000/api/ratings/${this.ratingId}`, { song_id: this.song.id, user_id: this.user_id, rating: newRating },
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
                    .then(response => {
                        console.log('Rating updated successfully');
                    })
                    .catch(error => {
                        console.log(error);
                    });
            } else if (!this.ratingExists) {
                // If rating does not exist, make a POST request
                axios.post(`http://127.0.0.1:5000/api/ratings`, { song_id: this.song.id, user_id: this.user_id, rating: newRating },
                    { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
                    .then(response => {
                        console.log('Rating created successfully');
                        this.ratingExists = true;
                        this.ratingId = response.data.id;
                    })
                    .catch(error => {
                        console.log(error);
                    });
            }
        }

    },
    mounted() {
        const song_id = this.$route.params.id;
        this.fetchSongDetails(song_id);
        this.fetchRatingDetails(song_id, this.user_id);
    },
    watch: {
        rating: {
            handler() {
                try {
                    this.updateRating(this.rating);
                    setTimeout(() => {
                        this.showRating = false;
                    }, 3500);
                } catch (error) {
                    console.error('Error in watcher:', error);
                }
            },
            deep: true
        },
        '$route': 'fetchSongDetails'
    },
    setup() {
        const reactionIcons = ref([
            { icon: '👎', pop: false, float: false },
            { icon: '❤️', pop: false, float: false },
            { icon: '🔥', pop: false, floa: false },

        ]);

        const triggerAnimation = (index) => {
            reactionIcons.value[index].pop = true;
            reactionIcons.value[index].float = true;
            setTimeout(() => {
                reactionIcons.value[index].pop = false;
                reactionIcons.value[index].float = false;
            }, 500); // Reset after 500ms
        };

        return {
            reactionIcons,
            triggerAnimation,
        };
    },
};
</script>
