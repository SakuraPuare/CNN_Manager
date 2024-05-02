<script lang="ts" setup>
import { onMounted, ref } from "vue";
import { getDetectListAPI } from "@/apis/detect/detect.ts";
import { getDetectListResponse } from "@/types/detect/detect";

const tableData = ref<getDetectListResponse>([]);

const columns = [
  {
    key: "id",
    dataKey: "id",
    title: "编号",
    width: 100,
    align: "center",
  },
  {
    key: "user_id",
    dataKey: "user_id",
    title: "用户编号",
    width: 100,
    align: "center",
  },
  {
    key: "image_id",
    dataKey: "image_id",
    title: "图片编号",
    width: 100,
    align: "center",
  },
  {
    key: "network_id",
    dataKey: "network_id",
    title: "网络编号",
    width: 100,
    align: "center",
  },
  {
    key: "output",
    dataKey: "output",
    title: "输出",
    width: 100,
    align: "center",
  },
  {
    key: "confidence",
    dataKey: "confidence",
    title: "置信度",
    width: 200,
    align: "center",
  },
  {
    key: "created_at",
    dataKey: "created_at",
    title: "创建于",
    width: 200,
    align: "center",
    cellRenderer: ({ cellData: created_at }: { cellData: string }): string => {
      const date = new Date(created_at);
      return date.toLocaleDateString() + " " + date.toLocaleTimeString();
    },
  },
  {
    key: "updated_at",
    dataKey: "updated_at",
    title: "修改于",
    width: 200,
    align: "center",
    cellRenderer: ({ cellData: updated_at }: { cellData: string }): string => {
      const date = new Date(updated_at);
      return date.toLocaleDateString() + " " + date.toLocaleTimeString();
    },
  },
];

onMounted(async () => {
  tableData.value = await getDetectListAPI();
  console.log(tableData.value);
});
</script>

<template>
  <div
    class="flex flex-col container mx-[3%] my-[2%] rounded-2xl p-8 space-y-4 text-center"
  >
    <div class="text-2xl font-bold">历史记录</div>
    <div class="flex-grow h-full w-full">
      <el-auto-resizer>
        <template #default="{ height, width }">
          <el-table-v2
            :columns="columns"
            :data="tableData"
            :fixed="true"
            :height="height"
            :stimated-row-height="50"
            :width="width"
          />
        </template>
      </el-auto-resizer>
    </div>
  </div>
</template>

<style scoped></style>
