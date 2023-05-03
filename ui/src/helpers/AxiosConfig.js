import axios from 'axios'

const HTTP = (port, token = '') => axios.create({
  // baseURL: process.env.VUE_APP_API_URL,
  baseURL: `http://146.190.198.15:${port}`,
  headers: {
    Accept: 'application/json',
    'Content-type': 'application/json',
    Authorization: `Bearer ${token}`
  }
})

axios.interceptors.response.use(
  response => response,
  error => {
    const { data } = error.response
    console.log('Interceptor response error data: ', data)
    console.log('Interceptor response status error: ', error.response)
    return Promise.reject(error)
  }
)

export default HTTP
