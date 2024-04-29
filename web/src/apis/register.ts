import http from "@/utils/http.ts";
import type { AllInfo } from "@/types/info";
import type { RegisterParams } from "@/types/register";

export const registerAPI = (params: RegisterParams): Promise<AllInfo> => {
  return http({
    url: "/register",
    method: "POST",
    data: params,
  }).then((res) => res.data as Promise<AllInfo>);
};
