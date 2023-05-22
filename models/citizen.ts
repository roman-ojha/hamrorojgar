import { User } from "./user";
import { Address } from "./address";

type GenderType = "Male" | "Female" | "Others";

export interface Citizen {
  id: number;
  user: User;
  f_name: string;
  m_name: string;
  l_name: string;
  mobile: number;
  date_of_birth: string;
  gender: GenderType;
  nationality: string;
  citizenship_no: string;
  photo: string;
  p_address: Address;
  t_address: Address;
}
