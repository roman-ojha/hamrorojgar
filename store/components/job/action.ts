import { JobsAction, JobActionType, JobState, JobAction } from "./types";
import { Dispatch } from "redux";
import { api } from "@/services/api";
import { isOkResponse } from "@/utils/checkStatus";

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
