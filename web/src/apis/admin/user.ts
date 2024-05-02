import {
  deleteUserParams,
  deleteUserResponse,
  getUserListParams,
  getUserListResponse,
  getUserParams,
  getUserResponse,
  postUserParams,
  postUserResponse,
  putUserParams,
  putUserResponse,
} from "@/types/admin/user";
import http from "@/utils/http";
import { PAGINATION } from "@/config.ts";

export const getUserAPI = async (
  params: getUserParams,
): Promise<getUserResponse> => {
  return http
    .get(`/admin/user/${params.id}`)
    .then((res) => res.data as Promise<getUserResponse>);
};

export const getUserListAPI = async (
  params: getUserListParams = {
    page: 1,
    limit: PAGINATION,
  },
): Promise<getUserListResponse> => {
  return http
    .get("/admin/user/list", { params })
    .then((res) => res.data as Promise<getUserListResponse>);
};

export const postUserAPI = async (
  params: postUserParams,
): Promise<postUserResponse> => {
  return http
    .post("/admin/user", { params })
    .then((res) => res.data as Promise<postUserResponse>);
};

export const putUserAPI = async (
  params: putUserParams,
): Promise<putUserResponse> => {
  const { id, ...rest } = params;
  return http
    .put(`/admin/user/${id}`, { rest })
    .then((res) => res.data as Promise<putUserResponse>);
};

export const deleteUserAPI = async (
  params: deleteUserParams,
): Promise<deleteUserResponse> => {
  return http
    .delete(`/admin/user/${params.id}`)
    .then((res) => res.data as Promise<deleteUserResponse>);
};
