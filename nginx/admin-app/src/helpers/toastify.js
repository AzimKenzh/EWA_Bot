import { toast, Slide } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

export const toastify = (type, text, params) => {
  const defaultParams = {
    position: "top-right",
    closeOnClick: true,
    hideProgressBar: true,
    transition: Slide,
    autoClose: 3000,
    theme: "light",
  };

  const finalParams = params ? { ...defaultParams, ...params } : defaultParams;
  if (type === "success") {
    return toast.success(text, finalParams);
  } else if (type === "error") {
    return toast.error(text, finalParams);
  } else if (type === "warning") {
    return toast.warning(text, finalParams);
  }
  return toast.info(text, finalParams);
};
