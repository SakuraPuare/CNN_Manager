import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  persist: true,
  state: () => ({
    username: "",
    email: "",
    is_admin: false,
    token: "",
  }),
  getters: {
    getUsername(): string {
      return this.username;
    },
    getEmail(): string {
      return this.email;
    },
    getIsAdmin(): boolean {
      return this.is_admin;
    },
    getToken(): string {
      return this.token;
    },
  },
  actions: {
    login(info: { username: string; email: string; is_admin: boolean; token: string }) {
      this.username = info.username;
      this.email = info.email;
      this.is_admin = info.is_admin;
      this.token = info.token;
    },
    logout() {
      this.username = "";
      this.email = "";
      this.is_admin = false;
      this.token = "";
    },
    checkLogin() {
      return this.token !== "";
    },
  },
});
