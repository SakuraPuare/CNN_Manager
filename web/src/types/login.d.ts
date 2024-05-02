import { User } from "@/types/types";

export type LoginParams = {
  username: string;
  password: string;
};

export type LoginResponse = User & {
  token: string;
};
