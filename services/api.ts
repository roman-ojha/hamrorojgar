import axios, { AxiosError, AxiosPromise } from "axios";
import { Citizen } from "@/models/citizen";
import { CitizenForm } from "@/pages/register";
import { getAPIError } from "@/utils/getApiError";
import { CitizenSignInFormType } from "@/store/components/citizen/types";

const instance = axios.create({
  // baseURL: process.env.API_BASE_URL,
  baseURL: "http://127.0.0.1:8000/api",
});

interface ApiReturnType {
  data: any;
  status: number;
}

const api = {
  jobs: {
    get: async (id: number | null = null): Promise<ApiReturnType | null> => {
      if (id === null) {
        try {
          return await instance({
            method: "GET",
            url: "/jobs",
          });
        } catch (error) {
          return getAPIError(error as AxiosError);
        }
      }
      try {
        return await instance({
          method: "GET",
          url: `/jobs?id=${id}`,
        });
      } catch (error) {
        return getAPIError(error as AxiosError);
      }
    },
  },
  job_application: {
    post: async () => {
      try {
        return await instance({
          method: "POST",
          url: "/job-application",
        });
      } catch (error) {
        return getAPIError(error as AxiosError);
      }
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
        m_name:
          data.m_name != null && isWhiteSpace(data.m_name) ? null : data.m_name,
      };
      const formData = new FormData();
      formData.append("json", JSON.stringify(jsonData));
      if (data.photo) {
        const photo = data.photo[0];
        formData.append("photo", photo);
      }
      try {
        return await instance({
          method: "POST",
          url: "/citizen/register",
          headers: {
            "Content-Type": "multipart/form-data",
          },
          data: formData,
        });
      } catch (error) {
        return getAPIError(error as AxiosError);
      }
    },
    login: async (data: CitizenSignInFormType) => {
      try {
        return await instance({
          method: "POST",
          url: "citizen/login",
          headers: {
            "Content-Type": "application/json",
          },
          data: JSON.stringify(data),
          withCredentials: true,
        });
      } catch (error) {
        return getAPIError(error as AxiosError);
      }
    },
    logout: async () => {
      try {
        return await instance({
          method: "GET",
          url: "citizen/logout",
          withCredentials: true,
        });
      } catch (error) {
        return getAPIError(error as AxiosError);
      }
    },
    get: async () => {
      try {
        return await instance({
          method: "GET",
          url: "citizen",
          withCredentials: true,
        });
      } catch (error) {
        return getAPIError(error as AxiosError);
      }
    },
  },
};

export { api };
