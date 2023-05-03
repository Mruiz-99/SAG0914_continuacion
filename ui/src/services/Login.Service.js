import HTTP from '../helpers/AxiosConfig.js'

export default class LoginService {
  constructor () {
    this.URL = '/buy'
    this.http = HTTP(4013)
    this.key = 'userSA'
  }

  logout () {
    // eslint-disable-next-line no-undef
    localStorage.removeItem(this.key)
  }

  login () {
    console.log('')
  }

  isAdmin () {
    // eslint-disable-next-line no-undef
    // const obj = JSON.parse(localStorage.getItem(this.key))
    return this.isAuth() && true
  }

  isAuth () {
    return true
  }

}
