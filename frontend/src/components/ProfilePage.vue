<template>
    <Navbar />
    <div class=" container">
        <div class="row-fluid">
            <div class="box overflow-auto">
                <img src="../assets/dp.jpg" alt="Profile Picture" class="dp">
                <h2>Username: {{ username }}</h2>
                <h6>Email: {{ email }}</h6>
                <button v-if="!showChangePasswordForm" @click="showChangePasswordForm = true">Change Password</button>
                <div v-if="showChangePasswordForm">
                    <input class="input-field" v-model="newPassword" type="password" placeholder="New Password"><br>
                    <input class="input-field" v-model="confirmPassword" type="password"
                        placeholder="Confirm Password"><br>
                    <div class="btn btn-primary btn-sm" @click="changePassword">Confirm</div> &nbsp;
                    <div class="btn btn-danger btn-sm" @click="showChangePasswordForm = false">Cancel</div>
                </div>
                <br>
                <h6 v-if="role !== 'User'" :class="{ 'blacklisted': blacklistStatus === 'Yes' }">Is Blacklisted: {{
                    blacklistStatus }}</h6>
                <button @click="confirmDeleteAccount">Delete Account</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.blacklisted {
    color: red;
    font-weight: bold;
}
.input-field {
    padding: 10px;
    margin: 5px;
    width: 30%;
    border-radius: 12px;
    border: 1px solid #ccc;
}
.overflow-auto {
    height: 84vh;
    overflow-y: auto;
}

.overflow-auto::-webkit-scrollbar {
    /* For Chrome, Safari, and Opera */
    width: 8px;
    border-radius: 100px;
}

.overflow-auto::-webkit-scrollbar-thumb {
    /* For Chrome, Safari, and Opera */
    background: #999;
    border-radius: 100px;
}
.dp{
    margin: 2%;
    /* margin-top: 3%; */
    /* width: 16%; */
    height: 30%;
    border-radius: 50%;
}
button {
    background-color: cadetblue;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    border-radius: 12px;
}
.btn{
    /* background-color: steelblue; */
    color: white;
    padding: 10px 15px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    border-radius: 12px;


}
.box {
    background-color: inherit;
    border: 1px solid #000;
    margin: auto;
    text-align: center;
    border-radius: 25px;
    margin-top: 20px;
    margin-bottom: 15px;
    margin-left: 12px;
    margin-right: 12px;
    padding-top: 7px;
    padding-left: 12px;
    padding-right: 12px;
    padding-bottom: 12px;
}
.row-fluid {
    /* display: flex; */
    flex-wrap: wrap;
    justify-content: space-around;
    align-content: center;
    align-items: center;
    margin-bottom: 20px;
    /* width: 70%; */
}
</style>

<script>
import { ref } from 'vue';
import Navbar from './NavBar.vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/authStore';
import axios from 'axios'; // Make sure to import axios

export default {
    components: {
        Navbar,
    },
    setup() {
        const store = useAuthStore();
        const username = store.user.username;
        const email = store.user.email;
        const role = store.user.role;
        const showChangePasswordForm = ref(false);
        const newPassword = ref('');
        const confirmPassword = ref('');
        const blacklistStatus = store.user.blacklisted ? 'Yes' : 'No';
        const accessToken = store.accessToken;
        const router = useRouter();

        const changePassword = async () => { 
            if (newPassword.value.length < 8 || newPassword.value.length > 16) {
                alert('Password must be between 8 to 16 characters long')
                return;
            }
            if (newPassword.value !== confirmPassword.value) {
                alert('Passwords do not match!');
                return;
            }
            try {
                const response = await axios.put(`http://127.0.0.1:5000/api/user/${store.user.id}`, {
                    password: newPassword.value,
                    username: username,
                    email: email,
                    role: role,
                },
                {
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                    },
                });
                showChangePasswordForm.value = false;
            } catch (error) {
                console.log(error);
            }
        };

        const confirmDeleteAccount = async () => {
            if (window.confirm('Are you sure you want to delete your account?')) {
                try {
                    const response = await axios.delete(`http://127.0.0.1:5000/api/user/${store.user.id}`, {
                        headers: {
                            'Authorization': `Bearer ${accessToken}`,
                        },
                    });
                    if (response.status === 200) {
                        await router.push('/');
                        store.logout();
                    }
                } catch (error) {
                    console.log(error);
                }
            }
        };

        return {
            role,
            username,
            email,
            showChangePasswordForm,
            newPassword,
            confirmPassword,
            blacklistStatus,
            changePassword,
            confirmDeleteAccount,
        };
    },
};
</script>
