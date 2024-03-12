<template>
    <div class="card text-center" style="width: fit-content;">
        <div class="card-body">
            <div class="card-title">album.title</div>
            <div class="card-content">
                <router-link :to="`/user/album/${album.id}`" class="btn btn-info btn-sm">View Tracks</router-link>
            </div>
        </div>
    </div>
</template>


<style scoped>
.card {
    background-image: url('../assets/card/2.jpg');
    background-size: cover;
    border-radius: 25px;
    border: 1px solid magenta;
}

.card-title {
    color: deeppink;
}

.card-body {
    padding: 10px;
}
</style>


<script>
export default {
    name: 'AlbumCard',
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