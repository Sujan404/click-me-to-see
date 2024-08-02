<template>
  <div class="flex-direction-column">
    <div>
      <h1>Hi</h1>
      <p>{{ currentUrl }}</p>
      <p>sdgdfg</p>
      <h1>I am Sujan Ale</h1>
      <h1>I am developing a full stack website to enhance my skill from coding to deploying</h1>
    </div>
    <div class="m-5 text-center">
      <router-link to="/signin" class="bg-teal-500 text-white mr-5 p-2 rounded-md">Sign In</router-link>
      <router-link to="/signup" class="bg-teal-500 text-white p-2 rounded-md">Sign Up</router-link>
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
import { SITE_INFO } from "@/queries";
import { apolloClient } from "@/apollo-config";
import { useRoute } from "vue-router";
import {useAppContentStatusStore} from "@/stores/appContentStatus"
export default {
  data() {
    return {
      mySite: null,
      currentUrl: useAppContentStatusStore.getCurrentUrl('currentUrl')
    }
  },
  async created() {
    const siteInfo = await apolloClient.query({
      query: SITE_INFO
    }
    );
    this.mySite = siteInfo.data.site;

    console.log("asdfasdf")
    console.log(this.currentUrl)
  },
};
</script>