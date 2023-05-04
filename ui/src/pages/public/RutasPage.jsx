import { useContext, useRef, useState } from 'react'
import { Controller, useForm } from 'react-hook-form'
import { Toast } from 'primereact/toast'
import { InputText } from 'primereact/inputtext'
import { Button } from 'primereact/button'
import { Context } from '../../store/Context.jsx'
import { classNames } from 'primereact/utils'
import RoutesService from '../../services/Ruta.Service.js'

const RutasPage = () => {
  const defaultValues = { nombre: '', zonas: '' }
  const [loading, setLoading] = useState(false)
  const toast = useRef(null)
  const { token } = useContext(Context)
  const routeService = new RoutesService(token)

  const {
    control,
    formState: { errors },
    handleSubmit
  } = useForm({ defaultValues })

  const onSubmit = async (data) => {
    try {
      setLoading(true)
      const res = await routeService.crearRutas(data.nombre, data.zonas.split(',').map(i => Number(i)))
      console.log(res)
    } catch (e) {
      toast.current.show({
        severity: 'error',
        summary: 'Error al enviar solicitud',
        detail: 'Error al comunicarse con el servidor, contacte a soporte'
      })
    } finally {
      setLoading(false)
    }
  }

  const getFormErrorMessage = (name) => {
    return errors[name]
      ? <small className='p-error'>{errors[name].message}</small>
      : <small className='p-error'>&nbsp;</small>
  }

  return (
    <>
      <div className='card w-11/12 md:w-2/5'>
        <Toast ref={toast} />
        <form onSubmit={handleSubmit(onSubmit)} className='flex flex-col gap-3 p-fluid'>
          <p className='text-3xl font-bold text-center'>Nueva Ruta</p>
          <Controller
            name='nombre'
            control={control}
            rules={{ required: 'nombre es requerido.' }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>
                  <InputText
                    id={field.name} value={field.value}
                    className={classNames({ 'p-invalid': fieldState.error })}
                    onChange={(e) => field.onChange(e.target.value)}
                  />
                  <label htmlFor={field.name}>Nombre</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Controller
            name='zonas'
            control={control}
            rules={{ required: 'zona es requerido.' }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>
                  <InputText
                    id={field.name} value={field.value}
                    className={classNames({ 'p-invalid': fieldState.error })}
                    onChange={(e) => field.onChange(e.target.value)}
                  />
                  <label htmlFor={field.name}>Zona</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Button label='Enviar' loading={loading} rounded />
        </form>

      </div>
    </>
  )
}
export default RutasPage
