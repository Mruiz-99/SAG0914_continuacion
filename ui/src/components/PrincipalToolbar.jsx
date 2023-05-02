import { useRef, useState } from 'react'
import { Menubar } from 'primereact/menubar'
import { Menu } from 'primereact/menu'
import { Badge } from 'primereact/badge'
import { Link, useNavigate } from 'react-router-dom'

const start = <Link to='/'><p className='text-3xl font-bold'>SA-G9</p></Link>
export const PrincipalToolbar = () => {
  const menu = useRef()
  const [countProducts] = useState(0)
  const navigate = useNavigate()

  const items = [
    {
      items: [
        {
          label: 'Registrarme',
          icon: 'pi pi-user-plus',
          visible: true,
          command: () => { navigate('/signup') }
        },
        {
          label: 'Iniciar Sesión',
          icon: 'pi pi-sign-in',
          visible: true,
          command: () => { navigate('/login', { replace: true }) }
        },
        {
          label: 'Editar Perfil',
          icon: 'pi pi-user-edit',
          visible: true,
          command: () => {
          }
        },
        {
          label: 'Cerrar Sesión',
          icon: 'pi pi-sign-out',
          visible: true,
          command: () => {
          }
        }
      ]
    }
  ]

  const RedirigWallet = () => {
    navigate('/wallet')
  }

  const end = (
    <div className='flex gap-3 items-center'>
      <Menu model={items} popup ref={menu} />
      <i
        className='pi pi-user' style={{ fontSize: '1.8rem', color: 'var(--primary-color)', cursor: 'pointer' }}
        onClick={(e) => menu.current.toggle(e)}
        onMouseEnter={(e) => menu.current.toggle(e)}
      />

      <i
        className='pi pi-shopping-cart p-overlay-badge'
        style={{ fontSize: '1.8rem', color: 'var(--primary-color)', cursor: 'pointer' }}
      >
        <Badge value={countProducts} />
        
      </i>
      <i
        className='pi pi-wallet p-overlay-badge'
        style={{ fontSize: '1.8rem', color: 'var(--primary-color)', cursor: 'pointer' }}
        onClick={RedirigWallet}
      >
        
      </i>

    </div>
  )
  return (
    <Menubar start={start} end={end} className='py-8 px-8 md:px-20' />
  )
}
