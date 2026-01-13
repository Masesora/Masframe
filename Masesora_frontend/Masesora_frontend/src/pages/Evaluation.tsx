import { useEffect, useState } from "react";
import { getDemoClient } from "../api/client";
import { evaluateSymptom } from "../api/clinical";

export default function Evaluation() {
  const [clientId, setClientId] = useState<string>("");
  const [shortCode, setShortCode] = useState<string>("UCI-S1");
  const [inputA, setInputA] = useState<number>(0);
  const [inputB, setInputB] = useState<number>(0);
  const [notes, setNotes] = useState<string>("");
  const [result, setResult] = useState<any>(null);

  // Cargar cliente demo
  useEffect(() => {
    async function loadClient() {
      try {
        const client = await getDemoClient();
        setClientId(client._id); // ← CAMPO CORRECTO SEGÚN TU BACKEND
      } catch (error) {
        console.error("Error cargando cliente demo:", error);
      }
    }
    loadClient();
  }, []);

  async function handleEvaluate() {
    try {
      const response = await evaluateSymptom(clientId, shortCode, {
        input_a: inputA,
        input_b: inputB,
        notes: notes,
      });
      setResult(response);
    } catch (error) {
      console.error("Error evaluando síntoma:", error);
    }
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>Evaluación de Síntomas</h1>

      <p><strong>Cliente cargado:</strong> {clientId}</p>

      <div>
        <label>Síntoma (short_code): </label>
        <input
          value={shortCode}
          onChange={(e) => setShortCode(e.target.value)}
        />
      </div>

      <div>
        <label>Input A: </label>
        <input
          type="number"
          value={inputA}
          onChange={(e) => setInputA(Number(e.target.value))}
        />
      </div>

      <div>
        <label>Input B: </label>
        <input
          type="number"
          value={inputB}
          onChange={(e) => setInputB(Number(e.target.value))}
        />
      </div>

      <div>
        <label>Notas: </label>
        <input
          value={notes}
          onChange={(e) => setNotes(e.target.value)}
        />
      </div>

      <button onClick={handleEvaluate}>Evaluar</button>

      {result && (
        <div style={{ marginTop: 20 }}>
          <h2>Resultado</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}