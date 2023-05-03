import { InputText } from 'primereact/inputtext'
import { Controller, useForm } from 'react-hook-form'
import { Button } from 'primereact/button'
import { classNames } from 'primereact/utils'
import { Password } from 'primereact/password'
import { useState } from 'react'
import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { Calendar } from 'primereact/calendar';
import dayjs from "dayjs";
import { Dropdown } from 'primereact/dropdown';

export const SignupForm = () => {
  const defaultValues = { cui: '', nombres: '', apellidos: '', correo: '', contraseña: '', contraseña2: '', fecha_nac: '', numero_grupo: '', seccion: '', tipo: '' }
  //cui, nombres, apellidos, contraseña, correo, fecha de nacimiento, tipo, numero grupo, sección
  const navigate = useNavigate()
  const [loading, setLoading] = useState(false)
  const tiposU = [
    { name: 'Empresario', code: 'E' },
    { name: 'Usuario Cliente', code: 'C' }
  ];
  const secc = [
    { name: 'N', code: 'N' },
    { name: 'A', code: 'A' }
  ];

  const {
    control,
    formState: { errors },
    handleSubmit,
    reset,
    getValues,
    watch
  } = useForm({ defaultValues })

  const onSubmit = async (data) => {
    setLoading(true)
    let fech = data['fecha_nac']
    let for_date = formatDate(fech)
    data['fecha_nac'] = for_date
    let tipo_E = data['tipo']['code']
    data['tipo'] = tipo_E
    let secc_E = data['seccion']['code']
    data['seccion'] = secc_E
    const rest = await nuevoUsuario(data);
    setTimeout(() => {
      reset()
      setLoading(false)
    }, 2000)
    navigate('/confirmEmail')
  }
  const watchShowAge = watch("tipo", false); // you can supply default value as second argument
  const watchAllFields = watch(); // when pass nothing as argument, you are watching everything
  const watchFields = watch(["tipo"]); // you can also target specific fields by their names




  const nuevoUsuario = async (data) => {
    const response = await fetch(
      'http://146.190.198.15:5050' + "/user/signin", {
      mode: 'cors',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'http://146.190.198.15:5050' + "/user/signin",
      },
      'body': JSON.stringify(
        /* {
          id_usuario: userObj.usuario.id_usuario.toString(),
          alias: userObj.usuario.alias,
          correo: userObj.usuario.correo,
          cantidad: cantidad,
          id_partido: part.toString(),
          id_categoria: cate.toString(),
        } */
        {
          cui: data['cui'],
          nombres: data['nombres'],
          apellidos: data['apellidos'],
          contrasena: data['contraseña'],
          correo: data['correo'],
          fecha_nacimiento: data['fecha_nac'],
          tipo: data['tipo'],
          numero_grupo: data['numero_grupo'],
          seccion_grupo: data['seccion']
        }
        /* {
          cui: 2168095170407,
          nombres: data['nombres'],
          apellidos: data['apellidos'],
          contrasena: data['contraseña'],
          correo: data['correo'],
          fecha_nacimiento: data['fecha_nac'],
          tipo: "E",
          numero_grupo: 914,
          seccion_grupo: "N"
        } */
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

  const formatDate = (date) => {
    return dayjs(date).format("YYYY-MM-DD");
  };

  return (
    <>
      <div className='card w-11/12 md:w-2/5'>
        <form onSubmit={handleSubmit(onSubmit)} className='flex flex-col gap-3 p-fluid'>
          <p className='text-3xl font-bold text-center'>Crear Cuenta</p>

          <Controller
            name='cui'
            control={control}
            rules={{
              required: 'cui es requerido.',
              minLength: { value: 13, message: 'El CUI debe tener 13 dígitos' },
              maxLength: { value: 13, message: 'El CUI debe tener 13 dígitos' },
            }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>
                  <InputText
                    id={field.name} value={field.value}
                    type="number"
                    maxLength="13"
                    pattern="[0-9]{0,13}"
                    className={classNames({ 'p-invalid': fieldState.error })}
                    onChange={(e) => field.onChange(e.target.value)}
                  />
                  <label htmlFor={field.name}>CUI *</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Controller
            name='nombres'
            control={control}
            rules={{ required: 'nombres son requeridos.' }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>
                  <InputText
                    id={field.name} value={field.value}
                    className={classNames({ 'p-invalid': fieldState.error })}
                    onChange={(e) => field.onChange(e.target.value)}
                  />
                  <label htmlFor={field.name}>Nombres *</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Controller
            name='apellidos'
            control={control}
            rules={{ required: 'apellidos son requeridos.' }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>
                  <InputText
                    id={field.name} value={field.value}
                    className={classNames({ 'p-invalid': fieldState.error })}
                    onChange={(e) => field.onChange(e.target.value)}
                  />
                  <label htmlFor={field.name}>Apellidos *</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Controller
            name='correo'
            control={control}
            rules={{ required: 'correo es requerido.' }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>
                  <InputText
                    id={field.name} value={field.value} type='email'
                    className={classNames({ 'p-invalid': fieldState.error })}
                    onChange={(e) => field.onChange(e.target.value)}
                  />
                  <label htmlFor={field.name}>Correo *</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Controller
            name='contraseña'
            control={control}
            rules={{
              required: 'contraseña es requerido.',
              minLength: { value: 5, message: 'La contraseña debe tener al menos 5 caracteres' }
            }}
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
                  <label htmlFor={field.name}>Contraseña *</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Controller
            name='contraseña2'
            control={control}
            rules={{
              required: 'contraseña es requerido.',
              validate: (value, formValues) => value === formValues.contraseña || 'Contraseñas no coinciden'
            }}
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
                  <label htmlFor={field.name}>Confirmar Contraseña *</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Controller
            name='fecha_nac'
            control={control}
            rules={{ required: 'Fecha es requerida.' }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>

                  <Calendar
                    id={field.name}
                    name="date"
                    dateFormat="dd/mm/yy"
                    type={'month'}
                    value={field.value}
                    className={classNames({ 'p-invalid': fieldState.error })}
                    onChange={(e) => field.onChange(e.target.value)}
                  />
                  <label htmlFor={field.name}>Fecha de Nacimiento *</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          <Controller
            name="tipo"
            control={control}
            rules={{ required: 'Tipo es requerido.' }}
            render={({ field, fieldState }) => (
              <>
                <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                <span className='p-float-label'>

                  <Dropdown
                    id={field.name}
                    value={field.value}
                    optionLabel="name"
                    placeholder="Select a tipo"
                    options={tiposU}
                    focusInputRef={field.ref}
                    onChange={(e) => field.onChange(e.value)}
                    className={classNames({ 'p-invalid': fieldState.error })}
                  />
                  <label htmlFor={field.name}>Tipo *</label>
                </span>
                {getFormErrorMessage(field.name)}
              </>
            )}
          />

          {watch('tipo').code == 'E' && <>


            <Controller
              name='numero_grupo'
              control={control}
              rules={{ required: 'número grupo es requerido.' }}
              render={({ field, fieldState }) => (
                <>
                  <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                  <span className='p-float-label'>

                    <InputText
                      id={field.name}
                      value={field.value}
                      type="number"
                      pattern="[0-9]"
                      className={classNames({ 'p-invalid': fieldState.error })}
                      onChange={(e) => field.onChange(e.target.value)}
                    />
                    <label htmlFor={field.name}>Número Grupo *</label>
                  </span>
                  {getFormErrorMessage(field.name)}
                </>
              )}
            />

            <Controller
              name="seccion"
              control={control}
              rules={{ required: 'Sección es requerido.' }}
              render={({ field, fieldState }) => (
                <>
                  <label htmlFor={field.name} className={classNames({ 'p-error': errors.value })} />
                  <span className='p-float-label'>

                    <Dropdown
                      id={field.name}
                      value={field.value}
                      optionLabel="name"
                      placeholder="Select a tipo"
                      options={secc}
                      focusInputRef={field.ref}
                      onChange={(e) => field.onChange(e.value)}
                      className={classNames({ 'p-invalid': fieldState.error })}
                    />
                    <label htmlFor={field.name}>Sección *</label>
                  </span>
                  {getFormErrorMessage(field.name)}
                </>
              )}
            />
          </>
          }
          <Button label='Registrarme' loading={loading} rounded />
          <Button
            label='Ya tengo cuenta' className='p-button-outlined' severity='secondary'
            onClick={() => navigate('/login')}
            rounded
          />
        </form>

      </div>
    </>
  )
}
