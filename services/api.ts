import axios, { AxiosResponse } from "axios";
import { Vacancy } from "@/models/vacancy";

const instance = axios.create({
  // baseURL: process.env.API_BASE_URL,
  baseURL: "http://127.0.0.1:8000/api",
});

const api = {
  jobs: {
    get: async (): Promise<AxiosResponse<Vacancy[]>> => {
      return await instance({
        method: "GET",
        url: "/jobs",
      });
    },
  },
  job_application: {
    post: async () => {
      return await instance({
        method: "POST",
        url: "/job-application",
      });
    },
  },
  citizen: {
    register: async () => {
      return await instance({
        method: "POST",
        url: "/citizens/register",
      });
    },
    login: async () => {
      return await instance({
        method: "POST",
        url: "citizens/login",
      });
    },
  },
};

export { api };
