import ReactDOM from "react-dom/client";
import 'bootstrap/dist/css/bootstrap.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import reportWebVitals from "./reportWebVitals";

import { ApolloProvider, ApolloClient, InMemoryCache } from "@apollo/client";

// Components
import Temp from "./routes/Temp/Temp";
import Invoices from "./routes/Temp/components/Invoices";
import Recipes from "./routes/Recipes/Recipes";


// TODO find a way to cleanly change the uri when accessing different apis (in the future)
const client = new ApolloClient({
  uri: process.env.REACT_APP_RECIPES_URI,
  cache: new InMemoryCache(),
});

const root = ReactDOM.createRoot(document.getElementById("root")!);

root.render(
  <ApolloProvider client={client}>
    <BrowserRouter>
      <Routes>
        {/* Let's be careful here, we may want to move to Switch routes based on changing requirements. */}
        <Route path="/" element={<Temp />}>
          <Route path="invoices" element={<Invoices />} />
          <Route
            path="*"
            element={
              <main style={{ padding: "1rem" }}>
                <p>There's nothing here!</p>
              </main>
            }
          />
        </Route>
        <Route path="/recipes" element={<Recipes />} />
      </Routes>
    </BrowserRouter>
  </ApolloProvider>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
