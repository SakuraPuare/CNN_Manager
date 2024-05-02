<script lang="ts" setup>
import { nextTick, onMounted, ref } from "vue";
import {
  deleteNetworkAPI,
  getNetworkListAPI,
  postNetworkAPI,
  putNetworkAPI,
} from "@/apis/network.ts";
import {
  deleteNetworkParams,
  getNetworkListResponse,
  postNetworkParams,
  putNetworkParams,
} from "@/types/network";
import { faAdd, faPen, faTrash } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { ElInput } from "element-plus";

const tableData = ref<getNetworkListResponse>([]);

const columns = [
  {
    key: "id",
    dataKey: "id",
    title: "编号",
    width: 100,
    align: "center",
  },
  {
    key: "name",
    dataKey: "name",
    title: "名称",
    width: 200,
    align: "center",
  },
  {
    key: "description",
    dataKey: "description",
    title: "描述",
    width: 200,
    align: "center",
  },
  {
    key: "network",
    dataKey: "network",
    title: "模型文件",
    width: 200,
    align: "center",
  },
  {
    key: "backend",
    dataKey: "backend",
    title: "后端",
    width: 200,
    align: "center",
  },
  {
    key: "catalog",
    dataKey: "catalog",
    title: "分类目录",
    width: 300,
    align: "center",
    cellRenderer: ({ cellData: catalog }: { cellData: string }): string => {
      const data = catalog
        .slice(1, -1)
        .split(", ")
        .map((item) => item.slice(1, -1));
      return data.join(", ");
    },
  },
];

const getData = async () => {
  tableData.value = await getNetworkListAPI();
};

onMounted(async () => {
  await getData();
});

const AddDialogVisible = ref<boolean>(false);
const EditDialogVisible = ref<boolean>(false);
const DeleteDialogVisible = ref<boolean>(false);
const DeleteConfirmDialogVisible = ref<boolean>(false);
const SelectNetwork = ref<postNetworkParams>({
  backend: "",
  catalog: "",
  description: "",
  name: "",
  network: "",
});
const CurrCatalog = ref<string[]>([]);
const inputValue = ref<string>("");
const inputVisible = ref(false);
const InputRef = ref<InstanceType<typeof ElInput>>();

const onAddNetwork = async () => {
  if (
    !(
      SelectNetwork.value.network &&
      SelectNetwork.value.name &&
      SelectNetwork.value.backend
    )
  ) {
    return;
  }
  parseCatalog();
  let params: postNetworkParams = SelectNetwork.value;
  console.log(params);
  await postNetworkAPI(params);
  await getData();
  AddDialogVisible.value = false;
  SelectNetwork.value = {
    backend: "",
    catalog: "",
    description: "",
    name: "",
    network: "",
  };
};

const onEditNetwork = async () => {
  if (
    !(
      SelectNetwork.value.network &&
      SelectNetwork.value.name &&
      SelectNetwork.value.backend
    )
  ) {
    return;
  }

  const dest = tableData.value.find(
    (item) => item.name === SelectNetwork.value.name,
  );
  if (!dest) {
    return;
  }

  parseCatalog();
  let params: putNetworkParams = {
    id: dest.id,
    ...SelectNetwork.value,
  };
  await putNetworkAPI(params);
  await getData();
  EditDialogVisible.value = false;
  SelectNetwork.value = {
    backend: "",
    catalog: "",
    description: "",
    name: "",
    network: "",
  };
};

const onDeleteNetwork = async () => {
  const dest = tableData.value.find(
    (item) => item.name === SelectNetwork.value.name,
  );
  if (!dest) {
    return;
  }

  const params: deleteNetworkParams = {
    id: dest.id,
  };
  await deleteNetworkAPI(params);
  await getData();
  DeleteDialogVisible.value = false;
  DeleteConfirmDialogVisible.value = false;
  SelectNetwork.value = {
    backend: "",
    catalog: "",
    description: "",
    name: "",
    network: "",
  };
};

const updateCatalog = () => {
  CurrCatalog.value = SelectNetwork.value.catalog
    .slice(1, -1)
    .split(", ")
    .map((item) => item.slice(1, -1));
};

const parseCatalog = () => {
  SelectNetwork.value.catalog =
    "[" + CurrCatalog.value.map((item) => `"${item}"`).join(", ") + "]";
};

const onUpdateSelectedNetwork = () => {
  const selectedNetwork = tableData.value.find(
    (item) => item.name === SelectNetwork.value.name,
  );
  if (!selectedNetwork) {
    return;
  }
  const { backend, catalog, description, name, network } = selectedNetwork;
  SelectNetwork.value = {
    backend,
    catalog,
    description,
    name,
    network,
  };
  updateCatalog();
};

const handleClose = (tag: string) => {
  CurrCatalog.value.splice(CurrCatalog.value.indexOf(tag), 1);
};

const showInput = () => {
  inputVisible.value = true;
  nextTick(() => {
    InputRef.value!.input!.focus();
  });
};

const handleInputConfirm = () => {
  if (inputValue.value) {
    CurrCatalog.value.push(inputValue.value);
  }
  inputVisible.value = false;
  inputValue.value = "";
};
</script>

<template>
  <div
    class="flex flex-col container mx-[3%] my-[2%] rounded-2xl p-8 space-y-4 text-center"
  >
    <div class="text-2xl font-bold">模型列表</div>
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
        添加模型
      </div>
      <div
        class="px-6 py-3 bg-yellow-500 rounded-2xl"
        @click="EditDialogVisible = !EditDialogVisible"
      >
        <font-awesome-icon :icon="faPen" />
        修改模型
      </div>
      <div
        class="px-6 py-3 bg-red-500 rounded-2xl"
        @click="DeleteDialogVisible = !DeleteDialogVisible"
      >
        <font-awesome-icon :icon="faTrash" />
        删除模型
      </div>
    </div>
  </div>

  <div>
    <el-dialog
      v-model="AddDialogVisible"
      align-center
      center
      draggable
      title="添加模型"
      width="700"
    >
      <div
        class="flex flex-col space-y-2 justify-center place-content-center items-center max-w-[80%] mx-auto"
      >
        <el-input
          v-model="SelectNetwork.name"
          placeholder="请输入模型名"
          type="text"
        >
          <template #prepend>模型名</template>
        </el-input>
        <el-input
          v-model="SelectNetwork.description"
          placeholder="请输入模型描述"
          type="text"
        >
          <template #prepend>模型描述</template>
        </el-input>
        <el-input
          v-model="SelectNetwork.network"
          placeholder="请输入模型文件"
          type="text"
        >
          <template #prepend>模型文件</template>
        </el-input>
        <el-input
          v-model="SelectNetwork.backend"
          placeholder="请输入后端"
          type="text"
        >
          <template #prepend>后端</template>
        </el-input>
        <div class="flex flex-row border rounded min-h-8 items-center w-full">
          <div class="flex h-full px-4">
            <div class="">检测分类</div>
          </div>
          <div class="flex-grow flex flex-wrap gap-2">
            <el-tag
              v-for="tag in CurrCatalog"
              :key="tag"
              :disable-transitions="false"
              closable
              size="large"
              @close="handleClose(tag)"
            >
              {{ tag }}
            </el-tag>
            <el-input
              v-if="inputVisible"
              ref="InputRef"
              v-model="inputValue"
              class="w-20"
              size="default"
              @blur="handleInputConfirm"
              @keyup.enter="handleInputConfirm"
            />
            <el-button
              v-else
              class="button-new-tag"
              size="default"
              @click="showInput"
            >
              + New Tag
            </el-button>
          </div>
        </div>
      </div>

      <template #footer>
        <div class="dialog-footer">
          <el-button @click="AddDialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="onAddNetwork"> Confirm</el-button>
        </div>
      </template>
    </el-dialog>

    <el-dialog
      v-model="EditDialogVisible"
      align-center
      center
      draggable
      title="编辑模型"
      width="700"
    >
      <div
        class="flex flex-col space-y-2 justify-center place-content-center items-center max-w-[80%] mx-auto"
      >
        <el-select
          v-model="SelectNetwork.name"
          placeholder="请选择模型"
          @change="onUpdateSelectedNetwork"
        >
          <el-option
            v-for="item in tableData"
            :key="item.name"
            :label="item.name"
            :value="item.name"
          />
        </el-select>

        <el-input
          v-model="SelectNetwork.name"
          placeholder="请输入模型名"
          type="text"
        >
          <template #prepend>模型名</template>
        </el-input>
        <el-input
          v-model="SelectNetwork.description"
          placeholder="请输入模型描述"
          type="text"
        >
          <template #prepend>模型描述</template>
        </el-input>
        <el-input
          v-model="SelectNetwork.network"
          placeholder="请输入模型文件"
          type="text"
        >
          <template #prepend>模型文件</template>
        </el-input>
        <el-input
          v-model="SelectNetwork.backend"
          placeholder="请输入后端"
          type="text"
        >
          <template #prepend>后端</template>
        </el-input>
        <div class="flex flex-row border rounded min-h-8 items-center w-full">
          <div class="flex h-full px-4">
            <div class="">检测分类</div>
          </div>
          <div class="flex-grow flex flex-wrap gap-2">
            <el-tag
              v-for="tag in CurrCatalog"
              :key="tag"
              :disable-transitions="false"
              closable
              size="large"
              @close="handleClose(tag)"
            >
              {{ tag }}
            </el-tag>
            <el-input
              v-if="inputVisible"
              ref="InputRef"
              v-model="inputValue"
              class="w-20"
              size="default"
              @blur="handleInputConfirm"
              @keyup.enter="handleInputConfirm"
            />
            <el-button
              v-else
              class="button-new-tag"
              size="default"
              @click="showInput"
            >
              + New Tag
            </el-button>
          </div>
        </div>
      </div>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="EditDialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="onEditNetwork"> Confirm</el-button>
        </div>
      </template>
    </el-dialog>

    <el-dialog
      v-model="DeleteDialogVisible"
      align-center
      center
      draggable
      title="删除模型"
      width="700"
    >
      <el-dialog
        v-model="DeleteConfirmDialogVisible"
        append-to-body
        title="确认删除"
        width="500"
      >
        <div>确认删除模型 {{ SelectNetwork.name }} 吗？</div>

        <template #footer>
          <div class="dialog-footer">
            <el-button @click="DeleteConfirmDialogVisible = false">
              Cancel
            </el-button>
            <el-button type="primary" @click="onDeleteNetwork">
              Confirm
            </el-button>
          </div>
        </template>
      </el-dialog>
      <div class="max-w-[80%] mx-auto">
        <el-select
          v-model="SelectNetwork.name"
          class="py-2"
          placeholder="请选择模型"
          @change="onUpdateSelectedNetwork"
        >
          <el-option
            v-for="item in tableData"
            :key="item.name"
            :label="item.name"
            :value="item.name"
          />
        </el-select>
      </div>

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
