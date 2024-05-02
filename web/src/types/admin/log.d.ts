import { Pagination } from "@/types";

export type getLogListParams = Pagination;

export type Log = {
  id: number;
  user_id: number;
  action: string;
  created_at: string;
  updated_at: string;
};

export type LogList = Log[];

export type getLogListResponse = LogList;
