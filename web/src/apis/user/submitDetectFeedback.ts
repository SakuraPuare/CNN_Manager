import http from "@/utils/http.ts";
import type { SubmitDetectFeedbackParams } from "@/types/user/submitDetectFeedback";

export const submitDetectFeedbackAPI = (
  params: SubmitDetectFeedbackParams,
): Promise<any> => {
  return http({
    url: "/detect/feedback",
    method: "POST",
    params: params,
  }).then((res) => res.data as Promise<any>);
};
