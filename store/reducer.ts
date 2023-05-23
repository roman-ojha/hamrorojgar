import { combineReducers } from "redux";
import { jobsReducer, jobReducer } from "./components/job/reducer";

const reducer = combineReducers({ jobsReducer, jobReducer });
export default reducer;
