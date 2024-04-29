<script lang="ts" setup>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faBan } from "@fortawesome/free-solid-svg-icons";

import { onMounted } from "vue";
import router from "@/utils/router.ts";

onMounted(() => {
  // wait for 3 seconds and then redirect to the home page
  setTimeout(() => {
    router.push("/");
  }, 5000);
});
</script>

<template>
  <div class="bg-red-300 h-screen w-screen">
    <div
      class="text-center font-bold space-y-4 flex flex-col items-center justify-center place-content-center h-full"
    >
      <font-awesome-icon :icon="faBan" class="h-64 w-64" />
      <h1 class="text-4xl text-center">401 Forbidden</h1>
      <p class="text-2xl text-center">
        You do not have permission to access this page.
      </p>
    </div>
  </div>
</template>

<style scoped></style>
