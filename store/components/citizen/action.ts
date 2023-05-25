import {
  CitizenActionType,
  CitizenAction,
  CitizenSignInFormType,
  CitizenLoginStatusAction,
} from "./types";
import { Dispatch } from "redux";
import { api } from "@/services/api";
import { isOkResponse } from "@/utils/checkApiStatus";
import { citizenLoginStatus } from "./reducer";

export const loginCitizen = (data: CitizenSignInFormType) => {
  return async (
    dispatch: Dispatch<CitizenAction | CitizenLoginStatusAction>
  ) => {
    const res = await api.citizen.login(data);
    if (res && isOkResponse(res.status)) {
      dispatch({
        type: CitizenActionType.STORE_AUTH_CITIZEN,
        payload: {
          is_authenticated: true,
          ...res.data,
        },
      });
      dispatch({
        type: CitizenActionType.CITIZEN_LOGIN_SUCCESS,
        payload: { is_logged_in: true },
      });
    } else if (res) {
      dispatch({
        type: CitizenActionType.CITIZEN_LOGIN_FAIL,
        payload: {
          is_logged_in: false,
          ...res.data,
        },
      });
    }
  };
};

export const resetLoginStatus = () => {
  return (dispatch: Dispatch<CitizenLoginStatusAction>) => {
    dispatch({
      type: CitizenActionType.CITIZEN_LOGIN_SUCCESS,
      payload: citizenLoginStatus,
    });
  };
};

export const getCitizen = () => {
  return async (dispatch: Dispatch<CitizenAction>) => {
    const res = await api.citizen.get();
    if (res && isOkResponse(res.status)) {
      dispatch({
        type: CitizenActionType.STORE_AUTH_CITIZEN,
        payload: {
          is_authenticated: true,
          ...res.data,
        },
      });
    }
  };
};
