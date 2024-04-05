<template>
    <Pie v-if="chartData" id="my-chart-id" style="width: 400px; height:400px" :options="options" :data="chartData" />
</template>

<style scoped>
#my-chart-id {
    background: whitesmoke;
    width: 400px;
    height: 500px;
    padding-bottom: 10px;
    border-radius: 15px;
}
</style>

<script>
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale } from 'chart.js'
import axios from 'axios'
import { useAuthStore } from '@/stores/authStore'

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale, LinearScale)

export default {
    name: 'PieChart',
    components: { Pie },
    data() {
        const store = useAuthStore()
        return {
            user_id: store.user.id,
            accessToken: store.accessToken,
            chartData: null,
            chartOptions: {
                responsive: true
            },
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Genre Distribution'
                    }
                },
            }
        }
    },
    async created() {
        const response = await axios.get('http://127.0.0.1:5000/api/song',
            { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
        const songs = response.data
        const genreCounts = songs.reduce((acc, song) => {
            acc[song.genre] = (acc[song.genre] || 0) + 1
            return acc
        }, {})
        this.chartData = {
            labels: Object.keys(genreCounts),
            datasets: [{
                data: Object.values(genreCounts),
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 2
            }]
        }
    }
}
</script>