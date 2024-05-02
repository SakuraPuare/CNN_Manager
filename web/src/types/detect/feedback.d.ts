import { Detail, Id, Pagination } from "../types";

export type Feedback = {
  id: number;
  user_id: number;
  detect_id: number;
  feedback: number;
  created_at: string;
  updated_at: string;
};

export type getFeedbackParams = Id;
export type getFeedbackResponse = Feedback;

export type getFeedbackListParams = Pagination;
export type getFeedbackListResponse = Feedback[];

export type postFeedbackParams = {
  detect_id: number;
  ground_truth: number;
};
export type postFeedbackResponse = Detail;

export type deleteFeedbackParams = Id;
export type deleteFeedbackResponse = Detail;
