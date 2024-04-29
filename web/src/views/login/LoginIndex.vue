<script lang="ts" setup>
import { onMounted, ref } from "vue";
import { useUserStore } from "@/stores/user.ts";
import { loginAPI } from "@/apis/login.ts";
import { LoginParams } from "@/types/login";
import { RegisterParams } from "@/types/register";
import router from "@/utils/router.ts";
import { registerAPI } from "@/apis/register.ts";

let loginPageStatus = ref<boolean>(true);

const user = useUserStore();

const username = ref<string>("");
const email = ref<string>("");
const password = ref<string>("");

const login = async () => {
  if (username.value === "" || password.value === "") {
    return null;
  }

  return await loginAPI({
    username: username.value,
    password: password.value,
  } as LoginParams);
};

const register = async () => {
  if (username.value === "" || email.value === "" || password.value === "") {
    return null;
  }

  return await registerAPI({
    username: username.value,
    email: email.value,
    password: password.value,
  } as RegisterParams);
};

const commit = async () => {
  let ret;
  if (loginPageStatus.value) {
    ret = await login();
  } else {
    ret = await register();
  }

  if (!ret) return;

  user.login(ret);

  if (user.checkLogin()) {
    setTimeout(() => {
      router.push("/");
    }, 300);
  }
};

onMounted(() => {
  if (user.checkLogin()) {
    router.push("/");
  }

  // bind enter key
  addEventListener("keypress", async (event) => {
    if (event.key === "Enter") await commit();
  });
});
</script>

<template>
  <div class="bg-blue-50 h-screen w-screen flex items-center justify-center">
    <div
      class="container max-w-[50%] max-h-[70%] h-full w-full px-32 py-16 flex flex-col items-center place-content-center justify-center text-center space-y-8 border-2 bg-blue-200 rounded-2xl"
    >
      <h1 v-if="loginPageStatus" class="text-4xl font-bold my-8">登录</h1>
      <h1 v-else class="text-4xl font-bold my-8">注册</h1>

      <div
        class="flex flex-col justify-center items-center space-y-4 max-w-[80%] h-full w-full"
      >
        <el-input
          v-model="username"
          placeholder="请输入用户名"
          size="large"
          title="用户名"
          type="text"
        ></el-input>

        <el-input
          v-if="!loginPageStatus"
          v-model="email"
          placeholder="请输入邮箱"
          size="large"
          title="邮箱"
          type="email"
        ></el-input>

        <el-input
          v-model="password"
          placeholder="请输入密码"
          size="large"
          title="密码"
          type="password"
        ></el-input>
      </div>
      <el-button
        v-if="loginPageStatus"
        class="mx-16"
        size="large"
        @click="commit"
        >登录
      </el-button>
      <el-button v-else class="mx-16" size="large" @click="commit"
        >注册
      </el-button>

      <span>
        <a
          href="javascript:void(0)"
          @click="loginPageStatus = !loginPageStatus"
        >
          {{ loginPageStatus ? "没有账号？点击注册" : "已有账号？点击登录" }}
        </a>
      </span>
    </div>
  </div>
</template>

<style scoped></style>
