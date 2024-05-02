<script setup>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { faGithub } from "@fortawesome/free-brands-svg-icons";
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { useUserStore } from "@/stores/user.ts";
import router from "@/utils/router.ts";

const user = useUserStore();

const logout = () => {
  user.logout();

  router.push("/login");
};
</script>

<template>
  <header
    id="header"
    class="px-[5%] h-16 text-white bg-blue-500 flex flex-row space-x-8 text-center items-center justify-center"
  >
    <img alt="logo" class="h-8 w-8" src="/vite.svg" />
    <router-link to="/">
      <span class="text-xl font-bold">CNN图像识别系统</span>
    </router-link>
    <div class="flex-grow"></div>
    <div class="flex flex-row items-center justify-center space-x-8">
      <span>
        <a href="https://github.com/">
          <font-awesome-icon :icon="faGithub" class="h-6 w-6" />
        </a>
      </span>

      <span v-if="user.checkLogin()">
        <el-popover :width="200" placement="bottom" trigger="click">
          <div class="text-center">
            <div>
              {{ user.username }}
            </div>
            <el-button type="text" @click="logout">退出</el-button>
          </div>
          <template #reference>
            <font-awesome-icon :icon="faUser" class="h-6 w-6" />
          </template>
        </el-popover>
      </span>
      <span v-else>
        <router-link to="/login">登陆</router-link>
      </span>
    </div>
  </header>
</template>

<style scoped></style>
