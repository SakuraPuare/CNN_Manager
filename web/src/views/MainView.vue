<script lang="ts" setup>
import { useUserStore } from "../stores/user.ts";
import { storeToRefs } from "pinia";

const user = useUserStore();
const { username, is_admin, token } = storeToRefs(user);
</script>

<template>
  <h2 class="text-blue-500 text-2xl font-bold">Here is main</h2>
  <p>username: {{ username }}</p>
  <p>is_admin: {{ is_admin }}</p>
  <p>token: {{ token }}</p>

  <el-button @click="user.logout()">logout</el-button>
</template>

<style scoped></style>
