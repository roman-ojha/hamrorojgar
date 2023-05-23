import { JobState, JobActionType, JobsAction, JobAction } from "./types";

const jobsState: JobState[] = [];
const jobState: JobState | null = null;

const jobsReducer = (
  state: typeof jobsState = jobsState,
  action: JobsAction
): typeof jobsState => {
  switch (action.type) {
    case JobActionType.FETCH_JOBS:
      return action.payload;
    default:
      return state;
  }
};

const jobReducer = (
  state: typeof jobState = jobState,
  action: JobAction
): JobState | null => {
  switch (action.type) {
    case JobActionType.FETCH_JOB:
      return action.payload;
    default:
      return state;
  }
};

export { jobsReducer, jobReducer };
