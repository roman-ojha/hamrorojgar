import {
  CitizenAction,
  CitizenActionType,
  CitizenState,
  CitizenLoginStatusAction,
} from "./types";

const citizenState: CitizenState | null = null;

export const citizenReducer = (
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

const citizenLoginStatus: any = null;

export const citizenLoginStatusReducer = (
  state: typeof citizenLoginStatus = citizenLoginStatus,
  action: CitizenLoginStatusAction
): typeof citizenLoginStatus => {
  switch (action.type) {
    case CitizenActionType.CITIZEN_LOGIN_FAIL:
      return action.payload;
    default:
      return state;
  }
};
