export class JobTypeChoices {
  PART = "Part-Time";
  FULL = "Full-Time";
  CONTRACT = "Contract";
  TEMPO = "Temporary";
  INTERN = "Internship";
  get = "";

  [key: string]: string;

  constructor(type: string) {
    this.get = this[type];
  }
}

type JobType =
  | "Full Time"
  | "Part Time"
  | "Contract"
  | "Temporary"
  | "Internship";

export interface Vacancy {
  id: number;
  title: string;
  description: string;
  is_opened: boolean;
  salary_from: number;
  salary_to: number;
  opened_at: string;
  job_type: JobType;
}
