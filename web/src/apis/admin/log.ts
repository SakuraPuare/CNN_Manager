import http from "@/utils/http.ts";
import { getLogListParams, getLogListResponse } from "@/types/admin/log";

export const getLogListAPI = async (
  params: getLogListParams,
): Promise<getLogListResponse> => {
  return http.get("/admin/log", { params });
};
