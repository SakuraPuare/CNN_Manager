import http from "@/utils/http.ts";
import { OrderNetworkParams } from "@/types/user/orderNetwork";

export const orderNetworkListAPI = (
  params: OrderNetworkParams,
): Promise<any> => {
  return http({
    url: "/network/" + params.network_id,
    method: "GET",
  }).then((res) => res.data as Promise<any>);
};
