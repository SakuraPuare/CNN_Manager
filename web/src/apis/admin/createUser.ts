import http from "@/utils/http.ts";
import type { UpdateUserInfo } from "@/types/info";
import type { CreateUserParams } from "@/types/admin/createUser";

export const createUserAPI = (
  params: CreateUserParams,
): Promise<UpdateUserInfo> => {
  return http({
    url: "/admin/user/create",
    method: "POST",
    data: params,
  }).then((res) => res.data as Promise<UpdateUserInfo>);
};
