import { createApp } from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import router from "./router";
import store from "./store";
import UploadButton from "vuetify-upload-button";
loadFonts();

createApp(App)
    .use(store)
    .use(router)
    .use(vuetify)
    .use(UploadButton)
    .mount("#app");
