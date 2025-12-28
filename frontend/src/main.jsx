import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter,Route } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import Home from "./pages/Home"
import Scorecards from "./pages/Scorecards"

export default function App() {
  <>
    <Route element={<MainLayout />}>
      <Route path="/" element={<Home />} />
      <Route path="/scorecards" element={<Scorecards />} />
    </Route>
  </>;
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </React.StrictMode>
);
