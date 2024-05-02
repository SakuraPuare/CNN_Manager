import http from "@/utils/http.ts";
import type { DetectImageParams } from "@/types/user/detectImage";

export const detectImageAPI = (params: DetectImageParams): Promise<any> => {
  return http({
    url: "/detect",
    method: "POST",
    data: params,
  }).then((res) => res.data as Promise<any>);
};
