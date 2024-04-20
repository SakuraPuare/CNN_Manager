import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  { path: "/", component: () => import("../views/MainView.vue") },
  { path: "/login", component: () => import("../views/LoginView.vue") },
  { path: "/register", component: () => import("../views/RegisterView.vue") },
  {
    path: "/:pathMatch(.*)*",
    component: () => import("../views/pages/404NotFoundView.vue"),
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
