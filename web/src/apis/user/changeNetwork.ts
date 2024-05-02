import http from "@/utils/http.ts";

export const changeNetworkAPI = (params: any): Promise<any> => {
  return http({
    url: "/network/" + params.network_id,
    method: "PUT",
    data: params,
  }).then((res) => res.data as Promise<any>);
};
