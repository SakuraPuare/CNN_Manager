import http from "@/utils/http.ts";
import type { AllInfo } from "@/types/info";
import { getFormData } from "@/utils/form.ts";
import type { LoginParams } from "@/types/login";

export const loginAPI = (params: LoginParams): Promise<AllInfo> => {
  const form = getFormData(params);
  return http({
    url: "/login",
    method: "POST",
    data: form,
  }).then((res) => res.data as Promise<AllInfo>);
};
