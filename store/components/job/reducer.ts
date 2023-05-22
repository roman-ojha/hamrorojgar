import { VacancyState, JobActiontype, JobAction } from "./types";

const initialState: VacancyState[] = [];

const storeVacancyReducer = (
  state: VacancyState[] = initialState,
  action: JobAction
): VacancyState[] => {
  switch (action.type) {
    case JobActiontype.STORE_VACANCIES:
      return action.payload;
    default:
      return state;
  }
};

export { storeVacancyReducer };
