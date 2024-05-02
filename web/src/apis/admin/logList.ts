import http from "@/utils/http.ts";
import type { LogListParams } from "@/types/admin/logList";

export const logListAPI = (params: LogListParams): Promise<any> => {
  return http({
    url: "/admin/log/list",
    method: "GET",
    params: params,
  }).then((res) => res.data as Promise<any>);
};
