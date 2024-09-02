<template>
    <div class="flex-direction-column">
        <div>
            <h1>Hello, </h1>
            <h1 v-if="loggedInUser">Welcome {{ loggedInUser.username }}</h1>
        </div>
        <div class="m-5 text-center">
            <div if="loggedInUser">
                <button @click="logout" class="bg-teal-500 text-white p-2 rounded-md">Logout</button>
            </div>
        </div>
        <div>
            <ul
                class="flex flex-wrap text-sm font-medium text-center text-gray-500 border-b border-gray-200 dark:border-gray-700 dark:text-gray-400">
                <li class="me-2">
                    <!-- may need @click.native in future -->
                    <router-link to="/user/profile" aria-current="page"
                     @click="setActive('profile')"
                       :class="{active:isActive('profile')}"
                        class="inline-block p-4 hover:text-gray-600  hover:bg-gray rounded-t-lg dark:hover:bg-gray-800 dark:hover:text-gray-300">Profile</router-link>
                </li>
                <!--  -->
                <li class="me-2">
                    <router-link to="/user/post"
                    @click="setActive('post')"
                       :class="{active:isActive('post')}"
                    class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Post</router-link>
                </li>
                <li class="me-2">
                    <router-link to="#"
                    @click="setActive('settings')"
                       :class="{active:isActive('settings')}"
                        class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Settings</router-link>
                </li>
                <li class="me-2">
                    <router-link to="#"
                     @click="setActive('contacts')"
                       :class="{active: activeLink === 'contacts'}"
                        class="inline-block p-4 rounded-t-lg hover:text-gray-600 hover:bg-gray-50 dark:hover:bg-gray-800 dark:hover:text-gray-300">Contacts</router-link>
                </li>
                <li>
                    <a
                        class="inline-block p-4 text-gray-400 rounded-t-lg cursor-not-allowed dark:text-gray-500">Disabled</a>
                </li>
            </ul>
        </div>
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

    <RouterView />
</template>

<style scoped>
.active{
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
import { CURRENT_USER, SITE_INFO } from "@/queries";
import { apolloClient } from "@/apollo-config";
import { useRoute } from "vue-router";
import { useAppContentStatusStore } from "@/stores/appContentStatus"
import { computed, ref } from 'vue';
import { userUserStore } from "@/stores/user"

export default {
    data() {
        return {
            mySite: null,
            activeLink : null,
        }
    },
    setup() {
        const route = useRoute();
        const userStore = userUserStore();
        const loggedInUser = computed(() => userStore.getUser);
        // console.log(route.matched[1])
        console.log(route.name)
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
        return { homePage, loggedInUser, userStore, route, isActive}
    },
    async created() {
        // console.log(localStorage.getItem("token"))

        const siteInfo = await apolloClient.query({
            query: SITE_INFO
        }
        );
        this.mySite = siteInfo.data.site;
    },
    methods: {
        setActive(link) {
            this.activeLink = link;  // Set the active link state when a link is clicked
        },
        async logout() {
            this.userStore.removeToken();
            this.userStore.removeUser();
            this.$router.push({ name: "SignIn" });
        }
    }
};
</script>