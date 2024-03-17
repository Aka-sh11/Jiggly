<!-- migrate to vue-chartjs from chartjs -->
<template>
    <div>
        <canvas ref="chart"></canvas>
    </div>
</template>

<style scoped>
canvas {
    background: whitesmoke;
    width: 800px;
    height: 350px;
    padding-bottom: 10px;
    border-radius: 15px;
}
</style>

<script>
import { ref, onMounted } from 'vue';
import { Chart, LinearScale, BarController, CategoryScale, BarElement } from 'chart.js';

Chart.register(LinearScale);
Chart.register(BarController);
Chart.register(CategoryScale);
Chart.register(BarElement);


export default {
    name: 'GraphChart',
    setup() {
        const chart = ref(null);

        onMounted(() => {
            chart.value = new Chart(chart.value.getContext('2d'), {
                type: 'bar',
                data: {
                    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                    datasets: [{
                        label: '# of Votes',
                        data: [12, 19, 3, 5, 2, 3],
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
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        });

        return { chart };
    }
};
</script>
