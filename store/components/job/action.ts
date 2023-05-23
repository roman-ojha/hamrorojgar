import { JobAction, JobActionType, JobState } from "./types";
import { Dispatch } from "redux";
import { api } from "@/services/api";

export const fetchJobs = () => {
  return async (dispatch: Dispatch<JobAction>) => {
    const data = (await api.jobs.get()).data;
    dispatch({
      type: JobActionType.FETCH_JOBS,
      payload: data,
    });
  };
};
