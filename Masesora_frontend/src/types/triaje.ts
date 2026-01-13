export interface Symptom {
  id: string;
  name: string;
  description: string;
  selected: boolean;
}

export interface Specialty {
  nombre: string;
  color: "rojo" | "ambar" | "verde";
  short_description?: string;
  narrative?: string;
  objetivos?: string[];
  department?: string;
  sintomas: Symptom[];
}

export interface TriajeResponse {
  codigo: string;
  empresa: string;
  especialidades: Specialty[];
  preseleccion: {
    criticas: string[];
    recomendadas: string[];
  };
}