import {
  getImageListParams,
  getImageListResponse,
  postImageParams,
  postImageResponse,
} from "@/types/image";
import http from "@/utils/http";

export const getImageListAPI = async (
  params: getImageListParams,
): Promise<getImageListResponse> => {
  return http
    .get("/image", { params })
    .then((res) => res.data as Promise<getImageListResponse>);
};

export const postImageAPI = async (
  data: postImageParams,
): Promise<postImageResponse> => {
  return http.post("/image", data).then((res) => res.data as postImageResponse);
};
