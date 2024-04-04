<template>
    <NavBar />
    <form class="container-fluid" @submit.prevent="EditPlaylistAlbum">
        <div class="container">
            <div class="header">
                <h4>{{ heading }}</h4>
                <input v-model="Name" type="text" class="form-control" :placeholder='placeholder' required />
            </div>
            <div class="centered">
                <input type="submit" class="btn btn-success" value="Edit" />
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
    padding-left: 12px;
    padding-right: 12px;
    /* padding-bottom: 12px; */
    display: flow;
}

.centered {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    height: 22vh;
    padding-right: 150px;
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
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import { useAuthStore } from '@/stores/authStore'

export default {
    name: 'EditPlaylistAlbum',
    components: {
        NavBar,
    },
    setup() {
        const store = useAuthStore()
        const Name = ref('')
        const router = useRouter()
        const route = useRoute()
        const heading = ref('')
        const placeholder = ref('')
        const Songs = ref([])
        const user_id = store.user.id
        const param = route.params.id
        const accessToken = store.accessToken

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

        const EditPlaylistAlbum = async () => {
            const selectedSongs = Songs.value.filter(song => song.selected).map(song => song.id)
            if (selectedSongs.length === 0) {
                alert('Must have at least one song.')
                return
            }
            // Call your API to create a edit playlist/album
            if (route.name === 'edit-playlist') {
                try {
                    // const selectedSongs = Songs.value.filter(song => song.selected).map(song => song.id)
                    const response = await axios.put(`http://127.0.0.1:5000/api/playlist/${param}`, {
                        name: Name.value,
                        user_id: user_id,
                        songs: selectedSongs
                    }, { headers:{ 'Authorization': `Bearer ${accessToken}`} })
                    console.log(response.data)
                } catch (error) {
                    alert('Failed to edit playlist:', error)
                }
            } else if (route.name === 'edit-album') {
                try {
                    // const selectedSongs = Songs.value.filter(song => song.selected).map(song => song.id)
                    const response = await axios.put(`http://127.0.0.1:5000/api/album/${param}`, {
                        name: Name.value,
                        user_id: user_id,
                        songs: selectedSongs
                    },
                    { headers:{ 'Authorization': `Bearer ${accessToken}`} })
                    console.log(response.data)
                } catch (error) {
                    alert('Failed to edit album:', error)
                }
            }
            // If form submission is successful, redirect to dashboard
            if (route.name === 'edit-playlist') {
                router.push('/user/dashboard')
            } else if (route.name === 'edit-album') {
                router.push('/creator/dashboard')
            }
        }
        onMounted(async () => {
            await fetchSongs()
            if (route.name === 'edit-playlist') {
                heading.value = 'Edit Playlist'
                placeholder.value = 'Playlist Name'
                try {
                    const response = await axios.get(`http://127.0.0.1:5000/api/playlist/${param}`,
                        { headers: { 'Authorization': `Bearer ${accessToken}` } })
                    const playlistSongs = response.data.songs
                    Name.value = response.data.name
                    Songs.value.forEach(song => {
                        if (playlistSongs.includes(song.id)) {
                            song.selected = true
                        }
                    })
                } catch (error) {
                    console.error('Failed to fetch album songs:', error)
                }
            } else if (route.name === 'edit-album') {
                heading.value = 'Edit Album'
                placeholder.value = 'Album Name'
                try {
                    const response = await axios.get(`http://127.0.0.1:5000/api/album/${param}`,
                        { headers: { 'Authorization': `Bearer ${accessToken}` } })
                    const albumSongs = response.data.songs
                    Name.value = response.data.name
                    Songs.value.forEach(song => {
                        if (albumSongs.includes(song.id)) {
                            song.selected = true
                        }
                    })
                } catch (error) {
                    console.error('Failed to fetch album songs:', error)
                }
            }
        })

        return {
            Name,
            EditPlaylistAlbum,
            heading,
            placeholder,
            Songs
        }
    }
}

</script>
