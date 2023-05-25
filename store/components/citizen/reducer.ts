import {
  CitizenAction,
  CitizenActionType,
  CitizenState,
  CitizenLoginStatusAction,
  CitizenLoginStatusState,
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

export const citizenLoginStatus: CitizenLoginStatusState = {
  email: [],
  password: [],
  non_field_errors: [],
  is_logged_in: false,
};

export const citizenLoginStatusReducer = (
  state: typeof citizenLoginStatus = citizenLoginStatus,
  action: CitizenLoginStatusAction
): typeof citizenLoginStatus => {
  switch (action.type) {
    case CitizenActionType.CITIZEN_LOGIN_FAIL:
      return action.payload;
    case CitizenActionType.CITIZEN_LOGIN_SUCCESS:
      return action.payload;
    default:
      return state;
  }
};
