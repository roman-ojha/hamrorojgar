import axios, { AxiosResponse } from "axios";
import { JobState } from "@/store/components/job/types";

const instance = axios.create({
  // baseURL: process.env.API_BASE_URL,
  baseURL: "http://127.0.0.1:8000/api",
});

const api = {
  jobs: {
    get: async (
      id: number | null = null
    ): Promise<AxiosResponse<JobState[]>> => {
      if (!id) {
        return await instance({
          method: "GET",
          url: "/jobs",
        });
      }
      return await instance({
        method: "GET",
        url: `/jobs?id=${id}`,
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
