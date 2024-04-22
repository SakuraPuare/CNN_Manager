import { defineStore } from "pinia";
import { UserState } from "../types/user.ts";

export const useUserStore = defineStore("user", {
  persist: true,
  state: (): UserState => ({
    username: "",
    is_admin: false,
    token: "",
  }),
  getters: {
    getUsername(): string {
      return this.username;
    },
    getIsAdmin(): boolean {
      return this.is_admin;
    },
    getToken(): string {
      return this.token;
    },
  },
  actions: {
    login(data: { username: string; is_admin: boolean; token: string }) {
      this.username = data.username;
      this.is_admin = data.is_admin;
      this.token = data.token;
    },
    logout() {
      this.username = "";
      this.is_admin = false;
      this.token = "";
    },
    checkLogin() {
      return this.token !== "";
    },
  },
});
