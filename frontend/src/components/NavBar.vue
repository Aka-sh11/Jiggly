<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">
                    <img src="../assets/jiggly2.png" alt="" width="30" height="24"
                        class="d-inline-block align-text-top">
                    <strong>Jiggly</strong>
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <div class="input-group">
                                <input v-model="query" type="search" name="search" class="form-control"
                                    style="width: 120px; margin:0px;height:31px; padding: 5px 2px 5px 5px; margin-right: 4px;"
                                    placeholder=" Search    🔍" @keypress.enter="search" />
                                <!-- <div v-if="filteredResults.length" class="dropdown">
                                    <a v-for="result in filteredResults" :key="result.id" class="dropdown-item"
                                        @click="router.push(`/song/${result.id}`)">{{ result.title }}</a>
                                </div> -->
                                <div class="dropdown" v-if="filteredResults.length">
                                    <div class="dropdown-menu show" aria-labelledby="dropdownMenuButton">
                                        <a class="dropdown-item" v-for="result in filteredResults" :key="result.id"
                                            @click="router.push(`/song/${result.id}`)">{{ result.title }}</a>
                                    </div>
                                </div>
                                <div class="dropdown" v-if="!filteredResults.length && searchPerformed">
                                    <div class="dropdown-menu show" aria-labelledby="dropdownMenuButton">
                                        <a class="dropdown-item">No results found</a>
                                    </div>
                                </div>
                            </div>
                        </li> <strong>⚕️</strong>
                        <li class="nav-item" v-if="user.role === 'Admin'">
                            <router-link to="/admin/dashboard" class="nav-link">Dashboard</router-link>
                        </li>
                        <li class="nav-item" v-if="user.role === 'User'">
                            <router-link to="/user/dashboard" class="nav-link">Dashboard</router-link>
                        </li>
                        <li class="nav-item" v-if="user.role === 'Creator'">
                            <router-link to="/creator/dashboard" class="nav-link">Dashboard</router-link>
                        </li><strong>⚕️</strong>
                        <li class="nav-item" v-if="user.role === 'User'">
                            <router-link to="/user/profile" class="nav-link">Profile</router-link>
                        </li>
                        <li class="nav-item" v-if="user.role === 'Creator'">
                            <router-link to="/creator/profile" class="nav-link">Profile</router-link>
                        </li><strong v-if="user.role !== 'Admin'">⚕️</strong>
                        <li class="nav-item">
                            <router-link to="/" class="nav-link">Logout</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</template>


<style scoped>
.dropdown {
    position: absolute;
    display: block;
    margin: 30%;


}

.dropdown-menu {
    position: relative;
    min-width: 160px;
    z-index: 1;
    box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
    background-color: inherit;
    ;
}

.dropdown-item {
    /* background-color: inherit; */
    color: rgb(12, 12, 12);
}

.dropdown:hover .dropdown-menu {
    display: block;
}

.navbar {
    background: -webkit-linear-gradient(315deg, #dc627c 25%, #647eff);
    padding-top: 0.4%;
    padding-bottom: 0.4%;
}

strong {
    background: -webkit-linear-gradient(109.6deg, rgba(48, 207, 208, 1) 11.2%, rgb(218, 63, 153) 92.5%);
    background-clip: text;
    -webkit-background-clip: text;
    -moz-background-clip: text;
    -moz-text-fill-color: transparent;
    -webkit-text-fill-color: transparent;
    filter: brightness(1.85);
}

#navbarNav {
    justify-content: flex-end;
}

a {
    color: cornsilk;
    /* height: 40px; */
    align-items: center;
}

.navbar-nav {
    align-items: center;
}
</style>

<script>
import { ref, computed, watch } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';

export default {
    name: 'NavBar',
    setup() {
        let user = ref({
            role: 'Admin',
            // role: 'User',
            // role: 'Creator' // This should be set based on the logged in user's role
        });
        let query = ref('');
        let results = ref([]);
        let searchPerformed = ref(false);

        let router = useRouter();

        let search = async () => {
            try {
                // Send a GET request to the /search endpoint with the query as a parameter
                let response = await axios.get('http://127.0.0.1:5000/search', { params: { search: query.value } });

                // Update the results with the data received from the server
                results.value = response.data.song_results;
                searchPerformed.value = true;
            } catch (error) {
                console.error(error);
            }
        };

        let filteredResults = computed(() => {
            if (!query.value) return [];
            return results.value.filter(result => result.title.toLocaleLowerCase().includes(query.value.toLocaleLowerCase()));
        });

        watch(query, (newQuery) => {
            // If the new query is empty, set searchPerformed to false
            if (!newQuery) {
                searchPerformed.value = false;
            }
        });

        // Return these variables so they can be used in your component
        return {
            user,
            query,
            results,
            router,
            search,
            filteredResults,
            searchPerformed
        };
    }
}
</script>
