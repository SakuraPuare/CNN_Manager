<script lang="ts" setup>
import {
  faClock,
  faCloud,
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
      <el-sub-menu index="2">
        <template #title>
          <el-icon>
            <font-awesome-icon :icon="faEye" />
          </el-icon>
          图像识别
        </template>
        <router-link to="/detect">
          <el-menu-item index="2-1">
            <el-icon>
              <font-awesome-icon :icon="faEye" />
            </el-icon>
            <template #title>图像检测</template>
          </el-menu-item>
        </router-link>
        <router-link to="/detect/history">
          <el-menu-item index="2-2">
            <el-icon>
              <font-awesome-icon :icon="faClock" />
            </el-icon>
            <template #title>历史记录</template>
          </el-menu-item>
        </router-link>
      </el-sub-menu>
      <el-sub-menu index="3">
        <template #title>
          <el-icon>
            <font-awesome-icon :icon="faImage" />
          </el-icon>
          图片管理
        </template>
        <router-link to="/image">
          <el-menu-item index="3-1">
            <el-icon>
              <font-awesome-icon :icon="faImage" />
            </el-icon>
            <template #title>图片查看</template>
          </el-menu-item>
        </router-link>
        <router-link to="/image/upload">
          <el-menu-item index="3-2">
            <el-icon>
              <font-awesome-icon :icon="faCloud" />
            </el-icon>
            <template #title>图片上传</template>
          </el-menu-item>
        </router-link>
      </el-sub-menu>
      <router-link to="/network">
        <el-menu-item>
          <el-icon>
            <font-awesome-icon :icon="faDatabase" />
          </el-icon>
          <template #title>模型管理</template>
        </el-menu-item>
      </router-link>
      <router-link to="/admin">
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
