import { AppState } from "@/store";
const jobSelector = (state: AppState) => state.jobReducer;
export { jobSelector };
