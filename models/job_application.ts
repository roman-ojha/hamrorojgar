import { Citizen } from "./citizen";
import { Vacancy } from "./vacancy";

export interface JobApplication {
  id: number;
  cv: string;
  is_approved: boolean;
  citizen: Citizen;
  vacancy: Vacancy;
}
