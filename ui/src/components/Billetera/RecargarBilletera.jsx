import { InputText } from 'primereact/inputtext'
import { Controller, useForm } from 'react-hook-form'
import { Button } from 'primereact/button'
import { classNames } from 'primereact/utils'
import { Password } from 'primereact/password'
import { useNavigate } from 'react-router-dom'
import React, { useState, useEffect } from 'react';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import walletpng from './assets/wallet.png'


export const WalletForm = () => {
//  idUsuario: 0,
  const [_wallet, setWallet] = useState([]);
  const imagenWallet = () => { return <img src={walletpng} alt='wallet' style={{ width: "20%", height: "20%" }}/> }
  useEffect(() => {
    // fetch('http://localhost:8080/api/wallets')
    //   .then(response => response.json())
    //   .then(data => setWallet(data));
    setWallet([{idWallet: 1, idUsuario: 1, monto: 1000}])
  }, []);

  const defaultValues = { idUsuario:''  }
  const idWallet = 0
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

  const getFormErrorMessage = (name) => {
    return errors[name]
      ? <small className='p-error'>{errors[name].message}</small>
      : <small className='p-error'>&nbsp;</small>
  }

  return (
    <>
       <div className="card">
        {/* Tabla para ver el estado actual de la billetera */}
        <DataTable value={_wallet} tableStyle={{ minWidth: '20rem' }}>
          <Column header="Image" body={imagenWallet}></Column>
          <Column field="monto" header="Saldo" ></Column>
        </DataTable>
       </div>
      <div className='card w-11/12 md:w-2/5'>
      

        <form onSubmit={handleSubmit(onSubmit)} className='flex flex-col gap-3 p-fluid'>
          <p className='text-3xl font-bold text-center'>Recargar Saldo</p>
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
