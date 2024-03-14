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
                            <label for="file" class="form-label">File (.mp3 format)</label>
                            <input type="file" class="form-control" @change="handleFileUpload" accept=".mp3" required />
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

export default {
    components: {
        NavBar
    },
    setup() {
        const route = useRoute()
        const router = useRouter()
        const heading = ref('')
        const buttonText = ref('')
        const song = ref({
            title: '',
            date: '',
            file: null,
            singer: '',
            genre: '',
            lyrics: '',
        })

        onMounted(() => {
            if (route.name === 'upload-song') {
                heading.value = 'Upload Song'
                buttonText.value = 'Add'
            } else if (route.name === 'edit-song') {
                heading.value = 'Edit Song'
                buttonText.value = 'Edit'
                // Fetch the song data from your server and update `song.value`
                // The song data will be used as placeholder values in the form
                // Use dummy data for testing
                song.value = {
                    title: 'Test Song',
                    date: '2024-03-14',
                    file: null,
                    singer: 'Test Singer',
                    genre: 'Test Genre',
                    lyrics: 'Test Lyrics',
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
            handleFileUpload(event) {
                song.value.file = event.target.files[0]
            },
            async uploadSong() {
                // Handle the form submission here
                // You can use the `fetch` API or a library like `axios` to send the form data to your server
                // You should wait for the server response before redirecting
                // Here's a dummy promise to simulate waiting for the server response
                await new Promise(resolve => setTimeout(resolve, 500))
                router.push('/creator/dashboard')
            }
        }
    },
}
</script>