<template>
    <NavBar />
    <div class="box-m">
        <div class="overflow-auto">
            <div class="box">
                <div class="header">
                    <h2>song.title</h2>
                    <nav>
                        <button class="btn btn-info btn-sm" @click="rateSong"
                            style="background-color: cadetblue;">Rate</button>

                        <div v-if="showRating">
                            <input type="range" id="rating" v-model.number="rating" min="0" max="5">
                            <span>{{ rating }}</span>
                        </div>
                    </nav>
                </div>
                <h6>song.singer | song.date[: 4]</h6>
                <audio controls>
                    <source :src="`/static/audio/song.filename`" type="audio/mpeg" />
                </audio>
                <div class="box" style="background-color: gainsboro;">
                    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Possimus voluptatibus expedita eligendi
                        voluptas, cum aliquid hic voluptatem asperiores. Ad aperiam doloribus nulla repudiandae qui
                        alias nemo minus natus eveniet delectus.</p>
                </div>
                <br />
                <div class="emoji" v-for="(item, index) in items" :key="index">
                    <button @click="animate(index)" :class="{ pop: item.pop, float: item.float }"
                        style="font-size: 1.2rem;">
                        {{ item.icon }}
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
nav {
    display: flex;
    justify-content: flex-end;
    align-items: center;

}

.emoji {
    display: inline-flex;
    justify-content: flex-end;
}

button {
    /* font-size: 1.2rem; */
    padding: 8px;
    /* margin: 5px; */
    border: none;
    background: none;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}

.overflow-auto {
    height: 80vh;
    overflow-y: auto;
}

.overflow-auto::-webkit-scrollbar {
    /* For Chrome, Safari, and Opera */
    width: 8px;
}

.overflow-auto::-webkit-scrollbar-thumb {
    /* For Chrome, Safari, and Opera */
    background: #999;
}

h2,
h6 {
    margin: 0 auto;
    text-align: left;
    margin-left: 0px;
    color: deeppink;
}

h6 {
    color: mediumorchid;
}

.header {
    display: flex;
    justify-content: center;
    align-items: center;
}

.box-m {
    padding-top: 0px;
    padding-bottom: 7px;
    padding-left: 18px;
    padding-right: 23px;
}

.box {
    display: flow;
    border: 1px solid #000;
    margin: auto;
    padding: 15px;
    text-align: center;
    border-radius: 25px;
    margin-top: 30px;
    margin-left: 12px;
    margin-right: 12px;
}

button.pop {
    transform: scale(1.8);
    /* Increase size to 120% */
}

button.float {
    animation: float 0.5s infinite;
}

/* button.float {
    animation: float 2s ease-in-out infinite;
} */

@keyframes float {
    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-20px);
    }

    100% {
        transform: translateY(0px);
    }
}
</style>

<script>
import NavBar from '@/components/NavBar.vue'
import { ref } from 'vue';

export default {
    components: {
        NavBar
    },
    data() {
        return {
            rating: 0,
            showRating: false,
        };
    },
    methods: {
        rateSong() {
            this.showRating = true;
        },
    },
    watch: {
        rating() {
            setTimeout(() => {
                this.showRating = false;
            }, 1000);
        }
    },
    setup() {
        const items = ref([
            { icon: '👍', pop: false, float: false },
            { icon: '❤️', pop: false, float: false },
            { icon: '🔥', pop: false, floa: false },
            { icon: '👎', pop: false, float: false },
            { icon: '😍', pop: false, float: false },
        ]);

        const animate = (index) => {
            items.value[index].pop = true;
            items.value[index].float = true;
            setTimeout(() => {
                items.value[index].pop = false;
                items.value[index].float = false;
            }, 500); // Reset after 500ms
        };

        return {
            items,
            animate,
        };
    },
};

</script>```
