import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "homeView",
      component: HomeView,
    },
    {
      path: "/animes/:slug",
      name: "anime",
      component: () => import("../views/AnimeView.vue"),
      props: true,
    },
    /*     {
      path: "/:countryName",
      name: "country",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/CountryView.vue"),
      props: true,
    }, */
  ],
});

export default router;
