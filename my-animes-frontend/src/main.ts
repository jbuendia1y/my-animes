import { createApp } from "vue";
import "./style.css";
import router from "./router";
import App from "./App.vue";

const app = createApp(App);

// Boostrap
import "bootstrap/dist/css/bootstrap.css";

app.use(router);

app.mount("#app");
