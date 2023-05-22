import { JobAction, JobActiontype , VacancyState} from "./types";
import { Dispatch } from "react";

export const storeVacancy = (data: VacancyState) => {
    return (dispatch: Dispatch<JobAction>) => {
        dispatch({
            type: JobActiontype.STORE_VACANCIES,
            payload: data,
        });
    }
}