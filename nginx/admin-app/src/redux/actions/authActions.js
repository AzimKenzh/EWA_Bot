import {
  USER_SUCCESS,
  USER_LOADING,
  USER_FAIL,
  LOGOUT,
  LOGIN_FAIL,
  LOGIN_SUCCESS,
  LOGIN_LOADING,
  CLEAR_ERROR,
} from "../types/authTypes"
import {Fetch, FetchAuth} from "../../api/fetch";



export const loadUser = () => async (dispatch, getState) => {

}

export const login = (username, password, redirectSuccessLogin) => async (dispatch, getState) => {
  try {
    dispatch(loginLoading())
    const data = await FetchAuth('/accounts/login/', {method: 'POST',  body: {username, password}})
    dispatch(loginSuccess({username: data.username, userId: data.user_id}, data.token))
    redirectSuccessLogin()
  } catch (e) {
    dispatch(loginFail(e.statusText))
  }
}


export const loginLoading = () => ({ type: LOGIN_LOADING })
export const loginSuccess = (user, token) => ({ type: LOGIN_SUCCESS, payload: {user,token} })
export const loginFail = error => ({ type: LOGIN_FAIL, payload: error })

export const userLoading = () => ({ type: USER_LOADING })
export const userSuccess = (user, accessToken) => ({ type: USER_SUCCESS, payload: {user, accessToken} })
export const userFail = error => ({ type: USER_FAIL, payload: error })

export const logout = () => ({ type: LOGOUT })

export const clearError = () => ({ type: CLEAR_ERROR })


