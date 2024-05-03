<script lang="ts" setup>
import { onMounted, ref } from "vue";
import { faAdd, faTrash } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import {
  getFeedbackListResponse,
  postFeedbackParams,
  StringIdFeedback,
} from "@/types/detect/feedback";
import {
  deleteFeedbackAPI,
  getFeedbackListAPI,
  postFeedbackAPI,
} from "@/apis/detect/feedback.ts";
import { getDetectListResponse } from "@/types/detect/detect";
import { getDetectAPI, getDetectListAPI } from "@/apis/detect/detect";
import { getNetworkAPI } from "@/apis/network";

const tableData = ref<getFeedbackListResponse>([]);

const columns = [
  {
    key: "id",
    dataKey: "id",
    title: "编号",
    width: 150,
    align: "center",
  },
  {
    key: "user_id",
    dataKey: "user_id",
    title: "用户编号",
    width: 150,
    align: "center",
  },
  {
    key: "detect_id",
    dataKey: "detect_id",
    title: "检测编号",
    width: 150,
    align: "center",
  },
  {
    key: "feedback",
    dataKey: "feedback",
    title: "反馈",
    width: 150,
    align: "center",
  },
  {
    key: "created_at",
    dataKey: "created_at",
    title: "创建于",
    width: 300,
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
    width: 300,
    align: "center",
    cellRenderer: ({ cellData: updated_at }: { cellData: string }): string => {
      const date = new Date(updated_at);
      return date.toLocaleDateString() + " " + date.toLocaleTimeString();
    },
  },
];

const getData = async () => {
  tableData.value = await getFeedbackListAPI();
  DetectList.value = await getDetectListAPI();
};

onMounted(async () => {
  await getData();
});

const AddDialogVisible = ref<boolean>(false);
const DeleteDialogVisible = ref<boolean>(false);
const DeleteConfirmDialogVisible = ref<boolean>(false);
const SelectFeedback = ref<StringIdFeedback>({
  detect_id: "",
  feedback: "",
  id: "",
});
const SelectDetectCatalog = ref<Array<string>>([]);
const DetectList = ref<getDetectListResponse>([]);

const onAddFeedback = async () => {
  if (
    SelectFeedback.value.detect_id === "" ||
    SelectFeedback.value.feedback === ""
  ) {
    return;
  }

  const params: postFeedbackParams = {
    detect_id: Number(SelectFeedback.value.detect_id),
    ground_truth: Number(SelectFeedback.value.feedback),
  };
  await postFeedbackAPI(params);
  await getData();
  AddDialogVisible.value = false;
};

const onDeleteFeedback = async () => {
  if (SelectFeedback.value.id === "") {
    return;
  }

  await deleteFeedbackAPI({ id: Number(SelectFeedback.value.feedback) });
  await getData();
  DeleteDialogVisible.value = false;
  DeleteConfirmDialogVisible.value = false;
};

const parseCatalog = (str: string) => {
  return str
    .slice(1, -1)
    .split(", ")
    .map((item) => item.slice(1, -1));
};

const onUpdateSelectedFeedbackAdd = async () => {
  const detect = await getDetectAPI({
    id: Number(SelectFeedback.value.detect_id),
  });
  const network = await getNetworkAPI({ id: detect.network_id });
  SelectDetectCatalog.value = parseCatalog(network.catalog);
  console.log(SelectDetectCatalog.value);
};

const onUpdateSelectedFeedbackDelete = async () => {
  const curr = tableData.value.find(
    (item) => item.feedback === Number(SelectFeedback.value.feedback),
  );
  if (!curr) {
    return;
  }

  SelectFeedback.value = {
    detect_id: curr.detect_id.toString(),
    feedback: curr.feedback.toString(),
    id: curr.id.toString(),
  };
};
</script>

<template>
  <div
    class="flex flex-col container mx-[3%] my-[2%] rounded-2xl p-8 space-y-4 text-center"
  >
    <div class="text-2xl font-bold">反馈列表</div>
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
    <div
      class="flex flex-row h-fit w-[80%] mx-auto justify-evenly text-white text-center"
    >
      <div
        class="px-6 py-3 bg-blue-500 rounded-2xl"
        @click="AddDialogVisible = !AddDialogVisible"
      >
        <font-awesome-icon :icon="faAdd" />
        添加反馈
      </div>
      <div
        class="px-6 py-3 bg-red-500 rounded-2xl"
        @click="DeleteDialogVisible = !DeleteDialogVisible"
      >
        <font-awesome-icon :icon="faTrash" />
        删除反馈
      </div>
    </div>
  </div>

  <div>
    <el-dialog
      v-model="AddDialogVisible"
      align-center
      center
      draggable
      title="添加反馈"
      width="700"
    >
      <div
        class="flex flex-col space-y-2 justify-center place-content-center items-center max-w-[80%] mx-auto"
      >
        <el-select
          v-model="SelectFeedback.detect_id"
          class="py-2"
          placeholder="请选择检测"
          @change="onUpdateSelectedFeedbackAdd"
        >
          <el-option
            v-for="item in DetectList"
            :key="item.id"
            :label="`检测${item.id} <- 模型${item.network_id}`"
            :value="item.id"
          />
        </el-select>

        <el-select
          v-if="SelectDetectCatalog.length > 0"
          v-model="SelectFeedback.feedback"
          class="py-2"
          placeholder="请选择反馈"
        >
          <el-option
            v-for="(item, index) in SelectDetectCatalog"
            :key="index"
            :label="item"
            :value="index"
          />
        </el-select>
      </div>

      <template #footer>
        <div class="dialog-footer">
          <el-button @click="AddDialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="onAddFeedback"> Confirm</el-button>
        </div>
      </template>
    </el-dialog>

    <el-dialog
      v-model="DeleteDialogVisible"
      align-center
      center
      draggable
      title="删除反馈"
      width="700"
    >
      <el-dialog
        v-model="DeleteConfirmDialogVisible"
        append-to-body
        title="确认删除"
        width="500"
      >
        <div>确认删除反馈 {{ SelectFeedback.feedback }} 吗？</div>

        <template #footer>
          <div class="dialog-footer">
            <el-button @click="DeleteConfirmDialogVisible = false">
              Cancel
            </el-button>
            <el-button type="primary" @click="onDeleteFeedback">
              Confirm
            </el-button>
          </div>
        </template>
      </el-dialog>

      <el-select
        v-model="SelectFeedback.feedback"
        class="py-2"
        placeholder="请选择检测"
        @change="onUpdateSelectedFeedbackDelete"
      >
        <el-option
          v-for="item in tableData"
          :key="item.id"
          :label="`检测${item.id} -> 反馈${item.feedback}`"
          :value="item.id"
        />
      </el-select>

      <template #footer>
        <div class="dialog-footer">
          <el-button @click="DeleteDialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="DeleteConfirmDialogVisible = true">
            Confirm
          </el-button>
        </div>
      </template>
    </el-dialog>
  </div>
</template>

<style scoped></style>
