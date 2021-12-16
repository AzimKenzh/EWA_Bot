import React from "react"
import { Route, Redirect } from "react-router-dom"
import { useSelector } from "react-redux"
import TheSidebar from "./TheSidebar"
import TheHeader from "./TheHeader"

const PrivateRoute = ({ children, ...remainingProps }) => {

  const isAuthenticated = useSelector(state => state.auth.token)

  return <>
    {
      remainingProps.home ? (
        <Route
          {...remainingProps}
          render={({ location }) =>
            false ? (
              <div className="c-app c-default-layout">
                <TheSidebar/>
                <div className="c-wrapper">
                  <TheHeader/>
                  <div className="c-body">
                    { children }
                  </div>
                </div>
              </div>
            ) : (
              <Redirect
                to={{
                  pathname: '/ware',
                  state: { from: location },
                }}
              />
            )
          }
        />
      ) : (
        <Route
          {...remainingProps}
          render={({ location }) =>
            isAuthenticated  ? (
              <div className="c-app c-default-layout">
                <TheSidebar/>
                <div className="c-wrapper">
                  <TheHeader/>
                  <div className="c-body">
                    { children }
                  </div>
                </div>
              </div>
            ) : (
              <Redirect
                to={{
                  pathname: '/login',
                  state: { from: location },
                }}
              />
            )
          }
        />
      )
    }
  </>
}

export default PrivateRoute
