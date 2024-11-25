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
                    <span>Photo URL: {{ notification.photo_url }}</span>
                    <br />
                    <span>Photo URL: {{ notification.ocr_text }}</span>
                </li>
            </ul>
            <h1 v-else>No notifications yet...</h1>
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
// import { FileUpload } from 'primevue/fileupload';
// import { ProgressBar } from 'primevue/progressbar';
// import { Message } from 'primevue/message';
// import { Badge } from 'primevue/badge';

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
        // FileUpload,
        // ProgressBar,
        // Message,
        // Badge,
    },
    setup() {
        const route = useRoute();
        const userStore = userUserStore();
        const loggedInUser = computed(() => userStore.getUser);
        // console.log(route.matched[1])
        // console.log(route.name)
        // Reactive WebSocket state
        const { status, data: wsData, send, open, close } = useWebSocket(
            'ws://localhost:8001/ws/bill_notifications/'
        );

        const socket = new WebSocket("ws://localhost:8001/ws/bill_notifications/");
        console.log(socket)
        socket.onopen = () => {
            console.log('WebSocket connection established.');
        };

        socket.onerror = (error) => {
            console.error('WebSocket error:', error);
        };

        socket.onclose = () => {
            console.log('WebSocket connection closed.');
        };
        socket.onmessage = (event) => {
            console.log('Message received from server:', event.data);
            // Optionally parse the message if it's in JSON format
            const message = JSON.parse(event.data);
            console.log('Parsed message:', message);
        };
        // console.log(wsData.value)

        // Watch for changes in wsData
        watch(() => wsData.value, (newData) => {
            if (newData) {
                const event = JSON.parse(newData);
                notifications.value.push(event);
                console.log("Received notification:", event);
            }
        });

        // Parse WebSocket data into notifications
        const notifications = ref([]);
        wsData.value && notifications.value.push(JSON.parse(wsData.value));

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
            status, // WebSocket status (open, connecting, closed) 
        }
    },
    async created() {
        // console.log(localStorage.getItem("token"))

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
            const files = event.files; // Get the file to upload
            console.log("uashfkjhsdf")
            // Define the mutation for the file upload
            try {
                await files.forEach((file) => {
                    const response = this.$apollo.mutate({
                        mutation: Bill_IMAGE, // Your mutation for file upload
                        variables: {
                            userId: this.loggedInUser.id,
                            name: file.name,
                            description: file.name,
                            photo: file
                        },  // Send the file as a variable
                    });
                    console.log("Upload response:", response);
                })

                // Optionally, you can display a success message or update the UI
            } catch (error) {
                console.error("File upload failed:", error);
                // Handle error accordingly
            }
            console.log("the end")
        },
    }
};
</script>