import { AppState } from "@/store";
export type { JobState } from "./types";
const jobsSelector = (state: AppState) => state.jobsReducer;
const jobSelector = (state: AppState) => state.jobReducer;
export { jobsSelector, jobSelector };
