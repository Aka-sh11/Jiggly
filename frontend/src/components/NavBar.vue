<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
            <img src="../assets/logo.png" alt="" width="30" height="24" class="d-inline-block align-text-top">
            <strong>My App</strong>
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
                <li class="nav-item">
                <router-link to="/userdashboard" class="nav-link">Dashboard</router-link>
                </li>
                <li class="nav-item">
                <router-link to="/usercreatorlogin" class="nav-link">Login</router-link>
                </li>
            </ul>
            </div>
        </div>
        </nav>
    </div>
</template>


<script>
export default {
  name: 'NavBar'
}
</script>