<script lang="ts" setup>
import { useUserStore } from "./stores/user.ts";
import { StoreGeneric, storeToRefs } from "pinia";

const user = useUserStore();
const { username, is_admin, token } = storeToRefs(<StoreGeneric>user);
</script>

<template>
  <router-view />

  <p>username: {{ username }}</p>
  <p>is_admin: {{ is_admin }}</p>
  <p>token: {{ token }}</p>
  <el-button @click="user.logout()">logout</el-button>
</template>

<style scoped></style>
