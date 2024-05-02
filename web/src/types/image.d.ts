import { Pagination } from "./types";

export type Image = {
  id: number;
  user_id: number;
  name: string;
  description: string | null;
  image_hash: string;
  height: number;
  width: number;
  file_size: number;
  type: string;
  created_at: string;
  updated_at: string;
};

export type getImageListParams = Pagination;
export type getImageListResponse = Image[];

export type postImageParams = {
  file: File;
};
export type postImageResponse = Image;
