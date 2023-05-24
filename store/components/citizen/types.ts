import { Citizen } from "@/models/citizen";
import { User } from "@/models/user";
import { Address } from "@/models/address";

export interface CitizenState extends Citizen {
  user: User;
  p_address: Address;
  t_address: Address;
}

export interface CitizenSignInFormType {
  email: string;
  password: string;
}

export enum CitizenActionType {
  STORE_AUTH_CITIZEN = "STORE_AUTH_CITIZEN",
}

export interface StoreAuthCitizen {
  type: CitizenActionType.STORE_AUTH_CITIZEN;
  payload: CitizenState;
}
export type CitizenAction = StoreAuthCitizen;
