import http from "@/utils/http.ts";
import type { RegisterParams, RegisterResponse } from "@/types/register";

export const registerAPI = (
  params: RegisterParams,
): Promise<RegisterResponse> => {
  return http
    .post("/register", params)
    .then((res) => res.data as Promise<RegisterResponse>);
};
