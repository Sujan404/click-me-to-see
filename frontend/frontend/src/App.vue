<template>
  <!-- <div v-if="homePage" class="flex-direction-column">

  </div> -->
  <router-view> </router-view>
  <router-view name="a"></router-view>
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
import { SITE_INFO } from "@/queries";
import { apolloClient } from "@/apollo-config";
import { useRoute } from "vue-router";
import { computed } from 'vue';
import { userUserStore } from "@/stores/user"
import AboutMe from "@/views/home/AboutMe.vue"
import Navigation from "@/views/home/Navigation.vue"


export default {
  components: {
    AboutMe,
    Navigation
  },

  setup() {
    const route = useRoute();
    const userStore = userUserStore();

    const loggedInUser = computed(() => userStore.getUser);
    const homePage = computed(() => {
      // return route.path === '/signin' || route.path === '/signup' || route.path === '/user' || route.path === '/user/profile' ||  route.path === '/user/post' || route.path === '/2024/bastion-host-architecture';
      return route.path === '/'
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

    // console.log(this.loggedInUser)
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