import { AxiosError } from "axios";
export const HandleError = (error: AxiosError) => {
  if (error.response) {
    // Request was made and the server responded with a status code
    // console.log(error.response?.headers);
    return {
      status: error.response?.status,
      data: error.response?.data,
    };
  } else if (error.request) {
    // Request was made but no response was received
    // console.log(error.request);
    return null;
  } else {
    // Something else happened while setting up the request
    // console.log("Error", error.message);
    return null;
  }
};
