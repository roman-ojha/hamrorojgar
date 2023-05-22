import { User } from "./user";

type GovernmentType = "Federal" | "Province" | "Local";

export interface Government {
  id: number;
  user: User;
  gov_type: GovernmentType;
  location: string;
  //   contact_no: number;
}
