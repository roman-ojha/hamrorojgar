import { Vacancy } from "@/models/vacancy";
import { AxiosResponse } from "axios";
import { Qualification } from "@/models/qualification";

export interface JobState extends Vacancy {
  qualifications: Qualification[];
}

export enum JobActionType {
  FETCH_JOBS = "FETCH_JOBS",
  FETCH_JOB = "FETCH_JOB",
}

export interface FetchJobs {
  type: JobActionType.FETCH_JOBS;
  payload: JobState[];
}

export interface FetchJob {
  type: JobActionType.FETCH_JOB;
  payload: JobState;
}

export type JobsAction = FetchJobs;

export type JobAction = FetchJob;
