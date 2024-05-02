<script lang="ts" setup>
import { useUserStore } from "@/stores/user";

const user = useUserStore();
</script>

<template>
  <div
    class="flex h-full w-full space-y-8 items-center justify-center place-content-center"
  >
    <h2 class="text-4xl font-bold">欢迎！管理员 {{ user.username }}</h2>
  </div>
</template>

<style scoped></style>
