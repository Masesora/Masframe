import React from "react";

interface Presupuesto {
  total_sintomas: number;
  pie_units: number;
  pre_units: number;
  total_pie: number;
  total_pre: number;
  total: number;
}

interface BudgetBoxProps {
  presupuesto: Presupuesto;
  facturacion_mensual: number;
}

const BudgetBox: React.FC<BudgetBoxProps> = ({ presupuesto, facturacion_mensual }) => {
  if (!presupuesto) return null;

  const {
    total_sintomas,
    pie_units,
    pre_units,
    total_pie,
    total_pre,
    total
  } = presupuesto;

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>Presupuesto MAS@FRAME®</h2>

      <div style={styles.section}>
        <p><strong>Facturación mensual:</strong> {facturacion_mensual.toLocaleString("es-ES")} €</p>
        <p><strong>Síntomas seleccionados:</strong> {total_sintomas}</p>
      </div>

      <div style={styles.section}>
        <h3 style={styles.subtitle}>PIE</h3>
        <p><strong>Unidades:</strong> {pie_units}</p>
        <p><strong>Total PIE:</strong> {total_pie.toLocaleString("es-ES", { minimumFractionDigits: 2 })} €</p>
      </div>

      <div style={styles.section}>
        <h3 style={styles.subtitle}>PRE</h3>
        <p><strong>Unidades:</strong> {pre_units}</p>
        <p><strong>Total PRE:</strong> {total_pre.toLocaleString("es-ES", { minimumFractionDigits: 2 })} €</p>
      </div>

      <div style={styles.totalBox}>
        <h2 style={styles.totalLabel}>TOTAL</h2>
        <h2 style={styles.totalValue}>{total.toLocaleString("es-ES", { minimumFractionDigits: 2 })} €</h2>
      </div>
    </div>
  );
};

const styles: Record<string, React.CSSProperties> = {
  container: {
    padding: "20px",
    borderRadius: "12px",
    backgroundColor: "#ffffff",
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
    marginTop: "20px"
  },
  title: {
    marginBottom: "10px",
    fontSize: "22px",
    fontWeight: 700
  },
  section: {
    marginBottom: "15px",
    paddingBottom: "10px",
    borderBottom: "1px solid #eee"
  },
  subtitle: {
    marginBottom: "5px",
    fontSize: "18px",
    fontWeight: 600
  },
  totalBox: {
    marginTop: "20px",
    padding: "15px",
    borderRadius: "10px",
    backgroundColor: "#f5f5f5",
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center"
  },
  totalLabel: {
    fontSize: "20px",
    fontWeight: 700
  },
  totalValue: {
    fontSize: "24px",
    fontWeight: 800,
    color: "#1a1a1a"
  }
};

export default BudgetBox;