import axios from "axios";
import { useUserStore } from "../stores/user.ts";
import router from "./router.ts";

axios.defaults.headers.get["Access-Control-Allow-Origin"] = "*";
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";

const service = axios.create({
  baseURL: "http://localhost:8000/", // api的base_url
  timeout: 5000, // 请求超时时间
});

// request拦截器
service.interceptors.request.use(
  (config) => {
    // 在这里你可以做一些请求前的操作
    // 如设置token
    const store = useUserStore();
    if (store.token) {
      config.headers["Authorization"] = `Bearer ${store.token}`;
    }
    return config;
  },
  (error) => {
    // 处理请求错误
    console.error(error); // for debug
    Promise.reject(error).then((r) => console.log(r));
  },
);

// response拦截器
service.interceptors.response.use(
  (response) => {
    if (response.status === 401) {
      router.push("/login").then((r) => console.log(r));
    }
    return response;
  },
  (error) => {
    console.error(error); // for debug
    return Promise.reject(error);
  },
);

export default service;
