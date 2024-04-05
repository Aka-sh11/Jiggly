import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import './assets/main.css'
import { useAuthStore } from "./stores/authStore";

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

const pinia = createPinia()
const app = createApp(App)

app.use(pinia)
app.use(router)

const store = useAuthStore()

app.mount('#app')
