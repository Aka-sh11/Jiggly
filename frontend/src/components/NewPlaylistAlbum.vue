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
            <div class="box-s" v-for="song in Songs" :key="song.id">
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
import { useAuthStore } from '@/stores/authStore'


export default {
    components: {
        NavBar
    },
    setup() {
        const store = useAuthStore()
        const user_id = store.user.id
        const accessToken = store.accessToken
        const Name = ref('')
        const router = useRouter()
        const route = useRoute()
        const heading = ref('')
        const placeholder = ref('')
        const Songs = ref([])

        const fetchSongs = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/song',
                    { headers: { 'Authorization': `Bearer ${accessToken}` } })
                Songs.value = response.data // Update the songs array with the fetched data
                Songs.value.forEach(song => {
                    song.selected = false;
                })
            } catch (error) {
                console.error('Failed to fetch songs:', error)
            }
        }

        const createPlaylistAlbum = async () => {
            const selectedSongs = Songs.value.filter(song => song.selected).map(song => song.id)

            // Prepare the data for the POST request
            const Data = {
                name: Name.value,
                user_id: user_id,
                songs: selectedSongs
            }
            // Call your API to create a new playlist/album
            if (route.name === 'new-playlist') {
                try {
                    // Send the POST request to create the album
                    await axios.post('http://127.0.0.1:5000/api/playlist', Data,
                        { headers: { 'Authorization': `Bearer ${accessToken}` } })

                    // Redirect to the creator dashboard
                    router.push('/user/dashboard')
                } catch (error) {
                    console.error('Failed to create playlist:', error)
                }
            } else if (route.name === 'new-album') {
                try {
                    // Send the POST request to create the album
                    await axios.post('http://127.0.0.1:5000/api/album', Data,
                        { headers: { 'Authorization': `Bearer ${accessToken}` } })

                    // Redirect to the creator dashboard
                    router.push('/creator/dashboard')
                } catch (error) {
                    console.error('Failed to create album:', error)
                }
            }
        }
        onMounted(() => {
            fetchSongs()
            if (route.name === 'new-playlist') {
                heading.value = 'Create New Playlist'
                placeholder.value = 'Enter Playlist Name'
            } else if (route.name === 'new-album') {
                heading.value = 'Create New Album'
                placeholder.value = 'Enter Album Name'
            }
        })

        return {
            Name,
            createPlaylistAlbum,
            heading,
            placeholder,
            Songs
        }
    }
}
</script>