import {
  CitizenActionType,
  CitizenAction,
  CitizenSignInFormType,
} from "./types";
import { Dispatch } from "redux";
import { api } from "@/services/api";
import { isOkResponse } from "@/utils/checkApiStatus";
import { setCookie, getCookie } from "@/utils/handleCookie";

export const loginCitizen = (data: CitizenSignInFormType) => {
  return async (dispatch: Dispatch<CitizenAction>) => {
    const res = await api.citizen.login(data);
    console.log(getCookie("auth"));
    if (res && isOkResponse(res.status)) {
      console.log(res.data);
      dispatch({
        type: CitizenActionType.STORE_AUTH_CITIZEN,
        payload: res.data,
      });
    }
  };
};
