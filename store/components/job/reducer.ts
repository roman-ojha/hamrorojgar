import { JobState, JobActionType, JobAction } from "./types";

const jobsState: JobState[] = [];
const jobState: JobState | null = null;

const jobsReducer = (
  state: typeof jobsState = jobsState,
  action: JobAction
): typeof jobsState => {
  switch (action.type) {
    case JobActionType.FETCH_JOBS:
      return action.payload;
    default:
      return state;
  }
};

export { jobsReducer };
