import { Detail, Id, Pagination, User } from "../types";

export type createUser = {
  username: string;
  email: string;
  is_admin: boolean;
  password: string;
};

export type StringIdUser = createUser & {
  id: string;
};

export type getUserParams = Id;
export type getUserResponse = User;

export type getUserListParams = Pagination;
export type getUserListResponse = User[];

export type postUserParams = createUser;
export type postUserResponse = User;

export type putUserParams = Id & createUser;
export type putUserResponse = Detail;

export type deleteUserParams = Id;
export type deleteUserResponse = Detail;
