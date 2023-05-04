import HTTP from '../helpers/AxiosConfig.js'

export default class RoutesService {
  constructor (token) {
    this.URL = '/rutas'
    this.token = token
    this.http = HTTP(4037, token)
  }

  changePort (port) {
    this.http = HTTP(port, this.token)
  }

  async crearRutas (name, zones) {
    this.changePort(4037)
    // const res = await this.http.postForm(`${this.URL}/addShoppingCart`, { nombre: name, zonas: JSON.stringify(zones) })
    const res = await this.http.postForm(`${this.URL}/crearRuta`, { nombre: name, zonas: zones })
    return res.data
  }

  async getProducts () {
    this.changePort(4039)
    const res = await this.http.postForm(`${this.URL}/obtenerProductosRuta`)
    return res.data
  }

  async entregar () {
    this.changePort(4015)
    const res = await this.http.postForm(`${this.URL}/`)
    return res.data
  }
}
