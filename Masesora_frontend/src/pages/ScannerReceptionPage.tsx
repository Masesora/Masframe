import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import styles from "./ScannerReceptionPage.module.css";
import "./ScannerReceptionPage.animations.css";

export default function ScannerReceptionPage() {
  const { codigo } = useParams();

  const [data, setData] = useState<any>(null);
  const [selectedSymptoms, setSelectedSymptoms] = useState<string[]>([]);
  const [error, setError] = useState("");

  // ============================================================
  // 1. Cargar datos desde el backend
  // ============================================================
  useEffect(() => {
    async function fetchData() {
      try {
        const res = await fetch(
          `${import.meta.env.VITE_API_URL}/scanner/result/${codigo}`
        );

        if (!res.ok) throw new Error("Backend no respondió");

        const json = await res.json();
        setData(json);

        const crit = json.preseleccion?.criticas || [];
        const rec = json.preseleccion?.recomendadas || [];
        setSelectedSymptoms([...crit, ...rec]);
      } catch {
        setError("No se pudo cargar el diagnóstico");
      }
    }

    fetchData();
  }, [codigo]);

  if (error) return <p className="error-box">{error}</p>;
  if (!data) return <p>Cargando...</p>;

  // ============================================================
  // 2. Manejo de selección de síntomas
  // ============================================================
  const toggleSymptom = (id: string) => {
    setSelectedSymptoms((prev) =>
      prev.includes(id) ? prev.filter((x) => x !== id) : [...prev, id]
    );
  };

  // ============================================================
  // 3. Cálculo del presupuesto dinámico (REESCRITO)
  // ============================================================
  const base = parseFloat(String(data?.presupuesto_base?.total ?? 0));

  const extra = (data?.sintomas ?? [])
    .filter((s: any) => selectedSymptoms.includes(s.id))
    .map((s: any) => Number(s.precio) || 0)
    .reduce((a: number, b: number) => a + b, 0);

  const total = base + extra;

  // ============================================================
  // 4. Render (REESCRITO)
  // ============================================================
  return (
    <div className={`${styles.scannerContainer} fadeIn`}>
      <h1>Recepción Clínica MAS@FRAME®</h1>

      {/* Narrativa */}
      <section className="narrativa fadeInSlow">
        <p>{data.narrativa?.bienvenida || ""}</p>
        <p>{data.narrativa?.diagnostico_inicial || ""}</p>
        <p>{data.narrativa?.clinica_te_acompana || ""}</p>
      </section>

      {/* Diagnóstico visual */}
      <section className="diagnostico-box fadeIn">
        <h2>Tu puerta clínica</h2>
        <div
          className="color-box"
          style={{
            backgroundColor: data?.diagnostico?.color || "#999",
            width: "120px",
            height: "120px",
            borderRadius: "12px",
          }}
        ></div>
        <h3>{data?.diagnostico?.nombre || "Sin diagnóstico"}</h3>
        <p>{data?.diagnostico?.descripcion || ""}</p>
      </section>

      {/* Especialidades */}
      <section className="fadeIn">
        <h2>Especialidades recomendadas</h2>
        {(data?.especialidades ?? []).length > 0 ? (
          data.especialidades.map((esp: any) => (
            <div key={esp.nombre} className="especialidad-card">
              <h3>{esp.nombre}</h3>
              <p>{esp.short_description || ""}</p>
              <p>{esp.narrative || ""}</p>
            </div>
          ))
        ) : (
          <p>No hay especialidades disponibles.</p>
        )}
      </section>

      {/* Síntomas */}
      <section className="fadeIn">
        <h2>Síntomas</h2>

        {(data?.sintomas ?? []).length === 0 && (
          <p>No hay síntomas disponibles.</p>
        )}

        <ul>
          {(data?.sintomas ?? []).map((s: any) => (
            <li key={s.id}>
              <label>
                <input
                  type="checkbox"
                  checked={selectedSymptoms.includes(s.id)}
                  onChange={() => toggleSymptom(s.id)}
                />
                {s.nombre || "Sin nombre"} — {s.precio || 0}€
                {s.critico && <strong> (crítico)</strong>}
              </label>
            </li>
          ))}
        </ul>
      </section>

      {/* Presupuesto */}
      <section className="presupuesto-box fadeIn">
        <h2>Presupuesto</h2>
        <p>Base: {base}€</p>
        <p>
          Total: <strong>{total}€</strong>
        </p>
      </section>

      <button className="btn-pago">Confirmar y pagar</button>
    </div>
  );
}