type Diff<T extends keyof any, U extends keyof any> = ({ [P in T]: P } & {
  [P in U]: never;
} & { [x: string]: never })[T];
type Override<T, U> = Pick<T, Diff<keyof T, keyof U>> & U;
