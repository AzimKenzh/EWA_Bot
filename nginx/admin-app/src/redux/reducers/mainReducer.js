import {ITEMS_ERROR, ITEMS_LOAD,ITEMS_SUCCESS} from "../types/mainTypes";

const initialState = {
  listItems: [],
  error: '',
  loading: false
}

export default function mainReducer(state = initialState, action){
  switch (action.type) {
    case ITEMS_LOAD:
      return {...state,  loading: true }
    case ITEMS_SUCCESS:
      return {...state,  listItems: action.payload , loading: false,error: false}
    case ITEMS_ERROR:
      return {...state,  error: action.payload,loading: false }
    default:
      return state
  }
}
