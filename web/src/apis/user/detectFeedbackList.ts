import http from "@/utils/http.ts";
import type { DetectFeedbackListParams } from "@/types/user/detectFeedbackList";

export const detectFeedbackListAPI = (
  params: DetectFeedbackListParams,
): Promise<any> => {
  return http({
    url: "/detect/feedback",
    method: "GET",
    params: params,
  }).then((res) => res.data as Promise<any>);
};
