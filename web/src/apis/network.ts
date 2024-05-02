import {
  deleteNetworkParams,
  deleteNetworkResponse,
  getNetworkListParams,
  getNetworkListResponse,
  getNetworkParams,
  getNetworkResponse,
  postNetworkParams,
  postNetworkResponse,
  putNetworkParams,
  putNetworkResponse,
} from "@/types/network";
import http from "@/utils/http";
import { PAGINATION } from "@/config.ts";

export const getNetworkAPI = (
  params: getNetworkParams,
): Promise<getNetworkResponse> => {
  return http
    .get(`/network/${params.id}`)
    .then((res) => res.data as Promise<getNetworkResponse>);
};

export const getNetworkListAPI = (
  params: getNetworkListParams = {
    page: 1,
    limit: PAGINATION,
  },
): Promise<getNetworkListResponse> => {
  return http
    .get("/network/list", { params })
    .then((res) => res.data as Promise<getNetworkListResponse>);
};

export const postNetworkAPI = (
  params: postNetworkParams,
): Promise<postNetworkResponse> => {
  return http
    .post("/network", { params })
    .then((res) => res.data as Promise<postNetworkResponse>);
};

export const putNetworkAPI = (
  params: putNetworkParams,
): Promise<putNetworkResponse> => {
  const { id, ...rest } = params;
  return http
    .put(`/network/${id}`, { rest })
    .then((res) => res.data as Promise<putNetworkResponse>);
};

export const deleteNetworkAPI = (
  params: deleteNetworkParams,
): Promise<deleteNetworkResponse> => {
  return http
    .delete(`/network/${params.id}`)
    .then((res) => res.data as Promise<deleteNetworkResponse>);
};
