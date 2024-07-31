<template>
  <div class="mx-auto h-screen w-full sm:w-2/3 md:w-1/3">
    <form action="POST" @submit.prevent="userSignIn()">
      <div class="bg-white rounded-xl w-full">
        <div class="space-y-4">
          <p v-if="errors.length">
            <ul>
              <li v-for="error in errors" class="text-center text-red-600/100 bg-yellow-300">{{ error }}</li>
            </ul>
          </p>
          <div>
            <label for="email" class="block mb-1 text-gray-600 font-medium">Username</label>
            <input type="text"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
              v-model="signInDetails.username" />
          </div>
          <div>
            <label for="email" class="block mb-1 text-gray-600 font-medium">Password</label>
            <input type="password"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-teal-500 focus:ring focus:ring-teal-300 focus:ring-opacity-50"
              v-model="signInDetails.password" />
          </div>
        </div>
        <button
          class="mt-4 w-full bg-teal-500 hover:bg-teal-700 focus:ring focus:ring-teal-100 text-white py-2 rounded-md text-lg tracking-wide">
          Sign In
        </button>
        <div class="text-right">
          <small>Don't have an account? Try
            <router-link to="/signup" class="text-teal-500 hover:underline">Sign Up</router-link>
            first.</small>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { userUserStore } from "@/stores/user";
import { USER_SIGNIN } from "@/mutations";
import { apolloClient } from "@/apollo-config";

export default {
  name: "SignInView",

  setup() {
    const userStore = userUserStore();
    return { userStore };
  },

  data() {
    return {
      signInDetails: {
        username: "",
        password: "",
      },
      errors:[]
    };
  },

  methods: {
    async userSignIn() {
      try{
        const user = await apolloClient.mutate({
        mutation: USER_SIGNIN,
        variables: {
          username: this.signInDetails.username,
          password: this.signInDetails.password,
        },
      });
      this.userStore.setToken(user.data.tokenAuth.token);
      this.userStore.setUser(user.data.tokenAuth.user);
      this.$router.push({ name: "home" })
    }catch(errors){
      console.log(errors.message)
      this.errors = [];
      this.errors.push(errors.message)
    }
  },
},
  };
</script>