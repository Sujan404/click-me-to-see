<template>
  <div v-if="!homePage" class="flex-direction-column">
    <div v-if="!loggedInUser">
      <h1>Hello, </h1>
      <div>
        <h1>I am home page of the portal before login</h1>
        <h1>Please create a account if you haven't or sign in if you have</h1>
      </div>

      <div class="m-5 text-center">
        <div>
          <router-link to="/signin" class="bg-teal-500 text-white mr-5 p-2 rounded-md">Sign In</router-link>
          <router-link to="/signup" class="bg-teal-500 text-white p-2 rounded-md">Sign Up</router-link>
        </div>

      </div>
    </div>
    <div v-else>
      <h1>You are logged into the application</h1>
      <a href="/user">Click here to go to portal</a>
      <!-- <button @click="logout" class="bg-teal-500 text-white p-2 rounded-md">Logout</button> -->
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
header {
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
  }
}
</style>

<script>
import { CURRENT_USER, SITE_INFO } from "@/queries";
import { apolloClient } from "@/apollo-config";
import { useRoute } from "vue-router";
import { useAppContentStatusStore } from "@/stores/appContentStatus"
import { computed } from 'vue';
import { userUserStore } from "@/stores/user"



export default {
  setup() {
    const route = useRoute();
    const userStore = userUserStore();

    const loggedInUser = computed(() => userStore.getUser);
    const homePage = computed(() => {
      return route.path === '/signin' || route.path === '/signup' || route.path === '/user' || route.path === '/user/profile';
    })
    return { homePage, loggedInUser, userStore, route }
  },
  data() {
    return {
      mySite: null,
    }
  },
  async created() {
    // if (this.loggedInUser){
    //   this.$router.push({name: "User"})
    // }
    // console.log(localStorage.getItem("token"))

    const siteInfo = await apolloClient.query({
      query: SITE_INFO
    }
    );
    this.mySite = siteInfo.data.site;

    console.log(this.loggedInUser)
  },
  methods: {
    async logout() {
      this.userStore.removeToken();
      this.userStore.removeUser();
      this.$router.push({ name: "SignIn" });
    }
  }
};
</script>