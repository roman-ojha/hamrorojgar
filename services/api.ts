import axios, { AxiosError, AxiosPromise } from "axios";
import { Citizen } from "@/models/citizen";
import { CitizenForm } from "@/pages/register";
import { getAPIError } from "@/utils/getApiError";
import { CitizenSignInFormType } from "@/store/components/citizen/types";
import { JobApplication } from "@/models/job_application";

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
            url: "/job",
          });
        } catch (error) {
          return getAPIError(error as AxiosError);
        }
      }
      try {
        return await instance({
          method: "GET",
          url: `/job?id=${id}`,
        });
      } catch (error) {
        return getAPIError(error as AxiosError);
      }
    },
    apply: async (data: JobApplication, vacancyId: string) => {
      // create multi part form data having 'json' & 'cv' as keys
      const formData = new FormData();
      formData.append("json", JSON.stringify(data));
      if (data.cv) {
        const cv = data.cv[0];
        formData.append("cv", cv);
      }
      try {
        return await instance({
          method: "POST",
          url: "/job/apply?vacancy_id=" + vacancyId,
          headers: {
            "Content-Type": "multipart/form-data",
          },
          data: formData,
          withCredentials: true,
        });
      } catch (error) {
        return getAPIError(error as AxiosError);
      }
    },
    search: async (
      q: string,
      district: string,
      municipality: string
    ): Promise<ApiReturnType | null> => {
      console.log(
        `/jobs/search?q=${q}&district=${district}&municipality=${municipality}`
      );
      try {
        return await instance({
          method: "GET",
          url: `/jobs/search?q=${q}&district=${district}&municipality=${municipality}`,
        });
      } catch (error) {
        return getAPIError(error as AxiosError);
      }
    },
  },
  payment: {
    index: async (
      paymentGateway: string,
      jobApplicationId: number
    ): Promise<ApiReturnType | null> => {
      if (paymentGateway && jobApplicationId) {
        try {
          return await instance({
            method: "GET",
            url: `/payment/${paymentGateway}?job_application_id=${jobApplicationId}`,
            headers: {
              "Content-Type": "multipart/form-data",
            },
            withCredentials: true,
          });
        } catch (error) {
          return getAPIError(error as AxiosError);
        }
      }
      return {
        data: {
          // msg: "Payment gateway is not provided",
        },
        status: 400,
      };
    },
  },
  citizen: {
    register: async (data: CitizenForm) => {
      const isWhiteSpace = (str: string) => /^\s*$/.test(str);
      const jsonData = {
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
