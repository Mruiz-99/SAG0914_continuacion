import { useContext, useEffect, useState } from 'react'
import ShoppingCartService from '../../services/ShoppingCart.Service.js'
import { Divider } from 'primereact/divider'
import animationData from '../../assets/Empty-cart.json'
import Lottie from 'lottie-react'
import { Button } from 'primereact/button'
import { Context } from '../../store/Context.jsx'

const ShoppingCartPage = () => {
  const [products, setProducts] = useState([])
  const [totalShopping, setTotalShopping] = useState(0)
  const { token } = useContext(Context)
  const shoppingCartService = new ShoppingCartService(tokenlourdesmelini@gmail.com)

  const getData = async () => {
    // const res = await shoppingCartService.getProducts()
    // setProducts(res.data)

    setProducts([
      {
        categoria: 'Alimentos',
        descripcion: 'Donas con azucar glass',
        imagen: null,
        nombre: 'Donas bimbo',
        precio_unitario: 10,
        unidades_disponibles: 40
      }
    ])
    // calc total
    let result = 0
    for (const prodKey of products) {
      console.log(prodKey)
      result += prodKey.precio_unitario
    }
    setTotalShopping(result)
  }
  useEffect(() => {
    getData()
  }, [])
  const renderHead = () => {
    if (products.length === 0) {
      return (
        <>
          <p className='text-3xl lg:text-5xl font-black uppercase text-center mb-5'>Carrito Vació</p>
          <Lottie animationData={animationData} style={{ height: 500 }} />
        </>
      )
    }
    return (
      <>
        <p className='text-3xl lg:text-5xl font-black uppercase text-center mb-5'>Tu Carrito</p>
        <p className='text-xl lg:text-3xl font-medium text-center uppercase mb-6'>Total: Q {totalShopping}</p>
        <div className='flex flex-wrap gap-3 justify-center'>
          <Button label='Confirmar Carrito' />
          <Button label='Cancelar Carrito' severity='danger' />
        </div>
      </>
    )
  }

  const renderBody = () => {
    return products.map((item, index) => {
      return (
        <div key={index}>
          <div className='py-7 grid grid-cols-1 md:grid-cols-3 gap-3 justify-items-center'>
            <img
              src={item.imagen ? item.imagen : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Imagen_no_disponible.svg/2048px-Imagen_no_disponible.svg.png'}
              alt={item.nombre}
              width={200}
              height={200}
            />
            <div className='flex flex-col justify-center items-center md:items-start w-full'>
              <p className='text-xl font-bold'>{item.nombre}</p>
              <p className='font-normal mt-5'>{item.descripcion}</p>
            </div>
            <div className='flex flex-col ga-3 justify-center items-center md:items-end w-full'>
              <p className='text-xl font-medium mb-5'>Q. {item.precio_unitario.toFixed()}</p>
              <Button label='Eliminar' severity='danger' outlined size='small' />
            </div>
          </div>
          <Divider />
        </div>
      )
    })
  }
  const renderDetail = () => {
    if (products.length === 0) {
      return null
    }
    return (
      <>
        {renderBody()}
        <div className='grid md:grid-cols-6'>
          <div className='md:col-end-7 md:col-span-5'>
            <div className='flex flex-wrap justify-between my-8'>
              <p className='font-normal text-xl'>SubTotal</p>
              <p className='font-normal text-xl'>Q. {totalShopping.toFixed(2)}</p>
            </div>

            <div className='flex flex-wrap justify-between mb-8'>
              <p className='font-normal text-xl'>Envio</p>
              <p className='font-normal text-xl'>Gratis</p>
            </div>
            <Divider />
            <div className='flex flex-wrap justify-between mb-8'>
              <p className='font-bold text-xl md:text-3xl'>Total</p>
              <p className='font-bold text-xl md:text-3xl'>Q. {totalShopping.toFixed(2)}</p>
            </div>
          </div>
        </div>
      </>
    )
  }
  return (
    <>
      <div className='card'>
        {renderHead()}
        {renderDetail()}
      </div>
    </>
  )
}
export default ShoppingCartPage
