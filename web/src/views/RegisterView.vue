<script lang="ts" setup>
import { onMounted, Ref, ref } from "vue";
import http from "../utils/http.ts";
import { useUserStore } from "../stores/user.ts";
import router from "../utils/router.ts";

const username: Ref<string> = ref("");
const password: Ref<string> = ref("");

const register: () => void = () => {
  console.log(username, password);
  http
    .post("/register", { username: username.value, password: password.value })
    .then((res) => {
      console.log(res);
      if (res.status === 200) {
        const data = res.data;
        const user = useUserStore();
        user.login(data.username, data.isadmin, data.token);
      } else if (res.status === 400) {
        console.log("register failed");
      } else {
      }
    });
};

onMounted(() => {
  const user = useUserStore();
  if (user.checkLogin()) {
    console.log("already login");
    router.push("/");
  }
});
</script>

<template>
  <div>
    <h1>Register</h1>
    <el-input v-model="username" placeholder="Email"></el-input>
    <el-input v-model="password" placeholder="Password"></el-input>
    <el-button @click="register">Register</el-button>
  </div>
</template>

<style scoped></style>
