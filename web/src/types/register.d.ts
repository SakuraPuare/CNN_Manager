import { User } from "@/types/user";

export type RegisterParams = {
  username: string;
  email: string;
  password: string;
};
export type RegisterResponse = User;
