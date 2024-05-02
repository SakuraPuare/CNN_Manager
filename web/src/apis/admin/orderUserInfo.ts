import http from "@/utils/http.ts";
import type { AllInfo } from "@/types/info";
import type { OrderUserInfoParams } from "@/types/admin/orderUserInfo";

export const orderUserInfoAPI = (
  params: OrderUserInfoParams,
): Promise<AllInfo> => {
  return http({
    url: "/admin/user/" + params.id,
    method: "GET",
  }).then((res) => res.data as Promise<AllInfo>);
};
