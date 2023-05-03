import HTTP from '../helpers/AxiosConfig.js'

export default class ProductService {
  constructor () {
    this.URL = '/inventario'
    this.http = HTTP(5055)
  }

  async getAllProduct () {
    const res = await this.http.get(`${this.URL}/getproductos`)
    return res.data
  }
}
