// src/api/auth.ts
const API = import.meta.env.VITE_API_URL;

export async function loginCliente(email: string, codigo: string) {
  const res = await fetch(`${API}/auth/login/cliente`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, codigo }),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || "Acceso cliente inválido");
  return data;
}

export async function loginInterno(email: string, password: string) {
  const res = await fetch(`${API}/auth/login/interno`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password }),
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || "Acceso interno inválido");
  return data;
}