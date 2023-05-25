import { Citizen } from "@/models/citizen";
import { User } from "@/models/user";
import { Address } from "@/models/address";

export interface CitizenState extends Citizen {
  user: User;
  p_address: Address;
  t_address: Address;
  is_authenticated: boolean;
}

export interface CitizenSignInFormType {
  email: string;
  password: string;
}

export enum CitizenActionType {
  STORE_AUTH_CITIZEN = "STORE_AUTH_CITIZEN",
  CITIZEN_LOGIN_SUCCESS = "CITIZEN_LOGIN_SUCCESS",
  CITIZEN_LOGIN_FAIL = "CITIZEN_LOGIN_FAIL",
}

export interface StoreAuthCitizen {
  type: CitizenActionType.STORE_AUTH_CITIZEN;
  payload: CitizenState;
}

export interface CitizenLoginStatusState {
  email?: string[];
  password?: string[];
  non_field_errors?: string[];
  is_logged_in: boolean;
}

export interface CitizenLoginSuccess {
  type: CitizenActionType.CITIZEN_LOGIN_SUCCESS;
  payload: CitizenLoginStatusState;
}

export interface CitizenLoginFail {
  type: CitizenActionType.CITIZEN_LOGIN_FAIL;
  payload: CitizenLoginStatusState;
}

export type CitizenAction = StoreAuthCitizen;

export type CitizenLoginStatusAction = CitizenLoginSuccess | CitizenLoginFail;
