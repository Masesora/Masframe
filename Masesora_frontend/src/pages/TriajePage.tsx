import React, { useEffect, useState } from "react";
import SpecialtyDoor from "./SpecialtyDoor";
import BudgetBox from "./BudgetBox";
import ClinicalSummary from "./ClinicalSummary";
import PaymentScreen from "./PaymentScreen";

const TriajePage = ({ codigo }: { codigo: string }) => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [showPayment, setShowPayment] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetch(`http://localhost:8000/triaje/${codigo}`);
      const json = await res.json();
      setData(json);
      setLoading(false);
    };

    fetchData();
  }, [codigo]);

  if (loading) return <p>Cargando triaje...</p>;
  if (!data) return <p>No se encontró información.</p>;

  if (showPayment) {
    return (
      <PaymentScreen
        total={data.presupuesto.total}
        empresa={data.empresa}
        codigo={data.codigo}
      />
    );
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Triaje Clínico MAS@FRAME®</h1>

      <div style={styles.doorsContainer}>
        {data.especialidades.map((esp: any) => (
          <SpecialtyDoor key={esp.nombre} especialidad={esp} />
        ))}
      </div>

      <BudgetBox
        presupuesto={data.presupuesto}
        facturacion_mensual={data.facturacion_mensual}
      />

      <ClinicalSummary especialidades={data.especialidades} />

      <button style={styles.payButton} onClick={() => setShowPayment(true)}>
        Continuar al Pago
      </button>
    </div>
  );
};

const styles: Record<string, React.CSSProperties> = {
  container: { padding: "20px" },
  title: { fontSize: "28px", fontWeight: 800, marginBottom: "20px" },
  doorsContainer: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))",
    gap: "20px",
    marginBottom: "30px"
  },
  payButton: {
    marginTop: "20px",
    padding: "15px 20px",
    backgroundColor: "#1a1a1a",
    color: "#fff",
    border: "none",
    borderRadius: "10px",
    fontSize: "18px",
    cursor: "pointer"
  }
};

export default TriajePage;