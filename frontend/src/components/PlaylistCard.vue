<template>
    <div class="card text-center" style="width: fit-content;">
        <div class="card-body">
            <div class="card-title">playlist.title</div>
            <div class="card-content">
                <router-link :to="`/user/playlist/playlist_name`" class="btn btn-info btn-sm">View Tracks</router-link>
            </div>
        </div>
    </div>
</template>


<style scoped>
.card {
    background-image: url('../assets/card/9.jpg');
    background-size: cover;
    border-radius: 25px;
    border: 1px solid aquamarine;
    margin-top: 12px;
}

.btn {
    background: cadetblue;
}

.card-title {
    color: darkturquoise;
}

.card-body {
    padding: 10px;
}
</style>


<script>
export default {
    name: 'PlaylistCard',
    data() {
        return {
            album: {
                title: '',
                id: ''
            }
        }
    }
}
</script>