import './assets/main.css'
import { createApp, provide, h } from "vue";
import App from "./App.vue";
import router from "./router";
import { apolloProvider } from "@/apollo-config";
import {apolloClient} from "@/apollo-config";
import { createPinia } from "pinia";
import VueApolloComponents from '@vue/apollo-components'
import { DefaultApolloClient } from '@vue/apollo-composable'
import { createHead } from '@unhead/vue'
import PrimeVue from 'primevue/config';
import FileUpload from 'primevue/fileupload';
import ProgressBar from 'primevue/progressbar';
import Message from 'primevue/message';
import Badge from 'primevue/badge';
import 'flowbite';
const head = createHead()
// const primeVue = PrimeVue()
const app = createApp(
  {
    setup() {
      provide(DefaultApolloClient, apolloClient)
  },
    render: () => h(App),
  }
);

app.use(createPinia()).use(head).use(PrimeVue)
   .component('FileUpload', FileUpload)
   .component('ProgressBar', ProgressBar)
   .component('Message', Message)
   .component('Badge', Badge)
   .use(router).use(apolloProvider).use(VueApolloComponents).mount("#app");
