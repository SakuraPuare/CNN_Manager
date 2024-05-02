import http from "@/utils/http.ts";
import { getLogListParams, getLogListResponse } from "@/types/admin/log";
import { PAGINATION } from "@/config.ts";

export const getLogListAPI = async (
  params: getLogListParams = {
    page: 1,
    limit: PAGINATION,
  },
): Promise<getLogListResponse> => {
  return http
    .get("/admin/log", { params })
    .then((res) => res.data as Promise<getLogListResponse>);
};
