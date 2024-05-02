<script lang="ts" setup>
import DrawerComp from "@/views/admin/components/DrawerComp.vue";

import { getHeightWithoutHeader } from "@/utils/page/responsive.ts";
import { onMounted, onUnmounted, ref } from "vue";

const pageHeight = ref<number>(0);

onMounted(() => {
  pageHeight.value = getHeightWithoutHeader();
  addEventListener("resize", () => {
    pageHeight.value = getHeightWithoutHeader();
  });
});

onUnmounted(() => {
  removeEventListener("resize", () => {
    pageHeight.value = getHeightWithoutHeader();
  });
});
</script>

<template>
  <div :style="`height: ${pageHeight}px`" class="flex">
    <DrawerComp />
    <div class="flex-grow flex">
      <router-view class="border-2" />
    </div>
  </div>
</template>

<style scoped></style>
