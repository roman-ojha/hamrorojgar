import { combineReducers } from "redux";
import { storeVacancyReducer } from "./components/job/reducer";

const reducer = combineReducers({ storeVacancyReducer });
export default reducer;
