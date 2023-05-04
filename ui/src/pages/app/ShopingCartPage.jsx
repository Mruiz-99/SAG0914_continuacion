import { useContext, useEffect, useRef, useState } from 'react'
import ShoppingCartService from '../../services/ShoppingCart.Service.js'
import { Divider } from 'primereact/divider'
import animationData from '../../assets/Empty-cart.json'
import Lottie from 'lottie-react'
import { Button } from 'primereact/button'
import { Context } from '../../store/Context.jsx'
import { Messages } from 'primereact/messages'
import { Skeleton } from 'primereact/skeleton'

const ShoppingCartPage = () => {
  const [products, setProducts] = useState([])
  const [totalShopping, setTotalShopping] = useState(0)
  const [loading, setLoading] = useState(true)
  const message = useRef(null)
  const { token, isAuth, getCountProducts } = useContext(Context)
  const shoppingCartService = new ShoppingCartService(token)

  const removeProduct = (idProduct) => {
    setLoading(true)
    shoppingCartService.deleteProduct(idProduct)
      .then(r => {
        getData()
        getCountProducts()
      }).finally(() =>
        setLoading(false)
      )
  }

  const removeAllProduct = () => {
    setLoading(true)
    shoppingCartService.cancelShopping()
      .then(r => {
        getData()
        getCountProducts()
      }).finally(() =>
        setLoading(false)
      )
  }

  const getData = () => {
    if (!isAuth) {
      setLoading(false)
      return
    }
    setLoading(true)
    shoppingCartService.getProducts().then(
      res => {
        if (res.data.length === 0 || Object.keys(res.data[0]).length === 0) {
          setProducts([])
          return
        }
        const temp = res.data.reduce((arr, product) => {
          const index = arr.findIndex(i => i.id_producto === product.id_producto)
          if (index >= 0) {
            arr[index].cantidad += 1
          } else {
            product.cantidad = 1
            arr.push(product)
          }
          return arr
        }, [])
        setProducts(temp)
        let result = 0
        for (const prodKey of res.data) {
          result += prodKey.precio_unitario
        }
        setTotalShopping(result)
      }
    ).catch(e => {
      console.error(e)
    }).finally(() => {
      setLoading(false)
    }
    )
  }
  useEffect(() => {
    getData()
  }, [])
  const renderHead = () => {
    if (products.length === 0 || Object.keys(products[0]).length === 0) {
      return (
        <>
          <p className='text-3xl lg:text-5xl font-black uppercase text-center mb-5'>Carrito Vació</p>
          <Lottie animationData={animationData} style={{ height: 500 }} />
          {isAuth
            ? <></>
            : <p className='text-xl text-center font-medium uppercase'> Inicia Sesison</p>}
        </>
      )
    }
    return (
      <>
        <p className='text-3xl lg:text-5xl font-black uppercase text-center mb-5'>Tu Carrito</p>
        <p className='text-xl lg:text-3xl font-medium text-center uppercase mb-6'>Total: Q {totalShopping}</p>
        <div className='flex flex-wrap gap-3 justify-center'>
          <Button label='Confirmar Carrito' />
          <Button label='Cancelar Carrito' severity='danger' onClick={removeAllProduct} />
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
              <p className='text-xl font-bold'>{item.cantidad} x {item.nombre}</p>
              <p className='font-normal mt-5'>{item.descripcion}</p>
            </div>
            <div className='flex flex-col ga-3 justify-center items-center md:items-end w-full'>
              <p className='text-xl font-medium mb-5'>{item.cantidad} x {item.precio_unitario} = Q. {item.cantidad * item.precio_unitario.toFixed()}</p>
              <Button label='Eliminar' severity='danger' outlined size='small' onClick={() => removeProduct(item.id_producto)} />
            </div>
          </div>
          <Divider />
        </div>
      )
    })
  }
  const renderDetail = () => {
    if (products.length === 0 || Object.keys(products[0]).length === 0) {
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
        {loading
          ? <>
            <Skeleton width='100%' height='150px' />
            <Divider />
            <Skeleton width='100%' height='350px' />
            </>
          : <>
            {renderHead()}
            {renderDetail()}
          </>}
      </div>
    </>
  )
}
export default ShoppingCartPage
