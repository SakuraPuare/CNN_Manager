<script lang="ts" setup>
import {
  faDatabase,
  faEye,
  faGear,
  faHome,
  faImage,
} from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
</script>

<template>
  <div class="max-w-[20%] w-[20%] h-full">
    <el-menu class="flex flex-col h-full">
      <router-link to="/">
        <el-menu-item>
          <el-icon>
            <font-awesome-icon :icon="faHome" />
          </el-icon>
          <template #title>主页</template>
        </el-menu-item>
      </router-link>
      <router-link to="/detect/">
        <el-menu-item>
          <el-icon>
            <font-awesome-icon :icon="faEye" />
          </el-icon>
          <template #title>检测图片</template>
        </el-menu-item>
      </router-link>
      <router-link to="/picture/">
        <el-menu-item>
          <el-icon>
            <font-awesome-icon :icon="faImage" />
          </el-icon>
          <template #title>图片管理</template>
        </el-menu-item>
      </router-link>
      <router-link to="/model/">
        <el-menu-item>
          <el-icon>
            <font-awesome-icon :icon="faDatabase" />
          </el-icon>
          <template #title>模型管理</template>
        </el-menu-item>
      </router-link>
      <router-link to="/admin/">
        <el-menu-item>
          <el-icon>
            <font-awesome-icon :icon="faGear" />
          </el-icon>
          <template #title>系统管理</template>
        </el-menu-item>
      </router-link>
    </el-menu>
  </div>
</template>

<style scoped></style>
