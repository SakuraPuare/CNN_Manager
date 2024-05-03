import { PAGINATION } from "@/config";
import { postDetectParams, postDetectResponse } from "@/types/detect/detect";
import {
  deleteFeedbackParams,
  deleteFeedbackResponse,
  getFeedbackListParams,
  getFeedbackListResponse,
  getFeedbackParams,
  getFeedbackResponse,
  postFeedbackParams,
  postFeedbackResponse,
} from "@/types/detect/feedback";
import http from "@/utils/http";

export const getFeedbackAPI = async (
  params: getFeedbackParams,
): Promise<getFeedbackResponse> => {
  return http
    .get(`/detect/feedback/${params.id}`)
    .then((res) => res.data as Promise<getFeedbackResponse>);
};

export const getFeedbackListAPI = async (
  params: getFeedbackListParams = {
    page: 1,
    limit: PAGINATION,
  },
): Promise<getFeedbackListResponse> => {
  return http
    .get("/detect/feedback/list", { params })
    .then((res) => res.data as Promise<getFeedbackListResponse>);
};

export const postFeedbackAPI = async (
  params: postFeedbackParams,
): Promise<postFeedbackResponse> => {
  return http
    .post("/detect/feedback", null, { params })
    .then((res) => res.data as Promise<postFeedbackResponse>);
};

export const deleteFeedbackAPI = async (
  params: deleteFeedbackParams,
): Promise<deleteFeedbackResponse> => {
  return http
    .delete(`/detect/feedback/${params.id}`)
    .then((res) => res.data as Promise<deleteFeedbackResponse>);
};
