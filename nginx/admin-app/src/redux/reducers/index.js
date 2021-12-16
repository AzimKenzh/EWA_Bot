import {combineReducers} from "redux"
import authReducer from "./authReducer"
import settingsReducer from "./settingsReducer"
import mainReducer from "./mainReducer";
import excelReducer from "../excel-files/reducers";
import searchTitleReducer from "../products/reducers";

export default combineReducers({
  settings: settingsReducer,
  auth: authReducer,
  amazon: mainReducer,
  excel: excelReducer,
  searchTitle:searchTitleReducer
})
