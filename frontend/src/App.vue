<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from './stores/authStore';

const store = useAuthStore();

store.fetchUserInfo();
</script>

<template>

  <RouterView />
</template>

<style scoped>
</style>
