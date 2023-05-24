import {
  CitizenActionType,
  CitizenAction,
  CitizenSignInFormType,
} from "./types";
import { Dispatch } from "redux";
import { api } from "@/services/api";
import { isOkResponse } from "@/utils/checkApiStatus";

export const loginCitizen = (data: CitizenSignInFormType) => {
  return async (dispatch: Dispatch<CitizenAction>) => {
    const res = await api.citizen.login(data);
    if (res && isOkResponse(res.status)) {
      dispatch({
        type: CitizenActionType.STORE_AUTH_CITIZEN,
        payload: res.data,
      });
    }
  };
};

export const getCitizen = () => {
  return async (dispatch: Dispatch<CitizenAction>) => {
    const res = await api.citizen.get();
    if (res && isOkResponse(res.status)) {
      console.log(res.data);
      dispatch({
        type: CitizenActionType.STORE_AUTH_CITIZEN,
        payload: res.data,
      });
    }
  };
};
