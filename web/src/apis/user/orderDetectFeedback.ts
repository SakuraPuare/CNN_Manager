import http from "@/utils/http.ts";
import type { OrderDetectFeedbackParams } from "@/types/user/orderDetectFeedback";

export const orderDetectFeedbackAPI = (
  params: OrderDetectFeedbackParams,
): Promise<any> => {
  return http({
    url: "/detect/feedback/" + params.detect_id,
    method: "GET",
  }).then((res) => res.data as Promise<any>);
};
