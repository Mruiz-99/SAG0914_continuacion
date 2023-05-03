import React, { useContext, useEffect, useRef, useState } from 'react'
import { Button } from 'primereact/button'
import { DataView, DataViewLayoutOptions } from 'primereact/dataview'
import { Tag } from 'primereact/tag'
import './home.css'
import { Image } from 'primereact/image'
import ProductService from '../../services/Product.Service.js'
import { Context } from '../../store/Context.jsx'
import ShoppingCartService from '../../services/ShoppingCart.Service.js'
import { Toast } from 'primereact/toast'
import { Messages } from 'primereact/messages'
import Lottie from 'lottie-react'
import animationData from '../../assets/ErrorServer.json'

const productService = new ProductService()

export const HomePage = () => {
  const [products, setProducts] = useState([])
  const [layout, setLayout] = useState('grid')
  const [loading, setLoading] = useState(false)
  const [visibleServerError, setVisibleServerError] = useState(false)
  const message = useRef(null)
  const { token, isAuth, getCountProducts } = useContext(Context)
  const toast = useRef(null)
  const shoppingCartService = new ShoppingCartService(token)
  const getData = () => {
    setLoading(true)
    productService.getAllProduct()
      .then(res => {
        setProducts(res.data)
        setVisibleServerError(false)
        if (isAuth) {
          getCountProducts()
        }
      })
      .catch(e => {
        if (e.code === 'ERR_NETWORK') {
          setVisibleServerError(true)
          message.current.show(
            { sticky: true, severity: 'error', summary: '', detail: 'Error al comunicarse con el servidor, en breve estaremos en funcionamiento', closable: true }
          )
        }
      })
      .finally(() => setLoading(false))
  }

  const addProduct = (idProducto) => {
    if (!isAuth) {
      toast.current.show({ severity: 'info', summary: 'No tienes una sesión activa', detail: 'Primer inicia sesión o registrate' })
      return
    }
    shoppingCartService.addProduct(idProducto, 1).then(r => {
      getCountProducts()
      toast.current.show({ severity: 'success', summary: 'Producto Agregado' })
      console.log(r)
    })
  }

  useEffect(() => {
    getData()
  }, [])

  const getSeverity = (product) => {
    if (product.unidades_disponibles > 0) return { value: 'IN STOCK', color: 'success' }
    return { value: 'OUT OF STOCK', color: 'danger' }
  }

  const listItem = (product) => {
    return (
      <div className='flex flex-col xl:flex-row xl:items-start p-6 gap-4 bg-white w-full mt-6 '>

        <Image
          className='h-1/5 drop-shadow-lg rounded-lg'
          src={product.imagen ? `${product.imagen}` : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Imagen_no_disponible.svg/2048px-Imagen_no_disponible.svg.png'} alt={product.nombre}
          width={100}
          height={100}
          preview
        />

        <div
          className='flex flex-col sm:flex-row justify-between  items-center xl:items-start flex-1 gap-4'
        >
          <div className='flex flex-col items-center sm:items-start gap-3'>
            <div className='text-2xl font-bold text-900'>{product.nombre}</div>
            <div className='flex items-center gap-3'>
              <span className='flex items-center gap-2'>
                <i className='pi pi-tag' />
                <span className='font-semibold'>{product.categoria}</span>
              </span>
              <Tag value={getSeverity(product).value} severity={getSeverity(product).color} />
            </div>
          </div>

          <div className='flex sm:flex-col items-center sm:items-end gap-3 sm:gap-2'>
            <span className='text-2xl font-semibold'>Q{product.precio_unitario}</span>
            <Button
              icon='pi pi-shopping-cart' className='p-button-rounded'
              disabled={product.stock === 0}
              onClick={() => addProduct(product.sku)}
            />
          </div>
        </div>

      </div>
    )
  }

  const gridItem = (product) => {
    return (
      <div className='mt-6 p-6 bg-white border rounded-3xl w-full  md:w-max '>

        <div className='flex flex-wrap items-center justify-between gap-2'>
          <div className='flex items-center gap-2'>
            <i className='pi pi-tag' />
            <span className='font-semibold'>{product.categoria}</span>
          </div>
          <Tag value={getSeverity(product).value} severity={getSeverity(product).color} />
        </div>

        <div className='flex flex-col items-center gap-3 py-5'>
          <Image
            className='w-3/4 drop-shadow-lg rounded-lg'
            src={product.imagen ? `${product.imagen}` : 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Imagen_no_disponible.svg/2048px-Imagen_no_disponible.svg.png'} alt={product.nombre}
            preview
            width='200'
            height='200'
          />
          <div className='text-2xl font-bold'>{product.nombre}</div>
        </div>

        <div className='flex items-center justify-between'>
          <span className='text-2xl font-semibold'>Q{product.precio_unitario}</span>
          <Button
            icon='pi pi-shopping-cart' className='p-button-rounded'
            disabled={product.stock === 0}
            onClick={() => addProduct(product.sku)}
          />
        </div>

      </div>
    )
  }

  const itemTemplate = (product, layout) => {
    if (!product) return

    if (layout === 'list') return listItem(product)
    else if (layout === 'grid') return gridItem(product)
  }

  const header = () => {
    return (
      <div className='flex justify-end'>
        <DataViewLayoutOptions layout={layout} onChange={(e) => setLayout(e.value)} />
      </div>
    )
  }

  return (
    <>
      <Toast ref={toast} />
      {visibleServerError
        ? <>
          <Messages ref={message} />
          <div className='flex flex-col items-center'>
            <Lottie animationData={animationData} style={{ height: 500 }} />
            <Button label='Intentar de nuevo' severity='info' rounded size='large' loading={loading}
                    onClick={ ()=> getData() }

            />
          </div>
          </>
        : <>
          <DataView value={products} itemTemplate={itemTemplate} layout={layout} header={header()} paginator rows={15} loading={loading} />
        </>}
    </>
  )
}
