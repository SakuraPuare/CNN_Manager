import {
  getDetectListParams,
  getDetectListResponse,
  getDetectParams,
  getDetectResponse,
  postDetectParams,
  postDetectResponse,
} from "@/types/detect/detect";
import http from "@/utils/http";
import { PAGINATION } from "@/config.ts";

export const getDetectAPI = async (
  params: getDetectParams
): Promise<getDetectResponse> => {
  return http
    .get(`/detect/${params.id}`)
    .then((res) => res.data as Promise<getDetectResponse>);
};

export const getDetectListAPI = async (
  params: getDetectListParams = {
    page: 1,
    limit: PAGINATION,
  }
): Promise<getDetectListResponse> => {
  return http
    .get("/detect/list", { params })
    .then((res) => res.data as Promise<getDetectListResponse>);
};

export const postDetectAPI = async (
  params: postDetectParams
): Promise<postDetectResponse> => {
  return http
    .post("/detect", null, { params })
    .then((res) => res.data as Promise<postDetectResponse>);
};
