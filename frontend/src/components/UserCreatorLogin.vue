<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-6 justify-content-center">
        <div class="logo">
          <img src="../assets/jiggly2.png" alt="Jiggly Logo" />
        </div>
        <div class="card md-5">
          <div class="card-body">
            <h3 class="card-title text-center">Login</h3>
            <form @submit.prevent="loginUser">
              <div class="form-group">
                <label for="username">Username</label>
                <input type="text" class="form-control" id="username" v-model="username" required>
                <label for="password">Password</label>
                <input type="password" class="form-control" id="password" v-model="password" required>
              </div>
              <button type="submit" class="btn btn-primary">Login</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  border: 1px;
  border-radius: 25px;
}

button {
  margin-top: 2%;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

h3 {
  height: 40px;
  /* background: -webkit-linear-gradient(315deg, #dc627c 25%, #647eff); */
  background: -webkit-linear-gradient(109.6deg, rgba(48, 207, 208, 1) 11.2%, rgb(218, 63, 153) 92.5%);
}

img {
  width: 18%;
}

.logo {
  padding: 8%;
  display: flex;
  justify-content: center;
}

.card-body {
  background: aliceblue;
  border-radius: 25px;
}
</style>

<script>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/authStore' 
import { useRouter } from 'vue-router'

export default {
  name: 'LoginForm',
  setup() {
    const username = ref('')
    const password = ref('')
    const store = useAuthStore()
    const router = useRouter()

    const loginUser = async () => {
      try {
        await store.login(username.value, password.value)

        if (store.isLoggedIn) {
          // Check the user's role and redirect them to the appropriate dashboard
          if (store.user.role === 'User') {
            router.push('/user/dashboard')
          } else if (store.user.role === 'Creator') {
            router.push('/creator/dashboard')
          }
        } else {
          // Handle error, e.g. show an error message
          console.error('Login failed')
        }
      } catch (error) {
        // Handle error, e.g. show an error message
        alert('Login Failed, ' + error.response.data)
      }
    }
    return {
      username,
      password,
      loginUser
    }
  }
}
</script>
