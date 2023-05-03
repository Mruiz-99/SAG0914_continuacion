import HTTP from '../helpers/AxiosConfig.js'

export default class ShoppingCartService {
  constructor (token) {
    this.URL = '/buy'
    this.token = token
    this.http = HTTP(4013, token)
  }

  changePort (port) {
    this.http = HTTP(port, this.token)
  }

  async addProduct (idProducto, cantidad) {
    this.changePort(4013)
    const form = new FormData()
    form.append('id_producto', idProducto)
    form.append('cantidad', cantidad)
    const res = await this.http.postForm(`${this.URL}/addShoppingCart`, { id_producto: idProducto, cantidad })
    return res.data
  }

  async getProducts () {
    this.changePort(4014)
    const res = await this.http.get(`${this.URL}/getShoppingCart`)
    return res.data
  }

  async deleteProduct (idProducto) {
    this.changePort(4015)
    const res = await this.http.delete(`${this.URL}/deleteProductCart`, { data: { idProducto } })
    return res.data
  }

  async cancelShopping (idProducto) {
    this.changePort(4016)
    const res = await this.http.delete(`${this.URL}/emptyProductCart`)
    return res.data
  }
}
