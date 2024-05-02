import {
  getImageListParams,
  getImageListResponse,
  postImageParams,
  postImageResponse,
} from "@/types/image";
import { getFormData } from "@/utils/form";
import http from "@/utils/http";

export const getImageListAPI = async (
  params: getImageListParams,
): Promise<getImageListResponse> => {
  return http
    .get("/image", { params })
    .then((res) => res.data as Promise<getImageListResponse>);
};

export const postImageAPI = async (
  params: postImageParams,
): Promise<postImageResponse> => {
  return http
    .post("/image", getFormData(params))
    .then((res) => res.data as Promise<postImageResponse>);
};
