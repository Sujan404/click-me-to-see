<template>
    <div>

        <Head>
            <title>Vue catch all /404 Not Found Route</title>
            <meta name="og:description" content="Vue catch all /404 Not Found Route">
            <meta name="og:keywords"
                content="Software Engineer, Docker, HTML, CSS, Python, Vue, JavaScript, Bastion Host Architecture">
        </Head>
        <div class="mb-3">
            <NavBar />
        </div>
        <div class="max-w-screen-xl mx-auto p-4 sm:p-6 xl:p-8">
            <h1 class="text-3xl">
                Vue catch all /404 Not Found Route
            </h1>
            <p id="read-text">2024-10-25 | 2 min read</p>
            <h2 class="text-lg my-3">
                It is quite common that we sometimes forget to handle undefined routes. If we do not handle undefined
                routes, it does not causes error but it results in empty blank page.
                Instead displaying empty blank page, it is good to display anything meaningful contents.
            </h2>
            <h2 class="text-lg my-3">
                For example: content not found or the route is not defined.
            </h2>
            <h1 class="text-xl font-bold">Technical Details</h1>
            <h1 class="text-xl font-bold my-3">Step 1: Create new component and give any name. For my case, I have
                created NotFound.vue</h1>
            <pre class="my-3">

&lt;template &gt;
    &lt;div class="flex flex-col min-h-screen w-full"&gt;
        &lt;div class="flex flex-col flex-grow justify-center mx-auto p-4 sm:p-6 xl:p-8"&gt;
            &lt;h1 class="text-3xl">Oops! The page you are looking for does not exist.&lt;/h1&gt;
            &lt;router-link class="text-xl" to="/">Go back to Home&lt;/router-link&gt;
        &lt;/div&gt;
    &lt;/div/&gt;
&lt;/template&gt;
            </pre>
            <h1 class="text-xl font-bold my-3">Step 2: Import that component in src/router/index.js</h1>
            <pre class="my-3">
import { createRouter, createWebHistory } from 'vue-router'
import RouteNotFound from '@/views/home/NotFound.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
  // Catch-all route for undefined paths
     {
      path: '/:pathMatch(.*)*',
      name: 'RouteNotFound',
      component: RouteNotFound
    },
  ]
})
            </pre>
            <h1 class="my-3">'/:pathMatch(.*)*' => This custom param regexp will match everything and if the route is
                not found then will redirect to the NotFound.vue.</h1>

            <h1 class="text-xl font-bold">Bottom link provides in-depth information</h1>
            <h2 class="text-lg my-3">
                <a href="https://router.vuejs.org/guide/essentials/dynamic-matching.html#Catch-all-404-Not-found-Route"
                    target="_blank">Catch all / 404 Not found Route</a>
            </h2>
        </div>
        <Footer />
    </div>
</template>
<script setup>
import NavBar from "@/views/home/Navigation.vue";
import Footer from "@/views/home/Footer.vue";
import { Head } from '@unhead/vue/components'
</script>
