<script lang="ts" setup>
import { onMounted, Ref, ref } from "vue";
import http from "../utils/http.ts";
import { useUserStore } from "../stores/user.ts";

const user = useUserStore();

const username: Ref<string> = ref("");
const password: Ref<string> = ref("");

const login: () => void = () => {
  console.log(username, password);
  http
    .post("/login", { username: username.value, password: password.value })
    .then((res) => {
      if (res.status === 200) {
        const data = res.data;
        console.log(data);
        user.login(data);
      } else if (res.status === 400) {
        console.log("invalid username or password");
      } else {
      }
    });
};

onMounted(() => {
  // const user = useUserStore();
  // if (user.checkLogin()) {
  //   console.log("already login");
  //   router.push("/");
  // }
});
</script>

<template>
  <p>login</p>
  <el-input v-model="username" title="用户名"></el-input>
  <el-input v-model="password" title="密码"></el-input>
  <el-button @click="login">登录</el-button>
</template>

<style scoped></style>
