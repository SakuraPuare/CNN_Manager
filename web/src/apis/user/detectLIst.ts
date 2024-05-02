import http from "@/utils/http.ts";

export const detectListAPI = (): Promise<any> => {
  return http({
    url: "/detect",
    method: "GET",
  }).then((res) => res.data as Promise<any>);
};
