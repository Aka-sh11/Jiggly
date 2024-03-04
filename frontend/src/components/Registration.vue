<template>
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-6 justify-content-center">
          <div class="logo">
            <img src="../assets/jiggly2.png" alt="Jiggly Logo" />
          </div>
          <div class="card md-5">
            <div class="card-body">
              <h3 class="card-title text-center">Registration</h3>
            <form @submit.prevent="register">
                <div class="form-group">
                    <label for="username">Username</label>
                    <input type="text" class="form-control" id="username" v-model="username" required>
                    <label for="email">Email</label>
                    <input type="email" class="form-control" id="email" v-model="email" required>
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" v-model="password" required>
                    <label for="confirmPassword">Confirm Password</label>
                    <input type="password" class="form-control" id="confirmPassword" v-model="confirmPassword" required>
                    <label for="role">Role</label><br>
                    <div class="role-container">
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="role" id="creator" value="creator" v-model="role" required>
                            <label class="form-check-label" for="creator">Creator</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="role" id="user" value="user" v-model="role" required>
                            <label class="form-check-label" for="user">User</label>
                        </div>
                    </div>
                </div>
                <button type="submit" class="btn btn-primary">Register</button>
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
  background: -webkit-linear-gradient(315deg, #dc627c 25%, #647eff);
}

img {
  width: 15%;
}

.logo {
  padding: 3%;
  display: flex;
  justify-content: center;
}

.card-body {
  background: aliceblue;
  border-radius: 25px;
}
.role-container {
  display: flex;
  justify-content: space-evenly;
}
</style>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  setup() {
    const username = ref('')
    const email = ref('')
    const password = ref('')
    const confirmPassword = ref('')
    const role = ref('')

    const register = async () => {
        // Check if username is between 4 to 10 characters long
      if (username.value.length < 4 || username.value.length > 10) {
        console.log('Username must be between 4 to 10 characters long')
        return
  }

      // Check if password is between 8 to 16 characters long
      if (password.value.length < 8 || password.value.length > 16) {
        console.log('Password must be between 8 to 16 characters long')
        return
  }
      // Check if password and confirm password fields match
      if (password.value !== confirmPassword.value) {
        console.log('Passwords do not match')
        return
      }

      // If they match, send a request to the server
      try {
        const response = await axios.post('/api/register', {
          username: username.value,
          email: email.value,
          password: password.value,
          role: role.value
        })
        console.log(response.data)
        // Navigate to login page
        this.$router.push('/login')
      } catch (error) {
        console.log(error)
      }
    }

    return {
      username,
      email,
      password,
      confirmPassword,
      role,
      register
    }
  }
}

</script>