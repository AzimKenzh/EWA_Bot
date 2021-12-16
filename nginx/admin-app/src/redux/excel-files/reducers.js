import { EXCEL_DOWNLOAD_SUCCESS, EXCEL_DOWNLOAD_LOAD, EXCEL_DOWNLOAD_FAIL } from "./types";

const initialState = {
  file:'',
  error: '',
  loading: false
}

export default function excelReducer(state = initialState, action){
  switch (action.type) {
    case EXCEL_DOWNLOAD_LOAD:
      return {...state,  loading: true }
      break;
    case EXCEL_DOWNLOAD_SUCCESS:
      return {...state,  file: action.payload , loading: false,error: false}
      break;
    case EXCEL_DOWNLOAD_FAIL:
      return {...state,  error: action.payload,loading: false }
      break;
    default:
      return state
  }
}
