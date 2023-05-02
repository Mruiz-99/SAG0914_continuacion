import { InputText } from 'primereact/inputtext'
import { Controller, useForm } from 'react-hook-form'
import { Button } from 'primereact/button'
import { classNames } from 'primereact/utils'
import { Password } from 'primereact/password'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

export const LoginForm = () => {
  const defaultValues = { correo: '', contraseña: '' }
  const navigate = useNavigate()
  const [loading, setLoading] = useState(false)

  const {
    control,
    formState: { errors },
    handleSubmit,
    reset
  } = useForm({ defaultValues })

  const onSubmit = (data) => {
    setLoading(true)
    console.log(data)
    setTimeout(() => {
      reset()
      setLoading(false)
    }, 2000)
  }

  const ingresar = async (data) => {
    console.log('info ');
    console.log(data);
    const response = await fetch(
      'http://146.190.198.15:5050' + "/user/signin", {
      mode: 'cors',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'http://146.190.198.15:5050' + "/user/signin",
      },
      'body': JSON.stringify(
        {
          contrasena: data['contraseña'],
          correo: data['correo']
        }
      )
    }
    ).then((response) => response.json());
    console.log(response);
    return response;

  };

  const getFormErrorMessage = (name) => {
    return errors[name]
      ? <small className='p-error'>{errors[name].message}</small>
      : <small className='p-error'>&nbsp;</small>
  }

  return (
    <>
      <div className='card w-11/12 md:w-2/5'>
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
