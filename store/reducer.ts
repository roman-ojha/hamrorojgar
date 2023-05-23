import { combineReducers } from "redux";
import { jobsReducer } from "./components/job/reducer";

const reducer = combineReducers({ jobsReducer });
export default reducer;
