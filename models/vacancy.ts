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
