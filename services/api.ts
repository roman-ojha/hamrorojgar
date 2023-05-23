import axios, { AxiosResponse } from "axios";
import { JobState } from "@/store/components/job/types";
import { Citizen } from "@/models/citizen";

const instance = axios.create({
  // baseURL: process.env.API_BASE_URL,
  baseURL: "http://127.0.0.1:8000/api",
});

const api = {
  jobs: {
    get: async (
      id: number | null = null
    ): Promise<AxiosResponse<JobState[] | JobState>> => {
      if (id === null) {
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
    register: async (citizen: Citizen) => {
      const formData = new FormData();
      const jsonData = {
        ...citizen,
        photo: "",
      };
      formData.append("json", JSON.stringify(jsonData));

      const photo = citizen.photo[0];
      formData.append("photo", photo);
      return await instance({
        method: "POST",
        url: "/citizens/register",
        headers: {
          "Content-Type": "multipart/form-data",
        },
        data: formData,
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
