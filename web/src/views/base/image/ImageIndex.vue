<script lang="ts" setup>
import { getImageListAPI } from "@/apis/image.ts";
import { onMounted, ref } from "vue";
import { Image } from "@/types/image";
import { BASE_URL } from "@/config.ts";

const imageList = ref<Image[]>([]);

onMounted(async () => {
  imageList.value = await getImageListAPI();
});
</script>

<template>
  <div
    class="flex flex-col container mx-[3%] my-[2%] rounded-2xl p-8 space-y-4"
  >
    <div class="text-2xl font-bold text-center">图片列表</div>

    <el-scrollbar class="w-full h-full">
      <div class="space-y-8">
        <div
          v-for="item in imageList"
          :key="item.id"
          class="h-64 w-full flex border-2 rounded-xl px-4 py-2 bg-blue-200"
        >
          <div class="w-[300px] my-auto mx-auto text-center">
            <el-image
              :src="`${BASE_URL}image/file/${item.image_hash}`"
              class="h-48"
              fit="contain"
              loading="lazy"
            />
          </div>
          <ul
            class="flex-grow flex flex-col flex-wrap h-full mx-4 my-8 text-xl space-y-1"
          >
            <li>文件名：{{ item.name }}</li>
            <li v-if="item.description">文件描述：{{ item.description }}</li>
            <li>图片类型：{{ item.type }}</li>
            <li>图片大小：{{ (item.file_size / 1024 / 1024).toFixed(2) }}MB</li>
            <li>上传时间：{{ new Date(item.created_at).toLocaleString() }}</li>
            <li>图片大小：{{ item.width }} x {{ item.height }}</li>
            <li>
              图片哈希：<span class="text-sm">{{ item.image_hash }}</span>
            </li>
          </ul>
        </div>
      </div>
    </el-scrollbar>
  </div>
</template>

<style scoped></style>
