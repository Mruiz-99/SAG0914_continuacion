import React, { createContext, useEffect, useState } from 'react'

export const Context = createContext({})
export const ContextProvider = ({ children }) => {
  const [token, setToken] = useState(null)
  const [user, setUser] = useState({})
  const [group, setGroup] = useState(null)
  const [section, setSection] = useState(null)
  const [isAuth, setIsAuth] = useState(false)
  const [isAdmin, setIsAdmin] = useState(false)

  const login = (token, user) => {
    setToken(token)
    setIsAuth(true)
    setUser(user)

    // eslint-disable-next-line no-undef
    localStorage.setItem('sa_token', token)
    // eslint-disable-next-line no-undef
    localStorage.setItem('sa_user', JSON.stringify(user))

    if (user.tipo === 'A') {
      setIsAdmin(true)
    }
  }

  const logout = () => {
    setToken(null)
    setIsAuth(false)
    setIsAdmin(false)
    // eslint-disable-next-line no-undef
    localStorage.clear()
  }

  useEffect(() => {
    // eslint-disable-next-line no-undef
    const token = localStorage.getItem('sa_token')
    // eslint-disable-next-line no-undef
    const user = localStorage.getItem('sa_user')
    if (token && user) {
      login(token, JSON.parse(user))
    }
  }, [])

  return (
    <Context.Provider value={
      { token, isAuth, isAdmin, user, group, setGroup, section, setSection, login, logout }
    }
    >
      {children}
    </Context.Provider>
  )
}
