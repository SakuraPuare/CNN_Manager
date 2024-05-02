import http from "@/utils/http.ts";
import type { DeleteUserParams } from "@/types/admin/deleteUser";
import { DetailInfo } from "@/types/info";

export const deleteUserAPI = async (
  params: DeleteUserParams,
): Promise<DetailInfo> => {
  return http({
    url: "/admin/user/" + params.id,
    method: "DELETE",
  }).then((res) => res.data as Promise<DetailInfo>);
};
