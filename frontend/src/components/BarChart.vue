<template>
    <div v-if="chartData">
        <Bar id="my-chart-id" style="width: 400px; height:400px" :options="options" :data="chartData" />
    </div>
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
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import axios from 'axios'
import { useAuthStore } from '@/stores/authStore'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    name: 'BarChart',
    components: { Bar },
    data() {
        const store = useAuthStore()
        return {
            chartData: null,
            user_id: store.user.id,
            accessToken: store.accessToken,
            chartOptions: {
                responsive: true
            },
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: 'Song Distribution'
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        }
    },
    async mounted() {
        let songs = await axios.get('http://127.0.0.1:5000/api/song',
            { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
        let ratings = await axios.get('http://127.0.0.1:5000/api/ratings',
            { headers: { 'Authorization': `Bearer ${this.accessToken}` } })
        let songRatings = {}

        ratings.data.forEach(rating => {
            let song = songs.data.find(song => song.id === rating.song_id)
            if (song) {
                if (!songRatings[song.title]) {
                    songRatings[song.title] = { total: 0, count: 0 }
                }
                songRatings[song.title].total += rating.rating
                songRatings[song.title].count++
            }
        })

        this.chartData = {
            labels: Object.keys(songRatings),
            datasets: [{
                label: 'Avg. Rating',
                data: Object.values(songRatings).map(rating => rating.total / rating.count),
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
