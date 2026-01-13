// src/api/scanner.ts
const API = import.meta.env.VITE_API_URL;

export async function getScannerResult(codigo: string) {
  const res = await fetch(`${API}/scanner/result/${codigo}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data.detail || "Error al obtener resultado del scanner");
  }

  return data; // JSON contrato 6.4
}