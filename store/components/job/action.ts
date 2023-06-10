import { JobsAction, JobActionType, JobState, JobAction } from "./types";
import { Dispatch } from "redux";
import { api } from "@/services/api";
import { isOkResponse } from "@/utils/checkApiStatus";

export const fetchJobs = () => {
  return async (dispatch: Dispatch<JobsAction>) => {
    const res = await api.jobs.get();
    if (res && isOkResponse(res.status)) {
      dispatch({
        type: JobActionType.FETCH_JOBS,
        payload: res.data as JobState[],
      });
    }
  };
};

export const storeJobs = (jobs: JobState[]) => {
  return async (dispatch: Dispatch<JobsAction>) => {
    dispatch({
      type: JobActionType.STORE_JOBS,
      payload: jobs,
    });
  };
};

export const fetchJob = (id: number) => {
  return async (dispatch: Dispatch<JobAction>) => {
    const res = await api.jobs.get(id);
    if (res && isOkResponse(res.status)) {
      dispatch({
        type: JobActionType.FETCH_JOB,
        payload: res.data as JobState,
      });
    }
  };
};
