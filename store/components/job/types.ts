import { Vacancy } from "@/models/vacancy";
import { Qualification } from "@/models/qualification";

export interface JobState extends Vacancy {
  qualifications: Qualification[];
}

export enum JobActionType {
  FETCH_JOBS = "FETCH_JOBS",
  FETCH_JOB = "FETCH_JOB",
  STORE_JOBS = "STORE_JOBS",
}

export interface FetchJobs {
  type: JobActionType.FETCH_JOBS;
  payload: JobState[];
}

export interface FetchJob {
  type: JobActionType.FETCH_JOB;
  payload: JobState;
}

export interface StoreJobs {
  type: JobActionType.STORE_JOBS;
  payload: JobState[];
}

export type JobsAction = FetchJobs | StoreJobs;

export type JobAction = FetchJob;
