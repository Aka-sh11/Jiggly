<template>
    <NavBar />

    <div class="container">
        <div class="card">
            <div class="card-title text-center">
                <h3>{{ heading }}</h3>
            </div>
            <div class="card-content">
                <form @submit.prevent="uploadSong">
                    <div class="row">
                        <div class="col">
                            <label for="title" class="form-label">Title</label>
                            <input class="form-control" type="text" :value="song.title"
                                @input="updateSong('title', $event.target.value)" placeholder="Song Name" required />
                            <label for="date" class="form-label">Release Date</label>
                            <input class="form-control" type="date" :value="song.date"
                                @input="updateSong('date', $event.target.value)" placeholder="Date" required />
                            <label for="filename" class="form-label">File (.mp3 format)</label>
                            <input type="file" class="form-control" @change="onFileChange" accept=".mp3" required />
                        </div>
                        <div class="col">
                            <label for="singer" class="form-label">Singer</label>
                            <input class="form-control" type="text" :value="song.singer"
                                @input="updateSong('singer', $event.target.value)" placeholder="Singer Name" required />
                            <label for="genre" class="form-label">Genre</label>
                            <input class="form-control" type="text" :value="song.genre"
                                @input="updateSong('genre', $event.target.value)" placeholder="Song Genre" required />
                        </div>
                        <div class="row" style="padding-left: 20px">
                            <label for="lyrics" class="form-label">Lyrics</label>
                            <textarea class="form-control" :value="song.lyrics"
                                @input="updateSong('lyrics', $event.target.value)" placeholder="Enter song lyrics here"
                                required style="height: 80px; width: 100%"></textarea>
                        </div>
                    </div>
                    <div class="text-center">
                        <button type="submit" class="btn btn-primary" style="margin-top: 10px; margin-bottom: 10px">
                            {{ buttonText }}
                        </button>

                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<style scoped>
.card {
    border-radius: 15px;
    background: aliceblue;
    margin-top: 25px;
}

.card-body {
    background: aliceblue;
    border-radius: 25px;
}

.row {
    padding-left: 20px;
}

h3 {
    height: 40px;
    background: -webkit-linear-gradient(109.6deg, rgba(48, 207, 208, 1) 11.2%, rgb(218, 63, 153) 92.5%);
}

/* .col {
    padding-right: 20px;
} */

form {
    margin-left: 15px;
    margin-right: 20px;
}

.form-label {
    margin-top: 0.5rem;
    margin-bottom: 0.1rem;
}

.btn {
    margin-left: 15px;
    margin-right: 15px;
    background: cadetblue;
}
</style>

<script>
import NavBar from './NavBar.vue'
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

export default {
    components: {
        NavBar
    },
    setup() {
        const route = useRoute()
        const router = useRouter()
        const heading = ref('')
        const buttonText = ref('')
        const songId = route.params.id
        const song = ref({
            title: '',
            date: '',
            filename: null,
            singer: '',
            genre: '',
            lyrics: '',
        })
        const originalSong = ref(null)

        onMounted(async () => {
            if (route.name === 'upload-song') {
                heading.value = 'Upload Song'
                buttonText.value = 'Add'
            } else if (route.name === 'edit-song') {
                heading.value = 'Edit Song'
                buttonText.value = 'Edit'
                // Fetch the song data from your server and update `song.value`
                try {
                    const response = await axios.get(`http://127.0.0.1:5000/api/song/${songId}`);
                    if (response.status === 200) {
                        song.value = response.data; // update song data with response
                        originalSong.value = { ...response.data }
                    } else {
                        alert('There was an error fetching the song details');
                    }
                } catch (error) {
                    alert(error.response.data);
                }
            }
        })

        const updateSong = (field, value) => {
            song.value[field] = value
        }

        return {
            heading,
            song,
            updateSong,
            buttonText,
            onFileChange(event) {
                song.value.filename = event.target.files[0].name
            },
            async uploadSong() {
                const formData = new FormData()
                Object.keys(song.value).forEach(key => {
                    formData.append(key, song.value[key])
                })

                // Append the dummy userId to the form data
                const dummyUserId = 6; // replace with your dummy user ID
                formData.append('user_id', dummyUserId)

                try {
                    let response;
                    if (route.name === 'edit-song') {

                        // Check if any changes have been made
                        if (JSON.stringify(song.value) !== JSON.stringify(originalSong.value)) {
                            // If it's an edit and changes have been made, make a PUT request
                            response = await axios({
                                method: 'put',
                                url: `http://127.0.0.1:5000/api/song/${songId}`,
                                data: formData,
                                headers: { 'Content-Type': 'application/json' }
                            })
                        } else {
                            alert('Please make some changes before submitting');
                            return;
                        }
                    } else {
                        // Otherwise, make a POST request
                        response = await axios({
                            method: 'post',
                            url: 'http://127.0.0.1:5000/api/song',
                            data: formData,
                            headers: { 'Content-Type': 'application/json' }
                        })
                    }

                    if (response.status === 200) {
                        router.push('/creator/dashboard')
                    } else {
                        // Handle the error
                        alert('There was an error uploading the song')
                    }
                } catch (error) {
                    alert(error.response.data)
                }
            }



        }
    },
}
</script>