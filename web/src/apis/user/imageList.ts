import http from "@/utils/http.ts";

export const imageListAPI = (): Promise<any> => {
  return http({
    url: "/image/list",
    method: "GET",
  }).then((res) => res.data as Promise<any>);
};
