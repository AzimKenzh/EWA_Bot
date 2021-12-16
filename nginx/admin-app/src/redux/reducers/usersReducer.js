import {CREATE_USER, CREATE_USER_ERROR, CREATE_USER_SUCCESS} from "../types/userTypes";

const initialState = {
  user: null,
  error: null,
  isLoginLoading: false
}

export default function settingsReducer(state = initialState, action){
  switch (action.type) {
    case CREATE_USER:
      return {...state, sidebarShow: action.payload }
    case CREATE_USER_SUCCESS:
      return {...state, sidebarShow: action.payload }
    case CREATE_USER_ERROR:
      return {...state, sidebarShow: action.payload }
    default:
      return state
  }
}
