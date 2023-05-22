import { JobAction, JobActiontype , VacancyState} from "./types";
import { Dispatch } from "redux";
import { createAsyncThunk } from "@reduxjs/toolkit";
import { api } from "@/services/api";

export const storeVacancy = () => {
    return async (dispatch: Dispatch<JobAction>) => {
        dispatch({
            type: JobActiontype.STORE_VACANCIES,
            payload: await api.vacancy.get(),
        });
    }
}