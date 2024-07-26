import { createApp, provide, h } from "vue";
import App from "./App.vue";
import router from "./router";
import { apolloProvider } from "@/apollo-config";
import { createPinia } from "pinia";
import VueApolloComponents from '@vue/apollo-components'
import { DefaultApolloClient } from '@vue/apollo-composable'

const app = createApp(
  {
    render: () => h(App),
  }
);

app.use(createPinia()).use(router).use(apolloProvider).use(VueApolloComponents).mount("#app");
