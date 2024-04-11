<template>
    <Navbar />
    <h2>All Albums</h2>
    <div class="col">
        <AlbumCard v-for="album in albums.sort((a, b) => a.name.localeCompare(b.name))" :key="album"
            :album="album.id" />
    </div>
</template>

<style scoped>
.col {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding-top: 10px;
}
h2 {
    text-align: center;
    margin-top: 5px;
    color: chocolate;
}
</style>

<script>
import Navbar from '@/components/NavBar.vue'
import AlbumCard from '@/components/AlbumCard.vue'
import { useAuthStore } from '@/stores/authStore'
import axios from 'axios'

export default {
    components: {
        Navbar, AlbumCard
    },
    data() {
        const store = useAuthStore()
        return {
            user_id: store.user.id,
            accessToken: store.accessToken,
            albums: []
        }
    },
    methods: {
        async loadAlbums() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/album',
                    {
                        headers: { 'Authorization': `Bearer ${this.accessToken}` }
                    });
                    this.albums = response.data;
            }
            catch (error) {
                console.error(error);
            }
        },
    },
    mounted() {
        this.loadAlbums();
    }
}

</script>