import axios from "axios";
import { useUserStore } from "@/stores/user.ts";
import router from "./router.ts";
import { ElMessage } from "element-plus";
import { BASE_URL } from "@/config.ts";

axios.defaults.headers.get["Access-Control-Allow-Origin"] = "*";
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";

const service = axios.create({
  baseURL: BASE_URL, // api的base_url
  timeout: 5000, // 请求超时时间
});

// request拦截器
service.interceptors.request.use(
  (config) => {
    // 在这里你可以做一些请求前的操作
    // 如设置token
    const user = useUserStore();
    if (user.token) {
      config.headers["Authorization"] = `Bearer ${user.token}`;
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
    if (response.status !== 200) {
      ElMessage({ message: response.data.detail || "服务异常", type: "error" });
    }
    if (response.status === 401) {
      const user = useUserStore();
      user.logout();
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
