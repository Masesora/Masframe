// src/pages/LoginPage.tsx
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { loginCliente, loginInterno } from "../api/auth";

export default function LoginPage() {
  const navigate = useNavigate();

  const [modo, setModo] = useState<"cliente" | "interno">("cliente");
  const [email, setEmail] = useState("");
  const [codigo, setCodigo] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError("");

    try {
      if (modo === "cliente") {
        const data = await loginCliente(email, codigo);
        localStorage.setItem("token", data.token || "");
        localStorage.setItem("role", "cliente");
        localStorage.setItem("codigo", codigo);
        navigate(`/scanner-reception/${codigo}`);
      }

      if (modo === "interno") {
        const data = await loginInterno(email, password);
        localStorage.setItem("token", data.token || "");
        localStorage.setItem("role", data.role);
        if (data.role === "admin") navigate("/admin-dashboard");
        if (data.role === "cc") navigate("/cc-dashboard");
        if (data.role === "aci") navigate("/aci-dashboard");
      }
    } catch (err: any) {
      setError(err.message || "Error de acceso");
    }
  }

  return (
    <div className="login-container">
      <h1>Acceso MAS@FRAME®</h1>

      <div className="login-tabs">
        <label>
          <input
            type="radio"
            name="modo"
            value="cliente"
            checked={modo === "cliente"}
            onChange={() => setModo("cliente")}
          />
          Cliente
        </label>
        <label>
          <input
            type="radio"
            name="modo"
            value="interno"
            checked={modo === "interno"}
            onChange={() => setModo("interno")}
          />
          Interno
        </label>
      </div>

      <form onSubmit={handleSubmit} className="login-form">
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        {modo === "cliente" && (
          <input
            type="text"
            placeholder="Código MAS®"
            value={codigo}
            onChange={(e) => setCodigo(e.target.value)}
            required
          />
        )}

        {modo === "interno" && (
          <input
            type="password"
            placeholder="Contraseña"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        )}

        {error && <p className="login-error">{error}</p>}

        <button type="submit">Acceder</button>
      </form>
    </div>
  );
}