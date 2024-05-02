import http from "@/utils/http.ts";

export const addNetworkAPI = (): Promise<any> => {
  return http({
    url: "/network/",
    method: "POST",
  }).then((res) => res.data as Promise<any>);
};
