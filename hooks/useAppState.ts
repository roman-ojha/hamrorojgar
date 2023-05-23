import { useDispatch, useSelector } from "react-redux";
import { bindActionCreators } from "redux";
import { actionCreators } from "@/store";
import { AppState } from "@/store";

type SelectorType = (state: AppState) => any;

const useAppState = <R>(
  selectors: SelectorType[]
): [typeof actionCreators, R] => {
  const actions = bindActionCreators(actionCreators, useDispatch());

  // eslint-disable-next-line react-hooks/rules-of-hooks
  const state = selectors.map((selector) => useSelector(selector)) as R;

  return [actions, state];
};

export { useAppState };
