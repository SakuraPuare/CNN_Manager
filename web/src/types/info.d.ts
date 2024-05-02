export type DetailInfo = {
  detail: string;
};


export type AllInfo = {
  id: number;
  username: string;
  is_admin: boolean;
  email: string;
  create_at: string;
  update_at: string;
  token: string;
};

export type StoreInfo = {
  username: string;
  email: string;
  is_admin: boolean;
  token: string;
};

export type UserInfo = {
  id: number;
  username: string;
  is_admin: boolean;
  email: string;
  create_at: string;
  update_at: string;
};

export type SelectUserInfo = {
  id: string;
  username: string;
  password: string;
  is_admin: boolean;
  email: string;
};

export type UpdateUserInfo = {
  username: string;
  password: string;
  is_admin: boolean;
  email: string;
};