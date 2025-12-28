import Navbar from "../components/Navbar";
import Footer from "../components/Footer";
import { Outlet } from "react-router-dom";

export default function MainLayout() {
  return (
    <>
      <Navbar />
      <main className="h-[80vh]">
        <Outlet />
      </main>
      <Footer />
    </>
  );
}
