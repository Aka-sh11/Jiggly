<template>
    <NavBar />
    <form class="container-fluid" @submit.prevent="EditPlaylist">
        <div class="container">
            <div class="header">
                <h4>Edit Playlist</h4>
                <input v-model="playlistName" type="text" class="form-control" placeholder="Playlist.Name" />
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'

export default {
    name: 'EditPlaylistAlbum',
    components: {
        NavBar,
    },
    setup() {
        const playlistName = ref('')
        const router = useRouter()

        const EditPlaylist = async () => {
            // Call your API to create a new playlist
            console.log(`Edit playlist: ${playlistName.value}`)
            // If form submission is successful, redirect to /user/dashboard
            router.push('/user/playlist/playlist_name')
        }

        return {
            playlistName,
            EditPlaylist
        }
    }
}

</script>
