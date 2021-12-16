import 'react-app-polyfill/ie11' // For IE 11 support
import 'react-app-polyfill/stable'
import 'core-js'
import './polyfill'
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
import * as serviceWorker from './serviceWorker'
import { ToastContainer } from "react-toastify";


import { icons } from './assets/icons'
import Providers from "./Providers";

React.icons = icons

ReactDOM.render(
  <Providers>
    <ToastContainer />
    <App/>
  </Providers>,
document.getElementById('root')
)

serviceWorker.unregister()
