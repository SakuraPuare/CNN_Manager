import { Pagination } from "../types";

export type Detect = {
  id: number;
  user_id: number;
  image_id: number;
  network_id: number;
  output: number;
  confidence: number;
  created_at: string;
  updated_at: string;
};

export type getDetectParams = Id;
export type getDetectResponse = Detect;

export type getDetectListParams = Pagination;
export type getDetectListResponse = Detect[];

export type postDetectParams = {
  hash: string;
  model_id: number;
};
export type postDetectResponse = {
  predicted: number;
  probability: number[];
  labels: string[];
};
