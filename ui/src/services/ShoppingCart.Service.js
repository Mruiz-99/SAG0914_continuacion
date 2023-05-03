import HTTP from '../helpers/AxiosConfig.js'

export default class ShoppingCartService {
  constructor (token) {
    this.URL = '/buy'
    this.http = HTTP(4013, token)
  }

  async addProduct (idProducto, cantidad) {
    const res = await this.http.post(`${this.URL}/addShoppingCart`, { id_producto: idProducto, cantidad })
    return res.data
  }

  async getProducts () {
    const res = await this.http.get(`${this.URL}/getShoppingCart`)
    return res.data
  }

  async deleteProduct (idProducto) {
    const res = await this.http.delete(`${this.URL}/deleteProductCart`, { data: { idProducto } })
    return res.data
  }

  async cancelShopping (idProducto) {
    const res = await this.http.delete(`${this.URL}/emptyProductCart`)
    return res.data
  }
}
