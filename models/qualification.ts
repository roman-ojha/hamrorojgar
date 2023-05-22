import { Vacancy } from "./vacancy";

export interface Qualification {
  id: number;
  description: string;
  vacancy: Vacancy;
}
