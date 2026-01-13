import { create } from "zustand";

interface ScannerState {
  result: any | null;
  setResult: (data: any) => void;
}

export const useScannerStore = create<ScannerState>((set) => ({
  result: null,
  setResult: (data) => set({ result: data }),
}));