import http from "@/utils/http.ts";

export const deleteNetworkAPI = (params: any): Promise<any> => {
  return http({
    url: "/network/" + params.network_id,
    method: "POST",
  }).then((res) => res.data as Promise<any>);
};
