<template>
    <NavBar />
    <div class="container">
        <div class="header">
            <h2>All Albums</h2>
        </div>
        <div class="row-fluid">
            <div class="box">
                <div class="overflow-auto">
                    <div v-for="album in sortedAlbums" :key="album.id" class="box-s">
                        <div class="header">
                            <h6>{{ album.name }}</h6>
                            <ul class="nav">
                                <li class="nav-item">
                                    <router-link to="/album/album_name" class="btn btn-info btn-sm">View
                                        Tracks</router-link>
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
    /* display: flex; */
    flex-wrap: wrap;
    justify-content: space-around;
    align-content: center;
    align-items: center;
    margin-bottom: 20px;
    /* width: 70%; */
}

.overflow-auto {
    height: 70vh;
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
    display: inline-flex;
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
    name: 'AdminAlbums',
    components: {
        NavBar
    },
    data() {
        return {
            albums: [
                { id: 1, name: 'Album 1' },
                { id: 2, name: 'Album 2' },
                { id: 3, name: 'Album 3' },
                { id: 4, name: 'Album 4' },
                { id: 5, name: 'Album 5' },
                { id: 6, name: 'Album 6' },
                { id: 7, name: 'Album 7' },
                { id: 8, name: 'Album 8' },
                { id: 9, name: 'Album 9' },
                { id: 10, name: 'Album 10' },
                // Add more albums here
            ],
        }
    },
    computed: {
        sortedAlbums() {
            // eslint-disable-next-line vue/no-side-effects-in-computed-properties
            return this.albums.sort((a, b) => a.name.localeCompare(b.name));
        },
    },
}
</script>