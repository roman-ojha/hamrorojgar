import { AppState } from "@/store";
export type { JobState } from "./types";
const jobsSelector = (state: AppState) => state.jobsReducer;
export { jobsSelector };
