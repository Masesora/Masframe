import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import ScannerReceptionPage from "./pages/ScannerReceptionPage";

// (Opcional) si mantienes estas páginas:
import ScannerFormPage from "./pages/ScannerFormPage";
// import ScannerResultPage from "./pages/ScannerResultPage"; // ❌ eliminar si no existe

export default function Router() {
  return (
    <BrowserRouter>
      <Routes>

        {/* PANTALLA 0 — Login */}
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<LoginPage />} />

        {/* CLIENTE — RECEPCIÓN CLÍNICA MAS@FRAME® */}
        <Route path="/scanner-reception/:codigo" element={<ScannerReceptionPage />} />

        {/* (Opcional) si aún usas el scanner antiguo */}
        <Route path="/scanner-form" element={<ScannerFormPage />} />
        {/* <Route path="/scanner-result" element={<ScannerResultPage />} /> */}

        {/* INTERNOS */}
        <Route path="/admin-dashboard" element={<div>Admin</div>} />
        <Route path="/cc-dashboard" element={<div>CC</div>} />
        <Route path="/aci-dashboard" element={<div>ACI</div>} />

      </Routes>
    </BrowserRouter>
  );
}