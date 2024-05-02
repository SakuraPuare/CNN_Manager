import http from "@/utils/http.ts";
import { DeleteDetectFeedbackParams } from "@/types/user/deleteDetectFeedback";

export const deleteDetectFeedbackAPI = (
  params: DeleteDetectFeedbackParams,
): Promise<any> => {
  return http({
    url: "/detect/feedback",
    method: "DELETE",
    params: params,
  }).then((res) => res.data as Promise<any>);
};
