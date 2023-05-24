import { AppState } from "@/store";
export type { CitizenState } from "./types";
const citizenSelector = (state: AppState) => state.citizenReducer;
export { citizenSelector };
