<script lang="ts" setup>
import { getNetworkListAPI } from "@/apis/network.ts";
import { Network } from "@/types/network";
import UploadComp from "@/views/base/components/UploadComp.vue";
import { onMounted, ref } from "vue";
import { postImageResponse } from "@/types/image";
import { postDetectAPI } from "@/apis/detect/detect.ts";
import { postDetectParams, postDetectResponse } from "@/types/detect/detect";

const selectedModelId = ref("");
const selectedModel = ref<Network>();
const modelList = ref<Network[]>([]);
const uploadResponse = ref<postImageResponse>();
const detectResponse = ref<postDetectResponse>();
// const tableColumns = ref<
//   Array<{
//     key: string;
//     dataKey: string;
//     title: string;
//     width: number;
//     align: "center";
//   }>
// >([]);
// const tableData = ref<Array<{ [x: string]: number }>>([]);

const detect = async () => {
  if (!selectedModelId.value || !uploadResponse.value) {
    return;
  }
  const params: postDetectParams = {
    hash: uploadResponse.value.image_hash,
    model_id: selectedModel.value!.id,
  };
  detectResponse.value = await postDetectAPI(params);
  // generateTableData();
};

const onSelectModel = async (model: string) => {
  for (const item of modelList.value) {
    if (item.name === model) {
      selectedModel.value = item;
      break;
    }
  }
  await detect();
};

const onUploadSuccess = async (response: postImageResponse) => {
  uploadResponse.value = response;
  await detect();
};

// const generateTableData = () => {
//   if (!detectResponse.value) {
//     return;
//   }
//   const labels = detectResponse.value.labels;
//
//   detectResponse.value.labels.map((label) => {
//     tableColumns.value.push({
//       key: label,
//       dataKey: label,
//       title: label,
//       width: 100,
//       align: "center",
//     });
//   });
//
//   const probability = detectResponse.value.probability;
//   const data: { [x: string]: number } = {};
//   for (let i = 0; i < labels.length; i++) {
//     data[labels[i]] = probability[i];
//   }
//   tableData.value = [data];
// };

onMounted(async () => {
  modelList.value = await getNetworkListAPI();
});
</script>

<template>
  <div
    class="flex h-full w-full space-y-8 items-center justify-center place-content-center text-center"
  >
    <div class="flex flex-col max-w-[80%] w-full space-y-4">
      <h1 class="text-3xl font-bold">图片检测</h1>

      <div class="flex">
        <el-select
          v-model="selectedModelId"
          class="flex-grow"
          clearable
          placeholder="请选择检测模型"
          @change="onSelectModel"
        >
          <el-option
            v-for="item in modelList"
            :key="item.name"
            :label="item.name"
            :value="item.name"
          />
        </el-select>
        <div>
          <el-button class="ml-4" type="primary" @click="detect">
            检测
          </el-button>
        </div>
      </div>

      <UploadComp :limit="1" @upload-success="onUploadSuccess" />
      <div v-if="detectResponse !== undefined" class="flex-grow flex flex-col">
        <!-- 检测结果 -->
        <div class="text-xl">
          检测结果：{{ detectResponse.labels[detectResponse.predicted] }}
        </div>
        <div class="text-xl">
          置信度：{{ detectResponse.probability[detectResponse.predicted] }}
        </div>
        <!-- <div class="h-full w-full">
          <el-auto-resizer>
            <template #default="{ height, width }">
              <el-table-v2
                :columns="tableColumns"
                :data="tableData"
                :height="height"
                :width="width"
                fixed
              />
            </template>
          </el-auto-resizer>
        </div> -->
      </div>
    </div>
  </div>
</template>

<style scoped></style>
