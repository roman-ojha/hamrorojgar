import { combineReducers } from "redux";
import { jobsReducer, jobReducer } from "./components/job/reducer";
import { citizenReducer } from "./components/citizen/reducer";

const reducer = combineReducers({ jobsReducer, jobReducer, citizenReducer });
export default reducer;
