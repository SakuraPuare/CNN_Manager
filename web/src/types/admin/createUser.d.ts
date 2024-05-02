import type { RegisterParams } from "../register";

export type CreateUserParams = RegisterParams & {
  is_admin: boolean;
};
