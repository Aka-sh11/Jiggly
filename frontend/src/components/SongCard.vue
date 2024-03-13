<template>
    <div class="card text-center" style="width: fit-content;">
        <div class="card-body">
            <div class="card-title">song.title</div>
            <div class="card-content">
                <audio controls>
                    <source :src="`/static/audio/${song.filename}`" type="audio/mpeg">
                </audio>
                <br />
                <router-link :to="`/song/song_name`" class="btn btn-info btn-sm">Read Lyrics</router-link>
            </div>
        </div>
    </div>
</template>


<style scoped>
.card {
    background-image: url('../assets/card/19.jpg');
    background-size: cover;
    border-radius: 25px;
    border: 1px solid magenta;
    margin-top: 12px;
    margin-bottom: 12px;
}

.card-title {
    color: deeppink;
}

.card-body {
    padding: 10px;
}

audio {
    width: 255px;
}
</style>


<script>
export default {
    name: 'SongCard',
    data() {
        return {
            song: {
                title: '',
                filename: '',
                id: ''
            }
        }
    }
}
</script>