import http from "@/utils/http.ts";
import { getFormData } from "@/utils/form.ts";
import type { LoginParams, LoginResponse } from "@/types/login";

export const loginAPI = async (params: LoginParams): Promise<LoginResponse> => {
  return http
    .post("/login", getFormData(params))
    .then((res) => res.data as Promise<LoginResponse>);
};
