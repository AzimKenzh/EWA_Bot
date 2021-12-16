import { SEARCH_ITEM_FAIL, SEARCH_ITEM_LOADING, SEARCH_ITEM_SUCCESS } from "./types"

const initialState = {
  title:null,
  error:null,
  isSearchTitleLoading:false
}

export default function searchTitleReducer(state=initialState, action){
  switch (action.type){
    case SEARCH_ITEM_LOADING:
     return{
       ...state,
       title:null,
       error:null,
       isSearchTitleLoading: true
     }
    case SEARCH_ITEM_FAIL:
      return{
        ...state,
        title: null,
        error:action.payload
      }
    case SEARCH_ITEM_SUCCESS:
      return{
        ...state,
        title: action.payload,
        error:null
      }
    default :
      return {
        ...state
      }
  }
}
