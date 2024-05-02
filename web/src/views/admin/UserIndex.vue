<script lang="ts" setup>
import { h, onMounted, ref, VNode } from "vue";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faAdd, faPen, faTrash } from "@fortawesome/free-solid-svg-icons";
import {
  deleteUserAPI,
  getUserListAPI,
  postUserAPI,
  putUserAPI,
} from "@/apis/admin/user.ts";
import {
  deleteUserParams,
  getUserListParams,
  getUserListResponse,
  putUserParams,
  StringIdUser,
} from "@/types/admin/user";

const tableData = ref<getUserListResponse>([]);
const currPage = ref<number>(1);

const columns = [
  {
    key: "id",
    dataKey: "id",
    title: "编号",
    width: 100,
    align: "center",
  },
  {
    key: "username",
    dataKey: "username",
    title: "用户名",
    width: 200,
    align: "center",
  },
  {
    key: "email",
    dataKey: "email",
    title: "邮箱",
    width: 300,
    align: "center",
  },
  {
    key: "is_admin",
    dataKey: "is_admin",
    title: "管理员权限",
    width: 150,
    align: "center",
    cellRenderer: ({ cellData: is_admin }: { cellData: string }): VNode => {
      return h(
        "span",
        {
          class: [
            "px-4",
            "py-1",
            "rounded-2xl",
            is_admin ? "bg-green-300" : "bg-red-300",
          ],
        },
        is_admin ? "是" : "否",
      );
    },
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

const getPageData = async () => {
  const params: getUserListParams = {
    page: currPage.value,
    limit: 10,
  };
  tableData.value = await getUserListAPI(params);
};

onMounted(async () => {
  await getPageData();
});

const AddDialogVisible = ref<boolean>(false);
const EditDialogVisible = ref<boolean>(false);
const DeleteDialogVisible = ref<boolean>(false);
const DeleteConfirmDialogVisible = ref<boolean>(false);

const SelectUser = ref<StringIdUser>({
  email: "",
  id: "",
  is_admin: false,
  password: "",
  username: "",
});

const onUpdateSelectedUser = () => {
  console.log(tableData.value);
  for (let i = 0; i < tableData.value.length; i++) {
    // compare string and number
    if (tableData.value[i].id === Number(SelectUser.value.id)) {
      SelectUser.value.email = tableData.value[i].email;
      SelectUser.value.is_admin = tableData.value[i].is_admin;
      SelectUser.value.username = tableData.value[i].username;
      break;
    }
  }
};

const onAddUser = async () => {
  if (!SelectUser.value.username || !SelectUser.value.email) {
    return;
  }
  await postUserAPI(SelectUser.value);
  await getPageData();
  AddDialogVisible.value = false;
};

const onEditUser = async () => {
  if (!SelectUser.value.username || !SelectUser.value.email) {
    return;
  }
  const params: putUserParams = {
    id: Number(SelectUser.value.id),
    username: SelectUser.value.username,
    email: SelectUser.value.email,
    is_admin: SelectUser.value.is_admin,
    password: "", // Add the missing "password" property
  };
  await putUserAPI(params);
  await getPageData();
  EditDialogVisible.value = false;
};

const onDeleteUser = async () => {
  onUpdateSelectedUser();
  const params: deleteUserParams = {
    id: Number(SelectUser.value.id),
  };
  await deleteUserAPI(params);
  await getPageData();
  DeleteDialogVisible.value = false;
  DeleteConfirmDialogVisible.value = false;
  SelectUser.value = {
    email: "",
    id: "",
    is_admin: false,
    password: "",
    username: "",
  };
};
</script>

<template>
  <div
    class="flex flex-col container mx-[3%] my-[2%] rounded-2xl p-8 space-y-4 text-center"
  >
    <div class="text-2xl font-bold">用户列表</div>
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
        添加用户
      </div>
      <div
        class="px-6 py-3 bg-yellow-500 rounded-2xl"
        @click="EditDialogVisible = !EditDialogVisible"
      >
        <font-awesome-icon :icon="faPen" />
        修改用户
      </div>
      <div
        class="px-6 py-3 bg-red-500 rounded-2xl"
        @click="DeleteDialogVisible = !DeleteDialogVisible"
      >
        <font-awesome-icon :icon="faTrash" />
        删除用户
      </div>
    </div>
  </div>

  <div>
    <el-dialog
      v-model="AddDialogVisible"
      align-center
      center
      draggable
      title="添加用户"
      width="700"
    >
      <div
        class="flex flex-col space-y-2 justify-center place-content-center items-center max-w-[80%] mx-auto"
      >
        <el-input
          v-model="SelectUser.username"
          placeholder="请输入用户名"
          type="text"
        >
          <template #prepend>用户名</template>
        </el-input>
        <el-input
          v-model="SelectUser.email"
          placeholder="请输入邮箱"
          type="email"
        >
          <template #prepend>邮箱</template>
        </el-input>
        <el-input
          v-model="SelectUser.password"
          placeholder="请输入密码"
          show-password
          type="password"
        >
          <template #prepend>密码</template>
        </el-input>
        <div>
          <el-checkbox v-model="SelectUser.is_admin">管理员权限</el-checkbox>
        </div>
      </div>

      <template #footer>
        <div class="dialog-footer">
          <el-button @click="AddDialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="onAddUser"> Confirm</el-button>
        </div>
      </template>
    </el-dialog>

    <el-dialog
      v-model="EditDialogVisible"
      align-center
      center
      draggable
      title="编辑用户"
      width="700"
    >
      <div class="max-w-[80%] mx-auto">
        <el-select
          v-model="SelectUser.id"
          class="py-2"
          placeholder="请选择用户"
          @change="onUpdateSelectedUser"
        >
          <el-option
            v-for="item in tableData"
            :key="item.id"
            :label="item.username"
            :value="item.id"
          />
        </el-select>
        <div
          v-if="SelectUser.id"
          class="flex flex-col space-y-2 justify-center place-content-center items-center"
        >
          <el-input v-model="SelectUser.username" placeholder="请输入用户名">
            <template #prepend>用户名</template>
          </el-input>
          <el-input v-model="SelectUser.email" placeholder="请输入邮箱">
            <template #prepend>邮箱</template>
          </el-input>
          <div>
            <el-checkbox v-model="SelectUser.is_admin">管理员权限</el-checkbox>
          </div>
        </div>
      </div>
      <template #footer>
        <div class="dialog-footer">
          <el-button @click="EditDialogVisible = false">Cancel</el-button>
          <el-button type="primary" @click="onEditUser"> Confirm</el-button>
        </div>
      </template>
    </el-dialog>

    <el-dialog
      v-model="DeleteDialogVisible"
      align-center
      center
      draggable
      title="删除用户"
      width="700"
    >
      <el-dialog
        v-model="DeleteConfirmDialogVisible"
        append-to-body
        title="确认删除"
        width="500"
      >
        <div>确认删除用户 {{ SelectUser.username }} 吗？</div>

        <template #footer>
          <div class="dialog-footer">
            <el-button @click="DeleteConfirmDialogVisible = false">
              Cancel
            </el-button>
            <el-button type="primary" @click="onDeleteUser">
              Confirm
            </el-button>
          </div>
        </template>
      </el-dialog>
      <div class="max-w-[80%] mx-auto">
        <el-select
          v-model="SelectUser.id"
          class="py-2"
          placeholder="请选择用户"
          @change="onUpdateSelectedUser"
        >
          <el-option
            v-for="item in tableData"
            :key="item.id"
            :label="item.username"
            :value="item.id"
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
