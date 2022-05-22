import ReactDOM from "react-dom/client";
import reportWebVitals from "./reportWebVitals";

import {
  ApolloProvider,
  createHttpLink,
  ApolloClient,
  InMemoryCache,
} from "@apollo/client";
import { setContext } from "@apollo/client/link/context";
import { getCookie } from "typescript-cookie";

import Temp from "./components/Temp/Temp";

const httpLink = createHttpLink({
  uri: "http://127.0.0.1:8080/graphql/",
});

const authLink = setContext((_, { headers }) => {
  return {
    headers: {
      ...headers,
      "x-csrftoken": getCookie("csrftoken"),
    },
  };
});

const client = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache(),
});

const root = ReactDOM.createRoot(document.getElementById("root")!);

root.render(
  <ApolloProvider client={client}>
    <Temp />
  </ApolloProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
