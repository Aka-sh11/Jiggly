import { defineStore } from 'pinia';
import axios from 'axios';

export const useAuthStore = defineStore({
  id: 'auth',
  state: () => ({
    user: null,
    accessToken: localStorage.getItem('accessToken'),
    isLoggedIn: false,
  }),
  getters: {
    isUserLoggedIn() {
      return this.isLoggedIn;
    },
    userInfo(){
      return this.user;
    }
  },
  actions: {
    async login(username, password) {
      try {
        const response = await axios.post('http://127.0.0.1:5000/login', { username, password });
        if (response.status === 200) {
          this.user = response.data.user;
          this.accessToken = response.data.access_token;
          localStorage.setItem('accessToken', this.accessToken);
          this.isLoggedIn = true;
        }
      } catch (error) {
        alert('Error during login: '+ error.response.data);
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
          localStorage.removeItem('accessToken');
          this.isLoggedIn = false;
        }
      } catch (error) {
        console.error('Error during logout:', error);
      }
    },
    async fetchUserInfo() {
      if (this.accessToken) {
        try {
          const response = await axios.get('http://127.0.0.1:5000/fetchuserinfo', {
            headers: {
              'Authorization': `Bearer ${this.accessToken}`
            }
          });
          if (response.status === 200) {
            this.user = response.data.user;
            this.isLoggedIn = true;
          }
        } catch (error) {
          console.error('Error fetching user info:', error);
        }
      }
    },
  },
  },
);


