import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function ScannerFormPage() {
  const [codigo, setCodigo] = useState("");
  const navigate = useNavigate();

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    if (!codigo.trim()) return;

    navigate(`/scanner-result/${codigo}`);
  }

  return (
    <div style={{ maxWidth: 400, margin: "40px auto" }}>
      <h1>Diagnóstico Inicial MAS@FRAME®</h1>
      <p>Introduce el código que has recibido para comenzar tu diagnóstico.</p>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Código MAS®"
          value={codigo}
          onChange={(e) => setCodigo(e.target.value)}
          required
          style={{ width: "100%", marginBottom: 10 }}
        />

        <button type="submit" style={{ width: "100%" }}>
          Acceder al diagnóstico
        </button>
      </form>
    </div>
  );
}