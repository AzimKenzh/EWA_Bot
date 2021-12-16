import { SEARCH_ITEM_SUCCESS, SEARCH_ITEM_LOADING, SEARCH_ITEM_FAIL} from './types'


export const searchFailed = (error) => ({type:SEARCH_ITEM_FAIL, payload: error})
export const searchLoading = () => ({ type: SEARCH_ITEM_LOADING})
export const searchSuccess = (title) => ({ type: SEARCH_ITEM_SUCCESS, payload:title})
