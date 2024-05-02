import http from "@/utils/http.ts";
import type { uploadImageParams } from "@/types/user/uploadImage";

export const uploadImageAPI = (params: uploadImageParams): Promise<any> => {
  return http({
    url: "/image/upload",
    method: "POST",
    data: params,
  }).then((res) => res.data as Promise<any>);
};
