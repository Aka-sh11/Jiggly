import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    user: null,
    accessToken: localStorage.getItem('accessToken'),
    isLoggedIn: false,
    // role: null,
  }),
  actions: {
    async login(username, password) {
      try {
        const response = await axios.post('http://127.0.0.1:5000/login', { username, password });
        if (response.status === 200) {
          this.user = response.data.user;
          this.accessToken = response.data.access_token;
        //   this.role = response.data.user.role;
          localStorage.setItem('accessToken', this.accessToken);
          this.isLoggedIn = true;
        }
      } catch (error) {
        console.error('Error during login:', error);
      }
    },
    async logout() {
      try {
        const response = await axios.post('http://127.0.0.1:5000/logout', {}, {
          headers: {
            'Authorization': `Bearer ${this.accessToken}`
          }
        });
        if (response.status === 200) {
          this.user = null;
          this.accessToken = null;
          // this.role = null;
          localStorage.removeItem('accessToken');
          this.isLoggedIn = false;
        }
      } catch (error) {
        console.error('Error during logout:', error);
      }
    },
    async fetchUserInfo() {
      try {
        const response = await axios.get('http://127.0.0.1:5000/fetchuserinfo', {
          headers: {
            'Authorization': `Bearer ${this.accessToken}`
          }
        });
        if (response.status === 200) {
          this.user = response.data.user;
        //   this.role = response.data.user.role;
        }
      } catch (error) {
        console.error('Error fetching user info:', error);
      }
    },
  },
});


