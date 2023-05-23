import { JobState, JobActionType, JobAction } from "./types";

const initialState: JobState[] = [];

const jobReducer = (
  state: typeof initialState = initialState,
  action: JobAction
): typeof initialState => {
  switch (action.type) {
    case JobActionType.FETCH_JOBS:
      return action.payload;
    default:
      return state;
  }
};

export { jobReducer };
