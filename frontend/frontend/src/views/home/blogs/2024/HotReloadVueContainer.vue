<template>
    <div>
        <div class="mb-3">
            <NavBar />
        </div>
        <div class="max-w-screen-xl mx-auto p-4 sm:p-6 xl:p-8">
            <h1 class="text-3xl">
                Hot reload the Vue
                with Vite inside docker container
            </h1>
            <div class="grid justify-items-center my-5">
                <img :src="imgUrl" class="text-center">
            </div>
            <h1 class="text-xl font-bold">Vue</h1>
            <h2 class="text-lg my-3">
                It is an open-source model-view-viewmodel front end JavaScript framewoork for building user interfaces
                and single-page applications. It is designed to be flexible and incrementally adoptable.
            </h2>
            <h1 class="text-xl font-bold">Vite</h1>
            <h2 class="text-lg my-3">
                Vite is a frontend tool that is used for building fast and optimized web applications.
                It uses a modern build system and a fast development server to provide a streamlined and efficient
                developement experience.
                Vite uses navtive ES modules and rollup to compile and optimize your code for production, resulting in
                faster build times and
                smaller bundle sizes.
            </h2>
            <h1 class="text-xl font-bold">Hot Reload</h1>
            <h2 class="text-lg my-3">
                Hot reloading is a feature that allows developers to see changes in their code immediately without
                needing to refresh the page manually.
            </h2>
            <h1 class="text-xl font-bold">Links provides indepth information</h1>
            <h2 class="text-lg my-3">
                <a href="https://medium.com/@kbooster17/how-to-fix-hot-reloading-not-working-in-vite-generated-reactjs-applications-85baea2e7659"
                    target="_blank">Hot reload in vite generated reatjs</a>
            </h2>
            <h2 class="text-lg my-3">
                <a href="https://vite.dev/config/server-options.html" target="_blank">Vite official site</a>
            </h2>
            <h2 class="text-lg my-3">
                <a href="https://www.youtube.com/watch?v=ZCLRgor-WZ8" target="_blank">Hot reload for vue</a>
            </h2>
            <h1 class="text-xl font-bold">Add following additional code to vite.config.js for WSL</h1>
            <pre class="my-3">
              
    export default defineConfig({
        server: {
            watch: {
            usePolling: true, // Enables polling for file changes for WSL
            },
        },
    })
            </pre>
        </div>
        <Footer />
    </div>
</template>

<script setup>
import imgUrl from "@/assets/images/vite-docker-vue.png";
import NavBar from "@/views/home/Navigation.vue";
import Footer from "@/views/home/Footer.vue";
</script>