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
                                    style="width: 120px; margin:0px;height:31px;" placeholder="Search" />
                                <button class="btn btn-info btn-sm" @click="search"
                                    style="height: 31px; padding: 0px; background-color: lightblue; margin-right:15px;">🔍</button>
                                <div v-if="filteredResults.length" class="dropdown">
                                    <div v-for="result in filteredResults" :key="result.id" class="dropdown-item">
                                        <router-link :to="`/songs/${result.name}`">{{ result.name }}</router-link>
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
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

export default {
    name: 'NavBar',
    data() {
        return {
            user: {
                // role: 'Admin',
                // role: 'User',
                role: 'Creator' // This should be set based on the logged in user's role
            }
        }
    },
    setup() {
        let query = ref('');
        let results = ref([
            // Your results here
        ]);

        let router = useRouter();

        let search = () => {
            // Your search function here
        };

        let filteredResults = computed(() => {
            if (!query.value) return [];
            return results.value.filter(result => result.name.includes(query.value));
        });

        // Return these variables so they can be used in your component
        return {
            query,
            results,
            router,
            search,
            filteredResults
        };
    }
}
</script>
