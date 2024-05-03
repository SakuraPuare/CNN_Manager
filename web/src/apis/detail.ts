import { DetailResponse } from "@/types/detail";
import http from "@/utils/http";

export const DetailAPI = async (): Promise<DetailResponse> => {
  return http.get("/detect").then((res) => res.data as Promise<DetailResponse>);
};
