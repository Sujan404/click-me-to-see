<template>
  <router-view> </router-view>
  <router-view name="a"></router-view>
  <router-view name="b"></router-view>
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

export default {
  setup() {
    const route = useRoute();
    const userStore = userUserStore();

    const loggedInUser = computed(() => userStore.getUser);

    return { loggedInUser, userStore, route }
  },
  data() {
    return {
      mySite: null,
    }
  },
  async created() {
    const siteInfo = await apolloClient.query({
      query: SITE_INFO
    }
    );
    this.mySite = siteInfo.data.site;
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