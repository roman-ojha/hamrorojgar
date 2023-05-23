import { combineReducers } from "redux";
import { jobReducer } from "./components/job/reducer";

const reducer = combineReducers({ jobReducer });
export default reducer;
