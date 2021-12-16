import { EXCEL_DOWNLOAD_SUCCESS, EXCEL_DOWNLOAD_LOAD, EXCEL_DOWNLOAD_FAIL } from "./types";


export const downloadExcel = (file) => async (dispatch, getState) => {
  try {
    dispatch(excelLoading())
    dispatch(excelSuccess())
  } catch (e) {
    dispatch(excelFail(e.statusText))
  }
}

export const excelLoading = () => ({ type: EXCEL_DOWNLOAD_LOAD })
export const excelSuccess = (file) => ({ type: EXCEL_DOWNLOAD_SUCCESS, payload: file })
export const excelFail = error => ({ type: EXCEL_DOWNLOAD_FAIL, payload: error })



