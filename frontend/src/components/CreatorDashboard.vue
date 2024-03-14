<template>
    <NavBar />
    <div class="container">
        <div class="row">
            <div class="box" style="display: unset">
                <div class="heading">
                    <h3 style="text-align: left; -webkit-text-fill-color: black;">Statisitics</h3>
                </div>
                <div class="row" style="padding-top: 8px">
                    <div class="col">
                        <em>Total Songs Uploaded</em> <br /><br />
                        <em>
                            <p>{{ current_user.songs.length }}</p>
                        </em>
                    </div>
                    <div class="col">
                        <em>Average Rating</em><br /><br />
                        <em>
                            <p>{{ average }}</p>
                        </em>
                    </div>
                    <div class="col">
                        <em>Total Albums</em><br /><br />
                        <p>{{ current_user.albums.length }}</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="row-fluid">
            <div class="col-fluid">
                <div class="box-header">
                    <h3 style="text-align: left; -webkit-text-fill-color: black;">Songs</h3>
                    <ul class="nav">
                        <li class="nav-item">
                            <router-link to="/creator/songs/upload" class="btn btn-primary btn-sm"
                                style="background: steelblue">Upload Song</router-link>
                        </li>
                    </ul>
                </div>
                <div class="row">
                    <div class="overflow-auto">
                        <div v-for="song in current_user.songs" :key="song.id" class="box"
                            style="margin-top: 15px; background-color: gainsboro; flex-direction: column;">
                            <div class="header">
                                <h5>song.title</h5>
                                <ul class="nav">
                                    <li class="nav-item">
                                        <router-link :to="'/songs/song_name'" class="btn btn-info btn-sm">View
                                            Lyrics</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link :to="'/creator/songs/song_name/edit'"
                                            class="btn btn-info btn-sm">Edit</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link :to="'/songs/song_name/delete' + song.id"
                                            class="btn btn-info btn-sm">Delete</router-link>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-fluid">
                <div class="box-header">
                    <h3 style="text-align: left; -webkit-text-fill-color: black;">Albums</h3>
                    <ul class="nav">
                        <li class="nav-item">
                            <router-link to="/creator/album/create" class="btn btn-primary btn-sm"
                                style="background: steelblue">Create Album</router-link>
                        </li>
                    </ul>
                </div>
                <div class="row">
                    <div class="overflow-auto">
                        <div v-for="album in current_user.albums" :key="album.id" class="box"
                            style="margin-top: 15px; background-color: gainsboro; flex-direction: column;">
                            <div class="header">
                                <h5>album.name</h5>
                                <ul class="nav">
                                    <li class="nav-item">
                                        <router-link :to="'/album/album_name'" class="btn btn-info btn-sm">View
                                            Tracks</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link :to="'/creator/album/album_name/edit'"
                                            class="btn btn-info btn-sm">Edit</router-link>
                                    </li>
                                    <li class="nav-item">
                                        <router-link :to="'/delete_album/' + album.id"
                                            class="btn btn-info btn-sm">Delete</router-link>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.header {
    display: flex;
    justify-content: center;
    align-items: center;
}

h3,
h5 {
    margin: 0 auto;
    text-align: left;
    margin-left: 0px;
}

@media only screen and (max-width: 600px) {
    .row-fluid {
        flex-direction: column;
    }
}

.btn {
    margin-left: 15px;
    margin-right: 15px;
    background: cadetblue;
}

.overflow-auto {
    height: 32vh;
    overflow-y: auto;
}

.overflow-auto::-webkit-scrollbar {
    /* For Chrome, Safari, and Opera */
    width: 8px;
}

.overflow-auto::-webkit-scrollbar-thumb {
    /* For Chrome, Safari, and Opera */
    background: #999;
}

.nav {
    display: flex;
    align-items: center;
    justify-content: flex-end;
}

.box-header {
    display: flex;
    justify-content: center;
    align-items: center;
}

.row-fluid {
    display: flex;
}

.col-fluid {
    border: 1px solid #000;
    margin: auto;
    padding: 10px;
    text-align: center;
    border-radius: 25px;
    padding-bottom: 0px;

}

.row {
    margin-bottom: 20px;
}

.box {
    display: flex;
    border: 1px solid #000;
    margin: auto;
    padding: 20px;
    text-align: center;
    border-radius: 25px;
    margin-top: 10px;
}

.col {
    background-color: gainsboro;
    border: 1px solid #000;
    margin: auto;
    padding: 10px;
    text-align: center;
    border-radius: 25px;
    margin-left: 15px;
    margin-right: 15px;
    padding-bottom: 0px;
}
</style>

<script>
import NavBar from './NavBar.vue'

export default {
    name: 'CreatorDashboard',
    components: {
        NavBar
    },
    data() {
        return {
            current_user: {
                songs: [1, 2, 3, 4], // This should be set based on the logged in user's songs
                albums: [1, 2, 3, 4], // This should be set based on the logged in user's albums
            },
            average: 0, // This should be set based on the average rating
        };
    },
}

</script>