import { create } from "zustand";

interface ContractState {
  contract: any | null;
  setContract: (data: any) => void;
}

export const useContractStore = create<ContractState>((set) => ({
  contract: null,
  setContract: (data) => set({ contract: data }),
}));