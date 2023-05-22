import { Vacancy } from "@/models/vacancy";
import { AxiosResponse } from "axios";

export interface VacancyState extends Vacancy {}

export enum JobActiontype {
  STORE_VACANCIES = "STORE_VACANCIES",
}

export interface StoreVacancies {
  type: JobActiontype.STORE_VACANCIES;
  payload: Vacancy[];
}

export type JobAction = StoreVacancies;
