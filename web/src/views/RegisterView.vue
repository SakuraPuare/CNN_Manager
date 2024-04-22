<script lang="ts" setup>
import { onMounted, Ref, ref } from "vue";
import http from "../utils/http.ts";
import { useUserStore } from "../stores/user.ts";
import router from "../utils/router.ts";

const user = useUserStore();
// const register_username: Ref<string> = ref("");
// const register_email: Ref<string> = ref("");
// const register_password: Ref<string> = ref("");

const register_username: Ref<string> = ref("sakurapuare");
const register_email: Ref<string> = ref("sakurapuare@sakurapuare.com");
const register_password: Ref<string> = ref("123456");

const register: () => void = () => {
  console.log(register_username, register_password);
  http
    .post("/register", {
      username: register_username.value,
      email: register_email.value,
      password: register_password.value,
    })
    .then((res) => {
      console.log(res);
      if (res.status === 200) {
        const data = res.data;
        user.login(data);
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
    <el-input
      v-model="register_username"
      placeholder="UserName"
      required
    ></el-input>
    <el-input
      v-model="register_email"
      :type="'email'"
      maxlength="50"
      pattern=".+@.+\.com"
      placeholder="Email"
      required
    ></el-input>
    <el-input
      v-model="register_password"
      placeholder="Password"
      required
      type="password"
    ></el-input>
    <el-button @click="register">Register</el-button>
  </div>
</template>

<style scoped></style>
