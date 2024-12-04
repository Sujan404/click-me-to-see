<template>
    <div class="flex flex-col min-h-screen w-full">
        <Navbar />
        <div class="flex flex-col flex-grow justify-center mx-auto">
            <div class="flex justify-between p-4 sm:p-6 xl:p-8">
                <div>
                    <h1 class="text-3xl">Hello, </h1>
                    <h1 class="text-3xl" v-if="loggedInUser">Welcome {{ loggedInUser.username }}</h1>
                    <div class="my-4">
                        <h1 class="text-3xl">The page will be functionable soon. Keep visiting this site.</h1>
                        <h1 class="text-3xl my-4"> 🙏 Thank you</h1>
                    </div>
                </div>

                <!-- <div class="m-5 text-center">
                <div if="loggedInUser">
                    <button @click="logout" class="bg-teal-500 text-white p-2 rounded-md">Logout</button>
                </div>
            </div> -->
            </div>
            <!-- <div class="flex flex-direction-column">
                <ul
                    class="flex flex-wrap text-sm font-medium text-center text-gray-500 dark:border-gray-700 dark:text-gray-400">
                    <li class="me-2"> -->
            <!-- may need @click.native in future -->
            <!-- <router-link to="/user/profile" aria-current="page" @click="setActive('profile')"
                            :class="{ active: isActive('profile') }"
                            class="inline-block p-4 hover:text-gray-600  hover:bg-gray rounded-t-lg dark:hover:bg-gray-800 dark:hover:text-gray-300">Profile</router-link>
                    </li> -->
            <!--  -->
            <!-- <li class="me-2">
                        <router-link to="/user/post" @click="setActive('post')" :class="{ active: isActive('post') }"
                            class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Post</router-link>
                    </li>
                    <li class="me-2">
                        <router-link to="#" @click="setActive('settings')" :class="{ active: isActive('settings') }"
                            class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Settings</router-link>
                    </li>
                    <li class="me-2">
                        <router-link to="#" @click="setActive('contacts')"
                            :class="{ active: activeLink === 'contacts' }"
                            class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Contacts</router-link>
                    </li>
                    <li>
                        <a
                            class="inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500">Disabled</a>
                    </li>
                </ul>
            </div> -->
            <!-- <RouterView /> -->

            <div
                class="relative items-center block p-6 bg-white border border-gray-100 rounded-lg shadow-md dark:bg-gray-800 dark:border-gray-800 dark:hover:bg-gray-700">
                <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white opacity-20">Noteworthy
                    technology acquisitions 2021</h5>
                <p class="font-normal text-gray-700 dark:text-gray-400 opacity-20">Here are the biggest enterprise
                    technology acquisitions of 2021 so far, in reverse chronological order.</p>
                <div class="card flex flex-col items-center gap-6">
                    <FileUpload mode="advanced" @select="onFileSelect" @uploader="onFileUpload" customUpload
                        accept="image/*" :multiple="true" severity="secondary" class="p-button-outlined" />
                    <img v-if="src" :src="src" alt="Image" class="shadow-md rounded-xl w-full sm:w-64"
                        style="filter: grayscale(100%)" />
                </div>
                <h1 class="text-3xl">WebSocket Notifications:</h1>
                <ul v-if="notifications.length > 0">
                    <li v-for="(notification, index) in notifications" :key="index">
                        <span>Event: {{ notification.event }}</span>
                        <br />
                        <span>Bill ID: {{ notification.bill_id }}</span>
                        <br />
                        <span>Image URL: <a :href="this.backendServer + notification.photo_url" target="_blank">{{
                            this.backendServer + notification.photo_url }}</a></span>
                        <br />
                        <span>Image text: {{ notification.ocr_text }}</span>
                    </li>
                </ul>
                <h1 v-else>No notifications yet...</h1>
                <div role="status" class="absolute -translate-x-1/2 -translate-y-1/2 top-2/4 left-1/2"
                    :class="{ invisible: !showSpinner }">
                    <svg aria-hidden="true" class="w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
                        viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                            fill="currentColor" />
                        <path
                            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                            fill="currentFill" />
                    </svg>
                    <span class="sr-only">Loading...</span>
                </div>
            </div>
        </div>
        <Footer />
    </div>

    <!-- <header>
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
  
      <div class="wrapper">
        <HelloWorld msg="You did it!" />
        <h1 class="text-3xl font-bold underline text-blue-600/100">Hello world!</h1>
  
        <nav>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">Aboout</RouterLink>
          <RouterLink to="/" v-if="mySite">{{mySite.name}}</RouterLink>
        </nav>
      </div>
    </header> -->

</template>

<style scoped>
.active {
    background-color: rgb(77, 70, 70);
    color: white;
}

/* header {
    line-height: 1.5;
    max-height: 100vh;
}

.logo {
    display: block;
    margin: 0 auto 2rem;
}

nav {
    width: 100%;
    font-size: 12px;
    text-align: center;
    margin-top: 2rem;
}

nav a.router-link-exact-active {
    color: var(--color-text);
}

nav a.router-link-exact-active:hover {
    background-color: transparent;
}

nav a {
    display: inline-block;
    padding: 0 1rem;
    border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
    border: 0;
}

@media (min-width: 1024px) {
    header {
        display: flex;
        place-items: center;
        padding-right: calc(var(--section-gap) / 2);
    }

    .logo {
        margin: 0 2rem 0 0;
    }

    header .wrapper {
        display: flex;
        place-items: flex-start;
        flex-wrap: wrap;
    }

    nav {
        text-align: left;
        margin-left: -1rem;
        font-size: 1rem;

        padding: 1rem 0;
        margin-top: 1rem;
    } */
/* } */
</style>

<script>
import { BILL_IMAGE_INFO, SITE_INFO } from "@/queries";
import { useWebSocket } from "@vueuse/core";
import { apolloClient } from "@/apollo-config";
import { useRoute } from "vue-router";
import { Bill_IMAGE } from "@/mutations"
import { computed, ref, watch } from 'vue';
import { userUserStore } from "@/stores/user"
import Navbar from "@/views/home/Navigation.vue"
import Footer from "@/views/home/Footer.vue"

export default {
    data() {
        return {
            billInfo: {},
            backendServer: import.meta.env.VITE_BACKEND_SERVER,
            mySite: null,
            activeLink: null,
            src: null,
        }
    },
    components: {
        Navbar,
        Footer,
    },
    setup() {
        
        const notifications = ref([]);
        const route = useRoute();
        const userStore = userUserStore();
        const loggedInUser = computed(() => userStore.getUser);
        const { status, data: wsData, send, open, close } = useWebSocket(
            'ws://localhost:8001/ws/bill_notifications/'
        );
        const showSpinner = ref(false);
        // Watch for changes in wsData
        watch(() => wsData.value, (newData) => {
            if (newData) {
                const event = JSON.parse(newData);
                notifications.value.push(event);
                showSpinner.value = false;
            }
        });

        const isActive = (linkName) => {
            return route.name && route.name.toLowerCase() === linkName.toLowerCase();
        }
        // if(route.matched[1] != undefined){
        //     routeName = route.matched[1].name.toLowerCase() // this is doing to add active class on the active link
        // }
        // console.log( route.matched[1].name.toLowerCase())
        const homePage = computed(() => {
            return route.path === '/signin' || route.path === '/signup';
        })
        return {
            homePage, loggedInUser, userStore, route, isActive, notifications,
            send, // Expose WebSocket methods for potential use
            open,
            close,
            status,
            showSpinner // WebSocket status (open, connecting, closed) 
        }
    },
    async created() {
        const siteInfo = await this.$apollo.query({
            query: SITE_INFO
        }
        );
        this.mySite = siteInfo.data.site;

        const billImageInfo = await this.$apollo.query({
            query: BILL_IMAGE_INFO
        });
        this.billInfo = billImageInfo.data.allBillImageInfo
    },
    methods: {
        setActive(link) {
            this.activeLink = link;  // Set the active link state when a link is clicked
        },
        async logout() {
            this.userStore.removeToken();
            this.userStore.removeUser();
            this.$router.push({ name: "SignIn" });
        },
        onFileSelect(event) {
            const file = event.files[0];
            const reader = new FileReader();

            reader.onload = async (e) => {
                this.src = e.target.result;
            };

            reader.readAsDataURL(file);
        },
        async onFileUpload(event) {
            this.showSpinner = true;
            const files = event.files; // Get the file to upload
            // Define the mutation for the file upload
            try {
                await files.forEach((file) => {
                    const response = this.$apollo.mutate({
                        mutation: Bill_IMAGE, 
                        variables: {
                            userId: this.loggedInUser.id,
                            name: file.name,
                            description: file.name,
                            photo: file
                        },
                    });
                    console.log("Upload response:", response);
                })
            } catch (error) {
                console.error("File upload failed:", error);
            }
            console.log("the end")
        },
    }
};
</script>