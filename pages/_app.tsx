import "../styles/base/reset.scss";
import type { AppProps } from "next/app";
import { Provider } from "react-redux";
import store from "@/store/store";
import {
  citizenSelector,
  CitizenState,
} from "@/store/components/citizen/selector";
import { useAppState } from "@/hooks/useAppState";
import { useEffect } from "react";

const AppComponent = ({ Component, pageProps }) => {
  const [{ getCitizen }, [citizen]] = useAppState<[CitizenState]>([
    citizenSelector,
  ]);
  useEffect(() => {
    getCitizen();
  }, []);
  return <Component {...pageProps} />;
};

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <Provider store={store}>
      <AppComponent Component={Component} pageProps={pageProps} />
    </Provider>
  );
}

export default MyApp;
