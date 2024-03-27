<template>
    <NavBar />
    <form class="container-fluid" @submit.prevent="createPlaylistAlbum">
        <div class="container">
            <div class="header">
                <h4>{{ heading }}</h4>
                <input v-model="Name" type="text" class="form-control" :placeholder='placeholder' required />
            </div>
            <div class="centered">
                <input type="submit" class="btn btn-success" value="Create" />
            </div>
        </div>
        <div class="blox">
            <div class="box-s" v-for="song in songs" :key="song.id">
                <div class="box-title">
                    <h6>{{ song.title }}</h6>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" v-model="song.selected" />
                    </div>
                </div>
            </div>
        </div>
    </form>
</template>

<style scoped>
.container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.btn {
    background-color: lightseagreen;
}

.card {
    background: none;
    border: none;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.box-s {
    background-color: gainsboro;
    /* background-image: url('../assets/card/6.jpg'); */
    background-size: cover;
    border: 1px solid #000;
    margin: auto;
    text-align: center;
    border-radius: 25px;
    margin-top: 20px;
    margin-left: 12px;
    margin-right: 12px;
    /* padding-top: 12px; */
    padding-left: 25px;
    padding-right: 15px;
    /* padding-bottom: 12px; */
    display: flow;
}

.centered {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    height: 22vh;
    padding-right: 150px;
    margin-right: 15px;
}

.box-title {
    display: flex;
    justify-content: space-between;
    padding-top: 10px;
    padding-bottom: 6px;
}

.form-check {
    width: 22px;
    height: 22px;
    padding-left: 35px;
}

.blox {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    max-height: 350px;
    overflow-y: auto;
}

input {
    text-align: center;
    background-color: azure;
}

.header {
    display: inline-flex;
    align-items: center;
    padding-top: 6px;
    padding-bottom: 4px;
    text-align: center;
    background-color: cornflowerblue;
    color: white;
    border-radius: 10px;
    margin-top: 15px;
    margin-bottom: 15px;
    padding-inline-end: inherit;
}
</style>

<script>
import NavBar from '@/components/NavBar.vue'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

export default {
    components: {
        NavBar
    },
    data() {
        return {
            songs: [],
            Name: ''
        }
    },
    created() {
        this.fetchSongs()
    },
    methods: {
        async fetchSongs() {
            try {
                const response = await axios.get('http://localhost:5000/api/song')
                this.songs = response.data.map(song => ({ ...song, selected: false }))
            } catch (error) {
                alert(error)
            }
        },
        async createPlaylistAlbum() {
            const songIds = this.songs.filter(song => song.selected).map(song => song.id)
            const data = {
                name: this.Name,
                song_ids: songIds,
                user_id: 6
            }

            if (this.$route.name === 'new-playlist') {
                console.log(`Creating new playlist: ${this.Name}`)
            } else if (this.$route.name === 'new-album') {
                console.log(`Creating new album: ${this.Name}`)
                try {
                    const response = await axios.post('http://127.0.0.1:5000/api/album', data)
                    console.log(response.data)
                } catch (error) {
                    alert(error)
                }
            }

            if (this.$route.name === 'new-playlist') {
                this.$router.push('/user/dashboard')
            } else if (this.$route.name === 'new-album') {
                this.$router.push('/creator/dashboard')
            }
        }
    },
    setup() {
        const router = useRouter()
        const route = useRoute()
        const heading = ref('')
        const placeholder = ref('')

        onMounted(() => {
            if (route.name === 'new-playlist') {
                heading.value = 'Create New Playlist'
                placeholder.value = 'Enter Playlist Name'
            } else if (route.name === 'new-album') {
                heading.value = 'Create New Album'
                placeholder.value = 'Enter Album Name'
            }
        })

        return {
            heading,
            placeholder
        }
    }
}
</script>