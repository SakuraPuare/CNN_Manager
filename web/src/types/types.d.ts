export type Pagination = {
  page: number;
  limit: number;
};

export type Id = {
  id: number;
};

export type Detail = {
  detail: string;
};

export type User = {
  id: number;
  username: string;
  email: string;
  is_admin: boolean;
  created_at: string;
  updated_at: string;
};

export type UserBase = {
  username: string;
  email: string;
  is_admin: boolean;
};