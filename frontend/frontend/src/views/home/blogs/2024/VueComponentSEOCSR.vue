<template>
    <div>

        <Head>
            <title>SEO for vue components Client Side Rendering(CSR)</title>
            <meta name="og:description" content="SEO for vue components Client Side Rendering (CSR)">
            <meta name="og:keywords"
                content="Software Engineer, Docker, HTML, CSS, Python, Vue, JavaScript, Bastion Host Architecture">
        </Head>
        <div class="mb-3">
            <NavBar />
        </div>
        <div class="max-w-screen-xl mx-auto p-4 sm:p-6 xl:p-8">
            <h1 class="text-3xl">
                SEO for vue components Client Side Rendering (CSR)
            </h1>
            <h2 class="text-lg my-3">
                Search Engine Optimization (SEO) for Vue components is essential when creating Single Page Applications (SPAs) in 
                Vue because it ensures that search engines and social media platforms can index and understand your content, which can be challenging for SPAs.
            </h2>
            <h2 class="text-lg my-3 font-bold">
                What is Client Side Rendering (CSR)?
            </h2>
            <h2 class="text-lg my-3">
                Client-side rendering (CSR) is a web development technique where, upon the user’s initial request, the server delivers only the static files 
                (HTML, CSS, and JavaScript) to the browser. The browser first loads the HTML and then downloads JavaScript, which generates the content dynamically on the client side. 
                Initially, users may see loading symbols until the JavaScript fully executes, making the website interactive and visible as users navigate and engage with the content. 
            </h2>
            <h1 class="text-xl font-bold">Technical Details</h1>
            <h1 class="text-lg my-3">There is <a href="https://unhead.unjs.io/" target="_blank">unjs/unhead</a> package available to manage head tags.</h1>
            <h1 class="text-xl font-bold my-3">Step 1: Install @unhead/vue dependency to your project</h1>
            <h1 class="text-lg my-3">npm install @unhead/vue</h1>
            <h1 class="text-xl font-bold my-3">Step 2: Register the Vue plugin in src/main.js</h1>
            <pre class="mt-3">
import { createApp } from "vue";
import router from "./router";
const head = createHead()
const app = createApp();

app.use(head).use(router).mount("#app");
            </pre>
            <h1 class="text-xl font-bold">Step 3: After you registered, use <span class="font-bold text-rose-500">useHead</span> in the components</h1>
            <h1 class="text-xl my-3">Options API: Just add script like shown bottom then it will automatically update in &lt;head&gt;&lt;/head&gt; tag.</h1>
            <pre class="my-3">
&lt;script&gt;
import { useHead } from '@unhead/vue'
    export default {
    setup() {
        useHead({
        title: "Add meta tags",
        meta: [
            {
            name: "og:description",
            content: "I am adding description meta tag for SEO.",
            },
            {
            name: "og:keywords",
            content: "Vue, Composition API, Client Side Rendering.",
            },
        ],
        });
    }
&lt;/script&gt;
            </pre>
            <h1 class="text-xl my-3">Composition API: It is slightly different form Options API </h1>
            <pre class="my-3">
&lt;template&gt;
    &lt;Head>
        &lt;title>Add meta tags&lt;/title>
        &lt;meta name="og:description" content="I am adding description meta tag for SEO.">
        &lt;meta name="og:keywords" content="Vue, Composition API, Client Side Rendering">
    &lt;/Head>
&lt;/template&gt;
                
&lt;script&gt;
    import { Head } from '@unhead/vue/components'
&lt;/script&gt;
</pre>

            <h1 class="text-xl font-bold">Bottom link provides in-depth information</h1>
            <h2 class="text-lg my-3">
                <a href="https://unhead.unjs.io/setup/vue/installation"
                    target="_blank">Add meta tags in vue components</a>
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
