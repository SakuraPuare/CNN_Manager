import { defineStore } from "pinia";

interface UserState {
  username: string;
  is_admin: boolean;
  token: string;
}

export const useUserStore = defineStore("user", {
  state: (): UserState => ({
    username: "",
    is_admin: false,
    token: "",
  }),
  actions: {
    login(name: string, is_admin: boolean, token: string) {
      this.username = name;
      this.is_admin = is_admin;
      this.token = token;
    },
    logout() {
      this.username = "";
      this.is_admin = false;
      this.token = "";
    },
    checkLogin() {
      return this.token !== "";
    },
    getters: {
      token() {
        return this.token;
      },
      username() {
        return this.username;
      },
      is_admin() {
        return this.is_admin;
      },
    },
    setters: {
      setToken(token: string) {
        this.token = token;
      },
      setUserName(name: string) {
        this.username = name;
      },
      setIsAdmin(is_admin: boolean) {
        this.is_admin = is_admin;
      },
    },
  },
  persist: true,
});
