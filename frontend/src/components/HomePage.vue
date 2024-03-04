<script>
export default {
    name: 'JigglyCard',
}
</script>

<template>
    <div class="bg">
        <header>
            <div class="logo">
                <router-link to="/login/admin">
                    <img src="../assets/jiggly2.png" alt="Jiggly Logo" />
                </router-link>
            </div>
        </header>
        <main>
            <div class="content">
                <h1>Jiggly</h1>
                <h3> : Your Music Companion</h3>
                <p>Jiggly is a music player that allows you to listen to your favorite music on the go.</p>
            </div>
            <br>
            <div class="actions">
                <router-link to="/login">
                    <button type="button" class="btn btn-primary m-3">Sign In</button>
                </router-link>
                <router-link to="/register">
                    <button type="button" class="btn btn-secondary m-3">Sign Up</button>
                </router-link>
            </div>
        </main>
    </div>
</template>

<style scoped>
.bg {
        background-image: url('../assets/bg5.jpg');
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
img{
    width: 4%;
}
main {
    text-align: center;
    align-items: center;
    flex-direction: column;
    margin-top: 7rem;
    display: flex;
    justify-content: space-between;
    width: 100%;
}
.content {
    flex: 1;
    text-align: center;
}
.actions {
    flex: 1;
    display: flex;
    justify-content: space-evenly;
    align-items: center;
    padding-top: 5%;
}
h1, h3 {
    display: inline;
}
h1{
    background: -webkit-linear-gradient(315deg,#dc627c 25%,#647eff);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
h3{
    background: -webkit-linear-gradient(315deg,#647eff 25%,#dc627c);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
p{
    text-align: center;
}
</style>
