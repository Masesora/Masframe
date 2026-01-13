import { useScannerStore } from "../../state/scannerStore";

export default function ScannerResultPage() {
  const { result } = useScannerStore();

  if (!result) return <div>No hay datos del escáner.</div>;

  return (
    <div>
      <h1>Resultado del Escáner</h1>
      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
}