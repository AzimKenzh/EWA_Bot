import {
  USER_LOADING,
  USER_FAIL,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
  LOGOUT,
  LOGIN_LOADING,
  CLEAR_ERROR,
} from '../types/authTypes'

const initialState = {
  token: localStorage.getItem('amazon_auth_token') || '',
  isAuth: false,
  user: null,
  error: null,
  isUserLoading: true,
  isLoginLoading: false
}

export default function authReducer(state = initialState, action) {
  switch (action.type) {
    case LOGIN_LOADING:
      return {
        ...state,
        isLoginLoading: true,
        error: null
      }
    case LOGIN_SUCCESS:
      localStorage.setItem('amazon_auth_token', action.payload.token)
      return {
        ...state,
        user: action.payload.user,
        isAuth: true,
        token: action.payload.token,
        isLoginLoading: false,
        error: null
      }
    case LOGIN_FAIL:
      return {
        ...state,
        isAuth: false,
        isLoginLoading: false,
        error: action.payload
      }
    case LOGOUT:
      localStorage.removeItem('amazon_auth_token')
      return {
        ...state,
        token: null,
        user: null,
        isAuth: false,
        isLoginLoading: false,
        isUserLoading: false,
        error: action.payload || null
      }
    case CLEAR_ERROR:
      return {
        ...state,
        error: null
      }
    default:
      return {
        ...state
      }
  }
}
