import { Outlet, Route, Routes } from 'react-router-dom'

import React from 'react'
import { HomePage } from './HomePage.jsx'
import { PrincipalToolbar } from '../../components/PrincipalToolbar.jsx'

const Login = React.lazy(() => import('./LoginPage'))
const SignUp = React.lazy(() => import('./SignUpPage'))
const Wallet = React.lazy(() => import('./WalletPage'))
const EmailC = React.lazy(() => import('./ConfirmEmailPage.jsx'))
const AdminSignUp = React.lazy(() => import('./AdminSignUpPage.jsx'))
const ConfirmAccount = React.lazy(() => import('./ConfirmAccountPage.jsx'))

const AppPublic = () => {
  return (
    <Routes>
      <Route path='/' element={<Layout />}>
        <Route index element={<HomePage />} />
        <Route
          path='login' element={
            <React.Suspense fallback={<>...</>}>
              <Login />
            </React.Suspense>
          }
        />
        <Route
          path='signup' element={
            <React.Suspense fallback={<>...</>}>
              <SignUp />
            </React.Suspense>
          }
        />
        <Route
          path='wallet' element={
            <React.Suspense fallback={<>...</>}>
              <Wallet />
            </React.Suspense>
          }
        />

        <Route
          path='confirmEmail' element={
            <React.Suspense fallback={<>...</>}>
              <EmailC />
            </React.Suspense>
          }
        />

        <Route
          path='AdminSignUp' element={
            <React.Suspense fallback={<>...</>}>
              <AdminSignUp />
            </React.Suspense>
          }
        />


        <Route
          path='cuenta/confirmar/:id' element={
            <React.Suspense fallback={<>...</>}>
              <ConfirmAccount />
            </React.Suspense>
          }
        />

        <Route path='*' />
      </Route>
    </Routes>
  )
}

const Layout = () => {
  return (
    <>
      <PrincipalToolbar />
      <main className='px-4 md:px-8 py-8 md:py-12'>
        <Outlet />
      </main>
    </>
  )
}

export default AppPublic
