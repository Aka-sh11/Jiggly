<template>
    <NavBar />
    <div class="container">
        <div class="header">
            <h2>All Tracks</h2>
        </div>
        <div class="row-fluid">
            <div v-for="genre in genres" :key="genre.name" class="box">
                <div class="overflow-auto">
                    <div class="header">
                        <h6 style="color:crimson;">{{ genre.name }}</h6>
                    </div>
                    <div v-for="song in genre.songs" :key="song.id" class="box-s">
                        <div class="header">
                            <h6>{{ song.title }}</h6>
                            <ul class="nav">
                                <li class="nav-item">
                                    <router-link to="/songs/song_name" class="btn btn-info btn-sm">View
                                        Lyrics</router-link>
                                </li>
                                <li class="nav-item">
                                    <router-link to="#" class="btn btn-info btn-sm">Delete</router-link>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
@media only screen and (max-width: 600px) {
    .row-fluid {
        flex-direction: column;
    }
}

.row-fluid {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-content: center;
    align-items: center;
    margin-bottom: 20px;
}

.overflow-auto {
    height: 36vh;
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
}

.box {
    background-color: inherit;
    border: 1px solid #000;
    margin: auto;
    text-align: center;
    border-radius: 25px;
    margin-top: 20px;
    margin-bottom: 15px;
    margin-left: 12px;
    margin-right: 12px;
    padding-top: 7px;
    padding-left: 12px;
    padding-right: 12px;
    padding-bottom: 12px;
}

.box-s {
    background-color: gainsboro;
    border: 1px solid #000;
    margin: auto;
    text-align: center;
    border-radius: 25px;
    margin-top: 20px;
    margin-left: 12px;
    margin-right: 12px;
    padding-top: 7px;
    padding-left: 12px;
    padding-right: 12px;
    padding-bottom: 12px;
    display: flow;
}

.nav {
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

.btn {
    background: cadetblue;
    margin-left: 15px;
    margin-right: 15px;
}

.header {
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 8px;
}
</style>

<script>
import NavBar from './NavBar.vue'

export default {
    name: 'AdminTracks',
    components: {
        NavBar
    },
    data() {
        return {
            genres: [
                {
                    name: 'Genre 1',
                    songs: [
                        { id: 1, title: 'Song 1' },
                        { id: 2, title: 'Song 2' },
                        { id: 3, title: 'Song 3' },
                        { id: 4, title: 'Song 4' },
                    ],
                },
                {
                    name: 'Genre 2',
                    songs: [
                        { id: 3, title: 'Song 3' },
                        { id: 4, title: 'Song 4' },
                    ],
                },
                {
                    name: 'Genre 3',
                    songs: [
                        { id: 1, title: 'Song 1' },
                        { id: 2, title: 'Song 2' },
                        { id: 3, title: 'Song 3' },
                        { id: 4, title: 'Song 4' },
                    ],
                },
                {
                    name: 'Genre 1',
                    songs: [
                        { id: 1, title: 'Song 1' },
                        { id: 2, title: 'Song 2' },
                        { id: 3, title: 'Song 3' },
                        { id: 4, title: 'Song 4' },
                    ],
                },
                {
                    name: 'Genre 1',
                    songs: [
                        { id: 1, title: 'Song 1' },
                        { id: 2, title: 'Song 2' },
                        { id: 3, title: 'Song 3' },
                        { id: 4, title: 'Song 4' },
                    ],
                },
                {
                    name: 'Genre 1',
                    songs: [
                        { id: 1, title: 'Song 1' },
                        { id: 2, title: 'Song 2' },
                        { id: 3, title: 'Song 3' },
                        { id: 4, title: 'Song 4' },
                    ],
                },
                {
                    name: 'Genre 1',
                    songs: [
                        { id: 1, title: 'Song 1' },
                        { id: 2, title: 'Song 2' },
                        { id: 3, title: 'Song 3' },
                        { id: 4, title: 'Song 4' },
                    ],
                },
                {
                    name: 'Genre 1',
                    songs: [
                        { id: 1, title: 'Song 1' },
                        { id: 2, title: 'Song 2' },
                        { id: 3, title: 'Song 3' },
                        { id: 4, title: 'Song 4' },
                    ],
                },
            ],
        }
    },
}
</script>