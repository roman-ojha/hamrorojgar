import { AppState } from "@/store";
export type { CitizenState, CitizenLoginStatusState } from "./types";
const citizenSelector = (state: AppState) => state.citizenReducer;
const citizenLoginStatusSelector = (state: AppState) =>
  state.citizenLoginStatusReducer;
export { citizenSelector, citizenLoginStatusSelector };
