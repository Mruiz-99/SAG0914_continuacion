import { InputText } from 'primereact/inputtext'
import { Controller, useForm } from 'react-hook-form'
import { Button } from 'primereact/button'
import { classNames } from 'primereact/utils'
import { Password } from 'primereact/password'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Calendar } from 'primereact/calendar';
import dayjs from "dayjs";

export const ConfirmEmail = () => {
    const defaultValues = { cui: '', nombres: '', apellidos: '', correo: '', contraseña: '', contraseña2: '', fecha_nac: '', numero_grupo: '', seccion: '' }
    //cui, nombres, apellidos, contraseña, correo, fecha de nacimiento, tipo, numero grupo, sección
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
        let fech = data['fecha_nac']
        let for_date = formatDate(fech)
        data['fecha_nac'] = for_date
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

    const formatDate = (date) => {
        return dayjs(date).format("DD/MM/YYYY");
    };

    return (
        <>
            <div className='card w-11/12 md:w-2/5'>
                <div className='flex flex-col gap-3 p-fluid'>
                    <p className='text-4xl font-bold text-center'>Confirmar Cuenta</p>
                    <p className='text-2xl font-bold text-center'>Se envio un correo a su cuenta por favor de confirmar en su correo e ingrese a su cuenta</p>
                    <Button
                        label='Aceptar' className='p-button-outlined' severity='secondary'
                        onClick={() => navigate('/login')}
                        rounded
                    />
                </div>

            </div>
        </>
    )
}
