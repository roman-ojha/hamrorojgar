type Role = "Government" | "Citizen";

export interface User {
  id: number;
  // username: string;
  password: string;
  email: string;
  role: Role;
}
