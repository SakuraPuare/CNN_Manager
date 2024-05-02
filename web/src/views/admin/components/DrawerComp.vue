<script lang="ts" setup>
import { faHome, faList } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
</script>

<template>
  <div class="max-w-[20%] w-[20%] h-full">
    <el-menu class="flex flex-col h-full">
      <router-link to="/admin/">
        <el-menu-item>
          <el-icon>
            <font-awesome-icon :icon="faHome" />
          </el-icon>
          <template #title>系统管理</template>
        </el-menu-item>
      </router-link>
      <router-link to="/admin/user">
        <el-menu-item>
          <el-icon>
            <font-awesome-icon :icon="faList" />
          </el-icon>
          <template #title>用户管理</template>
        </el-menu-item>
        <!--          <el-sub-menu index="2-4">-->
        <!--            <template #title>-->
        <!--              <el-icon>-->
        <!--                <font-awesome-icon :icon="faList" />-->
        <!--              </el-icon>-->
        <!--              用户管理-->
        <!--            </template>-->

        <!--            <el-menu-item index="2-4-2">item two</el-menu-item>-->
        <!--            <el-menu-item index="2-4-3">item three</el-menu-item>-->
        <!--          </el-sub-menu>-->
      </router-link>
    </el-menu>
  </div>
</template>

<style scoped></style>
