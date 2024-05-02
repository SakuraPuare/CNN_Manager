import http from "@/utils/http.ts";
import type { AllInfo } from "@/types/info";
import { UserInfoListParams } from "@/types/admin/userInfoList";

export const userInfoListAPI = (
  params: UserInfoListParams,
): Promise<AllInfo[]> => {
  return http({
    url: "/admin/user/list",
    method: "GET",
    params: params,
  }).then((res) => res.data as Promise<AllInfo[]>);
};
