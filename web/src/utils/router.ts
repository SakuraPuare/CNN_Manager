import { createRouter, createWebHashHistory } from "vue-router";
import { useUserStore } from "@/stores/user.ts"; // const user = useUserStore();

// const user = useUserStore();

const routes = [
  {
    path: "/",
    meta: { title: "首页" },
    component: () => import("@/views/layout/LayoutIndex.vue"),
    children: [
      {
        path: "/test",
        component: () => import("@/views/test/TestIndex.vue"),
      },
    ],
  },
  {
    path: "/login",
    meta: { title: "登录" },
    component: () => import("../views/login/LoginIndex.vue"),
  },
  {
    path: "/mytest",
    meta: { title: "我的测试", needLogin: true },
    component: () => import("@/views/pages/404NotFoundView.vue"),
  },
  {
    path: "/404",
    meta: { title: "404 Not Found" },
    component: () => import("@/views/pages/404NotFoundView.vue"),
  },
  {
    path: "/403",
    meta: { title: "403 Forbidden" },
    component: () => import("@/views/pages/403ForbiddenView.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/404",
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const user = useUserStore();
  const needLogin = to.matched.some((record) => record.meta?.needLogin);
  console.log("needLogin", needLogin);
  if (needLogin) {
    const isLogin = user.checkLogin();
    console.log("isLogin", isLogin);
    if (isLogin) {
      next();
    } else {
      next("/403");
    }
  } else {
    next();
  }
});

export default router;
