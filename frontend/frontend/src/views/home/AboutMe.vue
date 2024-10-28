<template>
    <div>
        <div class="max-w-screen-xl mx-auto text-center">
            <div class="p-4 sm:p-6 xl:p-8">
                <div class="flex flex-wrap justify-center my-5">
                <img :src="imgUrl" class="text-center rounded-full">
            </div>
                <div>
                    <h1 class="md:text-5xl text-4xl lg:mt-20 md:mt-10 mt-5 text-green-600">
                        Hello, I am Sujan Ale, Software Engineer.
                    </h1>

                    <h2 class="text-lg my-2 text-orange-600">
                        I am an enthusiastic nerd who is always thriving to learn new things.
                        I have started this website to share my learnings that I have learnt so far and will be trying
                        my
                        best
                        to explicitly include my challenges and its overcomed ways in the blog.
                    </h2>
                </div>
            </div>
        </div>
        <div class="h-36 text-center flex flex-wrap justify-center bg-gray-100 my-12">
            <h1 class="md:text-5xl text-4xl my-6 text-blue-700 flex flex-wrap items-center">Things I have learnt</h1>
        </div>

        <div class="max-w-screen-xl mx-auto flex flex-wrap justify-around">
            <div class="max-w-sm p-6 border border-gray-200 rounded-lg shadow bg-gray-100 dark:border-gray-700">
                <a href="#">
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Bastion Host
                        Architecture</h5>
                </a>
                <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">Bastion Host architeture provides secured
                    access to resources in a private subnet without exposing them directly to the internet.</p>
                <router-link :to="{ name: 'BastionHost' }"
                    class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Read more
                    <svg class="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 5h12m0 0L9 1m4 4L9 9" />
                    </svg>
                </router-link>
            </div>
            <div class="max-w-sm p-6 border border-gray-200 rounded-lg shadow bg-gray-100 dark:border-gray-700">
                <a href="#">
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Why is docker so
                        popular?</h5>
                </a>
                <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">Docker is used to package applications into
                    containers. The container container all the dependencies required by an application
                    to run.
                </p>
                <router-link :to="{ name: 'Docker' }"
                    class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Read more
                    <svg class="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 5h12m0 0L9 1m4 4L9 9" />
                    </svg>
                </router-link>
            </div>
            <div class="max-w-sm p-6 border border-gray-200 rounded-lg shadow bg-gray-100 dark:border-gray-700">
                <a href="#">
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Hot reload the Vue
                        with Vite inside docker container</h5>
                </a>
                <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">Hot reload has been a manadotory tool for
                    saving time and smooth workflow for developers.</p>
                <router-link :to="{ name: 'HotReloadVueContainer' }"
                    class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Read more
                    <svg class="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 5h12m0 0L9 1m4 4L9 9" />
                    </svg>
                </router-link>
            </div>
            <div class="max-w-sm p-6 border border-gray-200 rounded-lg shadow bg-gray-100 dark:border-gray-700">
                <a href="#">
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">CSS Flex importance
                    </h5>
                </a>
                <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">Bastion Host architeture provides secured
                    access to resources in a private subnet without exposing them directly to the internet</p>
                <router-link :to="{ name: 'CssFlex' }"
                    class="inline-flex items-center px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    Read more
                    <svg class="rtl:rotate-180 w-3.5 h-3.5 ms-2" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                        fill="none" viewBox="0 0 14 10">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            d="M1 5h12m0 0L9 1m4 4L9 9" />
                    </svg>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script setup>
import imgUrl from "@/assets/images/me/sujan.png";
</script>

