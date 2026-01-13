import React, { useState } from "react";

interface Symptom {
  id: string;
  name: string;
  description: string;
  question?: string;
  domain?: string;
  selected: boolean;
}

interface Especialidad {
  nombre: string;
  color: "rojo" | "ambar" | "verde";
  short_description: string;
  narrative: string;
  objetivos: string[];
  department: string;
  sintomas: Symptom[];
}

const SpecialtyDoor = ({ especialidad }: { especialidad: Especialidad }) => {
  const [sintomas, setSintomas] = useState<Symptom[]>(especialidad.sintomas);

  const toggleSymptom = (id: string) => {
    setSintomas((prev: Symptom[]) =>
      prev.map((s: Symptom) =>
        s.id === id ? { ...s, selected: !s.selected } : s
      )
    );
  };

  const colorMap: Record<Especialidad["color"], string> = {
    rojo: "#ff4d4f",
    ambar: "#faad14",
    verde: "#52c41a"
  };

  return (
    <div style={{ ...styles.card, borderLeft: `10px solid ${colorMap[especialidad.color]}` }}>
      <h2 style={styles.title}>{especialidad.nombre}</h2>
      <p style={styles.short}>{especialidad.short_description}</p>
      <p style={styles.narrative}>{especialidad.narrative}</p>

      <h3 style={styles.subtitle}>Objetivos</h3>
      <ul>
        {especialidad.objetivos.map((o, i) => (
          <li key={i}>{o}</li>
        ))}
      </ul>

      <h3 style={styles.subtitle}>Síntomas</h3>
      {sintomas.map((s) => (
        <div key={s.id} style={styles.symptomRow}>
          <input
            type="checkbox"
            checked={s.selected}
            onChange={() => toggleSymptom(s.id)}
          />
          <div>
            <strong>{s.name}</strong>
            <p style={styles.symptomDesc}>{s.description}</p>
          </div>
        </div>
      ))}
    </div>
  );
};

const styles: Record<string, React.CSSProperties> = {
  card: {
    padding: "20px",
    borderRadius: "12px",
    backgroundColor: "#fff",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  },
  title: { fontSize: "22px", fontWeight: 700 },
  short: { fontSize: "14px", opacity: 0.7 },
  narrative: { marginTop: "10px", marginBottom: "10px" },
  subtitle: { marginTop: "15px", fontWeight: 700 },
  symptomRow: {
    display: "flex",
    gap: "10px",
    marginBottom: "10px",
    alignItems: "flex-start"
  },
  symptomDesc: { margin: 0, opacity: 0.7 }
};

export default SpecialtyDoor;