import http from "@/utils/http.ts";

export const networkListAPI = (): Promise<any> => {
  return http({
    url: "/network/",
    method: "GET",
  }).then((res) => res.data as Promise<any>);
};
