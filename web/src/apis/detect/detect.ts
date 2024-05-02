import {
  getDetectListParams,
  getDetectListResponse,
  postDetectParams,
  postDetectResponse,
} from "@/types/detect/detect";
import http from "@/utils/http";

export const getDetectListAPI = async (
  params: getDetectListParams,
): Promise<getDetectListResponse> => {
  return http
    .get("/detect/list", { params })
    .then((res) => res.data as Promise<getDetectListResponse>);
};

export const postDetectAPI = async (
  params: postDetectParams,
): Promise<postDetectResponse> => {
  return http
    .post("/detect", { params })
    .then((res) => res.data as Promise<postDetectResponse>);
};
