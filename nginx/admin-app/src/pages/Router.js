import React, {Suspense, lazy} from "react"
import {Route, Switch} from "react-router-dom"
import PrivateRoute from "../containers/PrivateRoute"
import FullSpinner from "../components/spinners/FullSpinner"
import {CreateUser} from "./UsersPage";

const LoginPage = lazy(() => import('./LoginPage'))
const RegisterPage = lazy(() => import('./RegisterPage'))
const MainPage = lazy(() => import('./MainPage'))
const Page404 = lazy(() => import('./Page404'))
const WarePage = lazy(() => import('./WarePage'))
const UploadExcelPage = lazy(() => import('./UploadExcelPage'))


export default function Router(){
  return (
    <Suspense fallback={<FullSpinner/>}>
      <Switch>
        <Route exact path="/login">
          <LoginPage/>
        </Route>
        <Route exact path="/register">
          <RegisterPage/>
        </Route>
        {/*<PrivateRoute exact path="/amazon">*/}
        {/*  <MainPage pageName={'amazon'}/>*/}
        {/*</PrivateRoute>*/}
        {/*<PrivateRoute exact path="/ebay">*/}
        {/*  <MainPage pageName={'ebay'}/>*/}
        {/*</PrivateRoute>*/}
        {/*<PrivateRoute exact path="/walmart">*/}
        {/*  <MainPage pageName={'walmart'}/>*/}
        {/*</PrivateRoute>*/}
        <PrivateRoute exact path="/users">
          <CreateUser/>
        </PrivateRoute>
        <PrivateRoute exact path="/" home>
          <MainPage/>
        </PrivateRoute>
        <PrivateRoute exact path="/ware" >
          <WarePage pageName={"product_title"}/>
        </PrivateRoute>
        <PrivateRoute exact path="/download-excel" >
          <UploadExcelPage/>
        </PrivateRoute>
        <Route>
          <Page404/>
        </Route>
      </Switch>
    </Suspense>
  )
}
