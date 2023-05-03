import { InputText } from 'primereact/inputtext'
import { Controller, useForm } from 'react-hook-form'
import { Button } from 'primereact/button'
import { classNames } from 'primereact/utils'
import { Password } from 'primereact/password'
import { useContext, useRef, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Context } from '../store/Context.jsx'
import { Toast } from 'primereact/toast'

export const LoginForm = () => {
  const defaultValues = { correo: '', contraseña: '' }
  const navigate = useNavigate()
  const [loading, setLoading] = useState(false)
  const ctx = useContext(Context)
  const toast = useRef(null)

  const {
    control,
    formState: { errors },
    handleSubmit
  } = useForm({ defaultValues })

  const onSubmit = async (data) => {
    setLoading(true)
    console.log(data)
    const rest = await ingresar(data)
    if (rest.estatus === 200) {
      toast.current.show({ severity: 'info', summary: 'Sesión Iniciada', detail: 'Bienvenido' })
      ctx.login(rest.token, rest.data)
      navigate('/')
    } else {
      toast.current.show({
        severity: 'error',
        summary: rest.error ? rest.error : 'Error al ingresar',
        detail: rest.mensaje ? rest.mensaje : ''
      })
      console.log('error', rest)
    }
    setLoading(false)
  }

  const ingresar = async (data) => {
    return await fetch(
      'http://146.190.198.15:5050' + '/user/login', {
        mode: 'cors',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': 'http://146.190.198.15:5050' + '/user/login'
        },
        body: JSON.stringify(
          {
            contrasena: data['contraseña'],
            correo: data.correo
          }
        )
      }
    ).then((response) => response.json())
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
          <p className='text-3xl font-bold text-center'>Inicio de Sesión</p>
          <Controller
            name='correo'
            control={control}
            rules={{ required: 'correo es requerido.' }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>
                  <InputText
                    id={field.name} value={field.value}
                    className={classNames({ 'p-invalid': fieldState.error })}
                    onChange={(e) => field.onChange(e.target.value)}
                  />
                  <label htmlFor={field.name}>Correo</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Controller
            name='contraseña'
            control={control}
            rules={{ required: 'contraseña es requerido.' }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>
                  <Password
                    id={field.name} value={field.value}
                    className={classNames({ 'p-invalid': fieldState.error })}
                    onChange={(e) => field.onChange(e.target.value)}
                    feedback={false}
                    toggleMask
                  />
                  <label htmlFor={field.name}>Contraseña</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Button label='Enviar' loading={loading} rounded />
          <Button
            label='Registrarme' className='p-button-outlined' severity='secondary'
            onClick={() => navigate('/signup')}
            rounded
          />
        </form>

      </div>
    </>
  )
}
