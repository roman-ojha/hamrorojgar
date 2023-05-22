import { Vacancy } from "@/models/vacancy";

export interface VacancyState extends Vacancy { }

export enum JobActiontype {
    STORE_VACANCIES = "STORE_VACANCIES",
}

export interface StoreVacancies {
    type: JobActiontype.STORE_VACANCIES;
    payload: VacancyState;
}

export type JobAction = StoreVacancies;