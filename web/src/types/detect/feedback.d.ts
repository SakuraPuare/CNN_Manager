import { Detail, Id, Pagination } from "../types";

export type Feedback = {
  id: number;
  user_id: number;
  detect_id: number;
  feedback: number;
  created_at: string;
  updated_at: string;
};
export type StringIdFeedback = {
  id: string;
  detect_id: string;
  feedback: string;
};

export type getFeedbackParams = Id;
export type getFeedbackResponse = Feedback;

export type getFeedbackListParams = Pagination;
export type getFeedbackListResponse = Feedback[];

export type postFeedbackParams = {
  detect_id: number;
  ground_truth: number;
};
export type postFeedbackResponse = Feedback;


export type deleteFeedbackParams = Id;
export type deleteFeedbackResponse = Detail;
