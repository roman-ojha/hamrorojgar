import { configureStore, applyMiddleware } from "@reduxjs/toolkit";
import reducer from "./reducer";
import thunkMiddleware from 'redux-thunk';

const store = configureStore({
    reducer,
    middleware: [thunkMiddleware],
});

export default store;
