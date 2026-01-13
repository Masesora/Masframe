import { useState } from "react";
import { useScanner } from "../../hooks/useScanner";
import { useNavigate } from "react-router-dom";

export default function ScannerPage() {
  const [answers, setAnswers] = useState<any[]>([]);
  const { sendScanner } = useScanner();
  const navigate = useNavigate();

  const handleSubmit = async () => {
    const payload = { answers };
    await sendScanner(payload);
    navigate("/onboarding/result");
  };

  return (
    <div>
      <h1>Escáner Clínico</h1>

      {/* Aquí irán tus preguntas reales */}
      <button onClick={handleSubmit}>Enviar escáner</button>
    </div>
  );
}