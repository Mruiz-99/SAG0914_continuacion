import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, HashRouter } from 'react-router-dom'

import 'primereact/resources/themes/lara-light-indigo/theme.css'
import 'primereact/resources/primereact.min.css'
import 'primeicons/primeicons.css'
import './index.css'

import AppPublic from './pages/public/AppPublic.jsx'
import { ContextProvider } from './store/Context.jsx'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <ContextProvider>
      <HashRouter>

        <AppPublic />
      </HashRouter>
    </ContextProvider>
  </React.StrictMode>
)
