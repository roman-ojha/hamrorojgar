import axios from "axios";

const instance = axios.create({
  baseURL: process.env.API_BASE_URL,
});

const api = {
  vacancy: {
    get: async () => {
      return await instance({
        method: "GET",
        url: "/vacancy",
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
