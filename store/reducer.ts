import { combineReducers } from "redux";
import { jobsReducer, jobReducer } from "./components/job/reducer";
import {
  citizenReducer,
  citizenLoginStatusReducer,
} from "./components/citizen/reducer";

const reducer = combineReducers({
  jobsReducer,
  jobReducer,
  citizenReducer,
  citizenLoginStatusReducer,
});
export default reducer;
