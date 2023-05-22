import reducer from "./reducer";
import store from "./store";
// export * as actionCreators from "./action";
// export * from "./middleware";
// export * from "./store";
export type AppState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
