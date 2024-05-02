import { Detail, Id, Pagination } from "@/types/types";

export type Network = {
  id: number;
  name: string;
  description: string;
  network: string;
  backend: string;
  catalog: string;
  created_at: string;
  updated_at: string;
};

export type StringIdNetwork = {
  id: string;
  name: string;
  description: string;
  network: string;
  backend: string;
  catalog: string;
  created_at: string;
  updated_at: string;
};

export type getNetworkParams = Id;
export type getNetworkResponse = Network;

export type getNetworkListParams = Pagination;
export type getNetworkListResponse = Network[];

export type postNetworkParams = {
  name: string;
  description: string;
  network: string;
  backend: string;
  catalog: string;
};
export type postNetworkResponse = Network;

export type putNetworkParams = Id & postNetworkParams;
export type putNetworkResponse = Detail;

export type deleteNetworkParams = Id;
export type deleteNetworkResponse = Detail;
