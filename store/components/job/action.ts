import { JobsAction, JobActionType, JobState, JobAction } from "./types";
import { Dispatch } from "redux";
import { api } from "@/services/api";

export const fetchJobs = () => {
  return async (dispatch: Dispatch<JobsAction>) => {
    const data = (await api.jobs.get()).data;
    dispatch({
      type: JobActionType.FETCH_JOBS,
      payload: data as JobState[],
    });
  };
};

export const fetchJob = (id: number) => {
  return async (dispatch: Dispatch<JobAction>) => {
    const data = (await api.jobs.get(id)).data;
    dispatch({
      type: JobActionType.FETCH_JOB,
      payload: data as JobState,
    });
  };
};
