import { AppState } from "@/store";
export type { JobState } from "./types";
const jobSelector = (state: AppState) => state.jobReducer;
export { jobSelector };
