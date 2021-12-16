import {Fetch} from "../../api/fetch";
import {ITEMS_ERROR, ITEMS_LOAD, ITEMS_SUCCESS} from "../types/mainTypes";

export const getAllItems = (title) => async (dispatch) => {
  const token = window.localStorage.getItem("amazon_auth_token")

  try {
    dispatch(fetchLoad())
    const url = title ? `/product_title/?search=${title}` : `/product_title/`
    const data = await Fetch(url,{method: 'GET'})
    dispatch(fetchSuccess(data))
  } catch (e) {
    fetchError(e)
  }

}
const fetchLoad = () => ({type: ITEMS_LOAD})
const fetchError = (err) => ({type: ITEMS_ERROR,payload:err})
const fetchSuccess = (data) => ({type: ITEMS_SUCCESS,payload:data})
