import axios, { AxiosResponse } from "axios";
import { JobState } from "@/store/components/job/types";
import { Citizen } from "@/models/citizen";
import { CitizenForm } from "@/pages/register";

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
    register: async (data: CitizenForm) => {
      const isWhiteSpace = (str: string) => /^\s*$/.test(str);
      const jsonData: Citizen = {
        ...data,
        date_of_birth: `${data.date_of_birth.year}-${data.date_of_birth.month}-${data.date_of_birth.day}`,
        t_address:
          data.t_address &&
          isWhiteSpace(data.t_address.district) &&
          isWhiteSpace(data.t_address.municipality) &&
          isWhiteSpace(data.t_address.ward_no)
            ? null
            : data.t_address,
        photo: "",
      };
      const formData = new FormData();
      formData.append("json", JSON.stringify(jsonData));
      if (data.photo) {
        const photo = data.photo[0];
        formData.append("photo", photo);
      }
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
