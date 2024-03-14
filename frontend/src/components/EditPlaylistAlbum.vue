<template>
    <NavBar />
    <form class="container-fluid" @submit.prevent="EditPlaylistAlbum">
        <div class="container">
            <div class="header">
                <h4>{{ heading }}</h4>
                <input v-model="playlistName" type="text" class="form-control" :placeholder='placeholder' />
            </div>
            <div class="centered">
                <input type="submit" class="btn btn-success" value="Edit" />
            </div>
        </div>
        <div class="blox">
            <div class="box-s" v-for="n in 15" :key="n">
                <div class="box-title">
                    <h6>song.titlehh</h6>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" :value="n" name="song_ids" checked />
                        <!-- if form value in playlist the checked -->
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

export default {
    name: 'EditPlaylistAlbum',
    components: {
        NavBar,
    },
    setup() {
        const Name = ref('')
        const router = useRouter()
        const route = useRoute()
        const heading = ref('')
        const placeholder = ref('')

        const EditPlaylistAlbum = async () => {
            // Call your API to create a edit playlist/album
            if (route.name === 'edit-playlist') {
                console.log(`Edited playlist: ${Name.value}`)
            } else if (route.name === 'edit-album') {
                console.log(`Edited album: ${Name.value}`)
            }
            // If form submission is successful, redirect to dashboard
            if (route.name === 'edit-playlist') {
                router.push('/user/dashboard')
            } else if (route.name === 'edit-album') {
                router.push('/creator/dashboard')
            }
        }
        onMounted(() => {
            if (route.name === 'edit-playlist') {
                heading.value = 'Edit Playlist'
                placeholder.value = 'Playlist.Name'
            } else if (route.name === 'edit-album') {
                heading.value = 'Edit Album'
                placeholder.value = 'Album.Name'
            }
        })

        return {
            Name,
            EditPlaylistAlbum,
            heading,
            placeholder
        }
    }
}

</script>
