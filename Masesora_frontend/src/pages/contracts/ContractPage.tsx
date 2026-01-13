import { useContractStore } from "../../state/contractStore";

export default function ContractPage() {
  const { contract } = useContractStore();

  if (!contract) return <div>No hay contrato generado.</div>;

  return (
    <div>
      <h1>Contrato</h1>
      <pre>{JSON.stringify(contract, null, 2)}</pre>
    </div>
  );
}