import { CitizenAction, CitizenActionType, CitizenState } from "./types";

const citizenState: CitizenState | null = null;

const citizenReducer = (
  state: typeof citizenState = citizenState,
  action: CitizenAction
): CitizenState | null => {
  switch (action.type) {
    case CitizenActionType.STORE_AUTH_CITIZEN:
      return action.payload;
    default:
      return state;
  }
};

export { citizenReducer };
